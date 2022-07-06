#!/bin/bash

date=`date "+%Y-%m"`
dir="/home/`whoami`/gscc/"
image_file="${dir}${date}-01_imassc_calender_1.jpeg"

#画像ファイルが存在していなければ新たに画像を取得し壁紙を設定する
if [ ! -f  ${image_file} ];then

	#画像取得処理
	python3 /home/`whoami`/py/gscc/gscc.py

	#壁紙に設定
	gsettings set org.gnome.desktop.background picture-uri "file://${image_file}"

fi

