// LeetCode 3377 - Digit Operations to Make Two Integers Equal
// https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

import "container/heap"

type item3377 struct{ cost, val int }
type h3377 []item3377

func (h h3377) Len() int            { return len(h) }
func (h h3377) Less(i, j int) bool  { return h[i].cost < h[j].cost }
func (h h3377) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *h3377) Push(x interface{}) { *h = append(*h, x.(item3377)) }
func (h *h3377) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minOperations(n int, m int) int {
	isPrime := sieve(100000)
	if isPrime[n] || isPrime[m] {
		// n itself is paid; if n prime cannot start? problem: cannot be prime at any point including start?
		if isPrime[n] {
			return -1
		}
	}
	dist := make([]int, 100000)
	for i := range dist {
		dist[i] = -1
	}
	h := &h3377{{n, n}}
	dist[n] = n
	for h.Len() > 0 {
		cur := heap.Pop(h).(item3377)
		if cur.cost != dist[cur.val] {
			continue
		}
		if cur.val == m {
			return cur.cost
		}
		s := []byte(itoa3377(cur.val))
		for i := 0; i < len(s); i++ {
			orig := s[i]
			for _, d := range []int{-1, 1} {
				nd := int(orig-'0') + d
				if nd < 0 || nd > 9 {
					continue
				}
				if i == 0 && nd == 0 && len(s) > 1 {
					continue
				}
				s[i] = byte('0' + nd)
				nv := atoi3377(string(s))
				s[i] = orig
				if isPrime[nv] {
					continue
				}
				nc := cur.cost + nv
				if dist[nv] == -1 || nc < dist[nv] {
					dist[nv] = nc
					heap.Push(h, item3377{nc, nv})
				}
			}
		}
	}
	return -1
}

func sieve(n int) []bool {
	p := make([]bool, n)
	for i := 2; i < n; i++ {
		p[i] = true
	}
	p[0], p[1] = false, false
	for i := 2; i*i < n; i++ {
		if p[i] {
			for j := i * i; j < n; j += i {
				p[j] = false
			}
		}
	}
	// invert: isPrime
	isP := make([]bool, n)
	for i := 2; i < n; i++ {
		isP[i] = p[i]
	}
	return isP
}

func itoa3377(x int) string {
	if x == 0 {
		return "0"
	}
	var b []byte
	for x > 0 {
		b = append([]byte{byte('0' + x%10)}, b...)
		x /= 10
	}
	return string(b)
}
func atoi3377(s string) int {
	v := 0
	for _, c := range s {
		v = v*10 + int(c-'0')
	}
	return v
}
