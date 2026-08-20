// LeetCode 3737 - Count Subarrays With Majority Element I
// https://leetcode.com/problems/count-subarrays-with-majority-element-i/

func countMajoritySubarrays(nums []int, target int) (ans int) {
	n := len(nums)
	for i := range nums {
		cnt := 0
		for j := i; j < n; j++ {
			if nums[j] == target {
				cnt++
			}
			if k := j - i + 1; cnt*2 > k {
				ans++
			}
		}
	}
	return
}
