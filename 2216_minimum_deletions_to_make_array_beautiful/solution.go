// LeetCode 2216 - Minimum Deletions to Make Array Beautiful
// https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

func minDeletion(nums []int) int {
	ans := 0
	i := 0
	for i+1 < len(nums) {
		if nums[i] == nums[i+1] {
			ans++
			i++
		} else {
			i += 2
		}
	}
	if (len(nums)-ans)%2 == 1 {
		ans++
	}
	return ans
}
