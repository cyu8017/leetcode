#!/usr/bin/env python3
"""Write Go solutions for folders 1143-1189."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(r"c:\Users\Charlie Yu\Documents\leetcode")
SOLUTIONS: dict[str, str] = {}

SOLUTIONS["1143_longest_common_subsequence"] = r'''// LeetCode 1143 - Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/

func longestCommonSubsequence(text1 string, text2 string) int {
	m, n := len(text1), len(text2)
	dp := make([]int, n+1)
	for i := 1; i <= m; i++ {
		prev := 0
		for j := 1; j <= n; j++ {
			cur := dp[j]
			if text1[i-1] == text2[j-1] {
				dp[j] = prev + 1
			} else if dp[j-1] > dp[j] {
				dp[j] = dp[j-1]
			}
			prev = cur
		}
	}
	return dp[n]
}
'''

SOLUTIONS["1144_decrease_elements_to_make_array_zigzag"] = r'''// LeetCode 1144 - Decrease Elements To Make Array Zigzag
// https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

func movesToMakeZigzag(nums []int) int {
	cost := func(start int) int {
		ans := 0
		inf := int(^uint(0) >> 1)
		for i := start; i < len(nums); i += 2 {
			left, right := inf, inf
			if i > 0 {
				left = nums[i-1]
			}
			if i+1 < len(nums) {
				right = nums[i+1]
			}
			limit := left
			if right < limit {
				limit = right
			}
			if nums[i]-limit+1 > 0 {
				ans += nums[i] - limit + 1
			}
		}
		return ans
	}
	a, b := cost(0), cost(1)
	if a < b {
		return a
	}
	return b
}
'''

SOLUTIONS["1145_binary_tree_coloring_game"] = r'''// LeetCode 1145 - Binary Tree Coloring Game
// https://leetcode.com/problems/binary-tree-coloring-game/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func btreeGameWinningMove(root *TreeNode, n int, x int) bool {
	left, right := 0, 0
	var dfs func(*TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		l, r := dfs(node.Left), dfs(node.Right)
		if node.Val == x {
			left, right = l, r
		}
		return l + r + 1
	}
	dfs(root)
	parentSide := n - left - right - 1
	best := left
	if right > best {
		best = right
	}
	if parentSide > best {
		best = parentSide
	}
	return best > n/2
}
'''

SOLUTIONS["1146_snapshot_array"] = r'''// LeetCode 1146 - Snapshot Array
// https://leetcode.com/problems/snapshot-array/

import "sort"

type SnapshotArray struct {
	snapID int
	data   [][][2]int
}

func Constructor(length int) SnapshotArray {
	data := make([][][2]int, length)
	for i := range data {
		data[i] = [][2]int{{0, 0}}
	}
	return SnapshotArray{data: data}
}

func (this *SnapshotArray) Set(index int, val int) {
	hist := this.data[index]
	if hist[len(hist)-1][0] == this.snapID {
		hist[len(hist)-1][1] = val
	} else {
		this.data[index] = append(hist, [2]int{this.snapID, val})
	}
}

func (this *SnapshotArray) Snap() int {
	id := this.snapID
	this.snapID++
	return id
}

func (this *SnapshotArray) Get(index int, snap_id int) int {
	hist := this.data[index]
	i := sort.Search(len(hist), func(i int) bool {
		return hist[i][0] > snap_id
	}) - 1
	return hist[i][1]
}
'''

SOLUTIONS["1147_longest_chunked_palindrome_decomposition"] = r'''// LeetCode 1147 - Longest Chunked Palindrome Decomposition
// https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

func longestDecomposition(text string) int {
	n := len(text)
	ans := 0
	i := 0
	for i < n-i {
		found := false
		for length := 1; length <= (n-2*i)/2; length++ {
			if text[i:i+length] == text[n-i-length:n-i] {
				ans += 2
				i += length
				found = true
				break
			}
		}
		if !found {
			ans++
			break
		}
	}
	return ans
}
'''

SOLUTIONS["1150_check_if_a_number_is_majority_element_in_a_sorted_array"] = r'''// LeetCode 1150 - Check If a Number Is Majority Element in a Sorted Array
// https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

import "sort"

func isMajorityElement(nums []int, target int) bool {
	left := sort.SearchInts(nums, target)
	right := sort.Search(len(nums), func(i int) bool { return nums[i] > target })
	return right-left > len(nums)/2
}
'''

SOLUTIONS["1151_minimum_swaps_to_group_all_1s_together"] = r'''// LeetCode 1151 - Minimum Swaps to Group All 1's Together
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

func minSwaps(data []int) int {
	ones := 0
	for _, x := range data {
		ones += x
	}
	if ones <= 1 {
		return 0
	}
	cur := 0
	for i := 0; i < ones; i++ {
		cur += data[i]
	}
	best := cur
	for i := ones; i < len(data); i++ {
		cur += data[i] - data[i-ones]
		if cur > best {
			best = cur
		}
	}
	return ones - best
}
'''

SOLUTIONS["1152_analyze_user_website_visit_pattern"] = r'''// LeetCode 1152 - Analyze User Website Visit Pattern
// https://leetcode.com/problems/analyze-user-website-visit-pattern/

import "sort"

func mostVisitedPattern(username []string, timestamp []int, website []string) []string {
	type visit struct {
		t    int
		site string
	}
	visits := map[string][]visit{}
	for i := range username {
		visits[username[i]] = append(visits[username[i]], visit{timestamp[i], website[i]})
	}
	scores := map[[3]string]int{}
	for _, vs := range visits {
		sort.Slice(vs, func(i, j int) bool { return vs[i].t < vs[j].t })
		sites := make([]string, len(vs))
		for i, v := range vs {
			sites[i] = v.site
		}
		patterns := map[[3]string]bool{}
		for i := 0; i < len(sites); i++ {
			for j := i + 1; j < len(sites); j++ {
				for k := j + 1; k < len(sites); k++ {
					patterns[[3]string{sites[i], sites[j], sites[k]}] = true
				}
			}
		}
		for p := range patterns {
			scores[p]++
		}
	}
	var best [3]string
	bestCount := -1
	first := true
	for p, c := range scores {
		if first || c > bestCount || (c == bestCount && (p[0] < best[0] || (p[0] == best[0] && (p[1] < best[1] || (p[1] == best[1] && p[2] < best[2]))))) {
			best, bestCount, first = p, c, false
		}
	}
	return []string{best[0], best[1], best[2]}
}
'''

SOLUTIONS["1153_string_transforms_into_another_string"] = r'''// LeetCode 1153 - String Transforms Into Another String
// https://leetcode.com/problems/string-transforms-into-another-string/

func canConvert(str1 string, str2 string) bool {
	if str1 == str2 {
		return true
	}
	mapping := map[byte]byte{}
	for i := 0; i < len(str1); i++ {
		a, b := str1[i], str2[i]
		if v, ok := mapping[a]; ok && v != b {
			return false
		}
		mapping[a] = b
	}
	seen := map[byte]bool{}
	for i := 0; i < len(str2); i++ {
		seen[str2[i]] = true
	}
	return len(seen) < 26
}
'''

SOLUTIONS["1154_day_of_the_year"] = r'''// LeetCode 1154 - Day of the Year
// https://leetcode.com/problems/day-of-the-year/

func dayOfYear(date string) int {
	year := atoi(date[0:4])
	month := atoi(date[5:7])
	day := atoi(date[8:10])
	leap := year%4 == 0 && (year%100 != 0 || year%400 == 0)
	days := []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	if leap {
		days[1] = 29
	}
	ans := day
	for i := 0; i < month-1; i++ {
		ans += days[i]
	}
	return ans
}

func atoi(s string) int {
	n := 0
	for i := 0; i < len(s); i++ {
		n = n*10 + int(s[i]-'0')
	}
	return n
}
'''

SOLUTIONS["1155_number_of_dice_rolls_with_target_sum"] = r'''// LeetCode 1155 - Number of Dice Rolls With Target Sum
// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

func numRollsToTarget(n int, k int, target int) int {
	const MOD = 1000000007
	dp := make([]int, target+1)
	dp[0] = 1
	for roll := 0; roll < n; roll++ {
		newDP := make([]int, target+1)
		for s := 0; s <= target; s++ {
			if dp[s] == 0 {
				continue
			}
			for face := 1; face <= k; face++ {
				if s+face <= target {
					newDP[s+face] = (newDP[s+face] + dp[s]) % MOD
				}
			}
		}
		dp = newDP
	}
	return dp[target]
}
'''

SOLUTIONS["1156_swap_for_longest_repeated_character_substring"] = r'''// LeetCode 1156 - Swap For Longest Repeated Character Substring
// https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

func maxRepOpt1(text string) int {
	count := [26]int{}
	for i := 0; i < len(text); i++ {
		count[text[i]-'a']++
	}
	n := len(text)
	ans := 0
	i := 0
	for i < n {
		j := i
		for j < n && text[j] == text[i] {
			j++
		}
		length := j - i
		k := j + 1
		for k < n && text[k] == text[i] {
			k++
		}
		length2 := 0
		if j < n {
			length2 = k - j - 1
		}
		cand := length + length2 + 1
		if cand > count[text[i]-'a'] {
			cand = count[text[i]-'a']
		}
		if cand > ans {
			ans = cand
		}
		i = j
	}
	return ans
}
'''

SOLUTIONS["1157_online_majority_element_in_subarray"] = r'''// LeetCode 1157 - Online Majority Element In Subarray
// https://leetcode.com/problems/online-majority-element-in-subarray/

import "sort"

type MajorityChecker struct {
	arr  []int
	pos  map[int][]int
}

func Constructor(arr []int) MajorityChecker {
	pos := map[int][]int{}
	for i, v := range arr {
		pos[v] = append(pos[v], i)
	}
	return MajorityChecker{arr: arr, pos: pos}
}

func (this *MajorityChecker) Query(left int, right int, threshold int) int {
	for try := 0; try < 20; try++ {
		cand := this.arr[left+((right-left+1)*((try*97+13)%1000)%(right-left+1))]
		// deterministic sample: use positions based on try
		_ = cand
	}
	// Boyer-Moore candidates via random-ish indices
	candidates := []int{}
	span := right - left + 1
	for t := 0; t < 20 && t < span; t++ {
		idx := left + (t*97+13)%span
		candidates = append(candidates, this.arr[idx])
	}
	for _, cand := range candidates {
		arr := this.pos[cand]
		lo := sort.SearchInts(arr, left)
		hi := sort.Search(len(arr), func(i int) bool { return arr[i] > right })
		if hi-lo >= threshold {
			return cand
		}
	}
	return -1
}
'''

# Fix 1157 properly with voting
SOLUTIONS["1157_online_majority_element_in_subarray"] = r'''// LeetCode 1157 - Online Majority Element In Subarray
// https://leetcode.com/problems/online-majority-element-in-subarray/

import "sort"

type MajorityChecker struct {
	arr []int
	pos map[int][]int
}

func Constructor(arr []int) MajorityChecker {
	pos := map[int][]int{}
	for i, v := range arr {
		pos[v] = append(pos[v], i)
	}
	return MajorityChecker{arr: arr, pos: pos}
}

func (this *MajorityChecker) Query(left int, right int, threshold int) int {
	span := right - left + 1
	seen := map[int]bool{}
	for t := 0; t < 30 && t < span; t++ {
		cand := this.arr[left+(t*7919+13)%span]
		if seen[cand] {
			continue
		}
		seen[cand] = true
		arr := this.pos[cand]
		lo := sort.SearchInts(arr, left)
		hi := sort.Search(len(arr), func(i int) bool { return arr[i] > right })
		if hi-lo >= threshold {
			return cand
		}
	}
	return -1
}
'''

SOLUTIONS["1160_find_words_that_can_be_formed_by_characters"] = r'''// LeetCode 1160 - Find Words That Can Be Formed by Characters
// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

func countCharacters(words []string, chars string) int {
	have := [26]int{}
	for i := 0; i < len(chars); i++ {
		have[chars[i]-'a']++
	}
	ans := 0
	for _, w := range words {
		need := [26]int{}
		ok := true
		for i := 0; i < len(w); i++ {
			need[w[i]-'a']++
			if need[w[i]-'a'] > have[w[i]-'a'] {
				ok = false
				break
			}
		}
		if ok {
			ans += len(w)
		}
	}
	return ans
}
'''

SOLUTIONS["1161_maximum_level_sum_of_a_binary_tree"] = r'''// LeetCode 1161 - Maximum Level Sum of a Binary Tree
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxLevelSum(root *TreeNode) int {
	queue := []*TreeNode{root}
	bestSum, bestLevel, level := root.Val, 1, 1
	for len(queue) > 0 {
		sum := 0
		size := len(queue)
		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]
			sum += node.Val
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		if sum > bestSum {
			bestSum, bestLevel = sum, level
		}
		level++
	}
	return bestLevel
}
'''

SOLUTIONS["1162_as_far_from_land_as_possible"] = r'''// LeetCode 1162 - As Far from Land as Possible
// https://leetcode.com/problems/as-far-from-land-as-possible/

func maxDistance(grid [][]int) int {
	n := len(grid)
	type cell struct{ r, c int }
	queue := []cell{}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				queue = append(queue, cell{i, j})
			}
		}
	}
	if len(queue) == 0 || len(queue) == n*n {
		return -1
	}
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	dist := -1
	for len(queue) > 0 {
		size := len(queue)
		dist++
		for i := 0; i < size; i++ {
			cur := queue[0]
			queue = queue[1:]
			for _, d := range dirs {
				nr, nc := cur.r+d[0], cur.c+d[1]
				if nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0 {
					grid[nr][nc] = 1
					queue = append(queue, cell{nr, nc})
				}
			}
		}
	}
	return dist
}
'''

SOLUTIONS["1163_last_substring_in_lexicographical_order"] = r'''// LeetCode 1163 - Last Substring in Lexicographical Order
// https://leetcode.com/problems/last-substring-in-lexicographical-order/

func lastSubstring(s string) string {
	i, j, k := 0, 1, 0
	n := len(s)
	for j+k < n {
		if s[i+k] == s[j+k] {
			k++
		} else if s[i+k] < s[j+k] {
			i = i + k + 1
			if i <= j {
				i = j + 1
			}
			j = i + 1
			if i > j {
				j = i + 1
			}
			// reset properly
			i, j, k = max(i, j), max(i, j)+1, 0
			_ = 0
		} else {
			j = j + k + 1
			k = 0
		}
	}
	// Use cleaner Duval-like algorithm
	i, j, k = 0, 1, 0
	for j+k < n {
		if s[i+k] == s[j+k] {
			k++
			continue
		}
		if s[i+k] < s[j+k] {
			i += k + 1
			if i <= j {
				i = j
				j = i + 1
			} else {
				j = i + 1
			}
		} else {
			j += k + 1
		}
		k = 0
		if j <= i {
			j = i + 1
		}
	}
	return s[i:]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
'''

# Fix 1163 - clean version only
SOLUTIONS["1163_last_substring_in_lexicographical_order"] = r'''// LeetCode 1163 - Last Substring in Lexicographical Order
// https://leetcode.com/problems/last-substring-in-lexicographical-order/

func lastSubstring(s string) string {
	i, j, k := 0, 1, 0
	n := len(s)
	for j+k < n {
		if s[i+k] == s[j+k] {
			k++
			continue
		}
		if s[i+k] < s[j+k] {
			i += k + 1
			if i <= j {
				i = j
			}
			j = i + 1
		} else {
			j += k + 1
		}
		k = 0
		if j <= i {
			j = i + 1
		}
	}
	return s[i:]
}
'''

SOLUTIONS["1165_single_row_keyboard"] = r'''// LeetCode 1165 - Single-Row Keyboard
// https://leetcode.com/problems/single-row-keyboard/

func calculateTime(keyboard string, word string) int {
	pos := [26]int{}
	for i := 0; i < len(keyboard); i++ {
		pos[keyboard[i]-'a'] = i
	}
	ans, cur := 0, 0
	for i := 0; i < len(word); i++ {
		next := pos[word[i]-'a']
		diff := next - cur
		if diff < 0 {
			diff = -diff
		}
		ans += diff
		cur = next
	}
	return ans
}
'''

SOLUTIONS["1166_design_file_system"] = r'''// LeetCode 1166 - Design File System
// https://leetcode.com/problems/design-file-system/

type FileSystem struct {
	vals map[string]int
}

func Constructor() FileSystem {
	return FileSystem{vals: map[string]int{}}
}

func (this *FileSystem) CreatePath(path string, value int) bool {
	if path == "/" || this.vals[path] != 0 {
		return false
	}
	// parent must exist unless root parent
	parent := path
	for i := len(path) - 1; i >= 0; i-- {
		if path[i] == '/' {
			parent = path[:i]
			break
		}
	}
	if parent != "" {
		if this.vals[parent] == 0 {
			return false
		}
	}
	this.vals[path] = value
	return true
}

func (this *FileSystem) Get(path string) int {
	if v, ok := this.vals[path]; ok {
		return v
	}
	return -1
}
'''

SOLUTIONS["1167_minimum_cost_to_connect_sticks"] = r'''// LeetCode 1167 - Minimum Cost to Connect Sticks
// https://leetcode.com/problems/minimum-cost-to-connect-sticks/

import "container/heap"

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

func connectSticks(sticks []int) int {
	h := minHeap(append([]int{}, sticks...))
	heap.Init(&h)
	ans := 0
	for h.Len() > 1 {
		a := heap.Pop(&h).(int)
		b := heap.Pop(&h).(int)
		ans += a + b
		heap.Push(&h, a+b)
	}
	return ans
}
'''

SOLUTIONS["1168_optimize_water_distribution_in_a_village"] = r'''// LeetCode 1168 - Optimize Water Distribution in a Village
// https://leetcode.com/problems/optimize-water-distribution-in-a-village/

import "sort"

func minCostToSupplyWater(n int, wells []int, pipes [][]int) int {
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
	edges := make([][]int, 0, len(wells)+len(pipes))
	for i, w := range wells {
		edges = append(edges, []int{0, i + 1, w})
	}
	edges = append(edges, pipes...)
	sort.Slice(edges, func(i, j int) bool { return edges[i][2] < edges[j][2] })
	ans := 0
	for _, e := range edges {
		a, b := find(e[0]), find(e[1])
		if a == b {
			continue
		}
		parent[b] = a
		ans += e[2]
	}
	return ans
}
'''

SOLUTIONS["1169_invalid_transactions"] = r'''// LeetCode 1169 - Invalid Transactions
// https://leetcode.com/problems/invalid-transactions/

import "strconv"
import "strings"

func invalidTransactions(transactions []string) []string {
	type tx struct {
		name, city, raw string
		time, amount    int
	}
	parsed := make([]tx, len(transactions))
	for i, t := range transactions {
		parts := strings.Split(t, ",")
		tm, _ := strconv.Atoi(parts[1])
		am, _ := strconv.Atoi(parts[2])
		parsed[i] = tx{parts[0], parts[3], t, tm, am}
	}
	invalid := map[string]bool{}
	for i := 0; i < len(parsed); i++ {
		a := parsed[i]
		if a.amount > 1000 {
			invalid[a.raw] = true
		}
		for j := 0; j < len(parsed); j++ {
			if i == j {
				continue
			}
			b := parsed[j]
			diff := a.time - b.time
			if diff < 0 {
				diff = -diff
			}
			if a.name == b.name && a.city != b.city && diff <= 60 {
				invalid[a.raw] = true
				invalid[b.raw] = true
			}
		}
	}
	ans := []string{}
	for _, t := range transactions {
		if invalid[t] {
			ans = append(ans, t)
		}
	}
	return ans
}
'''

SOLUTIONS["1170_compare_strings_by_frequency_of_the_smallest_character"] = r'''// LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
// https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

func numSmallerByFrequency(queries []string, words []string) []int {
	f := func(s string) int {
		best := byte('z' + 1)
		cnt := 0
		for i := 0; i < len(s); i++ {
			if s[i] < best {
				best = s[i]
				cnt = 1
			} else if s[i] == best {
				cnt++
			}
		}
		return cnt
	}
	wf := make([]int, len(words))
	for i, w := range words {
		wf[i] = f(w)
	}
	ans := make([]int, len(queries))
	for i, q := range queries {
		fq := f(q)
		for _, w := range wf {
			if w > fq {
				ans[i]++
			}
		}
	}
	return ans
}
'''

SOLUTIONS["1171_remove_zero_sum_consecutive_nodes_from_linked_list"] = r'''// LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List
// https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeZeroSumSublists(head *ListNode) *ListNode {
	dummy := &ListNode{Next: head}
	prefix := 0
	seen := map[int]*ListNode{0: dummy}
	for node := dummy; node != nil; node = node.Next {
		prefix += node.Val
		seen[prefix] = node
	}
	prefix = 0
	for node := dummy; node != nil; node = node.Next {
		prefix += node.Val
		node.Next = seen[prefix].Next
	}
	return dummy.Next
}
'''

SOLUTIONS["1172_dinner_plate_stacks"] = r'''// LeetCode 1172 - Dinner Plate Stacks
// https://leetcode.com/problems/dinner-plate-stacks/

import "container/heap"

type intHeap []int

func (h intHeap) Len() int            { return len(h) }
func (h intHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h intHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *intHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *intHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type DinnerPlates struct {
	capacity int
	stacks   [][]int
	avail    intHeap
	inAvail  map[int]bool
}

func Constructor(capacity int) DinnerPlates {
	return DinnerPlates{
		capacity: capacity,
		avail:    intHeap{},
		inAvail:  map[int]bool{},
	}
}

func (this *DinnerPlates) Push(val int) {
	for this.avail.Len() > 0 {
		idx := this.avail[0]
		if idx < len(this.stacks) && len(this.stacks[idx]) < this.capacity {
			break
		}
		heap.Pop(&this.avail)
		delete(this.inAvail, idx)
	}
	if this.avail.Len() == 0 {
		this.stacks = append(this.stacks, []int{})
		heap.Push(&this.avail, len(this.stacks)-1)
		this.inAvail[len(this.stacks)-1] = true
	}
	idx := this.avail[0]
	this.stacks[idx] = append(this.stacks[idx], val)
	if len(this.stacks[idx]) == this.capacity {
		heap.Pop(&this.avail)
		delete(this.inAvail, idx)
	}
}

func (this *DinnerPlates) Pop() int {
	return this.PopAtStack(len(this.stacks) - 1)
}

func (this *DinnerPlates) PopAtStack(index int) int {
	if index < 0 || index >= len(this.stacks) || len(this.stacks[index]) == 0 {
		return -1
	}
	st := this.stacks[index]
	val := st[len(st)-1]
	this.stacks[index] = st[:len(st)-1]
	if !this.inAvail[index] {
		heap.Push(&this.avail, index)
		this.inAvail[index] = true
	}
	for len(this.stacks) > 0 && len(this.stacks[len(this.stacks)-1]) == 0 {
		last := len(this.stacks) - 1
		this.stacks = this.stacks[:last]
		if this.inAvail[last] {
			delete(this.inAvail, last)
		}
	}
	return val
}
'''

SOLUTIONS["1175_prime_arrangements"] = r'''// LeetCode 1175 - Prime Arrangements
// https://leetcode.com/problems/prime-arrangements/

func numPrimeArrangements(n int) int {
	const MOD = 1000000007
	isPrime := func(x int) bool {
		if x < 2 {
			return false
		}
		for d := 2; d*d <= x; d++ {
			if x%d == 0 {
				return false
			}
		}
		return true
	}
	primes := 0
	for i := 1; i <= n; i++ {
		if isPrime(i) {
			primes++
		}
	}
	fact := func(x int) int {
		res := 1
		for i := 2; i <= x; i++ {
			res = res * i % MOD
		}
		return res
	}
	return fact(primes) * fact(n-primes) % MOD
}
'''

SOLUTIONS["1176_diet_plan_performance"] = r'''// LeetCode 1176 - Diet Plan Performance
// https://leetcode.com/problems/diet-plan-performance/

func dietPlanPerformance(calories []int, k int, lower int, upper int) int {
	window := 0
	for i := 0; i < k; i++ {
		window += calories[i]
	}
	ans := 0
	if window < lower {
		ans--
	} else if window > upper {
		ans++
	}
	for i := k; i < len(calories); i++ {
		window += calories[i] - calories[i-k]
		if window < lower {
			ans--
		} else if window > upper {
			ans++
		}
	}
	return ans
}
'''

SOLUTIONS["1177_can_make_palindrome_from_substring"] = r'''// LeetCode 1177 - Can Make Palindrome from Substring
// https://leetcode.com/problems/can-make-palindrome-from-substring/

func canMakePaliQueries(s string, queries [][]int) []bool {
	prefix := make([]int, len(s)+1)
	mask := 0
	for i := 0; i < len(s); i++ {
		mask ^= 1 << (s[i] - 'a')
		prefix[i+1] = mask
	}
	ans := make([]bool, len(queries))
	for i, q := range queries {
		bits := bitsCount(prefix[q[1]+1] ^ prefix[q[0]])
		ans[i] = bits/2 <= q[2]
	}
	return ans
}

func bitsCount(x int) int {
	c := 0
	for x > 0 {
		c += x & 1
		x >>= 1
	}
	return c
}
'''

SOLUTIONS["1178_number_of_valid_words_for_each_puzzle"] = r'''// LeetCode 1178 - Number of Valid Words for Each Puzzle
// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

func findNumOfValidWords(words []string, puzzles []string) []int {
	maskOf := func(s string) int {
		mask := 0
		for i := 0; i < len(s); i++ {
			mask |= 1 << (s[i] - 'a')
		}
		return mask
	}
	freq := map[int]int{}
	for _, w := range words {
		freq[maskOf(w)]++
	}
	ans := make([]int, len(puzzles))
	for i, puzzle := range puzzles {
		first := 1 << (puzzle[0] - 'a')
		full := maskOf(puzzle)
		sub := full
		total := 0
		for {
			if sub&first != 0 {
				total += freq[sub]
			}
			if sub == 0 {
				break
			}
			sub = (sub - 1) & full
		}
		ans[i] = total
	}
	return ans
}
'''

SOLUTIONS["1180_count_substrings_with_only_one_distinct_letter"] = r'''// LeetCode 1180 - Count Substrings with Only One Distinct Letter
// https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

func countLetters(s string) int {
	ans, length := 1, 1
	for i := 1; i < len(s); i++ {
		if s[i] == s[i-1] {
			length++
		} else {
			length = 1
		}
		ans += length
	}
	return ans
}
'''

SOLUTIONS["1181_before_and_after_puzzle"] = r'''// LeetCode 1181 - Before and After Puzzle
// https://leetcode.com/problems/before-and-after-puzzle/

import "sort"
import "strings"

func beforeAndAfterPuzzles(phrases []string) []string {
	split := make([][]string, len(phrases))
	for i, p := range phrases {
		split[i] = strings.Fields(p)
	}
	result := map[string]bool{}
	for i := 0; i < len(split); i++ {
		for j := 0; j < len(split); j++ {
			if i == j {
				continue
			}
			if split[i][len(split[i])-1] == split[j][0] {
				merged := append(append([]string{}, split[i]...), split[j][1:]...)
				result[strings.Join(merged, " ")] = true
			}
		}
	}
	ans := make([]string, 0, len(result))
	for s := range result {
		ans = append(ans, s)
	}
	sort.Strings(ans)
	return ans
}
'''

SOLUTIONS["1182_shortest_distance_to_target_color"] = r'''// LeetCode 1182 - Shortest Distance to Target Color
// https://leetcode.com/problems/shortest-distance-to-target-color/

import "sort"

func shortestDistanceColor(colors []int, queries [][]int) []int {
	pos := map[int][]int{}
	for i, c := range colors {
		pos[c] = append(pos[c], i)
	}
	ans := make([]int, len(queries))
	for qi, q := range queries {
		i, c := q[0], q[1]
		arr, ok := pos[c]
		if !ok {
			ans[qi] = -1
			continue
		}
		idx := sort.SearchInts(arr, i)
		best := int(^uint(0) >> 1)
		if idx < len(arr) && arr[idx]-i < best {
			best = arr[idx] - i
		}
		if idx > 0 && i-arr[idx-1] < best {
			best = i - arr[idx-1]
		}
		if best == int(^uint(0)>>1) {
			ans[qi] = -1
		} else {
			ans[qi] = best
		}
	}
	return ans
}
'''

SOLUTIONS["1183_maximum_number_of_ones"] = r'''// LeetCode 1183 - Maximum Number of Ones
// https://leetcode.com/problems/maximum-number-of-ones/

import "sort"

func maximumNumberOfOnes(width int, height int, sideLength int, maxOnes int) int {
	counts := []int{}
	for r := 0; r < sideLength; r++ {
		for c := 0; c < sideLength; c++ {
			rows := (height - r + sideLength - 1) / sideLength
			cols := (width - c + sideLength - 1) / sideLength
			counts = append(counts, rows*cols)
		}
	}
	sort.Sort(sort.Reverse(sort.IntSlice(counts)))
	ans := 0
	for i := 0; i < maxOnes && i < len(counts); i++ {
		ans += counts[i]
	}
	return ans
}
'''

SOLUTIONS["1184_distance_between_bus_stops"] = r'''// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

func distanceBetweenBusStops(distance []int, start int, destination int) int {
	if start > destination {
		start, destination = destination, start
	}
	clockwise := 0
	total := 0
	for i, d := range distance {
		total += d
		if i >= start && i < destination {
			clockwise += d
		}
	}
	if clockwise < total-clockwise {
		return clockwise
	}
	return total - clockwise
}
'''

SOLUTIONS["1185_day_of_the_week"] = r'''// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

func dayOfTheWeek(day int, month int, year int) string {
	// Sakamoto's methods
	t := []int{0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4}
	y := year
	if month < 3 {
		y--
	}
	w := (y + y/4 - y/100 + y/400 + t[month-1] + day) % 7
	days := []string{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
	return days[w]
}
'''

SOLUTIONS["1186_maximum_subarray_sum_with_one_deletion"] = r'''// LeetCode 1186 - Maximum Subarray Sum with One Deletion
// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

func maximumSum(arr []int) int {
	keep, delete, ans := arr[0], arr[0], arr[0]
	for i := 1; i < len(arr); i++ {
		x := arr[i]
		nd := keep
		if delete+x > nd {
			nd = delete + x
		}
		nk := keep + x
		if x > nk {
			nk = x
		}
		keep, delete = nk, nd
		if keep > ans {
			ans = keep
		}
		if delete > ans {
			ans = delete
		}
	}
	return ans
}
'''

SOLUTIONS["1187_make_array_strictly_increasing"] = r'''// LeetCode 1187 - Make Array Strictly Increasing
// https://leetcode.com/problems/make-array-strictly-increasing/

import "sort"

func makeArrayIncreasing(arr1 []int, arr2 []int) int {
	set := map[int]bool{}
	for _, x := range arr2 {
		set[x] = true
	}
	uniq := make([]int, 0, len(set))
	for x := range set {
		uniq = append(uniq, x)
	}
	sort.Ints(uniq)
	arr2 = uniq
	const inf = int(^uint(0) >> 1)
	dp := map[int]int{-1: 0}
	for _, num := range arr1 {
		newDP := map[int]int{}
		for prev, ops := range dp {
			if num > prev {
				if cur, ok := newDP[num]; !ok || ops < cur {
					newDP[num] = ops
				}
			}
			idx := sort.SearchInts(arr2, prev+1)
			if idx < len(arr2) {
				chosen := arr2[idx]
				if cur, ok := newDP[chosen]; !ok || ops+1 < cur {
					newDP[chosen] = ops + 1
				}
			}
		}
		dp = newDP
		if len(dp) == 0 {
			return -1
		}
	}
	best := inf
	for _, v := range dp {
		if v < best {
			best = v
		}
	}
	return best
}
'''

SOLUTIONS["1188_design_bounded_blocking_queue"] = r'''// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

import "sync"

type BoundedBlockingQueue struct {
	capacity int
	queue    []int
	mu       sync.Mutex
	notFull  *sync.Cond
	notEmpty *sync.Cond
}

func Constructor(capacity int) *BoundedBlockingQueue {
	q := &BoundedBlockingQueue{capacity: capacity, queue: []int{}}
	q.notFull = sync.NewCond(&q.mu)
	q.notEmpty = sync.NewCond(&q.mu)
	return q
}

func (this *BoundedBlockingQueue) Enqueue(element int) {
	this.mu.Lock()
	for len(this.queue) == this.capacity {
		this.notFull.Wait()
	}
	this.queue = append(this.queue, element)
	this.notEmpty.Signal()
	this.mu.Unlock()
}

func (this *BoundedBlockingQueue) Dequeue() int {
	this.mu.Lock()
	for len(this.queue) == 0 {
		this.notEmpty.Wait()
	}
	val := this.queue[0]
	this.queue = this.queue[1:]
	this.notFull.Signal()
	this.mu.Unlock()
	return val
}

func (this *BoundedBlockingQueue) Size() int {
	this.mu.Lock()
	defer this.mu.Unlock()
	return len(this.queue)
}
'''

SOLUTIONS["1189_maximum_number_of_balloons"] = r'''// LeetCode 1189 - Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/

func maxNumberOfBalloons(text string) int {
	count := [26]int{}
	for i := 0; i < len(text); i++ {
		count[text[i]-'a']++
	}
	ans := count['b'-'a']
	for _, v := range []int{count['a'-'a'], count['l'-'a'] / 2, count['o'-'a'] / 2, count['n'-'a']} {
		if v < ans {
			ans = v
		}
	}
	return ans
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


def main() -> None:
    written = []
    for name, content in sorted(SOLUTIONS.items()):
        folder = ROOT / name
        if not folder.is_dir() or is_sql(folder):
            continue
        (folder / "solution.go").write_text(content, encoding="utf-8", newline="\n")
        written.append(name)
        print(f"WROTE {name}")
    print(f"\nTotal written: {len(written)}")


if __name__ == "__main__":
    main()
