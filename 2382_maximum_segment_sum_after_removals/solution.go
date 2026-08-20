// LeetCode 2382 - Maximum Segment Sum After Removals
// https://leetcode.com/problems/maximum-segment-sum-after-removals/

func maximumSegmentSum(nums []int, removeQueries []int) []int64 {
	n := len(nums)
	parent := make([]int, n)
	sum := make([]int64, n)
	active := make([]bool, n)
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
		if ra == rb {
			return
		}
		parent[rb] = ra
		sum[ra] += sum[rb]
	}
	ans := make([]int64, n)
	var best int64
	for i := n - 1; i >= 0; i-- {
		ans[i] = best
		idx := removeQueries[i]
		active[idx] = true
		sum[idx] = int64(nums[idx])
		if idx > 0 && active[idx-1] {
			union(idx, idx-1)
		}
		if idx+1 < n && active[idx+1] {
			union(idx, idx+1)
		}
		if sum[find(idx)] > best {
			best = sum[find(idx)]
		}
	}
	return ans
}
