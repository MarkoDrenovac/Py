import psutil


print(" Broj corova :", psutil.cpu_count(logical=False))
print(" Ukupan broj corova :", psutil.cpu_count(logical=True))
print("\n")


cpu_frequency = psutil.cpu_freq()
print(f" Max frkvencija : {cpu_frequency.max:.2f}Mhz")
print(f" Min frkvencija : {cpu_frequency.min:.2f}Mhz")
print(f" Trenutna frkvencija : {cpu_frequency.current:.2f}Mhz")
print("\n")

for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f" CPU iskorištenost po core-u {i} : {percentage}%")
    print(f" Ukupna CPU iskorištenost : {psutil.cpu_percent()}%")
