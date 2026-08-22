// LeetCode 3471 - Find the Largest Almost Missing Integer
// https://leetcode.com/problems/find-the-largest-almost-missing-integer/

func largestInteger(nums []int, k int) int {
	n := len(nums)
	cnt := map[int]int{}
	for i := 0; i+k <= n; i++ {
		seen := map[int]bool{}
		for j := i; j < i+k; j++ {
			seen[nums[j]] = true
		}
		for x := range seen {
			cnt[x]++
		}
	}
	ans := -1
	for x, c := range cnt {
		if c == 1 && x > ans {
			ans = x
		}
	}
	return ans
}
