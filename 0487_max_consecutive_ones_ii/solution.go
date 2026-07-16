// LeetCode 0487 - Max Consecutive Ones II
// https://leetcode.com/problems/max-consecutive-ones-ii/

func findMaxConsecutiveOnes(nums []int) int {
	left := 0
	best := 0
	zeros := 0
	for right, num := range nums {
		if num == 0 {
			zeros++
		}
		for zeros > 1 {
			if nums[left] == 0 {
				zeros--
			}
			left++
		}
		if right-left+1 > best {
			best = right - left + 1
		}
	}
	return best
}
