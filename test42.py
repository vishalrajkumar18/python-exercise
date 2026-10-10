import struct
# imports struct module to inspect pointer size
bit_mode = struct.calcsize("P") * 8
# calculates pointer size in bytes and multiplies by 8 to get architecture bit size
print(f"Python is running in {bit_mode}bit mode.")
# displays 32bit or 64bit
