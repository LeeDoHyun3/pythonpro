def frequency_anaytic(s):
	d = {}
	for c in s:
		if c in d:
			d[c] += 1
		else:
			d[c] = 1

	d = sorted(d.items())
	for dd in d:
		print(dd[0], dd[1])
if __name__ == "__main__":
	msg = input('input your message: ')
	frequency_anaytic(msg)
