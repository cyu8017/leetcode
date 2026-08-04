// LeetCode 1399 - Count Largest Group
// https://leetcode.com/problems/count-largest-group/

func countLargestGroup(n int) int {
	digitSum := func(x int) int {
		s := 0
		for x > 0 {
			s += x % 10
			x /= 10
		}
		return s
	}
	c := map[int]int{}
	mx := 0
	for x := 1; x <= n; x++ {
		ds := digitSum(x)
		c[ds]++
		if c[ds] > mx {
			mx = c[ds]
		}
	}
	ans := 0
	for _, v := range c {
		if v == mx {
			ans++
		}
	}
	return ans
}
