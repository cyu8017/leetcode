// LeetCode 2455 - Average Value of Even Numbers That Are Divisible by Three
// https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

func averageValue(nums []int) int {
	sum, cnt := 0, 0
	for _, x := range nums {
		if x%6 == 0 {
			sum += x
			cnt++
		}
	}
	if cnt == 0 {
		return 0
	}
	return sum / cnt
}
