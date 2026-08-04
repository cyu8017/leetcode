#!/usr/bin/env python3
"""Write Go solutions for folders 1114-1156 (non-SQL stubs)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(r"c:\Users\Charlie Yu\Documents\leetcode")

SOLUTIONS: dict[str, str] = {}

SOLUTIONS["1114_print_in_order"] = r'''// LeetCode 1114 - Print in Order
// https://leetcode.com/problems/print-in-order/

type Foo struct {
	second chan struct{}
	third  chan struct{}
}

func Constructor() *Foo {
	return &Foo{
		second: make(chan struct{}),
		third:  make(chan struct{}),
	}
}

func (f *Foo) First(printFirst func()) {
	printFirst()
	close(f.second)
}

func (f *Foo) Second(printSecond func()) {
	<-f.second
	printSecond()
	close(f.third)
}

func (f *Foo) Third(printThird func()) {
	<-f.third
	printThird()
}
'''

SOLUTIONS["1115_print_foobar_alternately"] = r'''// LeetCode 1115 - Print FooBar Alternately
// https://leetcode.com/problems/print-foobar-alternately/

type FooBar struct {
	n    int
	fooS chan struct{}
	barS chan struct{}
}

func NewFooBar(n int) *FooBar {
	fb := &FooBar{
		n:    n,
		fooS: make(chan struct{}, 1),
		barS: make(chan struct{}, 1),
	}
	fb.fooS <- struct{}{}
	return fb
}

func (fb *FooBar) Foo(printFoo func()) {
	for i := 0; i < fb.n; i++ {
		<-fb.fooS
		printFoo()
		fb.barS <- struct{}{}
	}
}

func (fb *FooBar) Bar(printBar func()) {
	for i := 0; i < fb.n; i++ {
		<-fb.barS
		printBar()
		fb.fooS <- struct{}{}
	}
}
'''

SOLUTIONS["1116_print_zero_even_odd"] = r'''// LeetCode 1116 - Print Zero Even Odd
// https://leetcode.com/problems/print-zero-even-odd/

type ZeroEvenOdd struct {
	n    int
	zero chan struct{}
	even chan struct{}
	odd  chan struct{}
}

func NewZeroEvenOdd(n int) *ZeroEvenOdd {
	z := &ZeroEvenOdd{
		n:    n,
		zero: make(chan struct{}, 1),
		even: make(chan struct{}, 1),
		odd:  make(chan struct{}, 1),
	}
	z.zero <- struct{}{}
	return z
}

func (z *ZeroEvenOdd) Zero(printNumber func(int)) {
	for i := 0; i < z.n; i++ {
		<-z.zero
		printNumber(0)
		if i%2 == 0 {
			z.odd <- struct{}{}
		} else {
			z.even <- struct{}{}
		}
	}
}

func (z *ZeroEvenOdd) Even(printNumber func(int)) {
	for num := 2; num <= z.n; num += 2 {
		<-z.even
		printNumber(num)
		z.zero <- struct{}{}
	}
}

func (z *ZeroEvenOdd) Odd(printNumber func(int)) {
	for num := 1; num <= z.n; num += 2 {
		<-z.odd
		printNumber(num)
		z.zero <- struct{}{}
	}
}
'''

SOLUTIONS["1117_building_h2o"] = r'''// LeetCode 1117 - Building H2O
// https://leetcode.com/problems/building-h2o/

import "sync"

type H2O struct {
	hydrogen chan struct{}
	oxygen   chan struct{}
	mu       sync.Mutex
	count    int
}

func NewH2O() *H2O {
	h := &H2O{
		hydrogen: make(chan struct{}, 2),
		oxygen:   make(chan struct{}, 1),
	}
	h.hydrogen <- struct{}{}
	h.hydrogen <- struct{}{}
	return h
}

func (h *H2O) Hydrogen(releaseHydrogen func()) {
	<-h.hydrogen
	h.mu.Lock()
	h.count++
	if h.count == 2 {
		h.oxygen <- struct{}{}
	}
	h.mu.Unlock()
	releaseHydrogen()
}

func (h *H2O) Oxygen(releaseOxygen func()) {
	<-h.oxygen
	releaseOxygen()
	h.mu.Lock()
	h.count = 0
	h.mu.Unlock()
	h.hydrogen <- struct{}{}
	h.hydrogen <- struct{}{}
}
'''

SOLUTIONS["1118_number_of_days_in_a_month"] = r'''// LeetCode 1118 - Number of Days in a Month
// https://leetcode.com/problems/number-of-days-in-a-month/

func numberOfDays(year int, month int) int {
	days := []int{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	if month == 2 && isLeap(year) {
		return 29
	}
	return days[month]
}

func isLeap(year int) bool {
	return year%400 == 0 || (year%4 == 0 && year%100 != 0)
}
'''

SOLUTIONS["1119_remove_vowels_from_a_string"] = r'''// LeetCode 1119 - Remove Vowels from a String
// https://leetcode.com/problems/remove-vowels-from-a-string/

func removeVowels(s string) string {
	out := make([]byte, 0, len(s))
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if ch != 'a' && ch != 'e' && ch != 'i' && ch != 'o' && ch != 'u' {
			out = append(out, ch)
		}
	}
	return string(out)
}
'''

SOLUTIONS["1120_maximum_average_subtree"] = r'''// LeetCode 1120 - Maximum Average Subtree
// https://leetcode.com/problems/maximum-average-subtree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maximumAverageSubtree(root *TreeNode) float64 {
	best := 0.0
	var dfs func(*TreeNode) (int, int)
	dfs = func(node *TreeNode) (int, int) {
		if node == nil {
			return 0, 0
		}
		ls, lc := dfs(node.Left)
		rs, rc := dfs(node.Right)
		totalSum := ls + rs + node.Val
		totalCount := lc + rc + 1
		avg := float64(totalSum) / float64(totalCount)
		if avg > best {
			best = avg
		}
		return totalSum, totalCount
	}
	dfs(root)
	return best
}
'''

SOLUTIONS["1121_divide_array_into_increasing_sequences"] = r'''// LeetCode 1121 - Divide Array Into Increasing Sequences
// https://leetcode.com/problems/divide-array-into-increasing-sequences/

func canDivideIntoSubsequences(nums []int, k int) bool {
	freq := map[int]int{}
	maxFreq := 0
	for _, x := range nums {
		freq[x]++
		if freq[x] > maxFreq {
			maxFreq = freq[x]
		}
	}
	return len(nums) >= k*maxFreq
}
'''

SOLUTIONS["1122_relative_sort_array"] = r'''// LeetCode 1122 - Relative Sort Array
// https://leetcode.com/problems/relative-sort-array/

import "sort"

func relativeSortArray(arr1 []int, arr2 []int) []int {
	count := map[int]int{}
	for _, x := range arr1 {
		count[x]++
	}
	ans := make([]int, 0, len(arr1))
	for _, x := range arr2 {
		for count[x] > 0 {
			ans = append(ans, x)
			count[x]--
		}
		delete(count, x)
	}
	rest := make([]int, 0, len(count))
	for x := range count {
		rest = append(rest, x)
	}
	sort.Ints(rest)
	for _, x := range rest {
		for count[x] > 0 {
			ans = append(ans, x)
			count[x]--
		}
	}
	return ans
}
'''

SOLUTIONS["1123_lowest_common_ancestor_of_deepest_leaves"] = r'''// LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves
// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lcaDeepestLeaves(root *TreeNode) *TreeNode {
	var dfs func(*TreeNode) (*TreeNode, int)
	dfs = func(node *TreeNode) (*TreeNode, int) {
		if node == nil {
			return nil, 0
		}
		ln, ld := dfs(node.Left)
		rn, rd := dfs(node.Right)
		if ld > rd {
			return ln, ld + 1
		}
		if rd > ld {
			return rn, rd + 1
		}
		return node, ld + 1
	}
	node, _ := dfs(root)
	return node
}
'''

SOLUTIONS["1124_longest_well_performing_interval"] = r'''// LeetCode 1124 - Longest Well-Performing Interval
// https://leetcode.com/problems/longest-well-performing-interval/

func longestWPI(hours []int) int {
	score := 0
	firstSeen := map[int]int{0: -1}
	ans := 0
	for i, h := range hours {
		if h > 8 {
			score++
		} else {
			score--
		}
		if score > 0 {
			ans = i + 1
		} else if j, ok := firstSeen[score-1]; ok {
			if i-j > ans {
				ans = i - j
			}
		}
		if _, ok := firstSeen[score]; !ok {
			firstSeen[score] = i
		}
	}
	return ans
}
'''

SOLUTIONS["1125_smallest_sufficient_team"] = r'''// LeetCode 1125 - Smallest Sufficient Team
// https://leetcode.com/problems/smallest-sufficient-team/

func smallestSufficientTeam(req_skills []string, people [][]string) []int {
	skillID := map[string]int{}
	for i, s := range req_skills {
		skillID[s] = i
	}
	personMasks := make([]int, len(people))
	for i, skills := range people {
		mask := 0
		for _, skill := range skills {
			mask |= 1 << skillID[skill]
		}
		personMasks[i] = mask
	}
	target := (1 << len(req_skills)) - 1
	const inf = int(^uint(0) >> 1)
	dp := make([]int, 1<<len(req_skills))
	choice := make([]int, 1<<len(req_skills))
	prev := make([]int, 1<<len(req_skills))
	for i := range dp {
		dp[i] = inf
	}
	dp[0] = 0
	for state := 0; state <= target; state++ {
		if dp[state] == inf {
			continue
		}
		for i, mask := range personMasks {
			ns := state | mask
			if dp[state]+1 < dp[ns] {
				dp[ns] = dp[state] + 1
				choice[ns] = i
				prev[ns] = state
			}
		}
	}
	ans := []int{}
	for state := target; state != 0; state = prev[state] {
		ans = append(ans, choice[state])
	}
	return ans
}
'''

SOLUTIONS["1128_number_of_equivalent_domino_pairs"] = r'''// LeetCode 1128 - Number of Equivalent Domino Pairs
// https://leetcode.com/problems/number-of-equivalent-domino-pairs/

func numEquivDominoPairs(dominoes [][]int) int {
	count := map[int]int{}
	ans := 0
	for _, d := range dominoes {
		a, b := d[0], d[1]
		if a > b {
			a, b = b, a
		}
		key := a*10 + b
		ans += count[key]
		count[key]++
	}
	return ans
}
'''

SOLUTIONS["1129_shortest_path_with_alternating_colors"] = r'''// LeetCode 1129 - Shortest Path with Alternating Colors
// https://leetcode.com/problems/shortest-path-with-alternating-colors/

func shortestAlternatingPaths(n int, redEdges [][]int, blueEdges [][]int) []int {
	graph := [2][][]int{make([][]int, n), make([][]int, n)}
	for _, e := range redEdges {
		graph[0][e[0]] = append(graph[0][e[0]], e[1])
	}
	for _, e := range blueEdges {
		graph[1][e[0]] = append(graph[1][e[0]], e[1])
	}
	ans := make([]int, n)
	for i := range ans {
		ans[i] = -1
	}
	type state struct{ node, color, dist int }
	queue := []state{{0, 0, 0}, {0, 1, 0}}
	seen := [2][]bool{make([]bool, n), make([]bool, n)}
	seen[0][0], seen[1][0] = true, true
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if ans[cur.node] == -1 {
			ans[cur.node] = cur.dist
		}
		nextColor := 1 - cur.color
		for _, nxt := range graph[cur.color][cur.node] {
			if !seen[nextColor][nxt] {
				seen[nextColor][nxt] = true
				queue = append(queue, state{nxt, nextColor, cur.dist + 1})
			}
		}
	}
	return ans
}
'''

SOLUTIONS["1130_minimum_cost_tree_from_leaf_values"] = r'''// LeetCode 1130 - Minimum Cost Tree From Leaf Values
// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

func mctFromLeafValues(arr []int) int {
	stack := []int{int(^uint(0) >> 1)}
	ans := 0
	for _, x := range arr {
		for stack[len(stack)-1] <= x {
			mid := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			left := stack[len(stack)-1]
			if left < x {
				ans += mid * left
			} else {
				ans += mid * x
			}
		}
		stack = append(stack, x)
	}
	for len(stack) > 2 {
		mid := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		ans += mid * stack[len(stack)-1]
	}
	return ans
}
'''

SOLUTIONS["1131_maximum_of_absolute_value_expression"] = r'''// LeetCode 1131 - Maximum of Absolute Value Expression
// https://leetcode.com/problems/maximum-of-absolute-value-expression/

func maxAbsValExpr(arr1 []int, arr2 []int) int {
	n := len(arr1)
	ans := 0
	signs := [][2]int{{1, 1}, {1, -1}, {-1, 1}, {-1, -1}}
	for _, s := range signs {
		maxV, minV := arr1[0]*s[0]+arr2[0]*s[1]+0, arr1[0]*s[0]+arr2[0]*s[1]+0
		for i := 1; i < n; i++ {
			v := arr1[i]*s[0] + arr2[i]*s[1] + i
			if v > maxV {
				maxV = v
			}
			if v < minV {
				minV = v
			}
		}
		if maxV-minV > ans {
			ans = maxV - minV
		}
	}
	return ans
}
'''

SOLUTIONS["1133_largest_unique_number"] = r'''// LeetCode 1133 - Largest Unique Number
// https://leetcode.com/problems/largest-unique-number/

func largestUniqueNumber(nums []int) int {
	count := map[int]int{}
	for _, x := range nums {
		count[x]++
	}
	ans := -1
	for x, c := range count {
		if c == 1 && x > ans {
			ans = x
		}
	}
	return ans
}
'''

SOLUTIONS["1134_armstrong_number"] = r'''// LeetCode 1134 - Armstrong Number
// https://leetcode.com/problems/armstrong-number/

func isArmstrong(n int) bool {
	digits := 0
	for x := n; x > 0; x /= 10 {
		digits++
	}
	sum := 0
	for x := n; x > 0; x /= 10 {
		d := x % 10
		p := 1
		for i := 0; i < digits; i++ {
			p *= d
		}
		sum += p
	}
	return sum == n
}
'''

SOLUTIONS["1135_connecting_cities_with_minimum_cost"] = r'''// LeetCode 1135 - Connecting Cities With Minimum Cost
// https://leetcode.com/problems/connecting-cities-with-minimum-cost/

import "sort"

func minimumCost(n int, connections [][]int) int {
	parent := make([]int, n+1)
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
	sort.Slice(connections, func(i, j int) bool {
		return connections[i][2] < connections[j][2]
	})
	ans, used := 0, 0
	for _, e := range connections {
		a, b := find(e[0]), find(e[1])
		if a == b {
			continue
		}
		parent[b] = a
		ans += e[2]
		used++
		if used == n-1 {
			return ans
		}
	}
	return -1
}
'''

SOLUTIONS["1136_parallel_courses"] = r'''// LeetCode 1136 - Parallel Courses
// https://leetcode.com/problems/parallel-courses/

func minimumSemesters(n int, relations [][]int) int {
	graph := make([][]int, n+1)
	indeg := make([]int, n+1)
	for _, r := range relations {
		graph[r[0]] = append(graph[r[0]], r[1])
		indeg[r[1]]++
	}
	queue := []int{}
	for i := 1; i <= n; i++ {
		if indeg[i] == 0 {
			queue = append(queue, i)
		}
	}
	semesters, taken := 0, 0
	for len(queue) > 0 {
		size := len(queue)
		semesters++
		for i := 0; i < size; i++ {
			u := queue[0]
			queue = queue[1:]
			taken++
			for _, v := range graph[u] {
				indeg[v]--
				if indeg[v] == 0 {
					queue = append(queue, v)
				}
			}
		}
	}
	if taken == n {
		return semesters
	}
	return -1
}
'''

SOLUTIONS["1137_n_th_tribonacci_number"] = r'''// LeetCode 1137 - N-th Tribonacci Number
// https://leetcode.com/problems/n-th-tribonacci-number/

func tribonacci(n int) int {
	if n == 0 {
		return 0
	}
	if n <= 2 {
		return 1
	}
	a, b, c := 0, 1, 1
	for i := 3; i <= n; i++ {
		a, b, c = b, c, a+b+c
	}
	return c
}
'''

SOLUTIONS["1138_alphabet_board_path"] = r'''// LeetCode 1138 - Alphabet Board Path
// https://leetcode.com/problems/alphabet-board-path/

func alphabetBoardPath(target string) string {
	r, c := 0, 0
	out := []byte{}
	for i := 0; i < len(target); i++ {
		tr := int(target[i]-'a') / 5
		tc := int(target[i]-'a') % 5
		for r > tr {
			out = append(out, 'U')
			r--
		}
		for c > tc {
			out = append(out, 'L')
			c--
		}
		for c < tc {
			out = append(out, 'R')
			c++
		}
		for r < tr {
			out = append(out, 'D')
			r++
		}
		out = append(out, '!')
	}
	return string(out)
}
'''

SOLUTIONS["1139_largest_1_bordered_square"] = r'''// LeetCode 1139 - Largest 1-Bordered Square
// https://leetcode.com/problems/largest-1-bordered-square/

func largest1BorderedSquare(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	hor := make([][]int, m)
	ver := make([][]int, m)
	for i := 0; i < m; i++ {
		hor[i] = make([]int, n)
		ver[i] = make([]int, n)
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				if j > 0 {
					hor[i][j] = hor[i][j-1] + 1
				} else {
					hor[i][j] = 1
				}
				if i > 0 {
					ver[i][j] = ver[i-1][j] + 1
				} else {
					ver[i][j] = 1
				}
			}
		}
	}
	for side := min(m, n); side > 0; side-- {
		for i := side - 1; i < m; i++ {
			for j := side - 1; j < n; j++ {
				if hor[i][j] >= side && ver[i][j] >= side &&
					hor[i-side+1][j] >= side && ver[i][j-side+1] >= side {
					return side * side
				}
			}
		}
	}
	return 0
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
'''

SOLUTIONS["1140_stone_game_ii"] = r'''// LeetCode 1140 - Stone Game II
// https://leetcode.com/problems/stone-game-ii/

func stoneGameII(piles []int) int {
	n := len(piles)
	suffix := make([]int, n+1)
	for i := n - 1; i >= 0; i-- {
		suffix[i] = suffix[i+1] + piles[i]
	}
	memo := make([][]int, n)
	for i := range memo {
		memo[i] = make([]int, n+1)
		for j := range memo[i] {
			memo[i][j] = -1
		}
	}
	var dp func(int, int) int
	dp = func(i, m int) int {
		if i >= n {
			return 0
		}
		if memo[i][m] != -1 {
			return memo[i][m]
		}
		best := 0
		for x := 1; x <= 2*m && i+x-1 < n; x++ {
			v := suffix[i] - dp(i+x, max(m, x))
			if v > best {
				best = v
			}
		}
		memo[i][m] = best
		return best
	}
	return dp(0, 1)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
'''


def is_sql(folder: Path) -> bool:
    for rel in ("tests/config.json", "tests/cases.json"):
        p = folder / rel
        if p.exists():
            try:
                if json.loads(p.read_text(encoding="utf-8")).get("kind") == "sql":
                    return True
            except Exception:
                pass
    return False


def is_stub(text: str) -> bool:
    return bool(re.search(r"func\s+solve\s*\(\s*\)\s*\{\s*\}", text))


def main() -> None:
    written = []
    for name, content in sorted(SOLUTIONS.items()):
        folder = ROOT / name
        if not folder.is_dir():
            print(f"SKIP missing folder {name}")
            continue
        if is_sql(folder):
            print(f"SKIP sql {name}")
            continue
        go_path = folder / "solution.go"
        if go_path.exists() and not is_stub(go_path.read_text(encoding="utf-8")):
            # overwrite only if still stub-like, else write anyway for this batch
            pass
        go_path.write_text(content, encoding="utf-8", newline="\n")
        written.append(name)
        print(f"WROTE {name}")
    print(f"\nTotal written: {len(written)}")


if __name__ == "__main__":
    main()
