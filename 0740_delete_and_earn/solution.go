// LeetCode 0740 - Delete and Earn
// https://leetcode.com/problems/delete-and-earn/

func deleteAndEarn(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	maxNum := nums[0]
	for _, num := range nums {
		if num > maxNum {
			maxNum = num
		}
	}
	points := make([]int, maxNum+1)
	for _, num := range nums {
		points[num] += num
	}
	take, skip := 0, 0
	for _, value := range points {
		take, skip = skip+value, max(skip, take)
	}
	return max(take, skip)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
