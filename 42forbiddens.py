#  **************************************************************************  #
#                                                                              #
#                                                          :::      ::::::::   #
#    42forbiddens.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ahabachi <ahabachi@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/06 22:08:38 by ahabachi          #+#    #+#              #
#    Updated: 2022/11/07 06:09:49 by ahabachi         ###   ########.fr        #
#                                                                              #
#  **************************************************************************  #

ignored_functions = {
	'___stack_chk_fail', '___stack_chk_guard', 'dyld_stub_binder'
};

allowed_functions = eval(open("42forbiddens.json", "r").read());

import os;
import sys;

BLANK = '----------------';
tmp_file = ".DS_Store"

def usage(name):
	print ("usage: python " + name.split('/')[-1] + 
		" [filename] [Project] [Part:Mandatory|Bonus]")

def ft_ignored(function_name):
	if (function_name in ignored_functions):
		return (1);
	return (0);

def is_allowed(Project, Part, function_name):
	return (function_name in allowed_functions[Project][Part]);

program_names = {
	"libft.a" : ["libft", "mandatory"],
	"libftprintf.a" : ["ft_printf", "mandatory"],
	"philo" : ["philosophers", "mandatory"],
	"philo_bonus" : ["philosophers", "bonus"],
}

def get_project_name_and_part(filename):
	basename = filename.split('/')[-1].strip();
	if (basename in program_names):
		return (program_names[basename]);
	return ["", ""]

def ft_42forbiddens(filename, project = "", part = ""):
	[_project, _part] = get_project_name_and_part(filename);
	if (not (project)):
		project = _project
	if (not (part)):
		part = _part
	project = project.lower().strip();
	part = part.lower().strip();
	if ((not filename) or (not project) or (not part)):
		return (-1);
	os.system("nm \"{0}\" > \"{1}\"".format(filename, tmp_file));
	_detected = [];
	for line in open(tmp_file, "r"):
		line = line.strip().replace('\t', ' ')
		while ('  ' in line):
			line = line.replace('  ', ' ');
		arr = ([BLANK] + line.split(' '))[-3:];
		if (ft_ignored(arr[2])):
			continue ;
		if (arr[2][0] == '_'):
			arr[2] = arr[2][1:] # e.g _free --> free
		if (arr[0] == BLANK and arr[1] in ["U"]):
			if (not is_allowed(project, part, arr[2])):
				_detected.append(arr[2])
	if (_detected):
		_detected = str(_detected);
		_detected = _detected.replace("'",'"').replace("[",'{')
		_detected = _detected.replace("]",'}')
		print ("KO: Forbidden functions are detected:")
		print ("\t" + _detected)
		return (1)
	print ("OK: No forbidden functions detected")
	return (0);

# sys.argv = [sys.argv[0]] + ["/Users/ahabachi/Desktop/Projects/42cursus-philosophers/philo/philo"]

if (__name__ == "__main__"):
	argv = (sys.argv + ["", "", ""])[:4]
	if (ft_42forbiddens(argv[1], argv[2], argv[3]) < 0):
		usage(argv[0])
