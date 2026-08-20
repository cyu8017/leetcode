// LeetCode 0952 - Largest Component Size by Common Factor
// https://leetcode.com/problems/largest-component-size-by-common-factor/

func largestComponentSize(nums []int) int {
	mx := 0
	for _, num := range nums {
		if num > mx {
			mx = num
		}
	}
	parent := make([]int, mx+1)
	for i := range parent {
		parent[i] = i
	}
	var find func(int) int
	find = func(x int) int {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	union := func(a, b int) {
		parent[find(a)] = find(b)
	}
	factors := func(x int) []int {
		res := []int{}
		d := 2
		for d*d <= x {
			if x%d == 0 {
				res = append(res, d)
				for x%d == 0 {
					x /= d
				}
			}
			d++
		}
		if x > 1 {
			res = append(res, x)
		}
		return res
	}
	for _, num := range nums {
		for _, f := range factors(num) {
			union(num, f)
		}
	}
	count := map[int]int{}
	ans := 0
	for _, num := range nums {
		r := find(num)
		count[r]++
		if count[r] > ans {
			ans = count[r]
		}
	}
	return ans
}
