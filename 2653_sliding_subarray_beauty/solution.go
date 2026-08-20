// LeetCode 2653 - Sliding Subarray Beauty
// https://leetcode.com/problems/sliding-subarray-beauty/


func getSubarrayBeauty(nums []int, k int, x int) []int {
	freq := [101]int{} // offset 50 for -50..50
	ans := make([]int, len(nums)-k+1)
	for i, v := range nums {
		freq[v+50]++
		if i >= k {
			freq[nums[i-k]+50]--
		}
		if i >= k-1 {
			need := x
			val := 0
			for j := 0; j < 50; j++ {
				need -= freq[j]
				if need <= 0 {
					val = j - 50
					break
				}
			}
			ans[i-k+1] = val
		}
	}
	return ans
}
