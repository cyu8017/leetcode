// LeetCode 1133 - Largest Unique Number
// https://leetcode.com/problems/largest-unique-number/

func largestUniqueNumber(nums []int) int {
	count := map[int]int{}
	for _, x := range nums {
		count[x]++
	}
	ans := -1
	for x, c := range count {
		if c == 1 && x > ans {
			ans = x
		}
	}
	return ans
}
