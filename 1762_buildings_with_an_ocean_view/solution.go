// LeetCode 1762 - Buildings With an Ocean View
// https://leetcode.com/problems/buildings-with-an-ocean-view/

func findBuildings(heights []int) []int {
	ans := []int{}
	tallest := 0
	for i := len(heights) - 1; i >= 0; i-- {
		if heights[i] > tallest {
			ans = append(ans, i)
			tallest = heights[i]
		}
	}
	for l, r := 0, len(ans)-1; l < r; l, r = l+1, r-1 {
		ans[l], ans[r] = ans[r], ans[l]
	}
	return ans
}
