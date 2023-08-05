#Fixing infinite loop present in the previous algorithm
#using simple mathematical formula that LCM(x, y) = x * y / GCD(x, y)
import math



def compute():
	ans = 1
	for i in range(1, 21):
		ans *= i // math.gcd(i, ans)
	return str(ans)


if __name__ == "__main__":
	print(compute())

