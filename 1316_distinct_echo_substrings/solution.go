// LeetCode 1316 - Distinct Echo Substrings
// https://leetcode.com/problems/distinct-echo-substrings/

func distinctEchoSubstrings(text string) int {
	n := len(text)
	const mod1, mod2, bas int64 = 1000000007, 1000000009, 911382323
	h1 := make([]int64, n+1)
	h2 := make([]int64, n+1)
	p1 := make([]int64, n+1)
	p2 := make([]int64, n+1)
	p1[0], p2[0] = 1, 1
	for i := 0; i < n; i++ {
		code := int64(text[i])
		h1[i+1] = (h1[i]*bas + code) % mod1
		h2[i+1] = (h2[i]*bas + code) % mod2
		p1[i+1] = p1[i] * bas % mod1
		p2[i+1] = p2[i] * bas % mod2
	}
	hashed := func(left, right int) (int64, int64) {
		length := right - left
		a := (h1[right] - h1[left]*p1[length]%mod1 + mod1) % mod1
		b := (h2[right] - h2[left]*p2[length]%mod2 + mod2) % mod2
		return a, b
	}
	type key struct {
		len int
		a, b int64
	}
	echoes := map[key]bool{}
	for half := 1; half <= n/2; half++ {
		for left := 0; left <= n-2*half; left++ {
			a1, b1 := hashed(left, left+half)
			a2, b2 := hashed(left+half, left+2*half)
			if a1 == a2 && b1 == b2 {
				a, b := hashed(left, left+2*half)
				echoes[key{2 * half, a, b}] = true
			}
		}
	}
	return len(echoes)
}
