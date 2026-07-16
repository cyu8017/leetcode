// LeetCode 0485 - Max Consecutive Ones
// https://leetcode.com/problems/max-consecutive-ones/

func findMaxConsecutiveOnes(nums []int) int {
	best := 0
	current := 0
	for _, num := range nums {
		if num == 1 {
			current++
			if current > best {
				best = current
			}
		} else {
			current = 0
		}
	}
	return best
}
