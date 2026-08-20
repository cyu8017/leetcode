// LeetCode 2244 - Minimum Rounds to Complete All Tasks
// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

func minimumRounds(tasks []int) int {
	freq := map[int]int{}
	for _, t := range tasks {
		freq[t]++
	}
	ans := 0
	for _, c := range freq {
		if c == 1 {
			return -1
		}
		ans += (c + 2) / 3
	}
	return ans
}
