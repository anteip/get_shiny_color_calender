#!/bin/bash

date=`date "+%Y-%m"`
dir="/home/`whoami`/gscc/"
image_file="${dir}${date}-01_imassc_calender_1.jpeg"

#インターネットにアクセス可能か確認
ping -c 4 8.8.8.8
if [ ! $? = 0 ];then
	exit 1
fi

#画像ファイルが存在していなければ新たに画像を取得し壁紙を設定する
if [ ! -f  ${image_file} ];then

	#画像取得処理
	python3 ${dir}/gscc.py

	for i in ${dir}${date}*
	do
		#画像がデスクトップ用かどうかをサイズから判断
		width=`file ${i} | cut -d, -f8 | awk -F'x' '{print $1}'`
		height=`file ${i} | cut -d, -f8 | awk -F'x' '{print $2}'`
		if [ ${width} -gt ${height} ];then
			#壁紙に設定
			gsettings set org.gnome.desktop.background picture-uri "file://${i}"
			break 2
		fi      
	done

fi

