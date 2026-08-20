// LeetCode 3378 - Count Connected Components in LCM Graph
// https://leetcode.com/problems/count-connected-components-in-lcm-graph/

func countComponents(nums []int, threshold int) int {
	n := len(nums)
	parent := make([]int, n)
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
	idx := map[int]int{}
	for i, x := range nums {
		idx[x] = i
	}
	// for each possible multiple
	maxN := threshold
	for d := 1; d <= maxN; d++ {
		var first int = -1
		for m := d; m <= maxN; m += d {
			if i, ok := idx[m]; ok {
				if first == -1 {
					first = i
				} else if int64(nums[first])*int64(nums[i])/int64(gcd3378(nums[first], nums[i])) <= int64(threshold) {
					union(first, i)
				}
			}
		}
	}
	// simpler: union i,j if lcm <= threshold
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			a, b := nums[i], nums[j]
			g := gcd3378(a, b)
			if int64(a)/int64(g)*int64(b) <= int64(threshold) {
				union(i, j)
			}
		}
	}
	comp := map[int]bool{}
	for i := 0; i < n; i++ {
		comp[find(i)] = true
	}
	return len(comp)
}

func gcd3378(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
