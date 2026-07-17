// LeetCode 1860 - Incremental Memory Leak
// https://leetcode.com/problems/incremental-memory-leak/

func memLeak(memory1 int, memory2 int) []int {
	second := 1

	for memory1 >= second || memory2 >= second {
		if memory1 >= memory2 {
			memory1 -= second
		} else {
			memory2 -= second
		}
		second++
	}

	return []int{second, memory1, memory2}
}
