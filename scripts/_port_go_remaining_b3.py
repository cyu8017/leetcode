#!/usr/bin/env python3
"""Remaining Go solutions batch C."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STUBS = json.loads((ROOT / "scripts" / "_stubs_3500_3749.json").read_text(encoding="utf-8"))
S: dict[str, str] = {}

S["3609_minimum_moves_to_reach_target_in_grid"] = r'''
func minMoves(sx int, sy int, tx int, ty int) int {
	ans := 0
	for tx > sx || ty > sy {
		if tx < sx || ty < sy {
			return -1
		}
		if tx == ty {
			return -1
		}
		if tx > ty {
			if ty > sy {
				if tx >= 2*ty {
					if tx%2 != 0 {
						return -1
					}
					tx /= 2
				} else {
					tx -= ty
				}
				ans++
			} else {
				if ty != sy {
					return -1
				}
				for tx > sx {
					if tx >= 2*ty {
						if tx%2 != 0 {
							return -1
						}
						tx /= 2
					} else {
						tx -= ty
					}
					ans++
					if tx < sx {
						return -1
					}
				}
			}
		} else {
			if tx > sx {
				if ty >= 2*tx {
					if ty%2 != 0 {
						return -1
					}
					ty /= 2
				} else {
					ty -= tx
				}
				ans++
			} else {
				if tx != sx {
					return -1
				}
				for ty > sy {
					if ty >= 2*tx {
						if ty%2 != 0 {
							return -1
						}
						ty /= 2
					} else {
						ty -= tx
					}
					ans++
					if ty < sy {
						return -1
					}
				}
			}
		}
	}
	if tx == sx && ty == sy {
		return ans
	}
	return -1
}
'''

S["3656_determine_if_a_simple_graph_exists"] = r'''
func simpleGraphExists(degrees []int) bool {
	n := len(degrees)
	d := append([]int(nil), degrees...)
	sort.Sort(sort.Reverse(sort.IntSlice(d)))
	var sum int64
	for _, x := range d {
		if x < 0 || x >= n {
			return false
		}
		sum += int64(x)
	}
	if sum%2 == 1 {
		return false
	}
	prefix := make([]int64, n+1)
	for i := 0; i < n; i++ {
		prefix[i+1] = prefix[i] + int64(d[i])
	}
	for k := 1; k <= n; k++ {
		var right int64
		for i := k; i < n; i++ {
			if d[i] < k {
				right += int64(d[i])
			} else {
				right += int64(k)
			}
		}
		if prefix[k] > int64(k*(k-1))+right {
			return false
		}
	}
	return true
}
'''

S["3563_lexicographically_smallest_string_after_adjacent_removals"] = r'''
func lexicographicallySmallestString(s string) string {
	n := len(s)
	dp := make([][]string, n+1)
	for i := range dp {
		dp[i] = make([]string, n+1)
	}
	isConsec := func(a, b byte) bool {
		d := int(a) - int(b)
		if d < 0 {
			d = -d
		}
		return d == 1 || d == 25
	}
	for length := 1; length <= n; length++ {
		for i := 0; i+length <= n; i++ {
			j := i + length
			minStr := string(s[i]) + dp[i+1][j]
			for k := i + 1; k < j; k++ {
				if isConsec(s[i], s[k]) && dp[i+1][k] == "" {
					cand := dp[k+1][j]
					if cand < minStr {
						minStr = cand
					}
				}
			}
			dp[i][j] = minStr
		}
	}
	return dp[0][n]
}
'''

S["3518_smallest_palindromic_rearrangement_ii"] = r'''
func smallestPalindrome(s string, k int) string {
	const MAX = 1_000_000 + 1
	cnt := make([]int, 26)
	for i := 0; i < len(s); i++ {
		cnt[s[i]-'a']++
	}
	odd := 0
	for _, c := range cnt {
		if c%2 == 1 {
			odd++
		}
	}
	if odd > 1 {
		return ""
	}
	half := make([]int, 26)
	mid := byte(0)
	for i := 0; i < 26; i++ {
		half[i] = cnt[i] / 2
		if cnt[i]%2 == 1 {
			mid = byte('a' + i)
		}
	}
	nCk := func(n, kk int) int {
		if kk < 0 || kk > n {
			return 0
		}
		res := 1
		if kk > n-kk {
			kk = n - kk
		}
		for i := 1; i <= kk; i++ {
			res = res * (n - i + 1) / i
			if res >= MAX {
				return MAX
			}
		}
		return res
	}
	countArr := func(h []int) int {
		total := 0
		for _, f := range h {
			total += f
		}
		res := 1
		for _, f := range h {
			res *= nCk(total, f)
			if res >= MAX {
				return MAX
			}
			total -= f
		}
		return res
	}
	if countArr(half) < k {
		return ""
	}
	halfLen := 0
	for _, f := range half {
		halfLen += f
	}
	left := make([]byte, 0, halfLen)
	for t := 0; t < halfLen; t++ {
		for i := 0; i < 26; i++ {
			if half[i] == 0 {
				continue
			}
			half[i]--
			arr := countArr(half)
			if arr >= k {
				left = append(left, byte('a'+i))
				break
			}
			k -= arr
			half[i]++
		}
	}
	res := string(left)
	if mid != 0 {
		res += string(mid)
	}
	for i := len(left) - 1; i >= 0; i-- {
		res += string(left[i])
	}
	return res
}
'''

S["3509_maximum_product_of_subsequences_with_an_alternating_sum_equal_to_k"] = r'''
func maxProduct(nums []int, k int, limit int) int {
	const MIN = -5000
	sumAll := 0
	for _, v := range nums {
		sumAll += v
	}
	if abs(k) > sumAll {
		return -1
	}
	type key struct {
		i, product, state, kk int
	}
	memo := map[key]int{}
	var dp func(i, product, state, kk int) int
	dp = func(i, product, state, kk int) int {
		if i == len(nums) {
			if kk == 0 && state != 0 && product <= limit {
				return product
			}
			return MIN
		}
		kkkey := key{i, product, state, kk}
		if v, ok := memo[kkkey]; ok {
			return v
		}
		res := dp(i+1, product, state, kk)
		if state == 0 {
			res = max(res, dp(i+1, nums[i], 1, kk-nums[i]))
		}
		if state == 1 {
			np := product * nums[i]
			if np > limit+1 {
				np = limit + 1
			}
			res = max(res, dp(i+1, np, 2, kk+nums[i]))
		}
		if state == 2 {
			np := product * nums[i]
			if np > limit+1 {
				np = limit + 1
			}
			res = max(res, dp(i+1, np, 1, kk-nums[i]))
		}
		memo[kkkey] = res
		return res
	}
	ans := dp(0, 1, 0, k)
	if ans == MIN {
		return -1
	}
	return ans
}
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
'''

S["3665_twisted_mirror_path_count"] = r'''
func uniquePaths(grid [][]int) int {
	const MOD = 1_000_000_007
	m := len(grid)
	n := len(grid[0])
	// Simulate reflections when attempting to enter a mirror
	type pos struct{ i, j, di, dj int }
	memo := map[pos]int{}
	var dfs func(i, j, di, dj int) int
	dfs = func(i, j, di, dj int) int {
		if i < 0 || j < 0 || i >= m || j >= n {
			return 0
		}
		if i == m-1 && j == n-1 {
			return 1
		}
		key := pos{i, j, di, dj}
		if v, ok := memo[key]; ok {
			return v
		}
		res := 0
		// try move right
		ni, nj := i, j+1
		if nj < n {
			if grid[ni][nj] == 1 {
				// reflect down from mirror cell
				res = (res + reflect(ni, nj, 1, 0, &dfs)) % MOD
			} else {
				res = (res + dfs(ni, nj, 0, 1)) % MOD
			}
		}
		// try move down
		ni, nj = i+1, j
		if ni < m {
			if grid[ni][nj] == 1 {
				res = (res + reflect(ni, nj, 0, 1, &dfs)) % MOD
			} else {
				res = (res + dfs(ni, nj, 1, 0)) % MOD
			}
		}
		_ = di
		_ = dj
		memo[key] = res
		return res
	}
	var reflect func(i, j, di, dj int, dfs *func(int, int, int, int) int) int
	reflect = func(i, j, di, dj int, dfsPtr *func(int, int, int, int) int) int {
		// entered direction (di,dj) into mirror at i,j — turn: right->down, down->right
		ndi, ndj := di, dj
		if dj == 1 { // was moving right -> turn down
			ndi, ndj = 1, 0
		} else if di == 1 { // was moving down -> turn right
			ndi, ndj = 0, 1
		}
		ni, nj := i+ndi, j+ndj
		for ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] == 1 {
			i, j = ni, nj
			// entered with ndi,ndj
			if ndj == 1 {
				ndi, ndj = 1, 0
			} else {
				ndi, ndj = 0, 1
			}
			ni, nj = i+ndi, j+ndj
		}
		if ni < 0 || nj < 0 || ni >= m || nj >= n {
			return 0
		}
		return (*dfsPtr)(ni, nj, ndi, ndj)
	}
	return dfs(0, 0, 0, 0)
}
'''

S["3699_number_of_zigzag_arrays_i"] = r'''
func zigZagArrays(n int, l int, r int) int {
	const MOD = 1_000_000_007
	m := r - l + 1
	if n == 1 {
		return m % MOD
	}
	up := make([]int, m)
	down := make([]int, m)
	for j := 0; j < m; j++ {
		up[j] = 1
		down[j] = 1
	}
	for len_ := 2; len_ <= n; len_++ {
		prefDown := make([]int, m+1)
		for j := 0; j < m; j++ {
			prefDown[j+1] = (prefDown[j] + down[j]) % MOD
		}
		nup := make([]int, m)
		for j := 0; j < m; j++ {
			nup[j] = prefDown[j]
		}
		sufUp := make([]int, m+1)
		for j := m - 1; j >= 0; j-- {
			sufUp[j] = (sufUp[j+1] + up[j]) % MOD
		}
		ndown := make([]int, m)
		for j := 0; j < m; j++ {
			ndown[j] = sufUp[j+1]
		}
		up, down = nup, ndown
	}
	ans := 0
	for j := 0; j < m; j++ {
		ans = (ans + up[j]) % MOD
		ans = (ans + down[j]) % MOD
	}
	return ans
}
'''

S["3605_minimum_stability_factor_of_array"] = r'''
func minStable(nums []int, maxC int) int {
	n := len(nums)
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	ok := func(x int) bool {
		if x >= n {
			return true
		}
		changes := 0
		i := 0
		for i+x < n {
			g := nums[i]
			for j := i + 1; j <= i+x; j++ {
				g = gcd(g, nums[j])
			}
			if g > 1 {
				changes++
				i += x + 1
			} else {
				i++
			}
		}
		return changes <= maxC
	}
	lo, hi := 0, n
	for lo < hi {
		mid := (lo + hi) / 2
		if ok(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
'''

S["3685_subsequence_sum_after_capping_elements"] = r'''
func subsequenceSumAfterCapping(nums []int, k int) []bool {
	n := len(nums)
	sorted := append([]int(nil), nums...)
	sort.Ints(sorted)
	ans := make([]bool, n)
	reach := make([]bool, k+1)
	reach[0] = true
	idx := 0
	for x := 1; x <= n; x++ {
		for idx < n && sorted[idx] <= x {
			v := sorted[idx]
			for s := k; s >= v; s-- {
				if reach[s-v] {
					reach[s] = true
				}
			}
			idx++
		}
		tmp := append([]bool(nil), reach...)
		rem := n - idx
		for s := 0; s <= k; s++ {
			if !reach[s] {
				continue
			}
			for t := 1; t <= rem && s+t*x <= k; t++ {
				tmp[s+t*x] = true
			}
		}
		ans[x-1] = tmp[k]
	}
	return ans
}
'''

S["3664_two_letter_card_game"] = r'''
func score(cards []string, x byte) int {
	xx := 0
	left := make([]int, 26)
	right := make([]int, 26)
	for _, c := range cards {
		a, b := c[0], c[1]
		if a == x && b == x {
			xx++
		} else if a == x {
			left[b-'a']++
		} else if b == x {
			right[a-'a']++
		}
	}
	pairGroup := func(arr []int) (pairs, rem int) {
		total, mx := 0, 0
		for _, v := range arr {
			total += v
			if v > mx {
				mx = v
			}
		}
		pairs = total / 2
		if total-mx < pairs {
			pairs = total - mx
		}
		rem = total - 2*pairs
		return
	}
	lp, lr := pairGroup(left)
	rp, rr := pairGroup(right)
	ans := lp + rp
	rem := lr + rr
	use := xx
	if use > rem {
		use = rem
	}
	ans += use
	xx -= use
	ans += xx / 2
	return ans
}
'''

S["3677_count_binary_palindromic_numbers"] = r'''
func countBinaryPalindromes(n int64) int {
	if n == 0 {
		return 1
	}
	ans := 1 // 0
	// count all binary palindromes <= n
	s := strconv.FormatInt(n, 2)
	L := len(s)
	// all palindromes with length < L
	for len_ := 1; len_ < L; len_++ {
		half := (len_ + 1) / 2
		ans += 1 << (half - 1)
	}
	// length == L: build from first half
	half := (L + 1) / 2
	prefix := s[:half]
	// count prefixes from 10..0 to prefix-1
	start := 1 << (half - 1)
	prefVal, _ := strconv.ParseInt(prefix, 2, 64)
	ans += int(prefVal) - start
	// check if palindrome from prefix <= n
	pal := []byte(prefix)
	for i := half - 1 - (L % 2); i >= 0; i-- {
		pal = append(pal, prefix[i])
	}
	pval, _ := strconv.ParseInt(string(pal), 2, 64)
	if pval <= n {
		ans++
	}
	return ans
}
'''

S["3725_count_ways_to_choose_coprime_integers_from_rows"] = r'''
func countCoprime(mat [][]int) int {
	const MOD = 1_000_000_007
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	dp := map[int]int{}
	for _, v := range mat[0] {
		dp[v] = (dp[v] + 1) % MOD
	}
	for i := 1; i < len(mat); i++ {
		ndp := map[int]int{}
		for _, v := range mat[i] {
			for g, c := range dp {
				ng := gcd(g, v)
				ndp[ng] = (ndp[ng] + c) % MOD
			}
		}
		dp = ndp
	}
	return dp[1]
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
    if "strconv." in code:
        imps.append('"strconv"')
    if not imps:
        return code
    return "import (\n\t" + "\n\t".join(imps) + "\n)\n\n" + code


def main() -> None:
    skip = {"3665_twisted_mirror_path_count"}  # rewrite cleaner later
    ported = []
    for folder, body in S.items():
        if folder in skip:
            continue
        p = ROOT / folder / "solution.go"
        if not p.exists():
            continue
        cur = p.read_text(encoding="utf-8")
        if "func solve()" not in cur and folder != "3656_determine_if_a_simple_graph_exists":
            # 3656 is solve() stub
            if "func solve()" not in cur:
                continue
        if "func solve()" not in cur:
            continue
        code = with_imports(body.strip() + "\n")
        p.write_text(header(folder) + code, encoding="utf-8", newline="\n")
        ported.append(folder)
    print(len(ported))
    for x in ported:
        print(x)


if __name__ == "__main__":
    main()
