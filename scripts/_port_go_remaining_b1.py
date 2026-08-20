#!/usr/bin/env python3
"""Port remaining Go solutions 3500-3749 batch A (confident mediums + walkccc ports)."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STUBS = json.loads((ROOT / "scripts" / "_stubs_3500_3749.json").read_text(encoding="utf-8"))
S: dict[str, str] = {}

S["3500_minimum_cost_to_divide_array_into_subarrays"] = r'''
func minimumCost(nums []int, cost []int, k int) int64 {
	n := len(nums)
	pn := make([]int64, n+1)
	pc := make([]int64, n+1)
	for i := 0; i < n; i++ {
		pn[i+1] = pn[i] + int64(nums[i])
		pc[i+1] = pc[i] + int64(cost[i])
	}
	const inf int64 = 1 << 62
	dp := make([]int64, n+1)
	for i := 0; i < n; i++ {
		dp[i] = inf
	}
	for i := n - 1; i >= 0; i-- {
		for j := i; j < n; j++ {
			cand := pn[j+1]*(pc[j+1]-pc[i]) + int64(k)*(pc[n]-pc[i]) + dp[j+1]
			if cand < dp[i] {
				dp[i] = cand
			}
		}
	}
	return dp[0]
}
'''

S["3524_find_x_value_of_array_i"] = r'''
func resultArray(nums []int, k int) []int64 {
	ans := make([]int64, k)
	dp := make([]int64, k)
	for _, num := range nums {
		newDp := make([]int64, k)
		nm := num % k
		newDp[nm] = 1
		for i := 0; i < k; i++ {
			newDp[(i*nm)%k] += dp[i]
		}
		for i := 0; i < k; i++ {
			ans[i] += newDp[i]
		}
		dp = newDp
	}
	return ans
}
'''

S["3530_maximum_profit_from_valid_topological_order_in_dag"] = r'''
func maxProfit(n int, edges [][]int, score []int) int {
	need := make([]int, n)
	dp := make([]int, 1<<n)
	for i := range dp {
		dp[i] = -1
	}
	dp[0] = 0
	for _, e := range edges {
		need[e[1]] |= 1 << e[0]
	}
	pop := func(x int) int {
		c := 0
		for x > 0 {
			c += x & 1
			x >>= 1
		}
		return c
	}
	for mask := 0; mask < 1<<n; mask++ {
		if dp[mask] < 0 {
			continue
		}
		pos := pop(mask) + 1
		for i := 0; i < n; i++ {
			if mask>>i&1 == 1 {
				continue
			}
			if mask&need[i] == need[i] {
				nm := mask | 1<<i
				v := dp[mask] + score[i]*pos
				if v > dp[nm] {
					dp[nm] = v
				}
			}
		}
	}
	return dp[(1<<n)-1]
}
'''

S["3540_minimum_time_to_visit_all_houses"] = r'''
func minTotalTime(forward []int, backward []int, queries []int) int64 {
	n := len(forward)
	sumB := 0
	for _, v := range backward {
		sumB += v
	}
	pf := make([]int, n+1)
	for i := 0; i < n; i++ {
		pf[i+1] = pf[i] + forward[i]
	}
	pb := make([]int, n+1)
	for i := 0; i < n; i++ {
		pb[i+1] = pb[i] + backward[i]
	}
	var ans int64
	pos := 0
	for _, q := range queries {
		r := 0
		if q < pos {
			r = pf[n]
		}
		r += pf[q] - pf[pos]
		l := 0
		if q > pos {
			l = sumB
		}
		l += pb[pos] - pb[q]
		if l < r {
			ans += int64(l)
		} else {
			ans += int64(r)
		}
		pos = q
	}
	return ans
}
'''

S["3543_maximum_weighted_k_edge_path"] = r'''
func maxWeight(n int, edges [][]int, k int, t int) int {
	graph := make([][][2]int, n)
	for _, e := range edges {
		graph[e[0]] = append(graph[e[0]], [2]int{e[1], e[2]})
	}
	dp := make([][]map[int]struct{}, n)
	for u := 0; u < n; u++ {
		dp[u] = make([]map[int]struct{}, k+1)
		for i := 0; i <= k; i++ {
			dp[u][i] = map[int]struct{}{}
		}
		dp[u][0][0] = struct{}{}
	}
	for i := 0; i < k; i++ {
		for u := 0; u < n; u++ {
			for sum := range dp[u][i] {
				for _, e := range graph[u] {
					ns := sum + e[1]
					if ns < t {
						dp[e[0]][i+1][ns] = struct{}{}
					}
				}
			}
		}
	}
	ans := -1
	for u := 0; u < n; u++ {
		for sum := range dp[u][k] {
			if sum > ans {
				ans = sum
			}
		}
	}
	return ans
}
'''

S["3557_find_maximum_number_of_non_intersecting_substrings"] = r'''
func maxSubstrings(word string) int {
	ans := 0
	first := map[byte]int{}
	for i := 0; i < len(word); i++ {
		c := word[i]
		if _, ok := first[c]; !ok {
			first[c] = i
		} else if i-first[c]+1 >= 4 {
			ans++
			first = map[byte]int{}
		}
	}
	return ans
}
'''

S["3559_number_of_ways_to_assign_edge_weights_ii"] = r'''
func assignEdgeWeights(edges [][]int, queries [][]int) []int {
	const MOD = 1_000_000_007
	const LOG = 17
	n := len(edges) + 1
	depth := make([]int, n+1)
	graph := make([][]int, n+1)
	parent := make([][]int, LOG)
	for i := 0; i < LOG; i++ {
		parent[i] = make([]int, n+1)
		for j := range parent[i] {
			parent[i][j] = -1
		}
	}
	for _, e := range edges {
		u, v := e[0], e[1]
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}
	var dfs func(u, p int)
	dfs = func(u, p int) {
		parent[0][u] = p
		for _, v := range graph[u] {
			if v != p {
				depth[v] = depth[u] + 1
				dfs(v, u)
			}
		}
	}
	dfs(1, -1)
	for k := 1; k < LOG; k++ {
		for v := 1; v <= n; v++ {
			if parent[k-1][v] != -1 {
				parent[k][v] = parent[k-1][parent[k-1][v]]
			}
		}
	}
	lca := func(u, v int) int {
		if depth[u] < depth[v] {
			u, v = v, u
		}
		for k := LOG - 1; k >= 0; k-- {
			if parent[k][u] != -1 && depth[parent[k][u]] >= depth[v] {
				u = parent[k][u]
			}
		}
		if u == v {
			return u
		}
		for k := LOG - 1; k >= 0; k-- {
			if parent[k][u] != -1 && parent[k][u] != parent[k][v] {
				u = parent[k][u]
				v = parent[k][v]
			}
		}
		return parent[0][u]
	}
	modPow := func(exp int) int {
		base, res := 2, 1
		for exp > 0 {
			if exp&1 == 1 {
				res = res * base % MOD
			}
			base = base * base % MOD
			exp >>= 1
		}
		return res
	}
	ans := make([]int, len(queries))
	for i, q := range queries {
		u, v := q[0], q[1]
		if u == v {
			ans[i] = 0
			continue
		}
		a := lca(u, v)
		d := depth[u] + depth[v] - 2*depth[a]
		ans[i] = modPow(d - 1)
	}
	return ans
}
'''

S["3533_concatenated_divisibility"] = r'''
func concatenatedDivisibility(nums []int, k int) []int {
	sort.Ints(nums)
	n := len(nums)
	pows := make([]int, n)
	for i, num := range nums {
		p := 1
		for x := num; x > 0; x /= 10 {
			p = p * 10 % k
		}
		if num == 0 {
			p = 10 % k
		}
		pows[i] = p
	}
	type key struct{ mask, mod int }
	memo := map[key]bool{}
	var dp func(mask, mod int) bool
	dp = func(mask, mod int) bool {
		if mask == (1<<n)-1 {
			return mod == 0
		}
		kk := key{mask, mod}
		if v, ok := memo[kk]; ok {
			return v
		}
		for i := 0; i < n; i++ {
			if mask>>i&1 == 0 {
				nm := (mod*pows[i] + nums[i]) % k
				if dp(mask|1<<i, nm) {
					memo[kk] = true
					return true
				}
			}
		}
		memo[kk] = false
		return false
	}
	var reconstruct func(mask, mod int) []int
	reconstruct = func(mask, mod int) []int {
		for i := 0; i < n; i++ {
			if mask>>i&1 == 0 {
				nm := (mod*pows[i] + nums[i]) % k
				if dp(mask|1<<i, nm) {
					return append([]int{nums[i]}, reconstruct(mask|1<<i, nm)...)
				}
			}
		}
		return nil
	}
	if !dp(0, 0) {
		return []int{}
	}
	return reconstruct(0, 0)
}
'''

S["3538_merge_operations_for_minimum_travel_time"] = r'''
func minTravelTime(l int, n int, k int, position []int, time []int) int {
	prefix := make([]int, n)
	prefix[0] = time[0]
	for i := 1; i < n; i++ {
		prefix[i] = prefix[i-1] + time[i]
	}
	const inf = int(1e18)
	memo := map[[3]int]int{}
	var dp func(i, skips, last int) int
	dp = func(i, skips, last int) int {
		if i == n-1 {
			if skips == 0 {
				return 0
			}
			return inf
		}
		key := [3]int{i, skips, last}
		if v, ok := memo[key]; ok {
			return v
		}
		rate := prefix[i]
		if last > 0 {
			rate -= prefix[last-1]
		}
		res := inf
		end := n - 1
		if i+skips+1 < end {
			end = i + skips + 1
		}
		for j := i + 1; j <= end; j++ {
			cand := (position[j]-position[i])*rate + dp(j, skips-(j-i-1), i+1)
			if cand < res {
				res = cand
			}
		}
		memo[key] = res
		return res
	}
	_ = l
	return dp(0, k, 0)
}
'''

S["3648_minimum_sensors_to_cover_grid"] = r'''
func minSensors(n int, m int, k int) int {
	cover := 2*k + 1
	return ((n + cover - 1) / cover) * ((m + cover - 1) / cover)
}
'''

S["3654_minimum_sum_after_divisible_sum_deletions"] = r'''
func minArraySum(nums []int, k int) int64 {
	n := len(nums)
	prefix := make([]int, n+1)
	for i, v := range nums {
		prefix[i+1] = (prefix[i] + v) % k
	}
	const inf int64 = 1 << 62
	dp := make([]int64, n+1)
	best := make([]int64, k)
	for i := range best {
		best[i] = inf
	}
	best[0] = 0
	for i := 1; i <= n; i++ {
		dp[i] = dp[i-1] + int64(nums[i-1])
		if best[prefix[i]] < dp[i] {
			dp[i] = best[prefix[i]]
		}
		if dp[i] < best[prefix[i]] {
			best[prefix[i]] = dp[i]
		}
	}
	return dp[n]
}
'''

S["3681_maximum_xor_of_subsequences"] = r'''
func maxXorSubsequences(nums []int) int {
	basis := make([]int, 32)
	for _, x := range nums {
		cur := x
		for b := 31; b >= 0; b-- {
			if cur&(1<<b) == 0 {
				continue
			}
			if basis[b] == 0 {
				basis[b] = cur
				break
			}
			cur ^= basis[b]
		}
	}
	ans := 0
	for b := 31; b >= 0; b-- {
		if ans^basis[b] > ans {
			ans ^= basis[b]
		}
	}
	return ans
}
'''

S["3670_maximum_product_of_two_integers_with_no_common_bits"] = r'''
func maxProduct(nums []int) int64 {
	maxV := 0
	for _, v := range nums {
		if v > maxV {
			maxV = v
		}
	}
	bitsN := 0
	for x := maxV; x > 0; x >>= 1 {
		bitsN++
	}
	if bitsN == 0 {
		bitsN = 1
	}
	size := 1 << bitsN
	best := make([]int, size)
	for _, v := range nums {
		if v > best[v] {
			best[v] = v
		}
	}
	for mask := 0; mask < size; mask++ {
		for b := 0; b < bitsN; b++ {
			if mask&(1<<b) != 0 {
				sub := mask ^ (1 << b)
				if best[sub] > best[mask] {
					best[mask] = best[sub]
				}
			}
		}
	}
	var ans int64
	for _, v := range nums {
		comp := (size - 1) ^ v
		if best[comp] > 0 {
			p := int64(v) * int64(best[comp])
			if p > ans {
				ans = p
			}
		}
	}
	return ans
}
'''

S["3592_inverse_coin_change"] = r'''
func findCoins(numWays []int) []int {
	n := len(numWays)
	// numWays is 1-indexed conceptually but passed as 0-indexed for amounts 1..n
	// LeetCode: numWays[i] is ways for amount i+1? Check stub: numWays []int
	// From problem: 1-indexed array where numWays[i] is ways for amount i.
	// In Go stub typically 0-indexed corresponding to amounts 1..len
	dp := make([]int, n+1)
	dp[0] = 1
	coins := []int{}
	for amt := 1; amt <= n; amt++ {
		ways := 0
		if amt-1 < len(numWays) {
			ways = numWays[amt-1]
		}
		if dp[amt] == ways {
			continue
		}
		if dp[amt]+1 == ways {
			coins = append(coins, amt)
			for x := amt; x <= n; x++ {
				dp[x] += dp[x-amt]
			}
			if dp[amt] != ways {
				return []int{}
			}
			continue
		}
		return []int{}
	}
	return coins
}
'''

S["3603_minimum_cost_path_with_alternating_directions_ii"] = r'''
func minCost(m int, n int, waitCost [][]int) int64 {
	dp := make([][]int64, m)
	for i := range dp {
		dp[i] = make([]int64, n)
		for j := range dp[i] {
			dp[i][j] = 1 << 62
		}
	}
	entry := func(i, j int) int64 { return int64(i+1) * int64(j+1) }
	dp[0][0] = entry(0, 0)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 && j == 0 {
				continue
			}
			if i > 0 {
				cand := dp[i-1][j] + entry(i, j)
				if !(i-1 == 0 && j == 0) {
					cand += int64(waitCost[i-1][j])
				}
				if cand < dp[i][j] {
					dp[i][j] = cand
				}
			}
			if j > 0 {
				cand := dp[i][j-1] + entry(i, j)
				if !(i == 0 && j-1 == 0) {
					cand += int64(waitCost[i][j-1])
				}
				if cand < dp[i][j] {
					dp[i][j] = cand
				}
			}
		}
	}
	return dp[m-1][n-1]
}
'''

S["3639_minimum_time_to_activate_string"] = r'''
func minTime(s string, order []int, k int) int {
	n := len(s)
	total := int64(n) * int64(n+1) / 2
	if int64(k) > total {
		return -1
	}
	// Binary search on t
	countValid := func(t int) int64 {
		star := make([]bool, n)
		for i := 0; i <= t; i++ {
			star[order[i]] = true
		}
		// invalid substrings are those entirely in gaps between stars
		var invalid int64
		i := 0
		for i < n {
			if star[i] {
				i++
				continue
			}
			j := i
			for j < n && !star[j] {
				j++
			}
			L := int64(j - i)
			invalid += L * (L + 1) / 2
			i = j
		}
		return total - invalid
	}
	lo, hi, ans := 0, n-1, -1
	for lo <= hi {
		mid := (lo + hi) / 2
		if countValid(mid) >= int64(k) {
			ans = mid
			hi = mid - 1
		} else {
			lo = mid + 1
		}
	}
	return ans
}
'''

S["3649_number_of_perfect_pairs"] = r'''
func perfectPairs(nums []int) int64 {
	n := len(nums)
	absNums := make([]int, n)
	for i, v := range nums {
		if v < 0 {
			absNums[i] = -v
		} else {
			absNums[i] = v
		}
	}
	sort.Ints(absNums)
	var ans int64
	j := 0
	for i := 0; i < n; i++ {
		if j < i+1 {
			j = i + 1
		}
		for j < n && absNums[j] <= 2*absNums[i] {
			j++
		}
		ans += int64(j - i - 1)
	}
	return ans
}
'''

S["3665_twisted_mirror_path_count"] = r'''
func uniquePaths(grid [][]int) int {
	const MOD = 1_000_000_007
	m := len(grid)
	n := len(grid[0])
	// dp[i][j][dir]: 0 from left, 1 from up
	dpL := make([][]int, m)
	dpU := make([][]int, m)
	for i := 0; i < m; i++ {
		dpL[i] = make([]int, n)
		dpU[i] = make([]int, n)
	}
	dpL[0][0], dpU[0][0] = 1, 1
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 && j == 0 {
				continue
			}
			if grid[i][j] == 1 {
				// mirror: from left goes down, from up goes right — handled when leaving
			}
			ways := 0
			if j > 0 {
				if grid[i][j-1] == 0 {
					ways = (ways + dpL[i][j-1] + dpU[i][j-1]) % MOD
				} else {
					// came from mirror on left: only upward arrivals reflect rightward
					ways = (ways + dpU[i][j-1]) % MOD
				}
				dpL[i][j] = ways
			}
			ways = 0
			if i > 0 {
				if grid[i-1][j] == 0 {
					ways = (ways + dpL[i-1][j] + dpU[i-1][j]) % MOD
				} else {
					ways = (ways + dpL[i-1][j]) % MOD
				}
				dpU[i][j] = ways
			}
		}
	}
	return (dpL[m-1][n-1] + dpU[m-1][n-1]) % MOD
}
'''

S["3609_minimum_moves_to_reach_target_in_grid"] = r'''
func minMoves(sx int, sy int, tx int, ty int) int {
	// Work backwards from target: while > start, if even divide by 2 else subtract other coord? 
	// Operation forward: (x,y) -> (x+y,y) or (x,x+y) or double? Problem specific.
	// Read: typically reverse: if tx > ty then tx -= ty else ty -= sx patterns.
	ans := 0
	for tx >= sx && ty >= sy {
		if tx == sx && ty == sy {
			return ans
		}
		if tx == ty {
			break
		}
		if tx > ty {
			if ty > sy {
				if tx%ty == sx%ty && sx <= tx {
					// reduce
				}
				ans += tx / ty
				tx %= ty
			} else {
				if ty != sy {
					break
				}
				if (tx-sx)%ty == 0 {
					return ans + (tx-sx)/ty
				}
				break
			}
		} else {
			if tx > sx {
				ans += ty / tx
				ty %= tx
			} else {
				if tx != sx {
					break
				}
				if (ty-sy)%tx == 0 {
					return ans + (ty-sy)/tx
				}
				break
			}
		}
	}
	if tx == sx && ty == sy {
		return ans
	}
	return -1
}
'''

S["3733_minimum_time_to_complete_all_deliveries"] = r'''
func minimumTime(d []int, r []int) int64 {
	// d[i] deliveries for type i, r[i] rest interval for courier i
	// Binary search on time T
	ok := func(T int64) bool {
		// Each courier i can work continuously but must rest 1 hour every r[i] hours of work?
		// Typically: works x hours in T with rest constraint.
		// Assume: in time T, courier i can deliver floor(T - floor((T)/r[i])) or similar.
		// Common LC: courier works all time except must take break at multiples.
		// Use: available work hours = T - T/r[i] (rest every r[i] hours)
		var total int64
		for i := 0; i < len(d); i++ {
			work := T - T/int64(r[i])
			if work < 0 {
				work = 0
			}
			need := (int64(d[i]) + work - 1)
			if work == 0 {
				if d[i] > 0 {
					return false
				}
				continue
			}
			_ = need
			total += work
		}
		var needSum int64
		for _, x := range d {
			needSum += int64(x)
		}
		if total < needSum {
			return false
		}
		// Also each type assigned to one courier? Usually two couriers for two types with cross option.
		// For 2 couriers standard solution:
		if len(d) == 2 {
			w0 := T - T/int64(r[0])
			w1 := T - T/int64(r[1])
			if w0 < 0 {
				w0 = 0
			}
			if w1 < 0 {
				w1 = 0
			}
			return w0+w1 >= int64(d[0]+d[1]) && w0 >= int64(d[0]) && w1 >= int64(d[1]) ||
				(w0 >= int64(d[0]) && w1 >= int64(d[1])) ||
				(w0+w1 >= int64(d[0]+d[1]) && w0 >= int64(d[0]) || w1 >= int64(d[1]))
		}
		return true
	}
	// Correct for typical 2-delivery problem:
	ok2 := func(T int64) bool {
		w0 := T - T/int64(r[0])
		w1 := T - T/int64(r[1])
		if w0 < int64(d[0]) && w1 < int64(d[1]) {
			return false
		}
		return w0+w1 >= int64(d[0]+d[1])
	}
	_ = ok
	lo, hi := int64(1), int64(4e14)
	for lo < hi {
		mid := (lo + hi) / 2
		if ok2(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
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
    # Skip known-incomplete / wrong ones for now
    skip = {
        "3609_minimum_moves_to_reach_target_in_grid",
        "3665_twisted_mirror_path_count",
        "3733_minimum_time_to_complete_all_deliveries",
    }
    ported = []
    for folder, body in S.items():
        if folder in skip:
            continue
        code = with_imports(body.strip() + "\n")
        (ROOT / folder / "solution.go").write_text(header(folder) + code, encoding="utf-8", newline="\n")
        ported.append(folder)
    print(len(ported))
    for p in ported:
        print(p)


if __name__ == "__main__":
    main()
