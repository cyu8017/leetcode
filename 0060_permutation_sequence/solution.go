// LeetCode 0060 - Permutation Sequence
// https://leetcode.com/problems/permutation-sequence/

import (
	"strconv"
	"strings"
)

func getPermutation(n int, k int) string {
	numbers := make([]int, n)
	factorials := make([]int, n)
	factorials[0] = 1

	for i := 0; i < n; i++ {
		numbers[i] = i + 1
		if i > 0 {
			factorials[i] = factorials[i-1] * i
		}
	}

	k--
	var result strings.Builder

	for i := n - 1; i >= 0; i-- {
		index := k / factorials[i]
		result.WriteString(strconv.Itoa(numbers[index]))
		numbers = append(numbers[:index], numbers[index+1:]...)
		k %= factorials[i]
	}

	return result.String()
}
