#!/bin/bash
# @Author: zhumengyan
# @Date:   2018-04-03 14:20:57
# @Last Modified by:   zhumengyan
# @Last Modified time: 2018-04-03 20:18:52

###  Default parameter
###  Function for script description and usage
###  Command Line Parameter

###  Maintext
function is_done()
{
	##  判断上一个命令是否运行成功
	# $1  ##  name of file that you want to download

	if [ $? -ne 0 ];then
		echo -e "\033[31m $1 failed!!! \033[0m"
		echo -e "\033[31m $1 failed!!! \033[0m" >> download.log
	else
		echo -e "\033[34m $1 success!!! \033[0m"
		echo -e "\033[34m $1 success!!! \033[0m" >> download.log
	fi
}

for ((i=622;i<=637;i++))
do
	echo "SRR1047${i}.sra download beginning..."
	##  methods one
	wget ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByStudy/sra/SRP/SRP033/SRP033711/SRR1047${i}/SRR1047${i}.sra

	##  method two
	#prefetch SRR1047${i}

	is_done "SRR1039${i}.sra" 
done

echo -e "\033[46;37m pls check if some files haven't been downloaded!!! \033[0m"





