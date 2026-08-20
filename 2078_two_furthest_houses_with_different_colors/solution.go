// LeetCode 2078 - Two Furthest Houses With Different Colors
// https://leetcode.com/problems/two-furthest-houses-with-different-colors/

func maxDistance(colors []int) int {
	n := len(colors)
	ans := 0
	for i := 0; i < n; i++ {
		if colors[i] != colors[0] && i > ans {
			ans = i
		}
		if colors[i] != colors[n-1] && n-1-i > ans {
			ans = n - 1 - i
		}
	}
	return ans
}
