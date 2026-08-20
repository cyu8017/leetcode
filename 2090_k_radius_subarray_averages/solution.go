// LeetCode 2090 - K Radius Subarray Averages
// https://leetcode.com/problems/k-radius-subarray-averages/

func getAverages(nums []int, k int) []int {
	n := len(nums)
	ans := make([]int, n)
	for i := range ans {
		ans[i] = -1
	}
	if 2*k+1 > n {
		return ans
	}
	var sum int64
	for i := 0; i < 2*k+1; i++ {
		sum += int64(nums[i])
	}
	ans[k] = int(sum / int64(2*k+1))
	for i := k + 1; i+k < n; i++ {
		sum += int64(nums[i+k] - nums[i-k-1])
		ans[i] = int(sum / int64(2*k+1))
	}
	return ans
}
