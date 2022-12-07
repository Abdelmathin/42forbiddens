#  **************************************************************************  #
#                                                                              #
#                                                          :::      ::::::::   #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ahabachi <ahabachi@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/06 23:14:17 by ahabachi          #+#    #+#              #
#    Updated: 2022/11/06 23:20:49 by ahabachi         ###   ########.fr        #
#                                                                              #
#  **************************************************************************  #

ORIGINAL_FILES			=	42forbiddens.c 42forbiddens.cpp 42forbiddens.py\
							42forbiddens.sh Makefile 42forbiddens.can\
							42forbiddens.json 42forbiddens.rb LICENSE

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

RESET_FILE		=	habachi_reset.py
define RESET_CODE
if (1):\n\
import os\n\
def setup(filename):\n\
\tfilename = filename.replace('\\\n', ' ').replace('\\\t', ' ').split(' ');\n\
\ts2 = []\n\
\tfor i in filename:\n\
\t\ti = i.strip()\n\
\t\tif not i:continue\n\
\t\twhile ('//' in filename):filename = filename.replace('//', '/')\n\
\t\twhile i.startswith('./'):i = i[2:]\n\
\t\twhile i.endswith('/'):i = i[:-1]\n\
\t\tif (i in ['.', '..', '.git']):continue\n\
\t\tif i.startswith('.git/'):continue\n\
\t\ts2.append(i);\n\
\treturn (s2);\n\
def remove_file(filename):\n\
\ttry:print('removing:', i);os.system('rm -rf \"' + i + '\"')\n\
\texcept:pass\n\
s = setup(s);\n\
t = setup(t)\n\
for i in t:\n\
\tif not (i in s):\n\
\t\tremove_file(i)
endef

reset:
	@echo "t = '" `find .` "'" > ${RESET_FILE}
	@echo "s = '${ORIGINAL_FILES}'" >> ${RESET_FILE}
	@echo "${RESET_CODE}" >> ${RESET_FILE}
	@python ${RESET_FILE}
	@rm -rf ${RESET_FILE}

push: reset
	@git add *
	@git commit -m "committed on '`date`' by '`whoami`', hostname = '`hostname`'"
	@git push

.PHONY: reset push
