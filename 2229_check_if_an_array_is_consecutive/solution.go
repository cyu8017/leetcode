// LeetCode 2229 - Check if an Array Is Consecutive
// https://leetcode.com/problems/check-if-an-array-is-consecutive/

func isConsecutive(nums []int) bool {
	mn, mx := nums[0], nums[0]
	seen := map[int]bool{}
	for _, x := range nums {
		if seen[x] {
			return false
		}
		seen[x] = true
		if x < mn {
			mn = x
		}
		if x > mx {
			mx = x
		}
	}
	return mx-mn+1 == len(nums)
}
