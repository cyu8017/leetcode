// LeetCode 1470 - Shuffle the Array
// https://leetcode.com/problems/shuffle-the-array/

func shuffle(nums []int, n int) []int {
	answer := make([]int, 0, 2*n)
	for i := 0; i < n; i++ {
		answer = append(answer, nums[i], nums[i+n])
	}
	return answer
}
