// LeetCode 3271 - Hash Divided String
// https://leetcode.com/problems/hash-divided-string/

func stringHash(s string, k int) string {
	out := make([]byte, 0, len(s)/k)
	for i := 0; i < len(s); i += k {
		sum := 0
		for j := i; j < i+k; j++ {
			sum += int(s[j] - 'a')
		}
		out = append(out, byte('a'+sum%26))
	}
	return string(out)
}
