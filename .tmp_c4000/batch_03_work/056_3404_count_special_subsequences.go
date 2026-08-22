// LeetCode 3404 - Count Special Subsequences
// https://leetcode.com/problems/count-special-subsequences/

func numberOfSubsequences(nums []int) int64 {
	n := len(nums)
	var ans int64
	// p*r == q*s with indices i<j<k<l and j>i+1 etc gaps of at least 1
	for i := 0; i < n; i++ {
		for j := i + 2; j < n; j++ {
			for k := j + 2; k < n; k++ {
				for l := k + 2; l < n; l++ {
					if int64(nums[i])*int64(nums[k]) == int64(nums[j])*int64(nums[l]) {
						ans++
					}
				}
			}
		}
	}
	return ans
}
