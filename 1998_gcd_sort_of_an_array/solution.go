// LeetCode 1998 - GCD Sort of an Array
// https://leetcode.com/problems/gcd-sort-of-an-array/

import "sort"

func gcdSort(nums []int) bool {
	m := nums[0]
	for _, x := range nums {
		if x > m {
			m = x
		}
	}
	parent := make([]int, m+1)
	for i := range parent {
		parent[i] = i
	}
	var find func(x int) int
	find = func(x int) int {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	union := func(a, b int) {
		ra, rb := find(a), find(b)
		if ra != rb {
			parent[rb] = ra
		}
	}
	spf := make([]int, m+1)
	for i := range spf {
		spf[i] = i
	}
	for i := 2; i*i <= m; i++ {
		if spf[i] == i {
			for j := i * i; j <= m; j += i {
				if spf[j] == j {
					spf[j] = i
				}
			}
		}
	}
	seen := make(map[int]bool)
	for _, x := range nums {
		if seen[x] {
			continue
		}
		seen[x] = true
		y := x
		for y > 1 {
			p := spf[y]
			union(x, p)
			for y%p == 0 {
				y /= p
			}
		}
	}
	sortedNums := append([]int{}, nums...)
	sort.Ints(sortedNums)
	for i := range nums {
		if find(nums[i]) != find(sortedNums[i]) {
			return false
		}
	}
	return true
}
