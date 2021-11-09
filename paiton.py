#!/usr/bin/env python3
import os
import sys
import argparse
from os import path
from time import sleep

parser = argparse.ArgumentParser(description='This is a python subdomain finder with other tools, use to good porposes!')
parser.add_argument("-t","--target", help="Target")
# gropies = parser.add_mutually_exclusive_group()
# gropies.add_argument("-v", "--verbose", action="store_true", help="Verbose Mode")
args = parser.parse_args()

class GrimTracer:

	def __init__(self):
		self.target = args.target
    protocols = ["http://", "https://"]
    compr = [self.target.replace(x,"") for x in protocols if self.target.startswith(x)]

    self.blue = "\033[0;34m[*] - \033[0;0m"
    self.green = "\033[0;32m[+] - \033[0;0m"
		self.exitmsg = "\nShutting Down... \O/"

	def start(self):
		print("""
	               ,____
                   |---.\
           ___     |    `
          / .-\  ./=)
         |  |"|_/\/|
         ;  |-;| /_|
        / \_| |/ \ |
       /      \/\( |
       |   /  |` ) |
       /   \ _/    |
      /--._/  \    |
      `/|)    |    /
        /     |   |
      .'      |   |
jgs  /         \  |
    (_.-.__.__./  /

    Made by --> \033[0;31mFerreira\033[0;0m
    Github --> \033[0;31mhttps://github.com/ferreiraklet\033[0;0m
    \033[0;31m - \033[0;0mReconTracer is a tool that automates subdomain finding using diferents tools
    type -h for help!
			""")

  def grim(self):
    try:
      print(f"\n{self.blue} Starting GrimTracer...")
      if not path.exists("logs"):
        os.popen("mkdir logs")

      sleep(0.5)
      print(f"\n{self.blue} Initializing Assetfinder...")
      assetfinder()
      print(f"\n{self.green} Assetfinder finished!")
      sleep(0.5)
      print(f"\n{self.blue} Initializing sublist3r...")
      sublist3r()
      print(f"\n{self.green} Sublist3r finished!")
      sleep(0.5)
      print(f"\n{self.blue} Initializing Findomain...")
      findomain()
      print(f"{self.green} Findomain finished!")
      sleep(0.5)
      print(f"\n{self.blue} Initializing Subfinder...")
      subfinder()
      sleep(0.5)
      print(f"\n{self.blue} Patching up things...")
      handler()
      print(f"\n\n{self.green} GrimTracer Finished with sucess! {self.exitmsg}")
    except KeyboardInterrupt:
      print(f"\n{self.exitmsg}")
    except Exception as e:
      print(f"Something went wrong!\nError: {str(e)}")



  def assetfinder(self):
    try:
      subs = os.popen(f"assetfinder {self.target}").read()
      os.chdir("logs")
      with open(self.target, "a") as l:
        l.write(subs)
    except KeyboardInterrupt:
      print(f"\n{self.exitmsg}")
    except Exception as e:
      print(f"Something went wrong!\nError: {str(e)}")

  def sublist3r(self):
    try:
      subs = os.popen(f"sublist3r -d {self.target}").read()
      os.chdir("logs")
      with open(self.target, "a") as l:
        l.write(subs)
    except KeyboardInterrupt:
      print(f"\n{self.exitmsg}")
    except Exception as e:
      print(f"Something went wrong!\nError: {str(e)}")

  def findomain(self):
    try:
      subs = os.popen(f"findomain-linux --target {self.target}").read()
      os.chdir("logs")
      with open(self.target, "a") as l:
        l.write(subs)
    except KeyboardInterrupt:
      print(f"\n{self.exitmsg}")
    except Exception as e:
      print(f"Something went wrong!\nError: {str(e)}")

  def subfinder(self):
    try:
      subs = os.popen(f"subfinder -d {self.target}").read()
      os.chdir("logs")
      with open(self.target, "a") as l:
        l.write(subs)
    except KeyboardInterrupt:
      print(f"\n{self.exitmsg}")
    except Exception as e:
      print(f"Something went wrong!\nError: {str(e)}")

  def handler(self):
    try:
      os.chdir("logs")
      os.popen(f"cat {self.target} | sort | uniq > {self.target}1")
      os.remove(f"{self.target}")
    except KeyboardInterrupt:
      print(f"\n{self.exitmsg}")
    except Exception as e:
      print(f"Something went wrong!\nError: {str(e)}")

if __name__ == "__main__":
  grimT = GrimTracer()
  if self.target:
    grimT.start()
    grimT.grim()

