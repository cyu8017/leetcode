// LeetCode 2818 - Apply Operations to Maximize Score
// https://leetcode.com/problems/apply-operations-to-maximize-score/

import "sort"

func maximumScore(nums []int, k int) int {
	const mod = 1_000_000_007
	n := len(nums)
	score := make([]int, n)
	maxV := 0
	for _, v := range nums {
		if v > maxV {
			maxV = v
		}
	}
	spf := make([]int, maxV+1)
	for i := 2; i <= maxV; i++ {
		if spf[i] == 0 {
			for j := i; j <= maxV; j += i {
				if spf[j] == 0 {
					spf[j] = i
				}
			}
		}
	}
	primeScore := func(x int) int {
		seen := map[int]bool{}
		for x > 1 {
			p := spf[x]
			seen[p] = true
			for x%p == 0 {
				x /= p
			}
		}
		return len(seen)
	}
	for i, v := range nums {
		score[i] = primeScore(v)
	}
	left := make([]int, n)
	right := make([]int, n)
	st := []int{}
	for i := 0; i < n; i++ {
		for len(st) > 0 && score[st[len(st)-1]] < score[i] {
			st = st[:len(st)-1]
		}
		if len(st) == 0 {
			left[i] = -1
		} else {
			left[i] = st[len(st)-1]
		}
		st = append(st, i)
	}
	st = st[:0]
	for i := n - 1; i >= 0; i-- {
		for len(st) > 0 && score[st[len(st)-1]] <= score[i] {
			st = st[:len(st)-1]
		}
		if len(st) == 0 {
			right[i] = n
		} else {
			right[i] = st[len(st)-1]
		}
		st = append(st, i)
	}
	type pair struct{ v, cnt int }
	arr := make([]pair, n)
	for i := 0; i < n; i++ {
		arr[i] = pair{nums[i], (i - left[i]) * (right[i] - i)}
	}
	sort.Slice(arr, func(i, j int) bool { return arr[i].v > arr[j].v })
	modPow := func(a, b int) int {
		res := 1
		a %= mod
		for b > 0 {
			if b&1 == 1 {
				res = res * a % mod
			}
			a = a * a % mod
			b >>= 1
		}
		return res
	}
	ans := 1
	remain := k
	for _, p := range arr {
		if remain <= 0 {
			break
		}
		use := p.cnt
		if use > remain {
			use = remain
		}
		ans = ans * modPow(p.v, use) % mod
		remain -= use
	}
	return ans
}
