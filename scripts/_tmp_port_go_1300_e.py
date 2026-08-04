#!/usr/bin/env python3
"""Port Go solutions 1470-1499 (batch E)."""
import os

ROOT = r"c:\Users\Charlie Yu\Documents\leetcode"

SOLUTIONS = {}

SOLUTIONS["1470_shuffle_the_array"] = r'''// LeetCode 1470 - Shuffle the Array
// https://leetcode.com/problems/shuffle-the-array/

func shuffle(nums []int, n int) []int {
	answer := make([]int, 0, 2*n)
	for i := 0; i < n; i++ {
		answer = append(answer, nums[i], nums[i+n])
	}
	return answer
}
'''

SOLUTIONS["1471_the_k_strongest_values_in_an_array"] = r'''// LeetCode 1471 - The k Strongest Values in an Array
// https://leetcode.com/problems/the-k-strongest-values-in-an-array/

import "sort"

func getStrongest(arr []int, k int) []int {
	sort.Ints(arr)
	median := arr[(len(arr)-1)/2]
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	sort.Slice(arr, func(i, j int) bool {
		ai, aj := abs(arr[i]-median), abs(arr[j]-median)
		if ai != aj {
			return ai > aj
		}
		return arr[i] > arr[j]
	})
	return arr[:k]
}
'''

SOLUTIONS["1472_design_browser_history"] = r'''// LeetCode 1472 - Design Browser History
// https://leetcode.com/problems/design-browser-history/

type BrowserHistory struct {
	history []string
	index   int
}

func Constructor(homepage string) BrowserHistory {
	return BrowserHistory{history: []string{homepage}, index: 0}
}

func (this *BrowserHistory) Visit(url string) {
	this.history = this.history[:this.index+1]
	this.history = append(this.history, url)
	this.index++
}

func (this *BrowserHistory) Back(steps int) string {
	this.index -= steps
	if this.index < 0 {
		this.index = 0
	}
	return this.history[this.index]
}

func (this *BrowserHistory) Forward(steps int) string {
	this.index += steps
	if this.index >= len(this.history) {
		this.index = len(this.history) - 1
	}
	return this.history[this.index]
}
'''

SOLUTIONS["1473_paint_house_iii"] = r'''// LeetCode 1473 - Paint House III
// https://leetcode.com/problems/paint-house-iii/

func minCost(houses []int, cost [][]int, m int, n int, target int) int {
	const inf = int(1e15)
	type key struct{ prev, groups int }
	dp := map[key]int{{0, 0}: 0}
	for i, painted := range houses {
		nxt := map[key]int{}
		colors := []int{}
		if painted != 0 {
			colors = []int{painted}
		} else {
			for c := 1; c <= n; c++ {
				colors = append(colors, c)
			}
		}
		for k, value := range dp {
			for _, color := range colors {
				ng := k.groups
				if color != k.prev {
					ng++
				}
				if ng <= target {
					nv := value
					if painted == 0 {
						nv += cost[i][color-1]
					}
					nk := key{color, ng}
					if v, ok := nxt[nk]; !ok || nv < v {
						nxt[nk] = nv
					}
				}
			}
		}
		dp = nxt
	}
	ans := inf
	for k, v := range dp {
		if k.groups == target && v < ans {
			ans = v
		}
	}
	if ans == inf {
		return -1
	}
	return ans
}
'''

SOLUTIONS["1474_delete_n_nodes_after_m_nodes_of_a_linked_list"] = r'''// LeetCode 1474 - Delete N Nodes After M Nodes of a Linked List
// https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteNodes(head *ListNode, m int, n int) *ListNode {
	cur := head
	for cur != nil {
		for i := 0; i < m-1; i++ {
			if cur == nil {
				break
			}
			cur = cur.Next
		}
		if cur == nil {
			break
		}
		drop := cur.Next
		for i := 0; i < n; i++ {
			if drop != nil {
				drop = drop.Next
			}
		}
		cur.Next = drop
		cur = drop
	}
	return head
}
'''

SOLUTIONS["1475_final_prices_with_a_special_discount_in_a_shop"] = r'''// LeetCode 1475 - Final Prices With a Special Discount in a Shop
// https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

func finalPrices(prices []int) []int {
	ans := append([]int(nil), prices...)
	stack := []int{}
	for i, price := range prices {
		for len(stack) > 0 && prices[stack[len(stack)-1]] >= price {
			j := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			ans[j] -= price
		}
		stack = append(stack, i)
	}
	return ans
}
'''

SOLUTIONS["1476_subrectangle_queries"] = r'''// LeetCode 1476 - Subrectangle Queries
// https://leetcode.com/problems/subrectangle-queries/

type SubrectangleQueries struct {
	rectangle [][]int
}

func Constructor(rectangle [][]int) SubrectangleQueries {
	return SubrectangleQueries{rectangle: rectangle}
}

func (this *SubrectangleQueries) UpdateSubrectangle(row1 int, col1 int, row2 int, col2 int, newValue int) {
	for r := row1; r <= row2; r++ {
		for c := col1; c <= col2; c++ {
			this.rectangle[r][c] = newValue
		}
	}
}

func (this *SubrectangleQueries) GetValue(row int, col int) int {
	return this.rectangle[row][col]
}
'''

SOLUTIONS["1477_find_two_non_overlapping_sub_arrays_each_with_target_sum"] = r'''// LeetCode 1477 - Find Two Non-overlapping Sub-arrays Each With Target Sum
// https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

func minSumOfLengths(arr []int, target int) int {
	const inf = int(1e9)
	left, total, best, ans := 0, 0, inf, inf
	shortest := make([]int, len(arr))
	for i := range shortest {
		shortest[i] = inf
	}
	for right, x := range arr {
		total += x
		for total > target {
			total -= arr[left]
			left++
		}
		if total == target {
			length := right - left + 1
			if left > 0 && length+shortest[left-1] < ans {
				ans = length + shortest[left-1]
			}
			if length < best {
				best = length
			}
		}
		shortest[right] = best
	}
	if ans == inf {
		return -1
	}
	return ans
}
'''

SOLUTIONS["1478_allocate_mailboxes"] = r'''// LeetCode 1478 - Allocate Mailboxes
// https://leetcode.com/problems/allocate-mailboxes/

import "sort"

func minDistance(houses []int, k int) int {
	sort.Ints(houses)
	n := len(houses)
	cost := make([][]int, n)
	for i := range cost {
		cost[i] = make([]int, n)
		for j := i; j < n; j++ {
			mid := houses[(i+j)/2]
			s := 0
			for t := i; t <= j; t++ {
				d := houses[t] - mid
				if d < 0 {
					d = -d
				}
				s += d
			}
			cost[i][j] = s
		}
	}
	const inf = int(1e15)
	dp := make([]int, n+1)
	dp[0] = 0
	for i := 1; i <= n; i++ {
		dp[i] = inf
	}
	for mb := 0; mb < k; mb++ {
		ndp := make([]int, n+1)
		ndp[0] = 0
		for i := 1; i <= n; i++ {
			ndp[i] = inf
		}
		for j := 1; j <= n; j++ {
			for i := 0; i < j; i++ {
				v := dp[i] + cost[i][j-1]
				if v < ndp[j] {
					ndp[j] = v
				}
			}
		}
		dp = ndp
	}
	return dp[n]
}
'''

SOLUTIONS["1480_running_sum_of_1d_array"] = r'''// LeetCode 1480 - Running Sum of 1d Array
// https://leetcode.com/problems/running-sum-of-1d-array/

func runningSum(nums []int) []int {
	for i := 1; i < len(nums); i++ {
		nums[i] += nums[i-1]
	}
	return nums
}
'''

SOLUTIONS["1481_least_number_of_unique_integers_after_k_removals"] = r'''// LeetCode 1481 - Least Number of Unique Integers after K Removals
// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

import "sort"

func findLeastNumOfUniqueInts(arr []int, k int) int {
	countsMap := map[int]int{}
	for _, v := range arr {
		countsMap[v]++
	}
	counts := make([]int, 0, len(countsMap))
	for _, c := range countsMap {
		counts = append(counts, c)
	}
	sort.Ints(counts)
	removed := 0
	for _, count := range counts {
		if k < count {
			break
		}
		k -= count
		removed++
	}
	return len(counts) - removed
}
'''

SOLUTIONS["1482_minimum_number_of_days_to_make_m_bouquets"] = r'''// LeetCode 1482 - Minimum Number of Days to Make m Bouquets
// https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

func minDays(bloomDay []int, m int, k int) int {
	if m*k > len(bloomDay) {
		return -1
	}
	possible := func(day int) bool {
		bouquets, run := 0, 0
		for _, x := range bloomDay {
			if x <= day {
				run++
			} else {
				run = 0
			}
			if run == k {
				bouquets++
				run = 0
			}
		}
		return bouquets >= m
	}
	lo, hi := bloomDay[0], bloomDay[0]
	for _, d := range bloomDay {
		if d < lo {
			lo = d
		}
		if d > hi {
			hi = d
		}
	}
	for lo < hi {
		mid := (lo + hi) / 2
		if possible(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
'''

SOLUTIONS["1483_kth_ancestor_of_a_tree_node"] = r'''// LeetCode 1483 - Kth Ancestor of a Tree Node
// https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

type TreeAncestor struct {
	up [][]int
}

func Constructor(n int, parent []int) TreeAncestor {
	width := 1
	for (1 << width) < n {
		width++
	}
	up := make([][]int, width)
	up[0] = append([]int(nil), parent...)
	for b := 1; b < width; b++ {
		up[b] = make([]int, n)
		for i := 0; i < n; i++ {
			p := up[b-1][i]
			if p == -1 {
				up[b][i] = -1
			} else {
				up[b][i] = up[b-1][p]
			}
		}
	}
	return TreeAncestor{up: up}
}

func (this *TreeAncestor) GetKthAncestor(node int, k int) int {
	bit := 0
	for k > 0 && node != -1 {
		if k&1 == 1 {
			if bit >= len(this.up) {
				return -1
			}
			node = this.up[bit][node]
		}
		bit++
		k >>= 1
	}
	return node
}
'''

SOLUTIONS["1485_clone_binary_tree_with_random_pointer"] = r'''// LeetCode 1485 - Clone Binary Tree With Random Pointer
// https://leetcode.com/problems/clone-binary-tree-with-random-pointer/

type Node struct {
	Val    int
	Left   *Node
	Right  *Node
	Random *Node
}

func copyRandomBinaryTree(root *Node) *Node {
	copies := map[*Node]*Node{}
	var clone func(*Node) *Node
	clone = func(node *Node) *Node {
		if node == nil {
			return nil
		}
		if c, ok := copies[node]; ok {
			return c
		}
		copies[node] = &Node{Val: node.Val}
		copies[node].Left = clone(node.Left)
		copies[node].Right = clone(node.Right)
		copies[node].Random = clone(node.Random)
		return copies[node]
	}
	return clone(root)
}
'''

SOLUTIONS["1486_xor_operation_in_an_array"] = r'''// LeetCode 1486 - XOR Operation in an Array
// https://leetcode.com/problems/xor-operation-in-an-array/

func xorOperation(n int, start int) int {
	ans := 0
	for i := 0; i < n; i++ {
		ans ^= start + 2*i
	}
	return ans
}
'''

SOLUTIONS["1487_making_file_names_unique"] = r'''// LeetCode 1487 - Making File Names Unique
// https://leetcode.com/problems/making-file-names-unique/

import "fmt"

func getFolderNames(names []string) []string {
	used := map[string]int{}
	ans := make([]string, len(names))
	for i, name := range names {
		candidate := name
		if _, ok := used[name]; ok {
			k := used[name]
			for {
				candidate = fmt.Sprintf("%s(%d)", name, k)
				if _, exists := used[candidate]; !exists {
					break
				}
				k++
			}
			used[name] = k + 1
		}
		used[candidate] = 1
		ans[i] = candidate
	}
	return ans
}
'''

SOLUTIONS["1488_avoid_flood_in_the_city"] = r'''// LeetCode 1488 - Avoid Flood in The City
// https://leetcode.com/problems/avoid-flood-in-the-city/

import "sort"

func avoidFlood(rains []int) []int {
	ans := make([]int, len(rains))
	for i := range ans {
		ans[i] = -1
	}
	full := map[int]int{}
	dry := []int{}
	for i, lake := range rains {
		if lake == 0 {
			dry = append(dry, i)
			ans[i] = 1
		} else {
			if prev, ok := full[lake]; ok {
				j := sort.SearchInts(dry, prev+1)
				if j == len(dry) {
					return []int{}
				}
				ans[dry[j]] = lake
				dry = append(dry[:j], dry[j+1:]...)
			}
			full[lake] = i
		}
	}
	return ans
}
'''

SOLUTIONS["1489_find_critical_and_pseudo_critical_edges_in_minimum_spanning_tree"] = r'''// LeetCode 1489 - Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
// https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

import "sort"

func findCriticalAndPseudoCriticalEdges(n int, edges [][]int) [][]int {
	type edge struct{ w, a, b, i int }
	es := make([]edge, len(edges))
	for i, e := range edges {
		es[i] = edge{e[2], e[0], e[1], i}
	}
	sort.Slice(es, func(i, j int) bool { return es[i].w < es[j].w })
	const inf = int(1e18)
	mst := func(skip, force int) int {
		parent := make([]int, n)
		for i := range parent {
			parent[i] = i
		}
		var find func(int) int
		find = func(x int) int {
			for x != parent[x] {
				parent[x] = parent[parent[x]]
				x = parent[x]
			}
			return x
		}
		total, used := 0, 0
		if force >= 0 {
			e := es[force]
			parent[find(e.a)] = find(e.b)
			total += e.w
			used++
		}
		for j, e := range es {
			if j == skip || j == force {
				continue
			}
			x, y := find(e.a), find(e.b)
			if x != y {
				parent[x] = y
				total += e.w
				used++
			}
		}
		if used == n-1 {
			return total
		}
		return inf
	}
	base := mst(-1, -1)
	critical, pseudo := []int{}, []int{}
	for j, e := range es {
		if mst(j, -1) > base {
			critical = append(critical, e.i)
		} else if mst(-1, j) == base {
			pseudo = append(pseudo, e.i)
		}
	}
	sort.Ints(critical)
	sort.Ints(pseudo)
	return [][]int{critical, pseudo}
}
'''

SOLUTIONS["1490_clone_n_ary_tree"] = r'''// LeetCode 1490 - Clone N-ary Tree
// https://leetcode.com/problems/clone-n-ary-tree/

type Node struct {
	Val      int
	Children []*Node
}

func cloneTree(root *Node) *Node {
	if root == nil {
		return nil
	}
	children := make([]*Node, len(root.Children))
	for i, child := range root.Children {
		children[i] = cloneTree(child)
	}
	return &Node{Val: root.Val, Children: children}
}
'''

SOLUTIONS["1491_average_salary_excluding_the_minimum_and_maximum_salary"] = r'''// LeetCode 1491 - Average Salary Excluding the Minimum and Maximum Salary
// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

func average(salary []int) float64 {
	mn, mx, sum := salary[0], salary[0], 0
	for _, s := range salary {
		sum += s
		if s < mn {
			mn = s
		}
		if s > mx {
			mx = s
		}
	}
	return float64(sum-mn-mx) / float64(len(salary)-2)
}
'''

SOLUTIONS["1492_the_kth_factor_of_n"] = r'''// LeetCode 1492 - The kth Factor of n
// https://leetcode.com/problems/the-kth-factor-of-n/

func kthFactor(n int, k int) int {
	for x := 1; x <= n; x++ {
		if n%x == 0 {
			k--
			if k == 0 {
				return x
			}
		}
	}
	return -1
}
'''

SOLUTIONS["1493_longest_subarray_of_1s_after_deleting_one_element"] = r'''// LeetCode 1493 - Longest Subarray of 1's After Deleting One Element
// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

func longestSubarray(nums []int) int {
	left, zeros, ans := 0, 0, 0
	for right, x := range nums {
		if x == 0 {
			zeros++
		}
		for zeros > 1 {
			if nums[left] == 0 {
				zeros--
			}
			left++
		}
		if right-left > ans {
			ans = right - left
		}
	}
	return ans
}
'''

SOLUTIONS["1494_parallel_courses_ii"] = r'''// LeetCode 1494 - Parallel Courses II
// https://leetcode.com/problems/parallel-courses-ii/

func minNumberOfSemesters(n int, relations [][]int, k int) int {
	prereq := make([]int, n)
	for _, r := range relations {
		prereq[r[1]-1] |= 1 << (r[0] - 1)
	}
	full := (1 << n) - 1
	const inf = int(1e9)
	dp := make([]int, 1<<n)
	for i := range dp {
		dp[i] = inf
	}
	dp[0] = 0
	bitCount := func(x int) int {
		c := 0
		for x > 0 {
			c += x & 1
			x >>= 1
		}
		return c
	}
	for mask := 0; mask < 1<<n; mask++ {
		if dp[mask] == inf {
			continue
		}
		available := 0
		for c := 0; c < n; c++ {
			if mask>>c&1 == 0 && prereq[c]&mask == prereq[c] {
				available |= 1 << c
			}
		}
		var choices []int
		if bitCount(available) <= k {
			choices = []int{available}
		} else {
			for sub := available; sub > 0; sub = (sub - 1) & available {
				if bitCount(sub) == k {
					choices = append(choices, sub)
				}
			}
		}
		for _, take := range choices {
			next := mask | take
			if dp[mask]+1 < dp[next] {
				dp[next] = dp[mask] + 1
			}
		}
	}
	return dp[full]
}
'''

SOLUTIONS["1496_path_crossing"] = r'''// LeetCode 1496 - Path Crossing
// https://leetcode.com/problems/path-crossing/

func isPathCrossing(path string) bool {
	x, y := 0, 0
	seen := map[[2]int]bool{{0, 0}: true}
	move := map[byte][2]int{'N': {0, 1}, 'S': {0, -1}, 'E': {1, 0}, 'W': {-1, 0}}
	for i := 0; i < len(path); i++ {
		d := move[path[i]]
		x += d[0]
		y += d[1]
		if seen[[2]int{x, y}] {
			return true
		}
		seen[[2]int{x, y}] = true
	}
	return false
}
'''

SOLUTIONS["1497_check_if_array_pairs_are_divisible_by_k"] = r'''// LeetCode 1497 - Check If Array Pairs Are Divisible by k
// https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

func canArrange(arr []int, k int) bool {
	count := make([]int, k)
	for _, x := range arr {
		r := x % k
		if r < 0 {
			r += k
		}
		count[r]++
	}
	if count[0]%2 != 0 {
		return false
	}
	for r := 1; r < k; r++ {
		if count[r] != count[k-r] {
			return false
		}
	}
	return true
}
'''

SOLUTIONS["1498_number_of_subsequences_that_satisfy_the_given_sum_condition"] = r'''// LeetCode 1498 - Number of Subsequences That Satisfy the Given Sum Condition
// https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

import "sort"

func numSubseq(nums []int, target int) int {
	sort.Ints(nums)
	const mod = 1000000007
	left, right, ans := 0, len(nums)-1, 0
	powers := make([]int, len(nums)+1)
	powers[0] = 1
	for i := 1; i < len(powers); i++ {
		powers[i] = powers[i-1] * 2 % mod
	}
	for left <= right {
		if nums[left]+nums[right] <= target {
			ans = (ans + powers[right-left]) % mod
			left++
		} else {
			right--
		}
	}
	return ans
}
'''

SOLUTIONS["1499_max_value_of_equation"] = r'''// LeetCode 1499 - Max Value of Equation
// https://leetcode.com/problems/max-value-of-equation/

func findMaxValueOfEquation(points [][]int, k int) int {
	type pair struct{ x, v int }
	q := []pair{}
	ans := int(-1e18)
	for _, p := range points {
		x, y := p[0], p[1]
		for len(q) > 0 && x-q[0].x > k {
			q = q[1:]
		}
		if len(q) > 0 {
			v := x + y + q[0].v
			if v > ans {
				ans = v
			}
		}
		value := y - x
		for len(q) > 0 && q[len(q)-1].v <= value {
			q = q[:len(q)-1]
		}
		q = append(q, pair{x, value})
	}
	return ans
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
