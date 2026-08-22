// LeetCode 3455 - Shortest Matching Substring
// https://leetcode.com/problems/shortest-matching-substring/

import "strings"

func shortestMatchingSubstring(s string, p string) int {
	parts := strings.Split(p, "*")
	for len(parts) < 3 {
		parts = append(parts, "")
	}
	a, b, c := parts[0], parts[1], parts[2]
	n := len(s)
	ans := n + 1
	// find all positions
	findAll := func(sub string) []int {
		if sub == "" {
			res := make([]int, n+1)
			for i := range res {
				res[i] = i
			}
			return res
		}
		res := []int{}
		for i := 0; i+len(sub) <= n; i++ {
			if s[i:i+len(sub)] == sub {
				res = append(res, i)
			}
		}
		return res
	}
	posA := findAll(a)
	posB := findAll(b)
	posC := findAll(c)
	for _, ia := range posA {
		endA := ia + len(a)
		// find first b starting >= endA
		for _, ib := range posB {
			if ib < endA {
				continue
			}
			endB := ib + len(b)
			for _, ic := range posC {
				if ic < endB {
					continue
				}
				length := ic + len(c) - ia
				if length < ans {
					ans = length
				}
				break
			}
			break // greedy first b may not be optimal when b empty etc.
		}
	}
	// Better two pointer approach
	ans = n + 1
	j, k := 0, 0
	for _, ia := range posA {
		endA := ia + len(a)
		for j < len(posB) && posB[j] < endA {
			j++
		}
		if j == len(posB) {
			break
		}
		endB := posB[j] + len(b)
		for k < len(posC) && posC[k] < endB {
			k++
		}
		if k == len(posC) {
			break
		}
		length := posC[k] + len(c) - ia
		if length < ans {
			ans = length
		}
	}
	// Still not fully correct when choosing later b helps; use nested with pointers carefully
	ans = n + 1
	for _, ia := range posA {
		endA := ia + len(a)
		bi := sortSearch(posB, endA)
		for ; bi < len(posB); bi++ {
			endB := posB[bi] + len(b)
			ci := sortSearch(posC, endB)
			if ci < len(posC) {
				length := posC[ci] + len(c) - ia
				if length < ans {
					ans = length
				}
			}
			if b == "" {
				break
			}
			// for non-empty b, first matching is enough for fixed a (monotonic)
			break
		}
	}
	if ans == n+1 {
		return -1
	}
	return ans
}

func sortSearch(arr []int, x int) int {
	lo, hi := 0, len(arr)
	for lo < hi {
		mid := (lo + hi) / 2
		if arr[mid] < x {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return lo
}
