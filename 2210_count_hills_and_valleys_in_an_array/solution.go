// LeetCode 2210 - Count Hills and Valleys in an Array
// https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

func countHillValley(nums []int) int {
	compact := []int{nums[0]}
	for i := 1; i < len(nums); i++ {
		if nums[i] != compact[len(compact)-1] {
			compact = append(compact, nums[i])
		}
	}
	ans := 0
	for i := 1; i+1 < len(compact); i++ {
		if (compact[i] > compact[i-1] && compact[i] > compact[i+1]) || (compact[i] < compact[i-1] && compact[i] < compact[i+1]) {
			ans++
		}
	}
	return ans
}
