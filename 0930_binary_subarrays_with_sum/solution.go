// LeetCode 0930 - Binary Subarrays With Sum
// https://leetcode.com/problems/binary-subarrays-with-sum/

func numSubarraysWithSum(nums []int, goal int) int {
	count := map[int]int{0: 1}
	prefix, ans := 0, 0
	for _, x := range nums {
		prefix += x
		ans += count[prefix-goal]
		count[prefix]++
	}
	return ans
}
