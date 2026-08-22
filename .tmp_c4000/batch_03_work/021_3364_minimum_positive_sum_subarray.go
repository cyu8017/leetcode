// LeetCode 3364 - Minimum Positive Sum Subarray
// https://leetcode.com/problems/minimum-positive-sum-subarray/

func minimumSumSubarray(nums []int, l int, r int) int {
	n := len(nums)
	pref := make([]int, n+1)
	for i, x := range nums {
		pref[i+1] = pref[i] + x
	}
	ans := int(1e18)
	found := false
	for i := 0; i < n; i++ {
		for length := l; length <= r && i+length <= n; length++ {
			s := pref[i+length] - pref[i]
			if s > 0 && s < ans {
				ans = s
				found = true
			}
		}
	}
	if !found {
		return -1
	}
	return ans
}
