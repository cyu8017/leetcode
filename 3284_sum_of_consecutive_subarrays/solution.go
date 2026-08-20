// LeetCode 3284 - Sum of Consecutive Subarrays
// https://leetcode.com/problems/sum-of-consecutive-subarrays/

func rangeSum(nums []int) int {
	const mod = 1000000007
	n := len(nums)
	ans := 0
	i := 0
	for i < n {
		j := i
		for j+1 < n && (nums[j+1] == nums[j]+1 || nums[j+1] == nums[j]-1) {
			j++
		}
		// sum of all subarray sums in nums[i..j]
		length := j - i + 1
		for L := i; L <= j; L++ {
			s := 0
			for R := L; R <= j; R++ {
				s += nums[R]
				ans = (ans + s) % mod
			}
		}
		_ = length
		i = j + 1
	}
	return ans
}
