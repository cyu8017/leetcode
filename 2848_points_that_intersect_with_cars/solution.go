// LeetCode 2848 - Points That Intersect With Cars
// https://leetcode.com/problems/points-that-intersect-with-cars/

func numberOfPoints(nums [][]int) int {
	cov := [102]int{}
	for _, r := range nums {
		for x := r[0]; x <= r[1]; x++ {
			cov[x] = 1
		}
	}
	ans := 0
	for _, v := range cov {
		ans += v
	}
	return ans
}
