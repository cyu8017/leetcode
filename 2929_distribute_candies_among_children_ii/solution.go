// LeetCode 2929 - Distribute Candies Among Children II
// https://leetcode.com/problems/distribute-candies-among-children-ii/

func distributeCandies(n int, limit int) int64 {
	comb2 := func(x int64) int64 {
		if x < 0 {
			return 0
		}
		return (x + 1) * (x + 2) / 2
	}
	ans := comb2(int64(n))
	ans -= 3 * comb2(int64(n-(limit+1)))
	ans += 3 * comb2(int64(n-2*(limit+1)))
	ans -= comb2(int64(n-3*(limit+1)))
	return ans
}
