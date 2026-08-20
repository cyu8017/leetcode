// LeetCode 2762 - Continuous Subarrays
// https://leetcode.com/problems/continuous-subarrays/

func continuousSubarrays(nums []int) int64 {
	ans := int64(0)
	left := 0
	freq := map[int]int{}
	for right, v := range nums {
		freq[v]++
		for {
			mn, mx := v, v
			for k := range freq {
				if k < mn {
					mn = k
				}
				if k > mx {
					mx = k
				}
			}
			if mx-mn <= 2 {
				break
			}
			freq[nums[left]]--
			if freq[nums[left]] == 0 {
				delete(freq, nums[left])
			}
			left++
		}
		ans += int64(right - left + 1)
	}
	return ans
}
