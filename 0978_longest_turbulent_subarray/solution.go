// LeetCode 0978 - Longest Turbulent Subarray
// https://leetcode.com/problems/longest-turbulent-subarray/

func maxTurbulenceSize(arr []int) int {
	ans, cur := 1, 1
	for i := 1; i < len(arr); i++ {
		if arr[i] == arr[i-1] {
			cur = 1
		} else if i == 1 || (arr[i]-arr[i-1])*(arr[i-1]-arr[i-2]) < 0 {
			cur++
		} else {
			cur = 2
		}
		if cur > ans {
			ans = cur
		}
	}
	return ans
}
