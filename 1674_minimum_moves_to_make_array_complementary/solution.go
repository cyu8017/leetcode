// LeetCode 1674 - Minimum Moves to Make Array Complementary
// https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

func minMoves(nums []int, limit int) int {
	n := len(nums)
	d := make([]int, 2*limit+2)
	for i := 0; i < n/2; i++ {
		a, b := nums[i], nums[n-1-i]
		lo, hi := a, b
		if b < a {
			lo = b
		}
		if a > b {
			hi = a
		}
		lo++
		hi += limit
		s := a + b
		d[2] += 2
		d[lo]--
		d[s]--
		d[s+1]++
		d[hi+1]++
	}
	ans, cur := int(1e9), 0
	for s := 2; s <= 2*limit; s++ {
		cur += d[s]
		if cur < ans {
			ans = cur
		}
	}
	return ans
}
