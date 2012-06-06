from luks import LuksFile
import sys, getpass

if len(sys.argv) < 2:
	print "Usage: create.py <file> [stripes] [file to read]"
	sys.exit(1)

f = open(sys.argv[1], "wb+")

luks = LuksFile()

stripes = 4000
if len(sys.argv) > 2:
	stripes = int(sys.argv[2])

luks.create(f, "aes", "cbc-essiv:sha256", "sha1", 16, stripes)

pwd = getpass.getpass()
luks.set_key(0, pwd, 10000, stripes)

if len(sys.argv) > 3:
	f2 = open(sys.argv[3], "r")
	data = f2.read()
	padlen = 512 - (len(data) % 512)
	data += " " * padlen
	luks.encrypt_data(0, data)

else:
	data = "this is really cool:"
	data += "5#" * ((512-len(data))/2)

	luks.encrypt_data(0, data)
	luks.encrypt_data(512, data)
	luks.encrypt_data(1024, data)
	luks.truncate(512*3)

luks.close()
