// LeetCode 2367 - Number of Arithmetic Triplets
// https://leetcode.com/problems/number-of-arithmetic-triplets/

func arithmeticTriplets(nums []int, diff int) int {
	seen := map[int]bool{}
	for _, x := range nums {
		seen[x] = true
	}
	ans := 0
	for _, x := range nums {
		if seen[x+diff] && seen[x+2*diff] {
			ans++
		}
	}
	return ans
}
