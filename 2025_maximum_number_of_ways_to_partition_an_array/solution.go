// LeetCode 2025 - Maximum Number of Ways to Partition an Array
// https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

func waysToPartition(nums []int, k int) int {
	n := len(nums)
	pref := make([]int64, n)
	pref[0] = int64(nums[0])
	for i := 1; i < n; i++ {
		pref[i] = pref[i-1] + int64(nums[i])
	}
	total := pref[n-1]
	right := map[int64]int{}
	for i := 0; i < n-1; i++ {
		right[pref[i]]++
	}
	ans := 0
	if total%2 == 0 {
		ans = right[total/2]
	}
	left := map[int64]int{}
	for i := 0; i < n; i++ {
		diff := int64(k - nums[i])
		newTotal := total + diff
		cur := 0
		if newTotal%2 == 0 {
			half := newTotal / 2
			cur = left[half] + right[half-diff]
		}
		if cur > ans {
			ans = cur
		}
		if i < n-1 {
			left[pref[i]]++
			right[pref[i]]--
		}
	}
	return ans
}
