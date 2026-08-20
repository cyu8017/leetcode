// LeetCode 2765 - Longest Alternating Subarray
// https://leetcode.com/problems/longest-alternating-subarray/

func alternatingSubarray(nums []int) int {
	ans := -1
	n := len(nums)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			diff := j - i
			expect := 1
			if diff%2 == 0 {
				expect = -1
			}
			if nums[j]-nums[j-1] != expect {
				break
			}
			if nums[i+1]-nums[i] != 1 {
				break
			}
			if j-i+1 > ans {
				ans = j - i + 1
			}
		}
	}
	return ans
}
