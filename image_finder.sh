#!/bin/bash

md5hash='e5ed313192776744b9b93b1320b5e268'
images_dir='/home/valentina/Desktop/imagenes'
for i in {1..46}
do
	# Me fijo si existe el archivo porque no estaba uno del 1 al 46
	if !(-z ${images_dir}/imagen${i}.jpg)
	then
		# Guardo el hash MD5 de la imagen en la variable "hash"
		hash=md5sum ${images_dir}/imagen${i}.jpg
		if [ "$hash" == "$md5hash" ]
		then
			echo imagen${i}.jpg
		fi
	fi
done
