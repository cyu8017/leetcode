// LeetCode 2156 - Find Substring With Given Hash Value
// https://leetcode.com/problems/find-substring-with-given-hash-value/

func subStrHash(s string, power int, modulo int, k int, hashValue int) string {
	n := len(s)
	var pk int64 = 1
	for i := 0; i < k-1; i++ {
		pk = pk * int64(power) % int64(modulo)
	}
	var h int64
	ans := 0
	for i := n - 1; i >= n-k; i-- {
		h = (h*int64(power) + int64(s[i]-'a'+1)) % int64(modulo)
	}
	if h == int64(hashValue) {
		ans = n - k
	}
	for i := n - k - 1; i >= 0; i-- {
		h = (h - int64(s[i+k]-'a'+1)*pk%int64(modulo) + int64(modulo)) % int64(modulo)
		h = (h*int64(power) + int64(s[i]-'a'+1)) % int64(modulo)
		if h == int64(hashValue) {
			ans = i
		}
	}
	return s[ans : ans+k]
}
