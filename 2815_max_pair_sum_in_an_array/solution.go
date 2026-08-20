// LeetCode 2815 - Max Pair Sum in an Array
// https://leetcode.com/problems/max-pair-sum-in-an-array/

func maxSum(nums []int) int {
	best := map[int]int{}
	ans := -1
	for _, v := range nums {
		x := v
		md := 0
		for x > 0 {
			d := x % 10
			if d > md {
				md = d
			}
			x /= 10
		}
		if prev, ok := best[md]; ok {
			if prev+v > ans {
				ans = prev + v
			}
			if v > prev {
				best[md] = v
			}
		} else {
			best[md] = v
		}
	}
	return ans
}
