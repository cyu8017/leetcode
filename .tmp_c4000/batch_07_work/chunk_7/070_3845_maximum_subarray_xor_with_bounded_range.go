// LeetCode 3845 - Maximum Subarray XOR with Bounded Range
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

type xorNode3845 struct {
	next  [2]int
	count int
}

func maxSubarrayXor(nums []int, k int) int {
	nodes := []xorNode3845{{}}
	add := func(x, delta int) {
		u := 0
		nodes[u].count += delta
		for b := 15; b >= 0; b-- {
			bit := x >> b & 1
			if nodes[u].next[bit] == 0 {
				nodes[u].next[bit] = len(nodes)
				nodes = append(nodes, xorNode3845{})
			}
			u = nodes[u].next[bit]
			nodes[u].count += delta
		}
	}
	query := func(x int) int {
		u, res := 0, 0
		for b := 15; b >= 0; b-- {
			bit := x >> b & 1
			want := bit ^ 1
			v := nodes[u].next[want]
			if v != 0 && nodes[v].count > 0 {
				res |= 1 << b
				u = v
			} else {
				u = nodes[u].next[bit]
			}
		}
		return res
	}
	n := len(nums)
	pref := make([]int, n+1)
	for i, x := range nums {
		pref[i+1] = pref[i] ^ x
	}
	maxQ, minQ := make([]int, 0, n), make([]int, 0, n)
	left, trieLeft, ans := 0, 0, 0
	for r, x := range nums {
		for len(maxQ) > 0 && nums[maxQ[len(maxQ)-1]] <= x {
			maxQ = maxQ[:len(maxQ)-1]
		}
		maxQ = append(maxQ, r)
		for len(minQ) > 0 && nums[minQ[len(minQ)-1]] >= x {
			minQ = minQ[:len(minQ)-1]
		}
		minQ = append(minQ, r)
		for nums[maxQ[0]]-nums[minQ[0]] > k {
			if maxQ[0] == left {
				maxQ = maxQ[1:]
			}
			if minQ[0] == left {
				minQ = minQ[1:]
			}
			left++
		}
		add(pref[r], 1)
		for trieLeft < left {
			add(pref[trieLeft], -1)
			trieLeft++
		}
		if cur := query(pref[r+1]); cur > ans {
			ans = cur
		}
	}
	return ans
}