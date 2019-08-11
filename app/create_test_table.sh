#! /bin/bash

# Generamos un csv
TABLA=tabla_ejemplo
DB=vcop_inventario

CSV_LIST=$TABLA.csv
FILE_DESC="Fichero de ejemplo"

source ./__skeleton.sh


echo "entrando por aqui $FILE_NAME"

cd "$(dirname "$0")"
env

GettingData ( )
{
  MY_DATE=`DATE`
  echo "Nombre, Fecha"   >  $CSV_LIST
  echo "Pepe,${MY_DATE}" >> $CSV_LIST
}

Main
