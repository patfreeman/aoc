#!/bin/bash

id="ugkcyxxp"
password=""
i=0
while [ "${#password}" != "8" -a "${i}" != "1000" ]; do
	md5in=${id}${i}
	md5=`md5 -s ${md5in}`
	md=${md5##* }
	if [ ${md:0:5} == "00000" ]; then
		password=`echo -n ${password}${md5:5:1}`
		echo ${i} ${md5} ${password}
	fi
	let i+=1
done
echo ${password}
