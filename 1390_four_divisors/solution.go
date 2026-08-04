// LeetCode 1390 - Four Divisors
// https://leetcode.com/problems/four-divisors/

func sumFourDivisors(nums []int) int {
	ans := 0
	for _, x := range nums {
		ds := map[int]bool{}
		for d := 1; d*d <= x; d++ {
			if x%d == 0 {
				ds[d] = true
				ds[x/d] = true
			}
			if len(ds) > 4 {
				break
			}
		}
		if len(ds) == 4 {
			for v := range ds {
				ans += v
			}
		}
	}
	return ans
}
