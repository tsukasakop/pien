KANA = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ"

def pien():
	points = [ord(char) for char in "ぴえん"]
	pi = KANA.index("ぴ")
	e = KANA.index("え")
	n = KANA.index("ん")
	i = 0
	l = len(KANA)
	while pi - i >= 0 and e + i < l:
		input("".join([KANA[pi-i],KANA[e+i],KANA[n]]))
		i+=1;

def main():
	pien()

if __name__ == "__main__":
	main()
