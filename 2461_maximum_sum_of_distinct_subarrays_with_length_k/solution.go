// LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

func maximumSubarraySum(nums []int, k int) int64 {
	cnt := map[int]int{}
	var sum, ans int64
	for i, x := range nums {
		sum += int64(x)
		cnt[x]++
		if i >= k {
			y := nums[i-k]
			sum -= int64(y)
			cnt[y]--
			if cnt[y] == 0 {
				delete(cnt, y)
			}
		}
		if i >= k-1 && len(cnt) == k && sum > ans {
			ans = sum
		}
	}
	return ans
}
