// LeetCode 0526 - Beautiful Arrangement
// https://leetcode.com/problems/beautiful-arrangement/

func countArrangement(n int) int {
	count := 0
	used := make([]bool, n+1)

	var backtrack func(index int)
	backtrack = func(index int) {
		if index == n+1 {
			count++
			return
		}
		for num := 1; num <= n; num++ {
			if used[num] {
				continue
			}
			if index%num == 0 || num%index == 0 {
				used[num] = true
				backtrack(index + 1)
				used[num] = false
			}
		}
	}

	backtrack(1)
	return count
}
