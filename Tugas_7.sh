#!/bin/bash

{
   echo "==luas bidang persegi=="
   echo "Masukan Panjang"
   read panjang
   echo "Masukan Lebar"
   read lebar
   let luasbidangpersegi=$panjang*$lebar
   echo "Luas persegi :
$luasbidangpersegi"

}
