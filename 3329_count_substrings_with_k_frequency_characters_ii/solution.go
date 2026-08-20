// LeetCode 3329 - Count Substrings With K-Frequency Characters II
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/

func numberOfSubstrings(s string, k int) int64 {
	n := len(s)
	var ans int64
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
				ans += int64(n - j)
				break
			}
		}
	}
	return ans
}
