// LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
// https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

func missingInteger(nums []int) int {
	sum := nums[0]
	for i := 1; i < len(nums) && nums[i] == nums[i-1]+1; i++ {
		sum += nums[i]
	}
	seen := map[int]bool{}
	for _, v := range nums {
		seen[v] = true
	}
	for {
		if !seen[sum] {
			return sum
		}
		sum++
	}
}
