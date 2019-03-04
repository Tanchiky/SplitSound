# Required - pydub, ffmpeg
import os, glob, sys, configparser
from pydub import AudioSegment
from pydub.silence import split_on_silence

SSP_VER = "1.0"
SSP_PNAME = "SliceSound by Python"

# Defaults
files_path = os.path.dirname(os.path.abspath(__file__)) + "/source"
output_path = "output_files"
split_config = [1000, -40, 200]
possible_ext = ["mp3", "wav"]
ini_file = "./config.ini"
err_type = ["Error", "Waring", "Through", "Success"]

def message(mes, level, exitFlag=False):
    print(" > " + err_type[level] + " : " + mes) if level != -1 else print(" > " + mes),
    if exitFlag: exit()

message(SSP_PNAME + " / " + SSP_VER, -1)

# Check Config
message("Check Config file", -1)
config = configparser.ConfigParser()
config.read(ini_file) if os.path.isfile(ini_file) else message("config.ini file is not found", 0, True)
split_config[0] = int(config.get('setting', 'min_silence_len'))
split_config[1] = int(config.get('setting', 'silence_thresh'))
split_config[2] = int(config.get('setting', 'keep_silence'))
message("Loaded Config", -1)

# Check Argument
if len(sys.argv) > 1:
    if os.path.isdir(sys.argv[1]):
        files_path = sys.argv[1]
        if len(sys.argv) > 2: output_path = sys.argv[2] + "/"
    else:
        message( sys.argv[1] + " is not found", 0, True)
else: message("There isn't Option. Use the Default folder.", 1)

# Include Files / Check Dir
message("Loading Audio Files", -1)
def listup_AudioFiles(path):
    v = []
    for p in glob.glob(path):
        if not os.path.isdir(p): v.append(os.path.abspath(p))
    return v

# Check Files
message("Check Audio Files", -1)
fileLists = listup_AudioFiles(files_path + "/*")
if not fileLists: message("file is not found", 0, True)

# Check Dir
if not os.path.exists(files_path + "/" + output_path):
    message("Create output Directory", 3), os.makedirs(files_path + "/" + output_path)

# Split Process
message("Processing...", -1)
for fi in fileLists:
    fodir = os.path.dirname(fi) + "/"
    fname = os.path.splitext(os.path.basename(fi))

    # Supported format
    if fname[1][1:] != possible_ext[0] and fname[1][1:] != possible_ext[1]:
        if fname[0] != output_path: message(fi + " isn't in .wav/.mp3 Format", 2)
        continue

    # Include Sounds
    sound = AudioSegment.from_file(fi, format=fname[1][1:])
    chunks = split_on_silence(sound, min_silence_len=split_config[0], silence_thresh=split_config[1], keep_silence=split_config[2])

    for i, chunk in enumerate(chunks):
        out_fname = fname[0] + "_" + str(i) + fname[1]
        chunk.export(fodir + output_path + "/" + out_fname, format=fname[1][1:]), message("Create '" + out_fname + "'", 3, False)

message("Complete!", -1, True)