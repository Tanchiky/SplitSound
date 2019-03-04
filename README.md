# SplitSound
SplitSound on Python / Tanchiky

v1.0 - 初回版



## Features

**「は～！？この音声ファイルめちゃめちゃ一本で繋がってんじゃん！！」**

という問題をそこはかとなく解消する為に作りました。やったね。



(この前購入したサンプリング音源が1本Wavで繋がってて大変ムキーーーってなったので)



## なにかこ

音声ファイルの無音箇所で分割を行い、それぞれ出力ディレクトリにアウトプットするやつです。

対応している**音声形式は[.wav / .mp3]** です (pydub対応に準ずる)

config.ini内を書き換えることで切り取り等の細かい設定を変更可能です。

```
[setting]
min_silence_len = 1000	#1000ms以上無音があれば分割
silence_thresh = -45	#-45dB以下を無音と判別させる
keep_silence = 500  	#分割後500msくらい無音を残す
```



## QuickStart

コマンドライン上で動作

` python3 SSP.py "[読み込みたいファイルの詰まったディレクトリ]" "出力ディレクトリ名(省略可)" `



## Required

**Python 3** , **pydub** , **ffmpeg** 



