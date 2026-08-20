// LeetCode 2962 - Count Subarrays Where Max Element Appears at Least K Times
// https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

func countSubarrays(nums []int, k int) int64 {
	mx := nums[0]
	for _, v := range nums {
		if v > mx {
			mx = v
		}
	}
	var ans int64
	cnt, left := 0, 0
	for right, v := range nums {
		if v == mx {
			cnt++
		}
		for cnt >= k {
			if nums[left] == mx {
				cnt--
			}
			left++
		}
		ans += int64(left)
	}
	return ans
}
