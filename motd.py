import json
from mcstatus import JavaServer
import multiprocessing
from joblib import Parallel, delayed

num_cores = multiprocessing.cpu_count()

def get_motd(ip):
	try:
                server = JavaServer.lookup(ip+":25565")
                print("MOTD of IP: {}\n\t{}".format(ip, server.status().description.replace('\n', '\n\t')))
	except:
                print(f"Timeout on {ip}")

ips = json.loads(open("masscan.json").read())
Parallel(n_jobs=num_cores)(delayed(get_motd)(ip) for ip in ips)
