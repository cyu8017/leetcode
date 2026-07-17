// LeetCode 1781 - Sum of Beauty of All Substrings
// https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

func beautySum(s string) int {
	ans := 0
	for i := 0; i < len(s); i++ {
		var freq [26]int
		for j := i; j < len(s); j++ {
			freq[s[j]-'a']++
			lo := int(^uint(0) >> 1)
			hi := 0
			for _, count := range freq {
				if count > 0 {
					if count < lo {
						lo = count
					}
					if count > hi {
						hi = count
					}
				}
			}
			ans += hi - lo
		}
	}
	return ans
}
