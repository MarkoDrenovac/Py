#!/usr/bin/env python3
import psutil


def bytes_to_GB(bytes):
    gb = bytes/(1024*1024*1024)
    gb = round(gb, 2)
    return gb


virtual_memory = psutil.virtual_memory()


print(" Ukupno dostupno memorije :", bytes_to_GB(virtual_memory.total), "Gb")
print(" Ukupno slobodno memorije :", bytes_to_GB(virtual_memory.available), "Gb")
print(" Ukupna iskorištenost memorije :", bytes_to_GB(virtual_memory.used), "Gb")
print(" Ukupna iskorištenost u postotku :", virtual_memory.percent, "%")
print("\n")


swap = psutil.swap_memory()
print(f" Ukupno swap memorije :{bytes_to_GB(swap.total)}")
print(f" Ukupno slobodno swap memorije : {bytes_to_GB(swap.free)}")
print(f" Ukupna iskorištenost swap memorije : {bytes_to_GB(swap.used)}")
print(f" Ukupna iskorištenost swap memorije u postotku: {swap.percent}%")
