// LeetCode 0975 - Odd Even Jump
// https://leetcode.com/problems/odd-even-jump/

import "sort"

func oddEvenJumps(arr []int) int {
	n := len(arr)
	nextHigher := make([]int, n)
	nextLower := make([]int, n)
	type pair struct{ a, i int }
	order := make([]pair, n)
	for i, a := range arr {
		order[i] = pair{a, i}
	}
	sort.Slice(order, func(i, j int) bool {
		if order[i].a == order[j].a {
			return order[i].i < order[j].i
		}
		return order[i].a < order[j].a
	})
	stack := []int{}
	for _, p := range order {
		for len(stack) > 0 && stack[len(stack)-1] < p.i {
			nextHigher[stack[len(stack)-1]] = p.i
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, p.i)
	}
	sort.Slice(order, func(i, j int) bool {
		if order[i].a == order[j].a {
			return order[i].i < order[j].i
		}
		return order[i].a > order[j].a
	})
	stack = stack[:0]
	for _, p := range order {
		for len(stack) > 0 && stack[len(stack)-1] < p.i {
			nextLower[stack[len(stack)-1]] = p.i
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, p.i)
	}
	odd := make([]bool, n)
	even := make([]bool, n)
	odd[n-1], even[n-1] = true, true
	for i := n - 2; i >= 0; i-- {
		if nextHigher[i] != 0 {
			odd[i] = even[nextHigher[i]]
		}
		if nextLower[i] != 0 {
			even[i] = odd[nextLower[i]]
		}
	}
	ans := 0
	for _, v := range odd {
		if v {
			ans++
		}
	}
	return ans
}
