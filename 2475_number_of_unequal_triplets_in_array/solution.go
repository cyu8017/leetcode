// LeetCode 2475 - Number of Unequal Triplets in Array
// https://leetcode.com/problems/number-of-unequal-triplets-in-array/

func unequalTriplets(nums []int) int {
	cnt := map[int]int{}
	for _, x := range nums {
		cnt[x]++
	}
	ans, n, left := 0, len(nums), 0
	for _, c := range cnt {
		right := n - left - c
		ans += left * c * right
		left += c
	}
	return ans
}
