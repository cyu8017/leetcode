// LeetCode 0477 - Total Hamming Distance
// https://leetcode.com/problems/total-hamming-distance/

func totalHammingDistance(nums []int) int {
	total := 0
	for bit := 0; bit < 32; bit++ {
		zeros := 0
		ones := 0
		for _, value := range nums {
			if value&(1<<bit) != 0 {
				ones++
			} else {
				zeros++
			}
		}
		total += zeros * ones
	}
	return total
}
