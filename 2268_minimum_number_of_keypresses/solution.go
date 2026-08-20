// LeetCode 2268 - Minimum Number of Keypresses
// https://leetcode.com/problems/minimum-number-of-keypresses/

import "sort"

func minimumKeypresses(s string) int {
	freq := make([]int, 26)
	for i := 0; i < len(s); i++ {
		freq[s[i]-'a']++
	}
	sort.Slice(freq, func(i, j int) bool { return freq[i] > freq[j] })
	ans := 0
	for i, f := range freq {
		if f == 0 {
			break
		}
		ans += f * (i/9 + 1)
	}
	return ans
}
