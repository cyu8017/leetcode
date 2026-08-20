// LeetCode 0922 - Sort Array By Parity II
// https://leetcode.com/problems/sort-array-by-parity-ii/

func sortArrayByParityII(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)
	even, odd := 0, 0
	for _, x := range nums {
		if x%2 == 0 {
			ans[even] = x
			even += 2
		} else {
			ans[odd+1] = x
			odd += 2
		}
	}
	return ans
}
