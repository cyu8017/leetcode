// LeetCode 2928 - Distribute Candies Among Children I
// https://leetcode.com/problems/distribute-candies-among-children-i/

func distributeCandies(n int, limit int) int {
	ans := 0
	for i := 0; i <= limit; i++ {
		for j := 0; j <= limit; j++ {
			k := n - i - j
			if k >= 0 && k <= limit {
				ans++
			}
		}
	}
	return ans
}
