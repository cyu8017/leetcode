// LeetCode 2841 - Maximum Sum of Almost Unique Subarray
// https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

func maxSum(nums []int, m int, k int) int64 {
	freq := map[int]int{}
	var sum, ans int64
	for i, v := range nums {
		freq[v]++
		sum += int64(v)
		if i >= k {
			out := nums[i-k]
			sum -= int64(out)
			freq[out]--
			if freq[out] == 0 {
				delete(freq, out)
			}
		}
		if i >= k-1 && len(freq) >= m && sum > ans {
			ans = sum
		}
	}
	return ans
}
