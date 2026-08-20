// LeetCode 2003 - Smallest Missing Genetic Value in Each Subtree
// https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

func smallestMissingValueSubtree(parents []int, nums []int) []int {
	n := len(parents)
	children := make([][]int, n)
	for i := 1; i < n; i++ {
		children[parents[i]] = append(children[parents[i]], i)
	}
	ans := make([]int, n)
	for i := range ans {
		ans[i] = 1
	}
	one := -1
	for i, v := range nums {
		if v == 1 {
			one = i
			break
		}
	}
	if one < 0 {
		return ans
	}
	seen := map[int]bool{}
	var collect func(int)
	collect = func(u int) {
		if seen[nums[u]] {
			return
		}
		seen[nums[u]] = true
		for _, v := range children[u] {
			collect(v)
		}
	}
	miss := 1
	node := one
	prev := -1
	for node != -1 {
		for _, v := range children[node] {
			if v != prev {
				collect(v)
			}
		}
		seen[nums[node]] = true
		for seen[miss] {
			miss++
		}
		ans[node] = miss
		prev = node
		node = parents[node]
	}
	return ans
}
