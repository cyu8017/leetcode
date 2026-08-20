// LeetCode 2865 - Beautiful Towers I
// https://leetcode.com/problems/beautiful-towers-i/

func maximumSumOfHeights(heights []int) int64 {
	n := len(heights)
	var ans int64
	for peak := 0; peak < n; peak++ {
		var sum int64 = int64(heights[peak])
		mn := heights[peak]
		for i := peak - 1; i >= 0; i-- {
			if heights[i] < mn {
				mn = heights[i]
			}
			sum += int64(mn)
		}
		mn = heights[peak]
		for i := peak + 1; i < n; i++ {
			if heights[i] < mn {
				mn = heights[i]
			}
			sum += int64(mn)
		}
		if sum > ans {
			ans = sum
		}
	}
	return ans
}
