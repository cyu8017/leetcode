// LeetCode 0351 - Android Unlock Patterns
// https://leetcode.com/problems/android-unlock-patterns/

func numberOfPatterns(m int, n int) int {
	jumps := [81]int{
		-1, -1, 1, -1, -1, -1, 3, -1, 4,
		-1, -1, -1, 2, -1, 4, -1, -1, -1,
		1, -1, -1, -1, 6, -1, -1, -1, 5,
		-1, 2, -1, -1, -1, 5, -1, 6, -1,
		-1, -1, 4, -1, -1, -1, 7, -1, 8,
		-1, -1, -1, 5, -1, -1, -1, 8, -1,
		3, -1, 7, -1, -1, -1, -1, -1, 7,
		-1, -1, -1, 6, -1, 8, -1, -1, -1,
		4, -1, 5, -1, -1, -1, 7, -1, -1,
	}

	var isValid func(visited int, last int, nextCell int) bool
	isValid = func(visited int, last int, nextCell int) bool {
		if visited&(1<<nextCell) != 0 {
			return false
		}

		middle := jumps[last*9+nextCell]
		if middle >= 0 {
			return visited&(1<<middle) == 0
		}

		return abs(last/3-nextCell/3) <= 1 && abs(last%3-nextCell%3) <= 1
	}

	var dfs func(visited int, last int, length int) int
	dfs = func(visited int, last int, length int) int {
		if length > n {
			return 0
		}

		count := 0
		if m <= length && length <= n {
			count = 1
		}

		for nextCell := 0; nextCell < 9; nextCell++ {
			if isValid(visited, last, nextCell) {
				count += dfs(visited|(1<<nextCell), nextCell, length+1)
			}
		}

		return count
	}

	return dfs(1<<0, 0, 1)*4 + dfs(1<<1, 1, 1)*4 + dfs(1<<4, 4, 1)
}

func abs(value int) int {
	if value < 0 {
		return -value
	}
	return value
}
