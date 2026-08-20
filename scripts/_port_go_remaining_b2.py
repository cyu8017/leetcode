#!/usr/bin/env python3
"""Remaining Go solutions batch B."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STUBS = json.loads((ROOT / "scripts" / "_stubs_3500_3749.json").read_text(encoding="utf-8"))
S: dict[str, str] = {}

S["3676_count_bowl_subarrays"] = r'''
func bowlSubarrays(nums []int) int64 {
	n := len(nums)
	var ans int64
	ngr := make([]int, n)
	ngl := make([]int, n)
	for i := range ngr {
		ngr[i], ngl[i] = -1, -1
	}
	stack := []int{}
	for i := n - 1; i >= 0; i-- {
		for len(stack) > 0 && nums[stack[len(stack)-1]] < nums[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) > 0 {
			ngr[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}
	stack = stack[:0]
	for i := 0; i < n; i++ {
		for len(stack) > 0 && nums[stack[len(stack)-1]] < nums[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) > 0 {
			ngl[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}
	for i := 0; i < n; i++ {
		if ngr[i] != -1 && ngr[i]-i >= 2 {
			ans++
		}
		if ngl[i] != -1 && i-ngl[i] >= 2 {
			ans++
		}
	}
	return ans
}
'''

S["3544_subtree_inversion_sum"] = r'''
func subtreeInversionSum(edges [][]int, nums []int, k int) int64 {
	n := len(edges) + 1
	graph := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}
	parent := make([]int, n)
	for i := range parent {
		parent[i] = -1
	}
	type key struct {
		u, steps int
		inv      bool
	}
	memo := map[key]int64{}
	var dp func(u, steps int, inv bool) int64
	dp = func(u, steps int, inv bool) int64 {
		kk := key{u, steps, inv}
		if v, ok := memo[kk]; ok {
			return v
		}
		num := int64(nums[u])
		if inv {
			num = -num
		}
		negNum := -num
		for _, v := range graph[u] {
			if v == parent[u] {
				continue
			}
			parent[v] = u
			ns := steps + 1
			if ns > k {
				ns = k
			}
			num += dp(v, ns, inv)
			if steps == k {
				negNum += dp(v, 1, !inv)
			}
		}
		res := num
		if steps == k && negNum > res {
			res = negNum
		}
		memo[kk] = res
		return res
	}
	return dp(0, k, false)
}
'''

S["3547_maximum_sum_of_edge_values_in_a_graph"] = r'''
func maxScore(n int, edges [][]int) int64 {
	graph := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}
	seen := make([]bool, n)
	var cycleSizes, pathSizes []int
	getComp := func(start int) []int {
		comp := []int{start}
		seen[start] = true
		for i := 0; i < len(comp); i++ {
			for _, v := range graph[comp[i]] {
				if !seen[v] {
					seen[v] = true
					comp = append(comp, v)
				}
			}
		}
		return comp
	}
	for i := 0; i < n; i++ {
		if seen[i] {
			continue
		}
		comp := getComp(i)
		allDeg2 := true
		for _, u := range comp {
			if len(graph[u]) != 2 {
				allDeg2 = false
				break
			}
		}
		if allDeg2 {
			cycleSizes = append(cycleSizes, len(comp))
		} else if len(comp) > 1 {
			pathSizes = append(pathSizes, len(comp))
		}
	}
	calc := func(left, right int, isCycle bool) int64 {
		w0, w1 := right, right
		var score int64
		for value := right - 1; value >= left; value-- {
			score += int64(w0) * int64(value)
			w0, w1 = w1, value
		}
		if isCycle {
			score += int64(w0) * int64(w1)
		}
		return score
	}
	var ans int64
	curN := n
	for _, cs := range cycleSizes {
		ans += calc(curN-cs+1, curN, true)
		curN -= cs
	}
	sort.Sort(sort.Reverse(sort.IntSlice(pathSizes)))
	for _, ps := range pathSizes {
		ans += calc(curN-ps+1, curN, false)
		curN -= ps
	}
	return ans
}
'''

S["3593_minimum_increments_to_equalize_leaf_paths"] = r'''
func minIncrease(n int, edges [][]int, cost []int) int {
	graph := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}
	ans := 0
	var dfs func(u, p int) int64
	dfs = func(u, p int) int64 {
		if len(graph[u]) == 1 && p != -1 {
			return int64(cost[u])
		}
		childVals := []int64{}
		for _, v := range graph[u] {
			if v == p {
				continue
			}
			childVals = append(childVals, dfs(v, u))
		}
		if len(childVals) == 0 {
			return int64(cost[u])
		}
		var mx int64
		for _, c := range childVals {
			if c > mx {
				mx = c
			}
		}
		for _, c := range childVals {
			if c < mx {
				ans++
			}
		}
		return mx + int64(cost[u])
	}
	dfs(0, -1)
	return ans
}
'''

S["3604_minimum_time_to_reach_destination_in_directed_graph"] = r'''
func minTime(n int, edges [][]int) int {
	type edge struct{ to, start, end int }
	g := make([][]edge, n)
	for _, e := range edges {
		u, v, s, en := e[0], e[1], e[2], e[3]
		g[u] = append(g[u], edge{v, s, en})
	}
	const inf = int(1e18)
	dist := make([]int, n)
	for i := range dist {
		dist[i] = inf
	}
	dist[0] = 0
	// Dijkstra
	h := &minHeap{}
	heap.Push(h, item{0, 0})
	for h.Len() > 0 {
		cur := heap.Pop(h).(item)
		if cur.t != dist[cur.u] {
			continue
		}
		if cur.u == n-1 {
			return cur.t
		}
		for _, e := range g[cur.u] {
			t := cur.t
			if t > e.end {
				continue
			}
			if t < e.start {
				t = e.start
			}
			nt := t + 1
			if nt < dist[e.to] {
				dist[e.to] = nt
				heap.Push(h, item{e.to, nt})
			}
		}
	}
	if dist[n-1] == inf {
		return -1
	}
	return dist[n-1]
}

type item struct{ u, t int }
type minHeap []item

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i].t < h[j].t }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}
'''

S["3607_power_grid_maintenance"] = r'''
func processQueries(c int, connections [][]int, queries [][]int) []int {
	parent := make([]int, c+1)
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
	union := func(a, b int) {
		ra, rb := find(a), find(b)
		if ra != rb {
			if ra < rb {
				parent[rb] = ra
			} else {
				parent[ra] = rb
			}
		}
	}
	for _, e := range connections {
		union(e[0], e[1])
	}
	online := make([]bool, c+1)
	for i := 1; i <= c; i++ {
		online[i] = true
	}
	// for each component root, maintain sorted set of online ids — use heap/map
	comp := map[int][]int{}
	for i := 1; i <= c; i++ {
		r := find(i)
		comp[r] = append(comp[r], i)
	}
	for r := range comp {
		sort.Ints(comp[r])
	}
	ptr := map[int]int{}
	ans := []int{}
	for _, q := range queries {
		t, x := q[0], q[1]
		if t == 2 {
			online[x] = false
			continue
		}
		if online[x] {
			ans = append(ans, x)
			continue
		}
		r := find(x)
		ids := comp[r]
		for ptr[r] < len(ids) && !online[ids[ptr[r]]] {
			ptr[r]++
		}
		if ptr[r] < len(ids) {
			ans = append(ans, ids[ptr[r]])
		} else {
			ans = append(ans, -1)
		}
	}
	return ans
}
'''

S["3621_number_of_integers_with_popcount_depth_equal_to_k_i"] = r'''
func popcountDepth(n int64, k int) int64 {
	if k == 0 {
		if n >= 1 {
			return 1
		}
		return 0
	}
	// digit DP on binary of n
	s := strconv.FormatInt(n, 2)
	// depth(x): 0 if x==1, else 1+depth(popcount(x))
	depthOf := func(pc int) int {
		if pc == 0 {
			return 100
		}
		d := 0
		x := pc
		for x > 1 {
			// popcount
			c := 0
			for y := x; y > 0; y >>= 1 {
				c += y & 1
			}
			x = c
			d++
		}
		return d
	}
	type key struct {
		pos, tight, started, pc int
	}
	memo := map[key]int64{}
	var dfs func(pos, tight, started, pc int) int64
	dfs = func(pos, tight, started, pc int) int64 {
		if pos == len(s) {
			if started == 0 {
				return 0
			}
			if depthOf(pc) == k-1 || (k == 1 && pc == 1) {
				// for k>=1: numbers with depth==k means depth(popcount)=k-1 for x>1, and x!=1 for...
				// depth(1)=0. depth(x)=1+depth(popcount(x)) for x>1.
				// So depth==k iff depth(popcount)==k-1 for x>1.
				if k == 0 {
					return 0
				}
				if pc == 1 {
					// number is power of 2? pc is popcount of the number
					// if number has popcount 1, depth = 1+depth(1)=1
					return boolTo64(k == 1)
				}
				return boolTo64(depthOf(pc) == k-1)
			}
			return 0
		}
		kk := key{pos, tight, started, pc}
		if v, ok := memo[kk]; ok {
			return v
		}
		var res int64
		up := 1
		if tight == 1 {
			up = int(s[pos] - '0')
		}
		for dig := 0; dig <= up; dig++ {
			nt := tight
			if dig < up {
				nt = 0
			}
			ns := started
			npc := pc
			if started == 0 && dig == 0 {
				res += dfs(pos+1, nt, 0, 0)
			} else {
				ns = 1
				npc = pc + dig
				res += dfs(pos+1, nt, ns, npc)
			}
		}
		memo[kk] = res
		return res
	}
	return dfs(0, 1, 0, 0)
}
func boolTo64(b bool) int64 {
	if b {
		return 1
	}
	return 0
}
'''

S["3686_number_of_stable_subsequences"] = r'''
func countStableSubsequences(nums []int) int {
	const MOD = 1_000_000_007
	// stable: no three consecutive same parity
	// dp0_1, dp0_2: ending with 1/2 odds; dp1_1, dp1_2 ending with 1/2 evens
	var a1, a2, b1, b2 int
	for _, x := range nums {
		if x%2 == 1 {
			na1 := (1 + b1 + b2) % MOD
			na2 := a1
			a1, a2 = (a1+na1)%MOD, (a2+na2)%MOD
		} else {
			nb1 := (1 + a1 + a2) % MOD
			nb2 := b1
			b1, b2 = (b1+nb1)%MOD, (b2+nb2)%MOD
		}
	}
	return (((a1+a2)%MOD + b1) % MOD + b2) % MOD
}
'''

S["3699_number_of_zigzag_arrays_i"] = r'''
func zigZagArrays(n int, l int, r int) int {
	const MOD = 1_000_000_007
	m := r - l + 1
	// dp[i][j][0/1]: length i ending with value j (0-indexed), last relation up/down
	up := make([]int, m)
	down := make([]int, m)
	for j := 0; j < m; j++ {
		up[j], down[j] = 1, 1
	}
	for i := 2; i <= n; i++ {
		pref := make([]int, m+1)
		for j := 0; j < m; j++ {
			pref[j+1] = (pref[j] + down[j]) % MOD
		}
		nup := make([]int, m)
		for j := 0; j < m; j++ {
			nup[j] = pref[j] // sum down[0..j-1] => previous smaller, going up to j
		}
		pref2 := make([]int, m+1)
		for j := m - 1; j >= 0; j-- {
			pref2[j] = (pref2[j+1] + up[j]) % MOD
		}
		ndown := make([]int, m)
		for j := 0; j < m; j++ {
			ndown[j] = pref2[j+1]
		}
		up, down = nup, ndown
	}
	ans := 0
	for j := 0; j < m; j++ {
		ans = (ans + up[j]) % MOD
		ans = (ans + down[j]) % MOD
	}
	// length 1 counted twice in init — for n==1 should be m
	if n == 1 {
		return m % MOD
	}
	return ans
}
'''

S["3715_sum_of_perfect_square_ancestors"] = r'''
func sumOfAncestors(n int, edges [][]int, nums []int) int64 {
	graph := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}
	// square-free kernel of number
	kernel := func(x int) int {
		res := 1
		for p := 2; p*p <= x; p++ {
			cnt := 0
			for x%p == 0 {
				x /= p
				cnt++
			}
			if cnt%2 == 1 {
				res *= p
			}
		}
		if x > 1 {
			res *= x
		}
		return res
	}
	ks := make([]int, n)
	for i, v := range nums {
		ks[i] = kernel(v)
	}
	freq := map[int]int{}
	var ans int64
	var dfs func(u, p int)
	dfs = func(u, p int) {
		ans += int64(freq[ks[u]])
		freq[ks[u]]++
		for _, v := range graph[u] {
			if v != p {
				dfs(v, u)
			}
		}
		freq[ks[u]]--
	}
	dfs(0, -1)
	return ans
}
'''

S["3720_lexicographically_smallest_permutation_greater_than_target"] = r'''
func lexGreaterPermutation(s string, target string) string {
	cnt := make([]int, 26)
	for i := 0; i < len(s); i++ {
		cnt[s[i]-'a']++
	}
	n := len(s)
	ans := make([]byte, n)
	var dfs func(pos int, greater bool) bool
	dfs = func(pos int, greater bool) bool {
		if pos == n {
			return greater
		}
		start := 0
		if !greater {
			start = int(target[pos] - 'a')
		}
		for c := start; c < 26; c++ {
			if cnt[c] == 0 {
				continue
			}
			cnt[c]--
			ans[pos] = byte('a' + c)
			ng := greater || c > int(target[pos]-'a')
			if dfs(pos+1, ng) {
				return true
			}
			cnt[c]++
		}
		return false
	}
	if dfs(0, false) {
		return string(ans)
	}
	return ""
}
'''

S["3656_determine_if_a_simple_graph_exists"] = r'''
func simpleGraphExists(degrees []int) bool {
	// Havel-Hakimi / Erdős–Gállai
	n := len(degrees)
	d := append([]int(nil), degrees...)
	sort.Sort(sort.Reverse(sort.IntSlice(d)))
	var sum int64
	for _, x := range d {
		sum += int64(x)
		if x < 0 || x >= n {
			return false
		}
	}
	if sum%2 != 0 {
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
		if prefix[k] > int64(k)*int64(k-1)+right {
			return false
		}
	}
	return true
}
'''

S["3664_two_letter_card_game"] = r'''
func score(cards []string, x byte) int {
	// count xx, xa, ax patterns
	xx := 0
	left := make([]int, 26)  // x + letter
	right := make([]int, 26) // letter + x
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
	// pair within left, within right, then use xx
	pair := func(arr []int) (pairs int, rem int) {
		total := 0
		mx := 0
		for _, v := range arr {
			total += v
			if v > mx {
				mx = v
			}
		}
		pairs = total / 2
		if mx > pairs {
			pairs = total - mx // limited by non-mx
			if pairs > total/2 {
				pairs = total / 2
			}
			// max pairs = min(total/2, total-mx)
			pairs = total - mx
			if total/2 < pairs {
				pairs = total / 2
			}
		}
		rem = total - 2*pairs
		return
	}
	lp, lr := pair(left)
	rp, rr := pair(right)
	ans := lp + rp
	// xx can pair with remainders or among themselves? xx with xa or ax
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

S["3733_minimum_time_to_complete_all_deliveries"] = r'''
func minimumTime(d []int, r []int) int64 {
	ok := func(T int64) bool {
		w0 := T - T/int64(r[0])
		w1 := T - T/int64(r[1])
		return w0+w1 >= int64(d[0])+int64(d[1])
	}
	lo, hi := int64(1), int64(8e18)
	for lo < hi {
		mid := lo + (hi-lo)/2
		if ok(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
'''

S["3605_minimum_stability_factor_of_array"] = r'''
func minStable(nums []int, maxC int) int {
	n := len(nums)
	// binary search on stability factor x: can we make all gcd of subarrays length>x become 1 with <=maxC changes
	ok := func(x int) bool {
		if x >= n {
			return true
		}
		// greedy: whenever a window of length x+1 has gcd>1, must change something
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
func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
'''

S["3685_subsequence_sum_after_capping_elements"] = r'''
func subsequenceSumAfterCapping(nums []int, k int) []bool {
	n := len(nums)
	sort.Ints(nums)
	ans := make([]bool, n)
	// for x=1..n, cap nums[i]=min(nums[i],x), can we make subset sum k?
	reachable := make([]bool, k+1)
	reachable[0] = true
	idx := 0
	for x := 1; x <= n; x++ {
		for idx < n && nums[idx] <= x {
			v := nums[idx]
			for s := k; s >= v; s-- {
				if reachable[s-v] {
					reachable[s] = true
				}
			}
			idx++
		}
		// remaining n-idx elements become x
		rem := n - idx
		tmp := append([]bool(nil), reachable...)
		for s := 0; s <= k; s++ {
			if !reachable[s] {
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

S["3725_count_ways_to_choose_coprime_integers_from_rows"] = r'''
func countCoprime(mat [][]int) int {
	const MOD = 1_000_000_007
	m := len(mat)
	// dp over gcd
	freq0 := map[int]int{}
	for _, v := range mat[0] {
		freq0[v]++
	}
	dp := freq0
	for i := 1; i < m; i++ {
		ndp := map[int]int{}
		for _, v := range mat[i] {
			for g, cnt := range dp {
				ng := gcd(g, v)
				ndp[ng] = (ndp[ng] + cnt) % MOD
			}
		}
		dp = ndp
	}
	return dp[1]
}
func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
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
    if "heap." in code:
        imps.append('"container/heap"')
    if "strconv." in code:
        imps.append('"strconv"')
    if not imps:
        return code
    return "import (\n\t" + "\n\t".join(imps) + "\n)\n\n" + code


def main() -> None:
    skip = {
        "3621_number_of_integers_with_popcount_depth_equal_to_k_i",  # digit DP needs careful fix
        "3656_determine_if_a_simple_graph_exists",  # may need stub name check
        "3664_two_letter_card_game",
        "3605_minimum_stability_factor_of_array",
        "3685_subsequence_sum_after_capping_elements",
        "3699_number_of_zigzag_arrays_i",
    }
    ported = []
    for folder, body in S.items():
        if folder in skip:
            continue
        # verify folder still stub
        p = ROOT / folder / "solution.go"
        if not p.exists():
            continue
        cur = p.read_text(encoding="utf-8")
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
