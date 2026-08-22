// LeetCode 3796 - Find Maximum Value in a Constrained Sequence
// https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

func maxValue(n int, restrictions [][]int, diff []int) int {
	const infinity = int(^uint(0) >> 2)
	bound := make([]int, n)
	for i := range bound {
		bound[i] = infinity
	}
	bound[0] = 0
	for _, restriction := range restrictions {
		bound[restriction[0]] = restriction[1]
	}
	for i := 1; i < n; i++ {
		if candidate := bound[i-1] + diff[i-1]; candidate < bound[i] {
			bound[i] = candidate
		}
	}
	for i := n - 2; i >= 0; i-- {
		if candidate := bound[i+1] + diff[i]; candidate < bound[i] {
			bound[i] = candidate
		}
	}

	answer := 0
	for _, value := range bound {
		if value > answer {
			answer = value
		}
	}
	return answer
}