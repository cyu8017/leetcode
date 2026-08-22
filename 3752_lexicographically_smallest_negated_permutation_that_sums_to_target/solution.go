// LeetCode 3752 - Lexicographically Smallest Negated Permutation that Sums to Target
// https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

func lexicographicallySmallest(n int, target int64) []int {
	total := int64(n) * int64(n+1) / 2
	if target < -total || target > total || (total-target)%2 != 0 {
		return []int{}
	}

	remaining := (total - target) / 2
	negative := make([]bool, n+1)
	for value := n; value >= 1; value-- {
		if int64(value) <= remaining {
			negative[value] = true
			remaining -= int64(value)
		}
	}

	answer := make([]int, 0, n)
	for value := n; value >= 1; value-- {
		if negative[value] {
			answer = append(answer, -value)
		}
	}
	for value := 1; value <= n; value++ {
		if !negative[value] {
			answer = append(answer, value)
		}
	}
	return answer
}