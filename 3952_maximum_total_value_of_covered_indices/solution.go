// LeetCode 3952 - Maximum Total Value of Covered Indices
// https://leetcode.com/problems/maximum-total-value-of-covered-indices/

func maxTotalValue(nums []int, s string) int {
	answer := 0
	for i := 0; i < len(s); {
		if s[i] == '0' {
			i++
			continue
		}
		start := i
		for i < len(s) && s[i] == '1' {
			i++
		}
		end := i - 1
		if start == 0 {
			for index := start; index <= end; index++ {
				answer += nums[index]
			}
			continue
		}
		minimum := nums[start-1]
		total := 0
		for index := start - 1; index <= end; index++ {
			total += nums[index]
			if nums[index] < minimum {
				minimum = nums[index]
			}
		}
		answer += total - minimum
	}
	return answer
}