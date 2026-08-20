// LeetCode 2344 - Minimum Deletions to Make Array Divisible
// https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

import "sort"

func minOperations(nums []int, numsDivide []int) int {
	g := numsDivide[0]
	for i := 1; i < len(numsDivide); i++ {
		g = gcd(g, numsDivide[i])
	}
	sort.Ints(nums)
	for i, x := range nums {
		if g%x == 0 {
			return i
		}
	}
	return -1
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
