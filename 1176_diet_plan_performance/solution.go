// LeetCode 1176 - Diet Plan Performance
// https://leetcode.com/problems/diet-plan-performance/

func dietPlanPerformance(calories []int, k int, lower int, upper int) int {
	window := 0
	for i := 0; i < k; i++ {
		window += calories[i]
	}
	ans := 0
	if window < lower {
		ans--
	} else if window > upper {
		ans++
	}
	for i := k; i < len(calories); i++ {
		window += calories[i] - calories[i-k]
		if window < lower {
			ans--
		} else if window > upper {
			ans++
		}
	}
	return ans
}
