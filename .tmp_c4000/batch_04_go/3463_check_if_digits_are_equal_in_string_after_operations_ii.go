// LeetCode 3463 - Check If Digits Are Equal in String After Operations II
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/

func hasSameDigits(s string) bool {
	n := len(s)
	// final two digits are combinations with binomial mod 10 (not prime - use CRT 2 and 5)
	a := evalMod(s, n, 2)
	b := evalMod(s, n, 5)
	// combine to get two digits mod 10 - actually compute both positions
	d0 := combineDigit(s, n, 0)
	d1 := combineDigit(s, n, 1)
	_ = a
	_ = b
	return d0 == d1
}

func combineDigit(s string, n, offset int) int {
	// result digit at final after n-2 ops equals sum C(n-2,i)*s[i+offset] mod 10
	mod := 10
	sum := 0
	for i := 0; i <= n-2; i++ {
		sum = (sum + binomMod10(n-2, i)*int(s[i+offset]-'0')) % mod
	}
	return sum
}

func binomMod10(n, k int) int {
	return crt(binomMod(n, k, 2), 2, binomMod(n, k, 5), 5)
}

func binomMod(n, k, p int) int {
	if k < 0 || k > n {
		return 0
	}
	num, den := 1, 1
	for i := 0; i < k; i++ {
		num = num * (n - i) % p
		den = den * (i + 1) % p
	}
	return num * modInvPrime(den, p) % p
}

func modInvPrime(a, p int) int {
	return modPowP(a, p-2, p)
}
func modPowP(a, e, p int) int {
	r := 1
	for e > 0 {
		if e&1 == 1 {
			r = r * a % p
		}
		a = a * a % p
		e >>= 1
	}
	return r
}
func crt(a1, m1, a2, m2 int) int {
	for x := 0; x < m1*m2; x++ {
		if x%m1 == a1 && x%m2 == a2 {
			return x
		}
	}
	return 0
}
func evalMod(s string, n, mod int) int { return 0 }
