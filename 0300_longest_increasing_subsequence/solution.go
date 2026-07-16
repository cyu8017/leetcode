// LeetCode 0300 - Longest Increasing Subsequence
// https://leetcode.com/problems/longest-increasing-subsequence/

func lengthOfLIS(nums []int) int {
	piles := make([]int, 0)
	for _, num := range nums {
		left, right := 0, len(piles)
		for left < right {
			mid := left + (right-left)/2
			if piles[mid] < num {
				left = mid + 1
			} else {
				right = mid
			}
		}
		if left == len(piles) {
			piles = append(piles, num)
		} else {
			piles[left] = num
		}
	}
	return len(piles)
}
