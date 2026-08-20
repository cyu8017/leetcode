// LeetCode 3266 - Final Array State After K Multiplication Operations II
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

import "container/heap"

type p3266 struct{ v, i int }
type h3266 []p3266

func (h h3266) Len() int { return len(h) }
func (h h3266) Less(i, j int) bool {
	if h[i].v == h[j].v {
		return h[i].i < h[j].i
	}
	return h[i].v < h[j].v
}
func (h h3266) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *h3266) Push(x interface{}) { *h = append(*h, x.(p3266)) }
func (h *h3266) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func getFinalState(nums []int, k int, multiplier int) []int {
	const mod = 1000000007
	if multiplier == 1 {
		return nums
	}
	h := &h3266{}
	maxV := 0
	for i, v := range nums {
		heap.Push(h, p3266{v, i})
		if v > maxV {
			maxV = v
		}
	}
	for k > 0 && h.Len() > 0 {
		p := heap.Pop(h).(p3266)
		if int64(p.v)*int64(multiplier) > int64(maxV) && k >= len(nums) {
			heap.Push(h, p)
			break
		}
		nv := p.v * multiplier
		nums[p.i] = nv
		if nv > maxV {
			maxV = nv
		}
		heap.Push(h, p3266{nv, p.i})
		k--
	}
	if k > 0 {
		// distribute remaining multiplications evenly
		arr := make([]p3266, h.Len())
		copy(arr, *h)
		n := len(arr)
		full := k / n
		rem := k % n
		powFull := modPow3266(multiplier, full, mod)
		for i := range nums {
			nums[i] = int(int64(nums[i]) * powFull % mod)
		}
		// sort by current value for rem
		type iv struct{ v, i int }
		tmp := make([]iv, n)
		for i, x := range nums {
			tmp[i] = iv{x, i}
		}
		// use heap order for smallest rem elements
		hh := &h3266{}
		for i, v := range nums {
			heap.Push(hh, p3266{v, i})
		}
		for t := 0; t < rem; t++ {
			p := heap.Pop(hh).(p3266)
			p.v = int(int64(p.v) * int64(multiplier) % mod)
			nums[p.i] = p.v
			heap.Push(hh, p)
		}
		for i := range nums {
			nums[i] %= mod
		}
	} else {
		for i := range nums {
			nums[i] %= mod
		}
	}
	return nums
}

func modPow3266(a, e, mod int) int {
	r := 1
	a %= mod
	for e > 0 {
		if e&1 == 1 {
			r = int(int64(r) * int64(a) % int64(mod))
		}
		a = int(int64(a) * int64(a) % int64(mod))
		e >>= 1
	}
	return r
}
