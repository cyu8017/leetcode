// LeetCode 2709 - Greatest Common Divisor Traversal
// https://leetcode.com/problems/greatest-common-divisor-traversal/


func canTraverseAllPairs(nums []int) bool {
	n := len(nums)
	if n == 1 {
		return true
	}
	mx := 0
	for _, x := range nums {
		if x > mx {
			mx = x
		}
	}
	parent := make([]int, mx+1)
	for i := range parent {
		parent[i] = i
	}
	var find func(int) int
	find = func(x int) int {
		if parent[x] != x {
			parent[x] = find(parent[x])
		}
		return parent[x]
	}
	union := func(a, b int) {
		ra, rb := find(a), find(b)
		if ra != rb {
			parent[ra] = rb
		}
	}
	has := make([]bool, mx+1)
	for _, x := range nums {
		if x == 1 {
			return false
		}
		has[x] = true
	}
	sieve := make([]int, mx+1)
	for i := 2; i <= mx; i++ {
		if sieve[i] == 0 {
			for j := i; j <= mx; j += i {
				if sieve[j] == 0 {
					sieve[j] = i
				}
				if has[j] {
					union(i, j)
				}
			}
		}
	}
	root := find(nums[0])
	for _, x := range nums {
		if find(x) != root {
			return false
		}
	}
	return true
}
