from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
import os, sys
import webbrowser

now = datetime.now()

def get_jargon():
	jargon_page = "http://www.jargon.net"

	page = urlopen(jargon_page)

	soup = BeautifulSoup(page, "html.parser")

	jargon = soup.find("p")

	return jargon

def write_to_file(jargon, jargon_path):
	with open(os.path.join(jargon_path, "store.txt"), "w+") as file:
		file.write(now.strftime("%d/%m/%Y") + "\n")
		file.write(jargon)

def main():
	# Check if configuration files exist
	
	jargon_path = os.path.join(os.path.expanduser("~"), ".jargon/")

	if not os.path.isdir(jargon_path):
		os.mkdir(jargon_path)

	if not os.path.isfile(os.path.join(jargon_path, "store.txt")):
		with open(os.path.join(jargon_path, "store.txt"), "w+") as file:
			pass

	with open(os.path.join(jargon_path, "store.txt"), "r") as file:
		contents = file.readlines()

	if len(sys.argv) > 1:
		arg = sys.argv[1]
	else:
		arg = sys.argv[0]

	if arg != "open":
		print("\033[1m\033[4mJargon of the Day\033[0m\033[0m \n")
		if contents[0].replace("\n", "") == now.strftime("%d/%m/%Y"):
			print(contents[1])
		else:
			jargon = get_jargon()
			write_to_file(jargon.text.strip(), jargon_path)
			print(jargon.text.strip())
	else:
		jargon = get_jargon()
		link = jargon.find("a")
		webbrowser.open("http://www.jargon.net" + link["href"])

if __name__ == "__main__":
	main()