// LeetCode 2588 - Count the Number of Beautiful Subarrays
// https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/


func beautifulSubarrays(nums []int) int64 {
	freq := map[int]int{0: 1}
	xor, ans := 0, int64(0)
	for _, x := range nums {
		xor ^= x
		ans += int64(freq[xor])
		freq[xor]++
	}
	return ans
}
