// LeetCode 2154 - Keep Multiplying Found Values by Two
// https://leetcode.com/problems/keep-multiplying-found-values-by-two/

func findFinalValue(nums []int, original int) int {
	have := map[int]bool{}
	for _, x := range nums {
		have[x] = true
	}
	for have[original] {
		original *= 2
	}
	return original
}
