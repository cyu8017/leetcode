// LeetCode 1299 - Replace Elements with Greatest Element on Right Side
// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

func replaceElements(arr []int) []int {
	greatest := -1
	for i := len(arr) - 1; i >= 0; i-- {
		arr[i], greatest = greatest, max(greatest, arr[i])
	}
	return arr
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
