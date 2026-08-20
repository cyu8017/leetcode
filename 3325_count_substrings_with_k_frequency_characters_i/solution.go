// LeetCode 3325 - Count Substrings With K-Frequency Characters I
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/

func numberOfSubstrings(s string, k int) int {
	n := len(s)
	ans := 0
	for i := 0; i < n; i++ {
		freq := [26]int{}
		for j := i; j < n; j++ {
			freq[s[j]-'a']++
			ok := false
			for _, f := range freq {
				if f >= k {
					ok = true
					break
				}
			}
			if ok {
				ans += n - j
				break
			}
		}
	}
	return ans
}
