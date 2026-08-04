#!/usr/bin/env python3
"""Write Go solutions for folders 1190-1249."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(r"c:\Users\Charlie Yu\Documents\leetcode")
SOLUTIONS: dict[str, str] = {}

SOLUTIONS["1190_reverse_substrings_between_each_pair_of_parentheses"] = r'''// LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

func reverseParentheses(s string) string {
	stack := []byte{}
	for i := 0; i < len(s); i++ {
		if s[i] == ')' {
			chunk := []byte{}
			for len(stack) > 0 && stack[len(stack)-1] != '(' {
				chunk = append(chunk, stack[len(stack)-1])
				stack = stack[:len(stack)-1]
			}
			stack = stack[:len(stack)-1]
			stack = append(stack, chunk...)
		} else {
			stack = append(stack, s[i])
		}
	}
	return string(stack)
}
'''

SOLUTIONS["1191_k_concatenation_maximum_sum"] = r'''// LeetCode 1191 - K-Concatenation Maximum Sum
// https://leetcode.com/problems/k-concatenation-maximum-sum/

func kConcatenationMaxSum(arr []int, k int) int {
	const MOD = 1000000007
	kadane := func(nums []int) int {
		best, cur := 0, 0
		for _, x := range nums {
			cur += x
			if cur < 0 {
				cur = 0
			}
			if cur > best {
				best = cur
			}
		}
		return best
	}
	one := kadane(arr)
	if k == 1 {
		return one % MOD
	}
	twoArr := append(append([]int{}, arr...), arr...)
	two := kadane(twoArr)
	total := 0
	for _, x := range arr {
		total += x
	}
	ans := one
	if two > ans {
		ans = two
	}
	if total > 0 {
		cand := two + total*(k-2)
		if cand > ans {
			ans = cand
		}
	}
	return ans % MOD
}
'''

SOLUTIONS["1192_critical_connections_in_a_network"] = r'''// LeetCode 1192 - Critical Connections in a Network
// https://leetcode.com/problems/critical-connections-in-a-network/

func criticalConnections(n int, connections [][]int) [][]int {
	graph := make([][]int, n)
	for _, e := range connections {
		graph[e[0]] = append(graph[e[0]], e[1])
		graph[e[1]] = append(graph[e[1]], e[0])
	}
	disc := make([]int, n)
	low := make([]int, n)
	for i := range disc {
		disc[i] = -1
	}
	time := 0
	bridges := [][]int{}
	var dfs func(int, int)
	dfs = func(node, parent int) {
		disc[node] = time
		low[node] = time
		time++
		for _, nxt := range graph[node] {
			if nxt == parent {
				continue
			}
			if disc[nxt] == -1 {
				dfs(nxt, node)
				if low[nxt] < low[node] {
					low[node] = low[nxt]
				}
				if low[nxt] > disc[node] {
					a, b := node, nxt
					if a > b {
						a, b = b, a
					}
					bridges = append(bridges, []int{a, b})
				}
			} else if disc[nxt] < low[node] {
				low[node] = disc[nxt]
			}
		}
	}
	dfs(0, -1)
	return bridges
}
'''

SOLUTIONS["1195_fizz_buzz_multithreaded"] = r'''// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

import "sync"

type FizzBuzz struct {
	n       int
	current int
	cond    *sync.Cond
}

func NewFizzBuzz(n int) *FizzBuzz {
	fb := &FizzBuzz{n: n, current: 1}
	fb.cond = sync.NewCond(&sync.Mutex{})
	return fb
}

func (fb *FizzBuzz) run(pred func(int) bool, action func()) {
	fb.cond.L.Lock()
	defer fb.cond.L.Unlock()
	for fb.current <= fb.n {
		if pred(fb.current) {
			action()
			fb.current++
			fb.cond.Broadcast()
		} else {
			fb.cond.Wait()
		}
	}
}

func (fb *FizzBuzz) Fizz(printFizz func()) {
	fb.run(func(x int) bool { return x%3 == 0 && x%5 != 0 }, printFizz)
}

func (fb *FizzBuzz) Buzz(printBuzz func()) {
	fb.run(func(x int) bool { return x%5 == 0 && x%3 != 0 }, printBuzz)
}

func (fb *FizzBuzz) Fizzbuzz(printFizzBuzz func()) {
	fb.run(func(x int) bool { return x%15 == 0 }, printFizzBuzz)
}

func (fb *FizzBuzz) Number(printNumber func(int)) {
	fb.run(func(x int) bool { return x%3 != 0 && x%5 != 0 }, func() { printNumber(fb.current) })
}
'''

SOLUTIONS["1196_how_many_apples_can_you_put_into_the_basket"] = r'''// LeetCode 1196 - How Many Apples Can You Put into the Basket
// https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

import "sort"

func maxNumberOfApples(weight []int) int {
	sort.Ints(weight)
	total := 0
	for i, w := range weight {
		total += w
		if total > 5000 {
			return i
		}
	}
	return len(weight)
}
'''

SOLUTIONS["1197_minimum_knight_moves"] = r'''// LeetCode 1197 - Minimum Knight Moves
// https://leetcode.com/problems/minimum-knight-moves/

func minKnightMoves(x int, y int) int {
	if x < 0 {
		x = -x
	}
	if y < 0 {
		y = -y
	}
	memo := map[[2]int]int{}
	var dfs func(int, int) int
	dfs = func(a, b int) int {
		if a < b {
			a, b = b, a
		}
		key := [2]int{a, b}
		if v, ok := memo[key]; ok {
			return v
		}
		if a+b == 0 {
			return 0
		}
		if a+b == 2 {
			return 2
		}
		v := dfs(abs(a-1), abs(b-2))
		w := dfs(abs(a-2), abs(b-1))
		if w < v {
			v = w
		}
		memo[key] = v + 1
		return v + 1
	}
	return dfs(x, y)
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
'''

SOLUTIONS["1198_find_smallest_common_element_in_all_rows"] = r'''// LeetCode 1198 - Find Smallest Common Element in All Rows
// https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

func smallestCommonElement(mat [][]int) int {
	common := map[int]bool{}
	for _, x := range mat[0] {
		common[x] = true
	}
	for _, row := range mat[1:] {
		next := map[int]bool{}
		for _, x := range row {
			if common[x] {
				next[x] = true
			}
		}
		common = next
		if len(common) == 0 {
			return -1
		}
	}
	ans := int(^uint(0) >> 1)
	for x := range common {
		if x < ans {
			ans = x
		}
	}
	return ans
}
'''

SOLUTIONS["1199_minimum_time_to_build_blocks"] = r'''// LeetCode 1199 - Minimum Time to Build Blocks
// https://leetcode.com/problems/minimum-time-to-build-blocks/

import "container/heap"

type minH []int

func (h minH) Len() int            { return len(h) }
func (h minH) Less(i, j int) bool  { return h[i] < h[j] }
func (h minH) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minH) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *minH) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minBuildTime(blocks []int, split int) int {
	h := minH(append([]int{}, blocks...))
	heap.Init(&h)
	for h.Len() > 1 {
		heap.Pop(&h)
		b := heap.Pop(&h).(int)
		heap.Push(&h, b+split)
	}
	return h[0]
}
'''

SOLUTIONS["1200_minimum_absolute_difference"] = r'''// LeetCode 1200 - Minimum Absolute Difference
// https://leetcode.com/problems/minimum-absolute-difference/

import "sort"

func minimumAbsDifference(arr []int) [][]int {
	sort.Ints(arr)
	best := arr[1] - arr[0]
	for i := 2; i < len(arr); i++ {
		if arr[i]-arr[i-1] < best {
			best = arr[i] - arr[i-1]
		}
	}
	ans := [][]int{}
	for i := 1; i < len(arr); i++ {
		if arr[i]-arr[i-1] == best {
			ans = append(ans, []int{arr[i-1], arr[i]})
		}
	}
	return ans
}
'''

SOLUTIONS["1201_ugly_number_iii"] = r'''// LeetCode 1201 - Ugly Number III
// https://leetcode.com/problems/ugly-number-iii/

func nthUglyNumber(n int, a int, b int, c int) int {
	gcd := func(x, y int) int {
		for y != 0 {
			x, y = y, x%y
		}
		return x
	}
	lcm := func(x, y int) int { return x / gcd(x, y) * y }
	ab, ac, bc := lcm(a, b), lcm(a, c), lcm(b, c)
	abc := lcm(ab, c)
	count := func(x int) int {
		return x/a + x/b + x/c - x/ab - x/ac - x/bc + x/abc
	}
	lo, hi := 1, 2000000000
	for lo < hi {
		mid := lo + (hi-lo)/2
		if count(mid) >= n {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
'''

SOLUTIONS["1202_smallest_string_with_swaps"] = r'''// LeetCode 1202 - Smallest String With Swaps
// https://leetcode.com/problems/smallest-string-with-swaps/

import "sort"

func smallestStringWithSwaps(s string, pairs [][]int) string {
	parent := make([]int, len(s))
	for i := range parent {
		parent[i] = i
	}
	var find func(int) int
	find = func(x int) int {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	for _, p := range pairs {
		ra, rb := find(p[0]), find(p[1])
		parent[ra] = rb
	}
	groups := map[int][]byte{}
	for i := 0; i < len(s); i++ {
		r := find(i)
		groups[r] = append(groups[r], s[i])
	}
	for r := range groups {
		sort.Slice(groups[r], func(i, j int) bool { return groups[r][i] > groups[r][j] })
	}
	out := make([]byte, len(s))
	for i := 0; i < len(s); i++ {
		r := find(i)
		g := groups[r]
		out[i] = g[len(g)-1]
		groups[r] = g[:len(g)-1]
	}
	return string(out)
}
'''

SOLUTIONS["1203_sort_items_by_groups_respecting_dependencies"] = r'''// LeetCode 1203 - Sort Items by Groups Respecting Dependencies
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

func sortItems(n int, m int, group []int, beforeItems [][]int) []int {
	group = append([]int{}, group...)
	for i := 0; i < n; i++ {
		if group[i] == -1 {
			group[i] = m
			m++
		}
	}
	itemGraph := make([][]int, n)
	itemIndeg := make([]int, n)
	groupGraph := make([]map[int]bool, m)
	for i := range groupGraph {
		groupGraph[i] = map[int]bool{}
	}
	groupIndeg := make([]int, m)
	for v := 0; v < n; v++ {
		for _, u := range beforeItems[v] {
			itemGraph[u] = append(itemGraph[u], v)
			itemIndeg[v]++
			if group[u] != group[v] && !groupGraph[group[u]][group[v]] {
				groupGraph[group[u]][group[v]] = true
				groupIndeg[group[v]]++
			}
		}
	}
	topo := func(graph [][]int, indeg []int) []int {
		q := []int{}
		for i, d := range indeg {
			if d == 0 {
				q = append(q, i)
			}
		}
		order := []int{}
		for len(q) > 0 {
			u := q[0]
			q = q[1:]
			order = append(order, u)
			for _, v := range graph[u] {
				indeg[v]--
				if indeg[v] == 0 {
					q = append(q, v)
				}
			}
		}
		if len(order) != len(graph) {
			return nil
		}
		return order
	}
	gAdj := make([][]int, m)
	for u := 0; u < m; u++ {
		for v := range groupGraph[u] {
			gAdj[u] = append(gAdj[u], v)
		}
	}
	items := topo(itemGraph, itemIndeg)
	groups := topo(gAdj, groupIndeg)
	if items == nil || groups == nil {
		return []int{}
	}
	buckets := make([][]int, m)
	for _, item := range items {
		buckets[group[item]] = append(buckets[group[item]], item)
	}
	ans := []int{}
	for _, g := range groups {
		ans = append(ans, buckets[g]...)
	}
	return ans
}
'''

SOLUTIONS["1206_design_skiplist"] = r'''// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

import "sort"

type Skiplist struct {
	values []int
}

func Constructor() Skiplist {
	return Skiplist{values: []int{}}
}

func (this *Skiplist) Search(target int) bool {
	i := sort.SearchInts(this.values, target)
	return i < len(this.values) && this.values[i] == target
}

func (this *Skiplist) Add(num int) {
	i := sort.SearchInts(this.values, num)
	this.values = append(this.values, 0)
	copy(this.values[i+1:], this.values[i:])
	this.values[i] = num
}

func (this *Skiplist) Erase(num int) bool {
	i := sort.SearchInts(this.values, num)
	if i == len(this.values) || this.values[i] != num {
		return false
	}
	this.values = append(this.values[:i], this.values[i+1:]...)
	return true
}
'''

SOLUTIONS["1207_unique_number_of_occurrences"] = r'''// LeetCode 1207 - Unique Number of Occurrences
// https://leetcode.com/problems/unique-number-of-occurrences/

func uniqueOccurrences(arr []int) bool {
	count := map[int]int{}
	for _, x := range arr {
		count[x]++
	}
	seen := map[int]bool{}
	for _, c := range count {
		if seen[c] {
			return false
		}
		seen[c] = true
	}
	return true
}
'''

SOLUTIONS["1208_get_equal_substrings_within_budget"] = r'''// LeetCode 1208 - Get Equal Substrings Within Budget
// https://leetcode.com/problems/get-equal-substrings-within-budget/

func equalSubstring(s string, t string, maxCost int) int {
	left, cost, answer := 0, 0, 0
	for right := 0; right < len(s); right++ {
		diff := int(s[right]) - int(t[right])
		if diff < 0 {
			diff = -diff
		}
		cost += diff
		for cost > maxCost {
			d := int(s[left]) - int(t[left])
			if d < 0 {
				d = -d
			}
			cost -= d
			left++
		}
		if right-left+1 > answer {
			answer = right - left + 1
		}
	}
	return answer
}
'''

SOLUTIONS["1209_remove_all_adjacent_duplicates_in_string_ii"] = r'''// LeetCode 1209 - Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

func removeDuplicates(s string, k int) string {
	type pair struct {
		ch  byte
		cnt int
	}
	stack := []pair{}
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if len(stack) > 0 && stack[len(stack)-1].ch == ch {
			stack[len(stack)-1].cnt++
		} else {
			stack = append(stack, pair{ch, 1})
		}
		if stack[len(stack)-1].cnt == k {
			stack = stack[:len(stack)-1]
		}
	}
	out := []byte{}
	for _, p := range stack {
		for i := 0; i < p.cnt; i++ {
			out = append(out, p.ch)
		}
	}
	return string(out)
}
'''

SOLUTIONS["1210_minimum_moves_to_reach_target_with_rotations"] = r'''// LeetCode 1210 - Minimum Moves to Reach Target with Rotations
// https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

func minimumMoves(grid [][]int) int {
	n := len(grid)
	type state struct{ r, c, orient int }
	start, target := state{0, 0, 0}, state{n - 1, n - 2, 0}
	type item struct {
		s     state
		moves int
	}
	q := []item{{start, 0}}
	seen := map[state]bool{start: true}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		if cur.s == target {
			return cur.moves
		}
		r, c, orient := cur.s.r, cur.s.c, cur.s.orient
		nxt := []state{}
		if orient == 0 {
			if c+2 < n && grid[r][c+2] == 0 {
				nxt = append(nxt, state{r, c + 1, 0})
			}
			if r+1 < n && grid[r+1][c] == 0 && grid[r+1][c+1] == 0 {
				nxt = append(nxt, state{r + 1, c, 0}, state{r, c, 1})
			}
		} else {
			if r+2 < n && grid[r+2][c] == 0 {
				nxt = append(nxt, state{r + 1, c, 1})
			}
			if c+1 < n && grid[r][c+1] == 0 && grid[r+1][c+1] == 0 {
				nxt = append(nxt, state{r, c + 1, 1}, state{r, c, 0})
			}
		}
		for _, st := range nxt {
			if !seen[st] {
				seen[st] = true
				q = append(q, item{st, cur.moves + 1})
			}
		}
	}
	return -1
}
'''

SOLUTIONS["1213_intersection_of_three_sorted_arrays"] = r'''// LeetCode 1213 - Intersection of Three Sorted Arrays
// https://leetcode.com/problems/intersection-of-three-sorted-arrays/

func arraysIntersection(arr1 []int, arr2 []int, arr3 []int) []int {
	i, j, k := 0, 0, 0
	ans := []int{}
	for i < len(arr1) && j < len(arr2) && k < len(arr3) {
		a, b, c := arr1[i], arr2[j], arr3[k]
		if a == b && b == c {
			ans = append(ans, a)
			i++
			j++
			k++
		} else if a <= b && a <= c {
			i++
		} else if b <= a && b <= c {
			j++
		} else {
			k++
		}
	}
	return ans
}
'''

SOLUTIONS["1214_two_sum_bsts"] = r'''// LeetCode 1214 - Two Sum BSTs
// https://leetcode.com/problems/two-sum-bsts/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func twoSumBSTs(root1 *TreeNode, root2 *TreeNode, target int) bool {
	values := map[int]bool{}
	stack := []*TreeNode{}
	if root1 != nil {
		stack = append(stack, root1)
	}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		values[node.Val] = true
		if node.Left != nil {
			stack = append(stack, node.Left)
		}
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
	}
	stack = nil
	if root2 != nil {
		stack = append(stack, root2)
	}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if values[target-node.Val] {
			return true
		}
		if node.Left != nil {
			stack = append(stack, node.Left)
		}
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
	}
	return false
}
'''

SOLUTIONS["1215_stepping_numbers"] = r'''// LeetCode 1215 - Stepping Numbers
// https://leetcode.com/problems/stepping-numbers/

func countSteppingNumbers(low int, high int) []int {
	ans := []int{}
	if low == 0 {
		ans = append(ans, 0)
	}
	q := []int{}
	for i := 1; i <= 9; i++ {
		q = append(q, i)
	}
	for len(q) > 0 {
		x := q[0]
		q = q[1:]
		if x > high {
			continue
		}
		if x >= low {
			ans = append(ans, x)
		}
		last := x % 10
		if last > 0 {
			q = append(q, x*10+last-1)
		}
		if last < 9 {
			q = append(q, x*10+last+1)
		}
	}
	return ans
}
'''

SOLUTIONS["1216_valid_palindrome_iii"] = r'''// LeetCode 1216 - Valid Palindrome III
// https://leetcode.com/problems/valid-palindrome-iii/

func isValidPalindrome(s string, k int) bool {
	n := len(s)
	if n == 0 {
		return true
	}
	dp := make([]int, n)
	for i := n - 1; i >= 0; i-- {
		previous := 0
		for j := i + 1; j < n; j++ {
			old := dp[j]
			if s[i] == s[j] {
				dp[j] = previous
			} else {
				dp[j] = 1 + dp[j]
				if 1+dp[j-1] < dp[j] {
					dp[j] = 1 + dp[j-1]
				}
			}
			previous = old
		}
	}
	return dp[n-1] <= k
}
'''

SOLUTIONS["1217_minimum_cost_to_move_chips_to_the_same_position"] = r'''// LeetCode 1217 - Minimum Cost to Move Chips to The Same Position
// https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

func minCostToMoveChips(position []int) int {
	odd := 0
	for _, x := range position {
		odd += x & 1
	}
	even := len(position) - odd
	if odd < even {
		return odd
	}
	return even
}
'''

SOLUTIONS["1218_longest_arithmetic_subsequence_of_given_difference"] = r'''// LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

func longestSubsequence(arr []int, difference int) int {
	dp := map[int]int{}
	best := 0
	for _, x := range arr {
		dp[x] = dp[x-difference] + 1
		if dp[x] > best {
			best = dp[x]
		}
	}
	return best
}
'''

SOLUTIONS["1219_path_with_maximum_gold"] = r'''// LeetCode 1219 - Path with Maximum Gold
// https://leetcode.com/problems/path-with-maximum-gold/

func getMaximumGold(grid [][]int) int {
	rows, cols := len(grid), len(grid[0])
	var dfs func(int, int) int
	dfs = func(r, c int) int {
		gold := grid[r][c]
		grid[r][c] = 0
		best := 0
		for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
			nr, nc := r+d[0], c+d[1]
			if nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] > 0 {
				v := dfs(nr, nc)
				if v > best {
					best = v
				}
			}
		}
		grid[r][c] = gold
		return gold + best
	}
	ans := 0
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if grid[r][c] > 0 {
				v := dfs(r, c)
				if v > ans {
					ans = v
				}
			}
		}
	}
	return ans
}
'''

SOLUTIONS["1220_count_vowels_permutation"] = r'''// LeetCode 1220 - Count Vowels Permutation
// https://leetcode.com/problems/count-vowels-permutation/

func countVowelPermutation(n int) int {
	const mod = 1000000007
	a, e, i, o, u := 1, 1, 1, 1, 1
	for step := 1; step < n; step++ {
		a, e, i, o, u = (e+i+u)%mod, (a+i)%mod, (e+o)%mod, i, (i+o)%mod
	}
	return (a + e + i + o + u) % mod
}
'''

SOLUTIONS["1221_split_a_string_in_balanced_strings"] = r'''// LeetCode 1221 - Split a String in Balanced Strings
// https://leetcode.com/problems/split-a-string-in-balanced-strings/

func balancedStringSplit(s string) int {
	balance, answer := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == 'L' {
			balance++
		} else {
			balance--
		}
		if balance == 0 {
			answer++
		}
	}
	return answer
}
'''

SOLUTIONS["1222_queens_that_can_attack_the_king"] = r'''// LeetCode 1222 - Queens That Can Attack the King
// https://leetcode.com/problems/queens-that-can-attack-the-king/

func queensAttacktheKing(queens [][]int, king []int) [][]int {
	occupied := map[[2]int]bool{}
	for _, q := range queens {
		occupied[[2]int{q[0], q[1]}] = true
	}
	ans := [][]int{}
	for dr := -1; dr <= 1; dr++ {
		for dc := -1; dc <= 1; dc++ {
			if dr == 0 && dc == 0 {
				continue
			}
			r, c := king[0]+dr, king[1]+dc
			for r >= 0 && r < 8 && c >= 0 && c < 8 {
				if occupied[[2]int{r, c}] {
					ans = append(ans, []int{r, c})
					break
				}
				r += dr
				c += dc
			}
		}
	}
	return ans
}
'''

SOLUTIONS["1223_dice_roll_simulation"] = r'''// LeetCode 1223 - Dice Roll Simulation
// https://leetcode.com/problems/dice-roll-simulation/

func dieSimulator(n int, rollMax []int) int {
	const mod = 1000000007
	dp := make([][]int, 6)
	for j := 0; j < 6; j++ {
		dp[j] = make([]int, rollMax[j]+1)
		dp[j][1] = 1
	}
	for step := 1; step < n; step++ {
		totals := make([]int, 6)
		for j := 0; j < 6; j++ {
			for _, v := range dp[j] {
				totals[j] = (totals[j] + v) % mod
			}
		}
		all := 0
		for _, t := range totals {
			all = (all + t) % mod
		}
		nxt := make([][]int, 6)
		for j := 0; j < 6; j++ {
			nxt[j] = make([]int, len(dp[j]))
			nxt[j][1] = (all - totals[j] + mod) % mod
			for run := 2; run < len(dp[j]); run++ {
				nxt[j][run] = dp[j][run-1]
			}
		}
		dp = nxt
	}
	ans := 0
	for j := 0; j < 6; j++ {
		for _, v := range dp[j] {
			ans = (ans + v) % mod
		}
	}
	return ans
}
'''

SOLUTIONS["1224_maximum_equal_frequency"] = r'''// LeetCode 1224 - Maximum Equal Frequency
// https://leetcode.com/problems/maximum-equal-frequency/

func maxEqualFreq(nums []int) int {
	count := map[int]int{}
	frequencies := map[int]int{}
	answer := 0
	for i, x := range nums {
		old := count[x]
		if old > 0 {
			frequencies[old]--
			if frequencies[old] == 0 {
				delete(frequencies, old)
			}
		}
		count[x]++
		frequencies[old+1]++
		high := 0
		for f := range frequencies {
			if f > high {
				high = f
			}
		}
		idx := i + 1
		if high == 1 || frequencies[high]*high+1 == idx || (frequencies[high] == 1 && frequencies[high-1]*(high-1)+high == idx) {
			answer = idx
		}
	}
	return answer
}
'''

SOLUTIONS["1226_the_dining_philosophers"] = r'''// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

import "sync"

type DiningPhilosophers struct {
	forks [5]sync.Mutex
}

func Constructor() *DiningPhilosophers {
	return &DiningPhilosophers{}
}

func (d *DiningPhilosophers) WantsToEat(philosopher int, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork func()) {
	left, right := philosopher, (philosopher+1)%5
	first, second := left, right
	if philosopher%2 != 0 {
		first, second = right, left
	}
	d.forks[first].Lock()
	d.forks[second].Lock()
	pickLeftFork()
	pickRightFork()
	eat()
	putLeftFork()
	putRightFork()
	d.forks[second].Unlock()
	d.forks[first].Unlock()
}
'''

SOLUTIONS["1227_airplane_seat_assignment_probability"] = r'''// LeetCode 1227 - Airplane Seat Assignment Probability
// https://leetcode.com/problems/airplane-seat-assignment-probability/

func nthPersonGetsNthSeat(n int) float64 {
	if n == 1 {
		return 1.0
	}
	return 0.5
}
'''

SOLUTIONS["1228_missing_number_in_arithmetic_progression"] = r'''// LeetCode 1228 - Missing Number In Arithmetic Progression
// https://leetcode.com/problems/missing-number-in-arithmetic-progression/

func missingNumber(arr []int) int {
	difference := (arr[len(arr)-1] - arr[0]) / len(arr)
	for i := 1; i < len(arr); i++ {
		expected := arr[0] + i*difference
		if arr[i] != expected {
			return expected
		}
	}
	return arr[0]
}
'''

SOLUTIONS["1229_meeting_scheduler"] = r'''// LeetCode 1229 - Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler/

import "sort"

func minAvailableDuration(slots1 [][]int, slots2 [][]int, duration int) []int {
	sort.Slice(slots1, func(i, j int) bool { return slots1[i][0] < slots1[j][0] })
	sort.Slice(slots2, func(i, j int) bool { return slots2[i][0] < slots2[j][0] })
	i, j := 0, 0
	for i < len(slots1) && j < len(slots2) {
		start := slots1[i][0]
		if slots2[j][0] > start {
			start = slots2[j][0]
		}
		end := slots1[i][1]
		if slots2[j][1] < end {
			end = slots2[j][1]
		}
		if end-start >= duration {
			return []int{start, start + duration}
		}
		if slots1[i][1] < slots2[j][1] {
			i++
		} else {
			j++
		}
	}
	return []int{}
}
'''

SOLUTIONS["1230_toss_strange_coins"] = r'''// LeetCode 1230 - Toss Strange Coins
// https://leetcode.com/problems/toss-strange-coins/

func probabilityOfHeads(prob []float64, target int) float64 {
	dp := make([]float64, target+1)
	dp[0] = 1
	for _, p := range prob {
		for heads := target; heads >= 0; heads-- {
			v := dp[heads] * (1 - p)
			if heads > 0 {
				v += dp[heads-1] * p
			}
			dp[heads] = v
		}
	}
	return dp[target]
}
'''

SOLUTIONS["1231_divide_chocolate"] = r'''// LeetCode 1231 - Divide Chocolate
// https://leetcode.com/problems/divide-chocolate/

func maximizeSweetness(sweetness []int, k int) int {
	total := 0
	for _, v := range sweetness {
		total += v
	}
	lo, hi := 1, total/(k+1)
	for lo <= hi {
		mid := (lo + hi) / 2
		pieces, current := 0, 0
		for _, value := range sweetness {
			current += value
			if current >= mid {
				pieces++
				current = 0
			}
		}
		if pieces >= k+1 {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return hi
}
'''

SOLUTIONS["1232_check_if_it_is_a_straight_line"] = r'''// LeetCode 1232 - Check If It Is a Straight Line
// https://leetcode.com/problems/check-if-it-is-a-straight-line/

func checkStraightLine(coordinates [][]int) bool {
	x0, y0 := coordinates[0][0], coordinates[0][1]
	dx, dy := coordinates[1][0]-x0, coordinates[1][1]-y0
	for _, p := range coordinates[2:] {
		if (p[0]-x0)*dy != (p[1]-y0)*dx {
			return false
		}
	}
	return true
}
'''

SOLUTIONS["1233_remove_sub_folders_from_the_filesystem"] = r'''// LeetCode 1233 - Remove Sub-Folders from the Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

import "sort"
import "strings"

func removeSubfolders(folder []string) []string {
	sort.Strings(folder)
	ans := []string{}
	for _, path := range folder {
		if len(ans) == 0 || !strings.HasPrefix(path, ans[len(ans)-1]+"/") {
			ans = append(ans, path)
		}
	}
	return ans
}
'''

SOLUTIONS["1234_replace_the_substring_for_balanced_string"] = r'''// LeetCode 1234 - Replace the Substring for Balanced String
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

func balancedString(s string) int {
	count := map[byte]int{}
	for i := 0; i < len(s); i++ {
		count[s[i]]++
	}
	limit := len(s) / 4
	n := len(s)
	left, answer := 0, n
	ok := func() bool {
		for _, c := range []byte{'Q', 'W', 'E', 'R'} {
			if count[c] > limit {
				return false
			}
		}
		return true
	}
	for right := 0; right < n; right++ {
		count[s[right]]--
		for left < n && ok() {
			if right-left+1 < answer {
				answer = right - left + 1
			}
			count[s[left]]++
			left++
		}
	}
	return answer
}
'''

SOLUTIONS["1235_maximum_profit_in_job_scheduling"] = r'''// LeetCode 1235 - Maximum Profit in Job Scheduling
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/

import "sort"

func jobScheduling(startTime []int, endTime []int, profit []int) int {
	n := len(startTime)
	jobs := make([][3]int, n)
	for i := 0; i < n; i++ {
		jobs[i] = [3]int{endTime[i], startTime[i], profit[i]}
	}
	sort.Slice(jobs, func(i, j int) bool { return jobs[i][0] < jobs[j][0] })
	ends := []int{0}
	dp := []int{0}
	for _, job := range jobs {
		end, start, gain := job[0], job[1], job[2]
		i := sort.Search(len(ends), func(i int) bool { return ends[i] > start }) - 1
		best := dp[len(dp)-1]
		if dp[i]+gain > best {
			best = dp[i] + gain
		}
		ends = append(ends, end)
		dp = append(dp, best)
	}
	return dp[len(dp)-1]
}
'''

SOLUTIONS["1236_web_crawler"] = r'''// LeetCode 1236 - Web Crawler
// https://leetcode.com/problems/web-crawler/

import "sort"
import "strings"

type HtmlParser interface {
	GetUrls(url string) []string
}

func crawl(startUrl string, htmlParser HtmlParser) []string {
	hostOf := func(url string) string {
		u := strings.TrimPrefix(url, "http://")
		if i := strings.IndexByte(u, '/'); i >= 0 {
			return u[:i]
		}
		return u
	}
	host := hostOf(startUrl)
	seen := map[string]bool{startUrl: true}
	stack := []string{startUrl}
	for len(stack) > 0 {
		cur := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for _, url := range htmlParser.GetUrls(cur) {
			if hostOf(url) == host && !seen[url] {
				seen[url] = true
				stack = append(stack, url)
			}
		}
	}
	ans := make([]string, 0, len(seen))
	for u := range seen {
		ans = append(ans, u)
	}
	sort.Strings(ans)
	return ans
}
'''

SOLUTIONS["1237_find_positive_integer_solution_for_a_given_equation"] = r'''// LeetCode 1237 - Find Positive Integer Solution for a Given Equation
// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

type CustomFunction interface {
	f(x int, y int) int
}

func findSolution(customfunction CustomFunction, z int) [][]int {
	ans := [][]int{}
	x, y := 1, 1000
	for x <= 1000 && y >= 1 {
		value := customfunction.f(x, y)
		if value == z {
			ans = append(ans, []int{x, y})
			x++
			y--
		} else if value < z {
			x++
		} else {
			y--
		}
	}
	return ans
}
'''

SOLUTIONS["1238_circular_permutation_in_binary_representation"] = r'''// LeetCode 1238 - Circular Permutation in Binary Representation
// https://leetcode.com/problems/circular-permutation-in-binary-representation/

func circularPermutation(n int, start int) []int {
	ans := make([]int, 1<<n)
	for i := 0; i < 1<<n; i++ {
		ans[i] = start ^ i ^ (i >> 1)
	}
	return ans
}
'''

SOLUTIONS["1239_maximum_length_of_a_concatenated_string_with_unique_characters"] = r'''// LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

func maxLength(arr []string) int {
	type pair struct{ used, length int }
	masks := []pair{{0, 0}}
	for _, word := range arr {
		mask := 0
		ok := true
		for i := 0; i < len(word); i++ {
			bit := 1 << (word[i] - 'a')
			if mask&bit != 0 {
				ok = false
				break
			}
			mask |= bit
		}
		if !ok || bits(mask) != len(word) {
			continue
		}
		cur := masks
		for _, p := range cur {
			if p.used&mask == 0 {
				masks = append(masks, pair{p.used | mask, p.length + len(word)})
			}
		}
	}
	best := 0
	for _, p := range masks {
		if p.length > best {
			best = p.length
		}
	}
	return best
}

func bits(x int) int {
	c := 0
	for x > 0 {
		c += x & 1
		x >>= 1
	}
	return c
}
'''

SOLUTIONS["1240_tiling_a_rectangle_with_the_fewest_squares"] = r'''// LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

func tilingRectangle(n int, m int) int {
	if n > m {
		n, m = m, n
	}
	heights := make([]int, m)
	best := n * m
	var search func(int)
	search = func(used int) {
		if used >= best {
			return
		}
		low := heights[0]
		for _, h := range heights[1:] {
			if h < low {
				low = h
			}
		}
		if low == n {
			best = used
			return
		}
		left := 0
		for left < m && heights[left] != low {
			left++
		}
		right := left
		for right < m && heights[right] == low {
			right++
		}
		maxSize := n - low
		if right-left < maxSize {
			maxSize = right - left
		}
		for size := maxSize; size >= 1; size-- {
			for i := left; i < left+size; i++ {
				heights[i] = low + size
			}
			search(used + 1)
			for i := left; i < left+size; i++ {
				heights[i] = low
			}
		}
	}
	search(0)
	return best
}
'''

SOLUTIONS["1242_web_crawler_multithreaded"] = r'''// LeetCode 1242 - Web Crawler Multithreaded
// https://leetcode.com/problems/web-crawler-multithreaded/

import "sort"
import "strings"

type HtmlParser interface {
	GetUrls(url string) []string
}

func crawl(startUrl string, htmlParser HtmlParser) []string {
	hostOf := func(url string) string {
		u := strings.TrimPrefix(url, "http://")
		if i := strings.IndexByte(u, '/'); i >= 0 {
			return u[:i]
		}
		return u
	}
	host := hostOf(startUrl)
	seen := map[string]bool{startUrl: true}
	frontier := []string{startUrl}
	for len(frontier) > 0 {
		next := []string{}
		for _, cur := range frontier {
			for _, url := range htmlParser.GetUrls(cur) {
				if hostOf(url) == host && !seen[url] {
					seen[url] = true
					next = append(next, url)
				}
			}
		}
		frontier = next
	}
	ans := make([]string, 0, len(seen))
	for u := range seen {
		ans = append(ans, u)
	}
	sort.Strings(ans)
	return ans
}
'''

SOLUTIONS["1243_array_transformation"] = r'''// LeetCode 1243 - Array Transformation
// https://leetcode.com/problems/array-transformation/

func transformArray(arr []int) []int {
	for {
		nxt := append([]int{}, arr...)
		changed := false
		for i := 1; i < len(arr)-1; i++ {
			if arr[i] < arr[i-1] && arr[i] < arr[i+1] {
				nxt[i]++
				changed = true
			} else if arr[i] > arr[i-1] && arr[i] > arr[i+1] {
				nxt[i]--
				changed = true
			}
		}
		if !changed {
			return arr
		}
		arr = nxt
	}
}
'''

SOLUTIONS["1244_design_a_leaderboard"] = r'''// LeetCode 1244 - Design A Leaderboard
// https://leetcode.com/problems/design-a-leaderboard/

import "sort"

type Leaderboard struct {
	scores map[int]int
}

func Constructor() Leaderboard {
	return Leaderboard{scores: map[int]int{}}
}

func (this *Leaderboard) AddScore(playerId int, score int) {
	this.scores[playerId] += score
}

func (this *Leaderboard) Top(K int) int {
	vals := make([]int, 0, len(this.scores))
	for _, v := range this.scores {
		vals = append(vals, v)
	}
	sort.Sort(sort.Reverse(sort.IntSlice(vals)))
	sum := 0
	for i := 0; i < K && i < len(vals); i++ {
		sum += vals[i]
	}
	return sum
}

func (this *Leaderboard) Reset(playerId int) {
	delete(this.scores, playerId)
}
'''

SOLUTIONS["1245_tree_diameter"] = r'''// LeetCode 1245 - Tree Diameter
// https://leetcode.com/problems/tree-diameter/

func treeDiameter(edges [][]int) int {
	if len(edges) == 0 {
		return 0
	}
	graph := map[int][]int{}
	for _, e := range edges {
		graph[e[0]] = append(graph[e[0]], e[1])
		graph[e[1]] = append(graph[e[1]], e[0])
	}
	farthest := func(start int) (int, int) {
		type item struct{ node, dist int }
		q := []item{{start, 0}}
		seen := map[int]bool{start: true}
		last := item{start, 0}
		for len(q) > 0 {
			last = q[0]
			q = q[1:]
			for _, v := range graph[last.node] {
				if !seen[v] {
					seen[v] = true
					q = append(q, item{v, last.dist + 1})
				}
			}
		}
		return last.node, last.dist
	}
	endpoint, _ := farthest(edges[0][0])
	_, dist := farthest(endpoint)
	return dist
}
'''

SOLUTIONS["1246_palindrome_removal"] = r'''// LeetCode 1246 - Palindrome Removal
// https://leetcode.com/problems/palindrome-removal/

func minimumMoves(arr []int) int {
	n := len(arr)
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
		dp[i][i] = 1
	}
	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			dp[i][j] = 1 + dp[i+1][j]
			if arr[i] == arr[i+1] {
				v := 1
				if i+2 <= j {
					v += dp[i+2][j]
				}
				if v < dp[i][j] {
					dp[i][j] = v
				}
			}
			for k := i + 2; k <= j; k++ {
				if arr[i] == arr[k] {
					v := dp[i+1][k-1]
					if k < j {
						v += dp[k+1][j]
					}
					if v < dp[i][j] {
						dp[i][j] = v
					}
				}
			}
		}
	}
	return dp[0][n-1]
}
'''

SOLUTIONS["1247_minimum_swaps_to_make_strings_equal"] = r'''// LeetCode 1247 - Minimum Swaps to Make Strings Equal
// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

func minimumSwap(s1 string, s2 string) int {
	xy, yx := 0, 0
	for i := 0; i < len(s1); i++ {
		if s1[i] == 'x' && s2[i] == 'y' {
			xy++
		} else if s1[i] == 'y' && s2[i] == 'x' {
			yx++
		}
	}
	if (xy+yx)%2 != 0 {
		return -1
	}
	return xy/2 + yx/2 + 2*(xy%2)
}
'''

SOLUTIONS["1248_count_number_of_nice_subarrays"] = r'''// LeetCode 1248 - Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

func numberOfSubarrays(nums []int, k int) int {
	frequency := map[int]int{0: 1}
	odd, answer := 0, 0
	for _, x := range nums {
		odd += x & 1
		answer += frequency[odd-k]
		frequency[odd]++
	}
	return answer
}
'''

SOLUTIONS["1249_minimum_remove_to_make_valid_parentheses"] = r'''// LeetCode 1249 - Minimum Remove to Make Valid Parentheses
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

func minRemoveToMakeValid(s string) string {
	chars := []byte(s)
	opens := []int{}
	for i, ch := range chars {
		if ch == '(' {
			opens = append(opens, i)
		} else if ch == ')' {
			if len(opens) > 0 {
				opens = opens[:len(opens)-1]
			} else {
				chars[i] = 0
			}
		}
	}
	for _, i := range opens {
		chars[i] = 0
	}
	out := make([]byte, 0, len(chars))
	for _, ch := range chars {
		if ch != 0 {
			out = append(out, ch)
		}
	}
	return string(out)
}
'''


def main() -> None:
    written = []
    for name, content in sorted(SOLUTIONS.items()):
        folder = ROOT / name
        if not folder.is_dir():
            print("SKIP missing", name)
            continue
        (folder / "solution.go").write_text(content, encoding="utf-8", newline="\n")
        written.append(name)
        print("WROTE", name)
    print("\nTotal written:", len(written))


if __name__ == "__main__":
    main()
