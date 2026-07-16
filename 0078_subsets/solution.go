// LeetCode 0078 - Subsets
// https://leetcode.com/problems/subsets/

func subsets(nums []int) [][]int {
	result := [][]int{{}}

	for _, num := range nums {
		size := len(result)
		for i := 0; i < size; i++ {
			subset := append([]int(nil), result[i]...)
			subset = append(subset, num)
			result = append(result, subset)
		}
	}

	return result
}
