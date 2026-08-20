// LeetCode 2610 - Convert an Array Into a 2D Array With Conditions
// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/


func findMatrix(nums []int) [][]int {
	freq := map[int]int{}
	ans := [][]int{}
	for _, x := range nums {
		f := freq[x]
		if f == len(ans) {
			ans = append(ans, []int{})
		}
		ans[f] = append(ans[f], x)
		freq[x]++
	}
	return ans
}
