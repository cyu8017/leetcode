// LeetCode 3309 - Maximum Possible Number by Binary Concatenation
// https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

import "fmt"
import "sort"

func maxGoodNumber(nums []int) int {
	bs := make([]string, 3)
	for i, x := range nums {
		bs[i] = fmt.Sprintf("%b", x)
	}
	idx := []int{0, 1, 2}
	ans := 0
	var perm func(int)
	perm = func(i int) {
		if i == 3 {
			s := bs[idx[0]] + bs[idx[1]] + bs[idx[2]]
			v := 0
			for _, c := range s {
				v = v*2 + int(c-'0')
			}
			if v > ans {
				ans = v
			}
			return
		}
		for j := i; j < 3; j++ {
			idx[i], idx[j] = idx[j], idx[i]
			perm(i + 1)
			idx[i], idx[j] = idx[j], idx[i]
		}
	}
	_ = sort.Ints
	perm(0)
	return ans
}
