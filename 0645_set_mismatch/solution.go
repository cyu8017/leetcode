// LeetCode 0645 - Set Mismatch
// https://leetcode.com/problems/set-mismatch/

func findErrorNums(nums []int) []int {
	n := len(nums)
	seen := make([]int, n+1)
	duplicate, missing := -1, -1
	for _, value := range nums {
		seen[value]++
	}
	for value := 1; value <= n; value++ {
		if seen[value] == 2 {
			duplicate = value
		} else if seen[value] == 0 {
			missing = value
		}
	}
	return []int{duplicate, missing}
}
