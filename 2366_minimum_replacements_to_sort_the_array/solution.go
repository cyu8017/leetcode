// LeetCode 2366 - Minimum Replacements to Sort the Array
// https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

func minimumReplacement(nums []int) int64 {
	var ans int64
	n := len(nums)
	prev := nums[n-1]
	for i := n - 2; i >= 0; i-- {
		if nums[i] <= prev {
			prev = nums[i]
			continue
		}
		parts := (nums[i] + prev - 1) / prev
		ans += int64(parts - 1)
		prev = nums[i] / parts
	}
	return ans
}
