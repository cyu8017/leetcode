#!/usr/bin/env python3
"""Port Go solutions 1360-1388 (batch B)."""
import os

ROOT = r"c:\Users\Charlie Yu\Documents\leetcode"

SOLUTIONS = {}

SOLUTIONS["1360_number_of_days_between_two_dates"] = r'''// LeetCode 1360 - Number of Days Between Two Dates
// https://leetcode.com/problems/number-of-days-between-two-dates/

import "time"

func daysBetweenDates(date1 string, date2 string) int {
	a, _ := time.Parse("2006-01-02", date1)
	b, _ := time.Parse("2006-01-02", date2)
	d := int(a.Sub(b).Hours() / 24)
	if d < 0 {
		return -d
	}
	return d
}
'''

SOLUTIONS["1361_validate_binary_tree_nodes"] = r'''// LeetCode 1361 - Validate Binary Tree Nodes
// https://leetcode.com/problems/validate-binary-tree-nodes/

func validateBinaryTreeNodes(n int, leftChild []int, rightChild []int) bool {
	indeg := make([]int, n)
	for _, x := range append(append([]int{}, leftChild...), rightChild...) {
		if x != -1 {
			indeg[x]++
			if indeg[x] > 1 {
				return false
			}
		}
	}
	roots := []int{}
	for i, x := range indeg {
		if x == 0 {
			roots = append(roots, i)
		}
	}
	if len(roots) != 1 {
		return false
	}
	seen := map[int]bool{}
	st := roots
	for len(st) > 0 {
		u := st[len(st)-1]
		st = st[:len(st)-1]
		if seen[u] {
			return false
		}
		seen[u] = true
		for _, v := range []int{leftChild[u], rightChild[u]} {
			if v != -1 {
				st = append(st, v)
			}
		}
	}
	return len(seen) == n
}
'''

SOLUTIONS["1362_closest_divisors"] = r'''// LeetCode 1362 - Closest Divisors
// https://leetcode.com/problems/closest-divisors/

func closestDivisors(num int) []int {
	isqrt := func(x int) int {
		r := 0
		for r*r <= x {
			r++
		}
		return r - 1
	}
	var best []int
	for _, x := range []int{num + 1, num + 2} {
		for a := isqrt(x); a >= 1; a-- {
			if x%a == 0 {
				pair := []int{a, x / a}
				if best == nil || pair[1]-pair[0] < best[1]-best[0] {
					best = pair
				}
				break
			}
		}
	}
	return best
}
'''

SOLUTIONS["1363_largest_multiple_of_three"] = r'''// LeetCode 1363 - Largest Multiple of Three
// https://leetcode.com/problems/largest-multiple-of-three/

func largestMultipleOfThree(digits []int) string {
	cnt := [10]int{}
	sum := 0
	for _, d := range digits {
		cnt[d]++
		sum += d
	}
	rem := sum % 3
	remove := func(r, k int) bool {
		for d := r; d < 10; d += 3 {
			for cnt[d] > 0 && k > 0 {
				cnt[d]--
				k--
			}
			if k == 0 {
				return true
			}
		}
		return false
	}
	if rem != 0 && !remove(rem, 1) {
		remove(3-rem, 2)
	}
	var s []byte
	for d := 9; d >= 0; d-- {
		for i := 0; i < cnt[d]; i++ {
			s = append(s, byte('0'+d))
		}
	}
	if len(s) == 0 {
		return ""
	}
	if s[0] == '0' {
		return "0"
	}
	return string(s)
}
'''

SOLUTIONS["1365_how_many_numbers_are_smaller_than_the_current_number"] = r'''// LeetCode 1365 - How Many Numbers Are Smaller Than the Current Number
// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

import "sort"

func smallerNumbersThanCurrent(nums []int) []int {
	sorted := append([]int(nil), nums...)
	sort.Ints(sorted)
	rank := map[int]int{}
	for i, x := range sorted {
		if _, ok := rank[x]; !ok {
			rank[x] = i
		}
	}
	answer := make([]int, len(nums))
	for i, x := range nums {
		answer[i] = rank[x]
	}
	return answer
}
'''

SOLUTIONS["1366_rank_teams_by_votes"] = r'''// LeetCode 1366 - Rank Teams by Votes
// https://leetcode.com/problems/rank-teams-by-votes/

import "sort"

func rankTeams(votes []string) string {
	m := len(votes[0])
	count := map[byte][]int{}
	for i := 0; i < m; i++ {
		c := votes[0][i]
		count[c] = make([]int, m)
	}
	for _, v := range votes {
		for i := 0; i < len(v); i++ {
			count[v[i]][i]++
		}
	}
	teams := make([]byte, 0, m)
	for c := range count {
		teams = append(teams, c)
	}
	sort.Slice(teams, func(i, j int) bool {
		a, b := count[teams[i]], count[teams[j]]
		for k := 0; k < m; k++ {
			if a[k] != b[k] {
				return a[k] > b[k]
			}
		}
		return teams[i] < teams[j]
	})
	return string(teams)
}
'''

SOLUTIONS["1367_linked_list_in_binary_tree"] = r'''// LeetCode 1367 - Linked List in Binary Tree
// https://leetcode.com/problems/linked-list-in-binary-tree/

type ListNode struct {
	Val  int
	Next *ListNode
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSubPath(head *ListNode, root *TreeNode) bool {
	var match func(*ListNode, *TreeNode) bool
	match = func(a *ListNode, b *TreeNode) bool {
		if a == nil {
			return true
		}
		if b == nil || a.Val != b.Val {
			return false
		}
		return match(a.Next, b.Left) || match(a.Next, b.Right)
	}
	if root == nil {
		return false
	}
	return match(head, root) || isSubPath(head, root.Left) || isSubPath(head, root.Right)
}
'''

SOLUTIONS["1368_minimum_cost_to_make_at_least_one_valid_path_in_a_grid"] = r'''// LeetCode 1368 - Minimum Cost to Make at Least One Valid Path in a Grid
// https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

func minCost(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	const inf = int(1e9)
	dist := make([][]int, m)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			dist[i][j] = inf
		}
	}
	dist[0][0] = 0
	type pair struct{ r, c int }
	dq := []pair{{0, 0}}
	dirs := [][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	for len(dq) > 0 {
		cur := dq[0]
		dq = dq[1:]
		r, c := cur.r, cur.c
		for k, d := range dirs {
			x, y := r+d[0], c+d[1]
			if x >= 0 && x < m && y >= 0 && y < n {
				w := 0
				if k+1 != grid[r][c] {
					w = 1
				}
				nd := dist[r][c] + w
				if nd < dist[x][y] {
					dist[x][y] = nd
					if w == 0 {
						dq = append([]pair{{x, y}}, dq...)
					} else {
						dq = append(dq, pair{x, y})
					}
				}
			}
		}
	}
	return dist[m-1][n-1]
}
'''

SOLUTIONS["1370_increasing_decreasing_string"] = r'''// LeetCode 1370 - Increasing Decreasing String
// https://leetcode.com/problems/increasing-decreasing-string/

func sortString(s string) string {
	c := [26]int{}
	for i := 0; i < len(s); i++ {
		c[s[i]-'a']++
	}
	out := make([]byte, 0, len(s))
	for len(out) < len(s) {
		for i := 0; i < 26; i++ {
			if c[i] > 0 {
				out = append(out, byte('a'+i))
				c[i]--
			}
		}
		for i := 25; i >= 0; i-- {
			if c[i] > 0 {
				out = append(out, byte('a'+i))
				c[i]--
			}
		}
	}
	return string(out)
}
'''

SOLUTIONS["1371_find_the_longest_substring_containing_vowels_in_even_counts"] = r'''// LeetCode 1371 - Find the Longest Substring Containing Vowels in Even Counts
// https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

func findTheLongestSubstring(s string) int {
	first := map[int]int{0: -1}
	mask, ans := 0, 0
	vowels := "aeiou"
	for i := 0; i < len(s); i++ {
		for j := 0; j < 5; j++ {
			if s[i] == vowels[j] {
				mask ^= 1 << j
			}
		}
		if idx, ok := first[mask]; ok {
			if i-idx > ans {
				ans = i - idx
			}
		} else {
			first[mask] = i
		}
	}
	return ans
}
'''

SOLUTIONS["1372_longest_zigzag_path_in_a_binary_tree"] = r'''// LeetCode 1372 - Longest ZigZag Path in a Binary Tree
// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func longestZigZag(root *TreeNode) int {
	ans := 0
	var dfs func(*TreeNode) (int, int)
	dfs = func(node *TreeNode) (int, int) {
		if node == nil {
			return -1, -1
		}
		_, lr := dfs(node.Left)
		rl, _ := dfs(node.Right)
		a, b := lr+1, rl+1
		if a > ans {
			ans = a
		}
		if b > ans {
			ans = b
		}
		return a, b
	}
	dfs(root)
	return ans
}
'''

SOLUTIONS["1373_maximum_sum_bst_in_binary_tree"] = r'''// LeetCode 1373 - Maximum Sum BST in Binary Tree
// https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxSumBST(root *TreeNode) int {
	ans := 0
	const inf = int(1e9)
	var dfs func(*TreeNode) (bool, int, int, int)
	dfs = func(node *TreeNode) (bool, int, int, int) {
		if node == nil {
			return true, inf, -inf, 0
		}
		a, lx, lh, ls := dfs(node.Left)
		b, rx, rh, rs := dfs(node.Right)
		if a && b && lh < node.Val && node.Val < rx {
			s := ls + rs + node.Val
			if s > ans {
				ans = s
			}
			mn, mx := node.Val, node.Val
			if lx < mn {
				mn = lx
			}
			if rh > mx {
				mx = rh
			}
			return true, mn, mx, s
		}
		return false, 0, 0, 0
	}
	dfs(root)
	return ans
}
'''

SOLUTIONS["1374_generate_a_string_with_characters_that_have_odd_counts"] = r'''// LeetCode 1374 - Generate a String With Characters That Have Odd Counts
// https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

func generateTheString(n int) string {
	if n%2 == 1 {
		return string(make([]byte, n, n)) // filled below
	}
	b := make([]byte, n)
	for i := 0; i < n-1; i++ {
		b[i] = 'a'
	}
	b[n-1] = 'b'
	return string(b)
}
'''

# Fix 1374 - the odd case was wrong
SOLUTIONS["1374_generate_a_string_with_characters_that_have_odd_counts"] = r'''// LeetCode 1374 - Generate a String With Characters That Have Odd Counts
// https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

func generateTheString(n int) string {
	b := make([]byte, n)
	for i := range b {
		b[i] = 'a'
	}
	if n%2 == 0 {
		b[n-1] = 'b'
	}
	return string(b)
}
'''

SOLUTIONS["1375_number_of_times_binary_string_is_prefix_aligned"] = r'''// LeetCode 1375 - Number of Times Binary String Is Prefix-Aligned
// https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

func numTimesAllBlue(flips []int) int {
	ans, mx := 0, 0
	for i, x := range flips {
		if x > mx {
			mx = x
		}
		if mx == i+1 {
			ans++
		}
	}
	return ans
}
'''

SOLUTIONS["1376_time_needed_to_inform_all_employees"] = r'''// LeetCode 1376 - Time Needed to Inform All Employees
// https://leetcode.com/problems/time-needed-to-inform-all-employees/

func numOfMinutes(n int, headID int, manager []int, informTime []int) int {
	children := make([][]int, n)
	for i, p := range manager {
		if p != -1 {
			children[p] = append(children[p], i)
		}
	}
	var dfs func(int) int
	dfs = func(u int) int {
		best := 0
		for _, v := range children[u] {
			if t := dfs(v); t > best {
				best = t
			}
		}
		return informTime[u] + best
	}
	return dfs(headID)
}
'''

SOLUTIONS["1377_frog_position_after_t_seconds"] = r'''// LeetCode 1377 - Frog Position After T Seconds
// https://leetcode.com/problems/frog-position-after-t-seconds/

func frogPosition(n int, edges [][]int, t int, target int) float64 {
	g := make([][]int, n+1)
	for _, e := range edges {
		a, b := e[0], e[1]
		g[a] = append(g[a], b)
		g[b] = append(g[b], a)
	}
	var dfs func(u, p, time int, prob float64) float64
	dfs = func(u, p, time int, prob float64) float64 {
		kids := []int{}
		for _, v := range g[u] {
			if v != p {
				kids = append(kids, v)
			}
		}
		if time == t || len(kids) == 0 {
			if u == target {
				return prob
			}
			return 0
		}
		sum := 0.0
		for _, v := range kids {
			sum += dfs(v, u, time+1, prob/float64(len(kids)))
		}
		return sum
	}
	return dfs(1, 0, 0, 1.0)
}
'''

SOLUTIONS["1379_find_a_corresponding_node_of_a_binary_tree_in_a_clone_of_that_tree"] = r'''// LeetCode 1379 - Find a Corresponding Node of a Binary Tree in a Clone of That Tree
// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getTargetCopy(original *TreeNode, cloned *TreeNode, target *TreeNode) *TreeNode {
	type pair struct{ a, b *TreeNode }
	stack := []pair{{original, cloned}}
	for len(stack) > 0 {
		cur := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if cur.a == target || cur.a.Val == target.Val {
			return cur.b
		}
		if cur.a.Left != nil {
			stack = append(stack, pair{cur.a.Left, cur.b.Left})
		}
		if cur.a.Right != nil {
			stack = append(stack, pair{cur.a.Right, cur.b.Right})
		}
	}
	return nil
}
'''

SOLUTIONS["1380_lucky_numbers_in_a_matrix"] = r'''// LeetCode 1380 - Lucky Numbers in a Matrix
// https://leetcode.com/problems/lucky-numbers-in-a-matrix/

func luckyNumbers(matrix [][]int) []int {
	mins := map[int]bool{}
	for _, row := range matrix {
		mn := row[0]
		for _, v := range row[1:] {
			if v < mn {
				mn = v
			}
		}
		mins[mn] = true
	}
	maxs := map[int]bool{}
	for c := 0; c < len(matrix[0]); c++ {
		mx := matrix[0][c]
		for r := 1; r < len(matrix); r++ {
			if matrix[r][c] > mx {
				mx = matrix[r][c]
			}
		}
		maxs[mx] = true
	}
	var answer []int
	for v := range mins {
		if maxs[v] {
			answer = append(answer, v)
		}
	}
	return answer
}
'''

SOLUTIONS["1381_design_a_stack_with_increment_operation"] = r'''// LeetCode 1381 - Design a Stack With Increment Operation
// https://leetcode.com/problems/design-a-stack-with-increment-operation/

type CustomStack struct {
	maxSize int
	a       []int
}

func Constructor(maxSize int) CustomStack {
	return CustomStack{maxSize: maxSize}
}

func (this *CustomStack) Push(x int) {
	if len(this.a) < this.maxSize {
		this.a = append(this.a, x)
	}
}

func (this *CustomStack) Pop() int {
	if len(this.a) == 0 {
		return -1
	}
	x := this.a[len(this.a)-1]
	this.a = this.a[:len(this.a)-1]
	return x
}

func (this *CustomStack) Increment(k int, val int) {
	n := k
	if n > len(this.a) {
		n = len(this.a)
	}
	for i := 0; i < n; i++ {
		this.a[i] += val
	}
}
'''

SOLUTIONS["1382_balance_a_binary_search_tree"] = r'''// LeetCode 1382 - Balance a Binary Search Tree
// https://leetcode.com/problems/balance-a-binary-search-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func balanceBST(root *TreeNode) *TreeNode {
	var nodes []*TreeNode
	var walk func(*TreeNode)
	walk = func(x *TreeNode) {
		if x == nil {
			return
		}
		walk(x.Left)
		nodes = append(nodes, x)
		walk(x.Right)
	}
	walk(root)
	var build func(l, r int) *TreeNode
	build = func(l, r int) *TreeNode {
		if l >= r {
			return nil
		}
		m := (l + r) / 2
		x := nodes[m]
		x.Left = build(l, m)
		x.Right = build(m+1, r)
		return x
	}
	return build(0, len(nodes))
}
'''

SOLUTIONS["1383_maximum_performance_of_a_team"] = r'''// LeetCode 1383 - Maximum Performance of a Team
// https://leetcode.com/problems/maximum-performance-of-a-team/

import (
	"container/heap"
	"sort"
)

type minHeap []int

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func maxPerformance(n int, speed []int, efficiency []int, k int) int {
	type pair struct{ e, s int }
	people := make([]pair, n)
	for i := 0; i < n; i++ {
		people[i] = pair{efficiency[i], speed[i]}
	}
	sort.Slice(people, func(i, j int) bool { return people[i].e > people[j].e })
	h := &minHeap{}
	heap.Init(h)
	total, ans := 0, 0
	for _, p := range people {
		heap.Push(h, p.s)
		total += p.s
		if h.Len() > k {
			total -= heap.Pop(h).(int)
		}
		perf := total * p.e
		if perf > ans {
			ans = perf
		}
	}
	return ans % 1000000007
}
'''

SOLUTIONS["1385_find_the_distance_value_between_two_arrays"] = r'''// LeetCode 1385 - Find the Distance Value Between Two Arrays
// https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

import "sort"

func findTheDistanceValue(arr1 []int, arr2 []int, d int) int {
	b := append([]int(nil), arr2...)
	sort.Ints(b)
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	ans := 0
	for _, x := range arr1 {
		i := sort.SearchInts(b, x)
		ok := true
		if i < len(b) && abs(b[i]-x) <= d {
			ok = false
		}
		if i > 0 && abs(b[i-1]-x) <= d {
			ok = false
		}
		if ok {
			ans++
		}
	}
	return ans
}
'''

SOLUTIONS["1386_cinema_seat_allocation"] = r'''// LeetCode 1386 - Cinema Seat Allocation
// https://leetcode.com/problems/cinema-seat-allocation/

func maxNumberOfFamilies(n int, reservedSeats [][]int) int {
	rows := map[int]int{}
	for _, seat := range reservedSeats {
		r, c := seat[0], seat[1]
		if c >= 2 && c <= 9 {
			rows[r] |= 1 << (c - 2)
		}
	}
	ans := 2 * (n - len(rows))
	for _, m := range rows {
		left := m&0b00001111 == 0
		right := m&0b11110000 == 0
		middle := m&0b00111100 == 0
		if left && right {
			ans += 2
		} else if left || right || middle {
			ans++
		}
	}
	return ans
}
'''

SOLUTIONS["1387_sort_integers_by_the_power_value"] = r'''// LeetCode 1387 - Sort Integers by The Power Value
// https://leetcode.com/problems/sort-integers-by-the-power-value/

import "sort"

func getKth(lo int, hi int, k int) int {
	memo := map[int]int{}
	var power func(int) int
	power = func(x int) int {
		if x == 1 {
			return 0
		}
		if v, ok := memo[x]; ok {
			return v
		}
		var nxt int
		if x%2 == 0 {
			nxt = x / 2
		} else {
			nxt = 3*x + 1
		}
		memo[x] = 1 + power(nxt)
		return memo[x]
	}
	vals := make([]int, 0, hi-lo+1)
	for x := lo; x <= hi; x++ {
		vals = append(vals, x)
	}
	sort.Slice(vals, func(i, j int) bool {
		pi, pj := power(vals[i]), power(vals[j])
		if pi != pj {
			return pi < pj
		}
		return vals[i] < vals[j]
	})
	return vals[k-1]
}
'''

SOLUTIONS["1388_pizza_with_3n_slices"] = r'''// LeetCode 1388 - Pizza With 3n Slices
// https://leetcode.com/problems/pizza-with-3n-slices/

func maxSizeSlices(slices []int) int {
	k := len(slices) / 3
	line := func(a []int) int {
		dp := make([][]int, len(a)+2)
		for i := range dp {
			dp[i] = make([]int, k+1)
		}
		for i, x := range a {
			ii := i + 2
			for j := 1; j <= k; j++ {
				v := dp[ii-1][j]
				alt := dp[ii-2][j-1] + x
				if alt > v {
					v = alt
				}
				dp[ii][j] = v
			}
		}
		return dp[len(a)+1][k]
	}
	a := line(slices[:len(slices)-1])
	b := line(slices[1:])
	if a > b {
		return a
	}
	return b
}
'''


def main():
    for folder, content in SOLUTIONS.items():
        path = os.path.join(ROOT, folder, "solution.go")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content.lstrip("\n"))
        print("wrote", folder)


if __name__ == "__main__":
    main()
