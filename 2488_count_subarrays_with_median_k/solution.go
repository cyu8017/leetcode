// LeetCode 2488 - Count Subarrays With Median K
// https://leetcode.com/problems/count-subarrays-with-median-k/

func countSubarrays(nums []int, k int) int {
	pos := 0
	for i, x := range nums {
		if x == k {
			pos = i
			break
		}
	}
	bal := map[int]int{0: 1}
	cur := 0
	for i := pos - 1; i >= 0; i-- {
		if nums[i] < k {
			cur--
		} else {
			cur++
		}
		bal[cur]++
	}
	ans := bal[0] + bal[1]
	cur = 0
	for i := pos + 1; i < len(nums); i++ {
		if nums[i] < k {
			cur--
		} else {
			cur++
		}
		ans += bal[-cur] + bal[1-cur]
	}
	return ans
}
