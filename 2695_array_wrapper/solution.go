// LeetCode 2695 - Array Wrapper
// https://leetcode.com/problems/array-wrapper/


import "fmt"
import "strings"

type ArrayWrapper struct{ nums []int }

func Constructor(nums []int) ArrayWrapper {
	return ArrayWrapper{nums: append([]int{}, nums...)}
}

func (a ArrayWrapper) ValueOf() int {
	s := 0
	for _, x := range a.nums {
		s += x
	}
	return s
}

func (a ArrayWrapper) ToString() string {
	parts := make([]string, len(a.nums))
	for i, x := range a.nums {
		parts[i] = fmt.Sprintf("%d", x)
	}
	return "[" + strings.Join(parts, ",") + "]"
}
