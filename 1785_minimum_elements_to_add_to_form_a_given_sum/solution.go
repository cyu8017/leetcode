// LeetCode 1785 - Minimum Elements to Add to Form a Given Sum
// https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/

func minElements(nums []int, limit int, goal int) int {
	sum := 0
	for _, num := range nums {
		sum += num
	}
	diff := sum - goal
	if diff < 0 {
		diff = -diff
	}
	return (diff + limit - 1) / limit
}
