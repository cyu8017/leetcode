// LeetCode 3934 - Smallest Unique Subarray
// https://leetcode.com/problems/smallest-unique-subarray/

import "sort"

func smallestUniqueSubarray(nums []int) int {
	n := len(nums)
	sa := make([]int, n)
	rank := append([]int(nil), nums...)
	for i := range sa {
		sa[i] = i
	}
	for width := 1; width < n; width <<= 1 {
		sort.Slice(sa, func(i, j int) bool {
			a, b := sa[i], sa[j]
			if rank[a] != rank[b] {
				return rank[a] < rank[b]
			}
			ra, rb := -1, -1
			if a+width < n {
				ra = rank[a+width]
			}
			if b+width < n {
				rb = rank[b+width]
			}
			return ra < rb
		})
		next := make([]int, n)
		for i := 1; i < n; i++ {
			a, b := sa[i-1], sa[i]
			different := rank[a] != rank[b]
			ra, rb := -1, -1
			if a+width < n {
				ra = rank[a+width]
			}
			if b+width < n {
				rb = rank[b+width]
			}
			if different || ra != rb {
				next[b] = next[a] + 1
			} else {
				next[b] = next[a]
			}
		}
		rank = next
		if rank[sa[n-1]] == n-1 {
			break
		}
	}
	pos := make([]int, n)
	for i, x := range sa {
		pos[x] = i
	}
	lcp := make([]int, n-1)
	height := 0
	for i := 0; i < n; i++ {
		p := pos[i]
		if p == n-1 {
			height = 0
			continue
		}
		j := sa[p+1]
		for i+height < n && j+height < n && nums[i+height] == nums[j+height] {
			height++
		}
		lcp[p] = height
		if height > 0 {
			height--
		}
	}
	ans := n
	for p, start := range sa {
		need := 1
		if p > 0 && lcp[p-1]+1 > need {
			need = lcp[p-1] + 1
		}
		if p+1 < n && lcp[p]+1 > need {
			need = lcp[p] + 1
		}
		if need <= n-start && need < ans {
			ans = need
		}
	}
	return ans
}