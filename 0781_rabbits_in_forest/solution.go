// LeetCode 0781 - Rabbits in Forest
// https://leetcode.com/problems/rabbits-in-forest/

func numRabbits(answers []int) int {
	freq := map[int]int{}
	for _, a := range answers {
		freq[a]++
	}
	total := 0
	for answer, count := range freq {
		group := answer + 1
		groups := (count + group - 1) / group
		total += groups * group
	}
	return total
}
