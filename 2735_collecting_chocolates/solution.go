// LeetCode 2735 - Collecting Chocolates
// https://leetcode.com/problems/collecting-chocolates/


func minCost(nums []int, x int) int64 {
	n := len(nums)
	best := append([]int(nil), nums...)
	ans := int64(0)
	for _, v := range best {
		ans += int64(v)
	}
	for rot := 1; rot < n; rot++ {
		var cur int64
		for i := 0; i < n; i++ {
			v := nums[(i+rot)%n]
			if v < best[i] {
				best[i] = v
			}
			cur += int64(best[i])
		}
		cur += int64(rot) * int64(x)
		if cur < ans {
			ans = cur
		}
	}
	return ans
}
