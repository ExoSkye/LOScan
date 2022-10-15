with open("masscan.out") as f:
	with open("masscan.json", mode = "w") as g:
		text = f.read()
		text = text.replace("Discovered open port 25565/tcp on ",'"')
		text = text.replace("\n",'",\n')
		text = text.replace(" ","")
		text = "[" + text[:-2] + "]"
		g.write(text)
