// LeetCode 3289 - The Two Sneaky Numbers of Digitville
// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

func getSneakyNumbers(nums []int) []int {
	seen := map[int]bool{}
	ans := []int{}
	for _, x := range nums {
		if seen[x] {
			ans = append(ans, x)
		} else {
			seen[x] = true
		}
	}
	return ans
}
