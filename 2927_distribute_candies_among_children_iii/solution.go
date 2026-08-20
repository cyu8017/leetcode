// LeetCode 2927 - Distribute Candies Among Children III
// https://leetcode.com/problems/distribute-candies-among-children-iii/

func distributeCandies(n int, limit int) int64 {
	comb := func(x int64) int64 {
		if x < 2 {
			return 0
		}
		return x * (x - 1) / 2
	}
	ans := comb(int64(n) + 2)
	ans -= 3 * comb(int64(n-limit) + 1)
	ans += 3 * comb(int64(n-2*(limit+1)) + 2)
	ans -= comb(int64(n-3*(limit+1)) + 2)
	if ans < 0 {
		ans = 0
	}
	return ans
}
