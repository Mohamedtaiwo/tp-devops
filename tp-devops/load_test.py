import urllib.request
import time

url = "http://localhost:5000/"
n = 100
start = time.time()

for i in range(n):
    urllib.request.urlopen(url)

total = time.time() - start
print(f"Requetes: {n}")
print(f"Temps total: {round(total, 2)}s")
print(f"Requests/sec: {round(n/total, 2)}")
print(f"Average: {round(total/n*1000, 2)}ms")