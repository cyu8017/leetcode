// LeetCode 3866 - First Unique Even Element
// https://leetcode.com/problems/first-unique-even-element/

func firstUniqueEven(nums []int) int {
	cnt := make([]int, 101)
	for _, x := range nums {
		cnt[x]++
	}
	for _, x := range nums {
		if x%2 == 0 && cnt[x] == 1 {
			return x
		}
	}
	return -1
}
