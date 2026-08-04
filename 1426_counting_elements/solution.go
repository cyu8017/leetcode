// LeetCode 1426 - Counting Elements
// https://leetcode.com/problems/counting-elements/

func countElements(arr []int) int {
	values := map[int]bool{}
	for _, v := range arr {
		values[v] = true
	}
	ans := 0
	for _, v := range arr {
		if values[v+1] {
			ans++
		}
	}
	return ans
}
