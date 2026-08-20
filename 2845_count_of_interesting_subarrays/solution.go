// LeetCode 2845 - Count of Interesting Subarrays
// https://leetcode.com/problems/count-of-interesting-subarrays/

func countInterestingSubarrays(nums []int, modulo int, k int) int64 {
	freq := map[int]int{0: 1}
	var ans int64
	pref := 0
	for _, v := range nums {
		if v%modulo == k {
			pref++
		}
		need := (pref - k) % modulo
		if need < 0 {
			need += modulo
		}
		ans += int64(freq[need])
		freq[pref%modulo]++
	}
	return ans
}
