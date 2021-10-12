#!/bin/bash

backup_dir=$(date +'%d_%m_%Y')
backup_ant=$(date -d yesterday +'%d_%m_%Y')
cd home/valentina/Escritorio/Seguridad

# Cambia USUARIO por tu usuario, y modifica cualquier path que no este bien
rsync -av /home/valentina/Desktop/Seguridad/ /var/tmp/Backups/$hoy
# Pone los datos de tu base de datos
mysqldump --user=TU_USUARIO --password=TU_PASSWORD NOMBRE_DE_LA_BASE > "/var/tmp/Backups/${backup_dir}/copia_seguridad.sql

