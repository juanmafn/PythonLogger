#!/usr/bin/env python
# coding: utf8
__author__ = "Juan Manuel Fernández Nácher"

# Librerías del sistema
import os, time

class Log:

	def __init__(self, name):
		self.name = name

	def Enter(self, message):
		self.__print("ENTER", message)
	
	def Exit(self, message):
		self.__print("EXIT ", message)

	def Trace(self, message):
		self.__print("TRACE", message)

	def Debug(self, message):
		self.__print("DEBUG", message)

	def Info(self, message):
		self.__print("INFO ", message)

	def Warn(self, message):
		self.__print("WARN ", message)

	def Error(self, message):
		self.__print("ERROR", message)

	def Fatal(self, message):
		self.__print("FATAL", message)

	def __print(self, type, message):
		if not os.path.exists("logs"):
			os.mkdir("logs")
		
		fichero = time.strftime("%Y-%m-%d.log")
		fecha = time.strftime("%Y-%m-%d")
		hora = time.strftime("%H:%M:%S")
		
		fich = open("logs/"+fichero, "a")
		fich.write("{0} {1} {2} {3} : {4}\n".format(fecha, hora, type, self.name, message))
		fich.close()
