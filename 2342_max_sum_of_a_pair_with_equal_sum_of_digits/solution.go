// LeetCode 2342 - Max Sum of a Pair With Equal Sum of Digits
// https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

func maximumSum(nums []int) int {
	best := map[int]int{}
	ans := -1
	digitSum := func(x int) int {
		s := 0
		for x > 0 {
			s += x % 10
			x /= 10
		}
		return s
	}
	for _, x := range nums {
		ds := digitSum(x)
		if v, ok := best[ds]; ok {
			if v+x > ans {
				ans = v + x
			}
			if x > v {
				best[ds] = x
			}
		} else {
			best[ds] = x
		}
	}
	return ans
}
