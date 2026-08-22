// LeetCode 3432 - Count Partitions With Even Sum Difference
// https://leetcode.com/problems/count-partitions-with-even-sum-difference/

func countPartitions(nums []int) int {
	total := 0
	for _, x := range nums {
		total += x
	}
	ans, left := 0, 0
	for i := 0; i < len(nums)-1; i++ {
		left += nums[i]
		if (left-(total-left))%2 == 0 {
			ans++
		}
	}
	return ans
}
