// LeetCode 2089 - Find Target Indices After Sorting Array
// https://leetcode.com/problems/find-target-indices-after-sorting-array/

func targetIndices(nums []int, target int) []int {
	less, eq := 0, 0
	for _, x := range nums {
		if x < target {
			less++
		} else if x == target {
			eq++
		}
	}
	ans := make([]int, eq)
	for i := 0; i < eq; i++ {
		ans[i] = less + i
	}
	return ans
}
