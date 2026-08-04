// LeetCode 1228 - Missing Number In Arithmetic Progression
// https://leetcode.com/problems/missing-number-in-arithmetic-progression/

func missingNumber(arr []int) int {
	difference := (arr[len(arr)-1] - arr[0]) / len(arr)
	for i := 1; i < len(arr); i++ {
		expected := arr[0] + i*difference
		if arr[i] != expected {
			return expected
		}
	}
	return arr[0]
}
