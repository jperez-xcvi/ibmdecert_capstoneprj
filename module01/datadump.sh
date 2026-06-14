#!/bin/bash

# Nombre del contenedor de MySQL (ajústalo si tu contenedor se llama diferente)
CONTAINER_NAME="mysql_container"

# Exportar la tabla sales_data desde adentro del contenedor hacia el host
docker exec -i $CONTAINER_NAME mysqldump -u root -pPkvIeob8qrFZ83 sales sales_data > /home/jose/projects/ibmdecert_capstoneprj/module01/sales_data.sql

echo "Respaldo completado con éxito. Archivo generado: sales_data.sql"