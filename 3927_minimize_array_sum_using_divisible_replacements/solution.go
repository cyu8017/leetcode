// LeetCode 3927 - Minimize Array Sum Using Divisible Replacements
// https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/

func minArraySum(nums []int) int64 {
	maximum := 0
	present := make([]bool, 100001)
	for _, value := range nums {
		present[value] = true
		if value > maximum {
			maximum = value
		}
	}

	best := make([]int, maximum+1)
	for divisor := 1; divisor <= maximum; divisor++ {
		if !present[divisor] {
			continue
		}
		for multiple := divisor; multiple <= maximum; multiple += divisor {
			if best[multiple] == 0 {
				best[multiple] = divisor
			}
		}
	}

	var answer int64
	for _, value := range nums {
		answer += int64(best[value])
	}
	return answer
}