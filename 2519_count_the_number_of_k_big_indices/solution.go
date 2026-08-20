// LeetCode 2519 - Count the Number of K-Big Indices
// https://leetcode.com/problems/count-the-number-of-k-big-indices/

import "sort"

type fenwick struct{ bit []int }

func newFenwick(n int) *fenwick { return &fenwick{bit: make([]int, n+2)} }
func (f *fenwick) add(i, v int) {
	for i < len(f.bit) {
		f.bit[i] += v
		i += i & -i
	}
}
func (f *fenwick) sum(i int) int {
	s := 0
	for i > 0 {
		s += f.bit[i]
		i -= i & -i
	}
	return s
}

func kBigIndices(nums []int, k int) int {
	n := len(nums)
	uniq := append([]int(nil), nums...)
	sort.Ints(uniq)
	w := 0
	for i := 0; i < len(uniq); i++ {
		if i == 0 || uniq[i] != uniq[i-1] {
			uniq[w] = uniq[i]
			w++
		}
	}
	uniq = uniq[:w]
	rank := map[int]int{}
	for i, v := range uniq {
		rank[v] = i + 1
	}
	m := len(uniq)
	left := make([]int, n)
	ft := newFenwick(m)
	for i, x := range nums {
		r := rank[x]
		left[i] = ft.sum(r - 1)
		ft.add(r, 1)
	}
	right := make([]int, n)
	ft = newFenwick(m)
	for i := n - 1; i >= 0; i-- {
		r := rank[nums[i]]
		right[i] = ft.sum(r - 1)
		ft.add(r, 1)
	}
	ans := 0
	for i := 0; i < n; i++ {
		if left[i] >= k && right[i] >= k {
			ans++
		}
	}
	return ans
}
