// LeetCode 3334 - Find the Maximum Factor Score of Array
// https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

func maxScore(nums []int) int64 {
	n := len(nums)
	gcdAll := nums[0]
	lcmAll := nums[0]
	for i := 1; i < n; i++ {
		gcdAll = gcd3334(gcdAll, nums[i])
		lcmAll = lcm3334(lcmAll, nums[i])
	}
	ans := int64(gcdAll) * int64(lcmAll)
	for skip := 0; skip < n; skip++ {
		g, l := 0, 1
		first := true
		for i, x := range nums {
			if i == skip {
				continue
			}
			if first {
				g, l = x, x
				first = false
			} else {
				g = gcd3334(g, x)
				l = lcm3334(l, x)
			}
		}
		if first {
			continue
		}
		v := int64(g) * int64(l)
		if v > ans {
			ans = v
		}
	}
	return ans
}

func gcd3334(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
func lcm3334(a, b int) int {
	return a / gcd3334(a, b) * b
}
