// LeetCode 0763 - Partition Labels
// https://leetcode.com/problems/partition-labels/

func partitionLabels(s string) []int {
	last := map[byte]int{}
	for i := 0; i < len(s); i++ {
		last[s[i]] = i
	}
	start, end := 0, 0
	answer := []int{}
	for i := 0; i < len(s); i++ {
		if last[s[i]] > end {
			end = last[s[i]]
		}
		if i == end {
			answer = append(answer, end-start+1)
			start = i + 1
		}
	}
	return answer
}
