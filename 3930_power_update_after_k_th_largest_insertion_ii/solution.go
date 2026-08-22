// LeetCode 3930 - Power Update After K-th Largest Insertion II
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-ii/

import "sort"

func powerUpdate(nums []int, p int, queries [][]int) []int {
	const mod int64 = 1000000007
	vals := append([]int(nil), nums...)
	for _, q := range queries {
		vals = append(vals, q[0])
	}
	sort.Ints(vals)
	uniq := vals[:0]
	for _, x := range vals {
		if len(uniq) == 0 || uniq[len(uniq)-1] != x {
			uniq = append(uniq, x)
		}
	}
	bit := make([]int, len(uniq)+1)
	add := func(i int) {
		for i < len(bit) {
			bit[i]++
			i += i & -i
		}
	}
	kth := func(rank int) int {
		idx := 0
		step := 1
		for step<<1 < len(bit) {
			step <<= 1
		}
		for ; step > 0; step >>= 1 {
			if next := idx + step; next < len(bit) && bit[next] < rank {
				idx = next
				rank -= bit[next]
			}
		}
		return uniq[idx]
	}
	for _, x := range nums {
		add(sort.SearchInts(uniq, x) + 1)
	}
	pow := func(a, e int64) int64 {
		res := int64(1)
		for e > 0 {
			if e&1 != 0 {
				res = res * a % mod
			}
			a = a * a % mod
			e >>= 1
		}
		return res
	}
	ans := make([]int, len(queries))
	size, cur := len(nums), int64(p)
	for i, q := range queries {
		add(sort.SearchInts(uniq, q[0]) + 1)
		size++
		x := kth(size - q[1] + 1)
		cur = pow(cur, int64(x))
		ans[i] = int(cur)
	}
	return ans
}