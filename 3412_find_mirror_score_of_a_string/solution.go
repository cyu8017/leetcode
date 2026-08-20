// LeetCode 3412 - Find Mirror Score of a String
// https://leetcode.com/problems/find-mirror-score-of-a-string/

func calculateScore(s string) int64 {
	stacks := make([][]int, 26)
	var ans int64
	for i, c := range s {
		ci := int(c - 'a')
		mir := 25 - ci
		if len(stacks[mir]) > 0 {
			j := stacks[mir][len(stacks[mir])-1]
			stacks[mir] = stacks[mir][:len(stacks[mir])-1]
			ans += int64(i - j)
		} else {
			stacks[ci] = append(stacks[ci], i)
		}
	}
	return ans
}
