#!/usr/bin/env python3
"""Remaining Go solutions batch D — more hard/medium fills."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STUBS = json.loads((ROOT / "scripts" / "_stubs_3500_3749.json").read_text(encoding="utf-8"))
S: dict[str, str] = {}

S["3520_minimum_threshold_for_inversion_pairs_count"] = r'''
func minThreshold(nums []int, k int) int {
	mx := 0
	for _, v := range nums {
		if v > mx {
			mx = v
		}
	}
	l, r := 0, mx+1
	for l < r {
		m := (l + r) / 2
		if countInv(nums, k, m) {
			r = m
		} else {
			l = m + 1
		}
	}
	if l > mx {
		return -1
	}
	return l
}
func countInv(nums []int, k, threshold int) bool {
	sorted := []int{}
	inv := 0
	for _, num := range nums {
		// count values in (num, num+threshold]
		lo, hi := 0, len(sorted)
		for lo < hi {
			mid := (lo + hi) / 2
			if sorted[mid] <= num {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		left := lo
		lo, hi = 0, len(sorted)
		for lo < hi {
			mid := (lo + hi) / 2
			if sorted[mid] <= num+threshold {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		inv += lo - left
		// insert num
		lo, hi = 0, len(sorted)
		for lo < hi {
			mid := (lo + hi) / 2
			if sorted[mid] < num {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		sorted = append(sorted, 0)
		copy(sorted[lo+1:], sorted[lo:])
		sorted[lo] = num
	}
	return inv >= k
}
'''

S["3595_once_twice"] = r'''
func onceTwice(nums []int) []int {
	// bit counts mod 3 for each bit, then separate once vs twice
	ones := make([]int, 32)
	for _, x := range nums {
		for b := 0; b < 32; b++ {
			if (x>>b)&1 == 1 {
				ones[b]++
			}
		}
	}
	// For bits: count mod 3 is 1 if once has bit, 2 if twice has bit, 0 if neither (or both - impossible)
	once, twice := 0, 0
	for b := 0; b < 32; b++ {
		r := ones[b] % 3
		if r == 1 {
			once |= 1 << b
		} else if r == 2 {
			twice |= 1 << b
		}
	}
	// Conflict when both have same bit: r would be 0 mod 3. Need digital method.
	// Better: use two masks with ternary-like state machine per bit is hard.
	// Frequency via XOR of all with special:
	freq := map[int]int{}
	for _, x := range nums {
		freq[x]++
	}
	var a, b int
	for x, c := range freq {
		if c == 1 {
			a = x
		} else if c == 2 {
			b = x
		}
	}
	return []int{a, b}
}
'''

S["3680_generate_schedule"] = r'''
func generateSchedule(n int) [][]int {
	if n <= 3 {
		return [][]int{}
	}
	matches := [][]int{}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if i != j {
				matches = append(matches, []int{i, j})
			}
		}
	}
	// backtracking
	used := make([]bool, len(matches))
	sched := [][]int{}
	var last [2]int
	last[0], last[1] = -1, -1
	var dfs func() bool
	dfs = func() bool {
		if len(sched) == len(matches) {
			return true
		}
		for i, m := range matches {
			if used[i] {
				continue
			}
			if m[0] == last[0] || m[0] == last[1] || m[1] == last[0] || m[1] == last[1] {
				continue
			}
			used[i] = true
			sched = append(sched, m)
			prev := last
			last[0], last[1] = m[0], m[1]
			if dfs() {
				return true
			}
			last = prev
			sched = sched[:len(sched)-1]
			used[i] = false
		}
		return false
	}
	if dfs() {
		return sched
	}
	return [][]int{}
}
'''

S["3665_twisted_mirror_path_count"] = r'''
func uniquePaths(grid [][]int) int {
	const MOD = 1_000_000_007
	m := len(grid)
	n := len(grid[0])
	// dp[i][j] = ways to reach empty cell (i,j)
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	if grid[0][0] == 1 {
		return 0
	}
	dp[0][0] = 1
	// For each empty cell, propagate to next empty cells via moves/reflections
	type pair struct{ i, j int }
	nextCell := func(i, j, di, dj int) (int, int, bool) {
		ni, nj := i+di, j+dj
		for ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] == 1 {
			// reflect: right->down, down->right
			if dj == 1 {
				di, dj = 1, 0
			} else {
				di, dj = 0, 1
			}
			ni, nj = ni+di, nj+dj
		}
		if ni < 0 || nj < 0 || ni >= m || nj >= n {
			return 0, 0, false
		}
		return ni, nj, true
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 || dp[i][j] == 0 {
				continue
			}
			if ni, nj, ok := nextCell(i, j, 0, 1); ok {
				dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % MOD
			}
			if ni, nj, ok := nextCell(i, j, 1, 0); ok {
				dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % MOD
			}
		}
	}
	return dp[m-1][n-1]
}
'''

S["3700_number_of_zigzag_arrays_ii"] = r'''
func zigZagArrays(n int, l int, r int) int {
	// Same recurrence as I but n can be large — use matrix exponentiation
	const MOD = 1_000_000_007
	m := r - l + 1
	if n == 1 {
		return m % MOD
	}
	// state: [up_0..up_{m-1}, down_0..down_{m-1}]
	dim := 2 * m
	mul := func(A, B [][]int) [][]int {
		C := make([][]int, dim)
		for i := 0; i < dim; i++ {
			C[i] = make([]int, dim)
			for k := 0; k < dim; k++ {
				if A[i][k] == 0 {
					continue
				}
				for j := 0; j < dim; j++ {
					C[i][j] = (C[i][j] + A[i][k]*B[k][j]) % MOD
				}
			}
		}
		return C
	}
	pow := func(A [][]int, e int) [][]int {
		R := make([][]int, dim)
		for i := 0; i < dim; i++ {
			R[i] = make([]int, dim)
			R[i][i] = 1
		}
		for e > 0 {
			if e&1 == 1 {
				R = mul(R, A)
			}
			A = mul(A, A)
			e >>= 1
		}
		return R
	}
	M := make([][]int, dim)
	for i := 0; i < dim; i++ {
		M[i] = make([]int, dim)
	}
	// new_up[j] = sum down[0..j-1]
	for j := 0; j < m; j++ {
		for t := 0; t < j; t++ {
			M[j][m+t] = 1
		}
	}
	// new_down[j] = sum up[j+1..]
	for j := 0; j < m; j++ {
		for t := j + 1; t < m; t++ {
			M[m+j][t] = 1
		}
	}
	P := pow(M, n-1)
	ans := 0
	for j := 0; j < m; j++ {
		// initial up=1, down=1 each
		for t := 0; t < m; t++ {
			ans = (ans + P[j][t]) % MOD
			ans = (ans + P[j][m+t]) % MOD
			ans = (ans + P[m+j][t]) % MOD
			ans = (ans + P[m+j][m+t]) % MOD
		}
	}
	return ans
}
'''

S["3734_lexicographically_smallest_palindromic_permutation_greater_than_target"] = r'''
func lexPalindromicPermutation(s string, target string) string {
	cnt := make([]int, 26)
	for i := 0; i < len(s); i++ {
		cnt[s[i]-'a']++
	}
	n := len(s)
	odd := 0
	mid := -1
	for i := 0; i < 26; i++ {
		if cnt[i]%2 == 1 {
			odd++
			mid = i
		}
	}
	if odd > 1 {
		return ""
	}
	half := make([]int, 26)
	for i := 0; i < 26; i++ {
		half[i] = cnt[i] / 2
	}
	halfLen := n / 2
	ansLeft := make([]byte, halfLen)
	var dfs func(pos int, greater bool) bool
	dfs = func(pos int, greater bool) bool {
		if pos == halfLen {
			return greater || (mid >= 0 && byte('a'+mid) > target[halfLen]) || (mid < 0 && greater)
		}
		start := 0
		if !greater {
			start = int(target[pos] - 'a')
		}
		for c := start; c < 26; c++ {
			if half[c] == 0 {
				continue
			}
			half[c]--
			ansLeft[pos] = byte('a' + c)
			ng := greater || c > int(target[pos]-'a')
			if dfs(pos+1, ng) {
				return true
			}
			half[c]++
		}
		return false
	}
	// Also need mid comparison when left == target left half
	if !dfs(0, false) {
		return ""
	}
	res := string(ansLeft)
	if mid >= 0 {
		res += string(byte('a' + mid))
	}
	for i := halfLen - 1; i >= 0; i-- {
		res += string(ansLeft[i])
	}
	if res <= target {
		return ""
	}
	return res
}
'''

S["3655_xor_after_range_multiplication_queries_ii"] = r'''
func xorAfterQueries(nums []int, queries [][]int) int {
	const MOD = 1_000_000_007
	n := len(nums)
	// Difference array per step for large updates; apply then xor
	diff := make([]int, n+1)
	for i := range diff {
		diff[i] = 1
	}
	type upd struct{ l, r, k, v int }
	// For each unique k, apply range multiplies on arithmetic progression
	byK := map[int][]upd{}
	for _, q := range queries {
		l, r, k, v := q[0], q[1], q[2], q[3]
		byK[k] = append(byK[k], upd{l, r, k, v})
	}
	res := append([]int(nil), nums...)
	for k, ups := range byK {
		fac := make([]int, n)
		for i := range fac {
			fac[i] = 1
		}
		for _, u := range ups {
			for i := u.l; i <= u.r; i += k {
				fac[i] = fac[i] * u.v % MOD
			}
		}
		for i := 0; i < n; i++ {
			res[i] = res[i] * fac[i] % MOD
		}
	}
	ans := 0
	for _, v := range res {
		ans ^= v
	}
	return ans
}
'''

S["3743_maximize_cyclic_partition_score"] = r'''
func maximumScore(nums []int, k int) int64 {
	n := len(nums)
	// Duplicate array for cyclic
	a := append(append([]int{}, nums...), nums...)
	// dp: max score partitioning into at most k+1? segments — problem specific
	// Score often = sum of max of each part. Maximize with exactly/at most k cuts on cycle.
	// Standard: max sum of k segment-maximums on a cycle.
	if k >= n {
		var s int64
		for _, v := range nums {
			s += int64(v)
		}
		return s
	}
	// For each starting point, do DP on linear array of length n
	var best int64
	for start := 0; start < n; start++ {
		seg := a[start : start+n]
		// dp[i][j] = max score using first i elements with j segments
		dp := make([][]int64, n+1)
		for i := range dp {
			dp[i] = make([]int64, k+1)
			for j := range dp[i] {
				dp[i][j] = -1 << 60
			}
		}
		dp[0][0] = 0
		for i := 1; i <= n; i++ {
			for j := 1; j <= k && j <= i; j++ {
				mx := int64(0)
				for t := i; t >= j; t-- {
					if int64(seg[t-1]) > mx {
						mx = int64(seg[t-1])
					}
					if dp[t-1][j-1] > -1<<60 {
						cand := dp[t-1][j-1] + mx
						if cand > dp[i][j] {
							dp[i][j] = cand
						}
					}
				}
			}
		}
		if dp[n][k] > best {
			best = dp[n][k]
		}
	}
	return best
}
'''

S["3695_maximize_alternating_sum_using_swaps"] = r'''
func maxAlternatingSum(nums []int, swaps [][]int) int64 {
	n := len(nums)
	parent := make([]int, n)
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
	for _, s := range swaps {
		a, b := find(s[0]), find(s[1])
		if a != b {
			parent[a] = b
		}
	}
	compVals := map[int][]int{}
	compIdx := map[int][]int{}
	for i := 0; i < n; i++ {
		r := find(i)
		compVals[r] = append(compVals[r], nums[i])
		compIdx[r] = append(compIdx[r], i)
	}
	arr := make([]int, n)
	for r, vals := range compVals {
		idxs := compIdx[r]
		sort.Ints(vals)
		sort.Sort(sort.Reverse(sort.IntSlice(vals)))
		// assign largest to even indices preferentially within component
		even, odd := []int{}, []int{}
		for _, i := range idxs {
			if i%2 == 0 {
				even = append(even, i)
			} else {
				odd = append(odd, i)
			}
		}
		sort.Ints(even)
		sort.Ints(odd)
		// take largest |even| values for even positions
		ei := 0
		for _, v := range vals {
			if ei < len(even) {
				arr[even[ei]] = v
				ei++
			} else {
				arr[odd[ei-len(even)]] = v
				ei++
			}
		}
		_ = r
	}
	var ans int64
	for i, v := range arr {
		if i%2 == 0 {
			ans += int64(v)
		} else {
			ans -= int64(v)
		}
	}
	return ans
}
'''

S["3589_count_prime_gap_balanced_subarrays"] = r'''
func primeSubarray(nums []int, k int) int {
	mx := 0
	for _, v := range nums {
		if v > mx {
			mx = v
		}
	}
	isPrime := make([]bool, mx+1)
	for i := 2; i <= mx; i++ {
		isPrime[i] = true
	}
	for i := 2; i*i <= mx; i++ {
		if isPrime[i] {
			for j := i * i; j <= mx; j += i {
				isPrime[j] = false
			}
		}
	}
	n := len(nums)
	ans := 0
	// sliding window: subarrays where primes' max-min <= k and at least 2 primes
	for l := 0; l < n; l++ {
		primes := []int{}
		for r := l; r < n; r++ {
			if isPrime[nums[r]] {
				primes = append(primes, nums[r])
			}
			if len(primes) >= 2 {
				mn, mxp := primes[0], primes[0]
				for _, p := range primes {
					if p < mn {
						mn = p
					}
					if p > mxp {
						mxp = p
					}
				}
				if mxp-mn <= k {
					ans++
				}
			}
		}
	}
	return ans
}
'''

S["3630_partition_array_for_maximum_xor_and_and"] = r'''
func maximizeXorAndXor(nums []int) int64 {
	n := len(nums)
	var best int64
	// partition into 3 subsets (possibly empty?): A AND, B XOR, C XOR of XOR
	// Brute subsets for small n — check constraints via typical n<=20
	if n > 20 {
		n = 20
	}
	total := 0
	for _, v := range nums {
		total ^= v
	}
	for mask := 0; mask < 1<<n; mask++ {
		andVal := -1
		xorB := 0
		for i := 0; i < n; i++ {
			if mask>>i&1 == 1 {
				if andVal == -1 {
					andVal = nums[i]
				} else {
					andVal &= nums[i]
				}
			} else {
				xorB ^= nums[i]
			}
		}
		if andVal == -1 {
			andVal = 0
		}
		// remaining after removing AND set: further split XOR into two groups by submask of complement
		comp := ((1 << n) - 1) ^ mask
		for sub := comp; ; sub = (sub - 1) & comp {
			xor1 := 0
			for i := 0; i < n; i++ {
				if sub>>i&1 == 1 {
					xor1 ^= nums[i]
				}
			}
			xor2 := xorB ^ xor1
			score := int64(andVal) + int64(xor1) + int64(xor2)
			if score > best {
				best = score
			}
			if sub == 0 {
				break
			}
		}
	}
	return best
}
'''


def header(folder: str) -> str:
    meta = STUBS.get(folder, {})
    num = int(folder.split("_", 1)[0])
    title = meta.get("title") or folder.split("_", 1)[1].replace("_", " ").title()
    slug = meta.get("slug") or folder.split("_", 1)[1].replace("_", "-")
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n\n"


def with_imports(code: str) -> str:
    imps = []
    if "sort." in code:
        imps.append('"sort"')
    if not imps:
        return code
    return "import (\n\t" + "\n\t".join(imps) + "\n)\n\n" + code


def main() -> None:
    skip = {
        "3743_maximize_cyclic_partition_score",
        "3630_partition_array_for_maximum_xor_and_and",
        "3700_number_of_zigzag_arrays_ii",
        "3680_generate_schedule",  # backtracking may be too slow; still write for completeness later
        "3734_lexicographically_smallest_palindromic_permutation_greater_than_target",
    }
    ported = []
    for folder, body in S.items():
        if folder in skip:
            continue
        p = ROOT / folder / "solution.go"
        if not p.exists():
            continue
        cur = p.read_text(encoding="utf-8")
        if "func solve()" not in cur:
            continue
        code = with_imports(body.strip() + "\n")
        p.write_text(header(folder) + code, encoding="utf-8", newline="\n")
        ported.append(folder)
    # Also write some skipped that are still useful
    for folder in ["3665_twisted_mirror_path_count", "3520_minimum_threshold_for_inversion_pairs_count", "3595_once_twice", "3655_xor_after_range_multiplication_queries_ii", "3695_maximize_alternating_sum_using_swaps", "3589_count_prime_gap_balanced_subarrays"]:
        if folder in S and folder not in ported:
            p = ROOT / folder / "solution.go"
            cur = p.read_text(encoding="utf-8")
            if "func solve()" in cur:
                code = with_imports(S[folder].strip() + "\n")
                p.write_text(header(folder) + code, encoding="utf-8", newline="\n")
                ported.append(folder)
    print(len(ported))
    for x in ported:
        print(x)


if __name__ == "__main__":
    main()
