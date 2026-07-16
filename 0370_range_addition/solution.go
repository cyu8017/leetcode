// LeetCode 0370 - Range Addition
// https://leetcode.com/problems/range-addition/

func getModifiedArray(length int, updates [][]int) []int {
	diff := make([]int, length+1)

	for _, update := range updates {
		start := update[0]
		end := update[1]
		inc := update[2]
		diff[start] += inc
		if end+1 < len(diff) {
			diff[end+1] -= inc
		}
	}

	result := make([]int, length)
	running := 0
	for index := 0; index < length; index++ {
		running += diff[index]
		result[index] = running
	}

	return result
}
