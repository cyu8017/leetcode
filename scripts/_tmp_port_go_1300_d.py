#!/usr/bin/env python3
"""Port Go solutions 1429-1469 (batch D)."""
import os

ROOT = r"c:\Users\Charlie Yu\Documents\leetcode"

SOLUTIONS = {}

SOLUTIONS["1429_first_unique_number"] = r'''// LeetCode 1429 - First Unique Number
// https://leetcode.com/problems/first-unique-number/

type FirstUnique struct {
	counts map[int]int
	order  []int
	pos    map[int]int
}

func Constructor(nums []int) FirstUnique {
	f := FirstUnique{counts: map[int]int{}, pos: map[int]int{}}
	for _, v := range nums {
		f.Add(v)
	}
	return f
}

func (this *FirstUnique) ShowFirstUnique() int {
	for _, v := range this.order {
		if this.counts[v] == 1 {
			return v
		}
	}
	return -1
}

func (this *FirstUnique) Add(value int) {
	this.counts[value]++
	if this.counts[value] == 1 {
		this.order = append(this.order, value)
	}
}
'''

SOLUTIONS["1430_check_if_a_string_is_a_valid_sequence_from_root_to_leaves_path_in_a_binary_tree"] = r'''// LeetCode 1430 - Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
// https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isValidSequence(root *TreeNode, arr []int) bool {
	var visit func(*TreeNode, int) bool
	visit = func(node *TreeNode, index int) bool {
		if node == nil || index == len(arr) || node.Val != arr[index] {
			return false
		}
		if node.Left == nil && node.Right == nil {
			return index == len(arr)-1
		}
		return visit(node.Left, index+1) || visit(node.Right, index+1)
	}
	return visit(root, 0)
}
'''

SOLUTIONS["1431_kids_with_the_greatest_number_of_candies"] = r'''// LeetCode 1431 - Kids With the Greatest Number of Candies
// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

func kidsWithCandies(candies []int, extraCandies int) []bool {
	maximum := candies[0]
	for _, v := range candies {
		if v > maximum {
			maximum = v
		}
	}
	answer := make([]bool, len(candies))
	for i, v := range candies {
		answer[i] = v+extraCandies >= maximum
	}
	return answer
}
'''

SOLUTIONS["1432_max_difference_you_can_get_from_changing_an_integer"] = r'''// LeetCode 1432 - Max Difference You Can Get From Changing an Integer
// https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

import "strconv"
import "strings"

func maxDiff(num int) int {
	s := strconv.Itoa(num)
	high := s
	for i := 0; i < len(s); i++ {
		if s[i] != '9' {
			high = strings.ReplaceAll(s, string(s[i]), "9")
			break
		}
	}
	low := s
	if s[0] != '1' {
		low = strings.ReplaceAll(s, string(s[0]), "1")
	} else {
		for i := 1; i < len(s); i++ {
			if s[i] != '0' && s[i] != '1' {
				low = strings.ReplaceAll(s, string(s[i]), "0")
				break
			}
		}
	}
	h, _ := strconv.Atoi(high)
	l, _ := strconv.Atoi(low)
	return h - l
}
'''

SOLUTIONS["1433_check_if_a_string_can_break_another_string"] = r'''// LeetCode 1433 - Check If a String Can Break Another String
// https://leetcode.com/problems/check-if-a-string-can-break-another-string/

import "sort"

func checkIfCanBreak(s1 string, s2 string) bool {
	a := []byte(s1)
	b := []byte(s2)
	sort.Slice(a, func(i, j int) bool { return a[i] < a[j] })
	sort.Slice(b, func(i, j int) bool { return b[i] < b[j] })
	ge, le := true, true
	for i := range a {
		if a[i] < b[i] {
			ge = false
		}
		if a[i] > b[i] {
			le = false
		}
	}
	return ge || le
}
'''

SOLUTIONS["1434_number_of_ways_to_wear_different_hats_to_each_other"] = r'''// LeetCode 1434 - Number of Ways to Wear Different Hats to Each Other
// https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/

func numberWays(hats [][]int) int {
	const mod = 1000000007
	people := len(hats)
	wearers := make([][]int, 41)
	for person, choices := range hats {
		for _, hat := range choices {
			wearers[hat] = append(wearers[hat], person)
		}
	}
	dp := make([]int, 1<<people)
	dp[0] = 1
	for hat := 1; hat <= 40; hat++ {
		nxt := append([]int(nil), dp...)
		for mask, ways := range dp {
			if ways == 0 {
				continue
			}
			for _, person := range wearers[hat] {
				if mask>>person&1 == 0 {
					nxt[mask|(1<<person)] = (nxt[mask|(1<<person)] + ways) % mod
				}
			}
		}
		dp = nxt
	}
	return dp[(1<<people)-1]
}
'''

SOLUTIONS["1436_destination_city"] = r'''// LeetCode 1436 - Destination City
// https://leetcode.com/problems/destination-city/

func destCity(paths [][]string) string {
	starts := map[string]bool{}
	for _, p := range paths {
		starts[p[0]] = true
	}
	for _, p := range paths {
		if !starts[p[1]] {
			return p[1]
		}
	}
	return ""
}
'''

SOLUTIONS["1437_check_if_all_1s_are_at_least_length_k_places_away"] = r'''// LeetCode 1437 - Check If All 1's Are at Least Length K Places Away
// https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

func kLengthApart(nums []int, k int) bool {
	previous := -k - 1
	for i, value := range nums {
		if value == 1 {
			if i-previous <= k {
				return false
			}
			previous = i
		}
	}
	return true
}
'''

SOLUTIONS["1438_longest_continuous_subarray_with_absolute_diff_less_than_or_equal_to_limit"] = r'''// LeetCode 1438 - Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
// https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

func longestSubarray(nums []int, limit int) int {
	low, high := []int{}, []int{}
	left, answer := 0, 0
	for right, value := range nums {
		for len(low) > 0 && nums[low[len(low)-1]] > value {
			low = low[:len(low)-1]
		}
		for len(high) > 0 && nums[high[len(high)-1]] < value {
			high = high[:len(high)-1]
		}
		low = append(low, right)
		high = append(high, right)
		for nums[high[0]]-nums[low[0]] > limit {
			left++
			if low[0] < left {
				low = low[1:]
			}
			if high[0] < left {
				high = high[1:]
			}
		}
		if right-left+1 > answer {
			answer = right - left + 1
		}
	}
	return answer
}
'''

SOLUTIONS["1439_find_the_kth_smallest_sum_of_a_matrix_with_sorted_rows"] = r'''// LeetCode 1439 - Find the Kth Smallest Sum of a Matrix With Sorted Rows
// https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

import "container/heap"

type item struct{ value, i, j int }
type minHeap []item

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i].value < h[j].value }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func kthSmallest(mat [][]int, k int) int {
	sums := []int{0}
	for _, row := range mat {
		h := &minHeap{{sums[0] + row[0], 0, 0}}
		heap.Init(h)
		merged := []int{}
		for h.Len() > 0 && len(merged) < k {
			cur := heap.Pop(h).(item)
			merged = append(merged, cur.value)
			if cur.j+1 < len(row) {
				heap.Push(h, item{sums[cur.i] + row[cur.j+1], cur.i, cur.j + 1})
			}
			if cur.j == 0 && cur.i+1 < len(sums) {
				heap.Push(h, item{sums[cur.i+1] + row[0], cur.i + 1, 0})
			}
		}
		sums = merged
	}
	return sums[k-1]
}
'''

SOLUTIONS["1441_build_an_array_with_stack_operations"] = r'''// LeetCode 1441 - Build an Array With Stack Operations
// https://leetcode.com/problems/build-an-array-with-stack-operations/

func buildArray(target []int, n int) []string {
	answer := []string{}
	current := 1
	for _, value := range target {
		for current < value {
			answer = append(answer, "Push", "Pop")
			current++
		}
		answer = append(answer, "Push")
		current++
	}
	return answer
}
'''

SOLUTIONS["1442_count_triplets_that_can_form_two_arrays_of_equal_xor"] = r'''// LeetCode 1442 - Count Triplets That Can Form Two Arrays of Equal XOR
// https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

func countTriplets(arr []int) int {
	answer := 0
	for i := range arr {
		value := 0
		for k := i; k < len(arr); k++ {
			value ^= arr[k]
			if value == 0 {
				answer += k - i
			}
		}
	}
	return answer
}
'''

SOLUTIONS["1443_minimum_time_to_collect_all_apples_in_a_tree"] = r'''// LeetCode 1443 - Minimum Time to Collect All Apples in a Tree
// https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

func minTime(n int, edges [][]int, hasApple []bool) int {
	graph := make([][]int, n)
	for _, e := range edges {
		a, b := e[0], e[1]
		graph[a] = append(graph[a], b)
		graph[b] = append(graph[b], a)
	}
	var visit func(int, int) int
	visit = func(node, parent int) int {
		cost := 0
		for _, child := range graph[node] {
			if child != parent {
				childCost := visit(child, node)
				if childCost > 0 || hasApple[child] {
					cost += childCost + 2
				}
			}
		}
		return cost
	}
	return visit(0, -1)
}
'''

SOLUTIONS["1444_number_of_ways_of_cutting_a_pizza"] = r'''// LeetCode 1444 - Number of Ways of Cutting a Pizza
// https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

func ways(pizza []string, k int) int {
	const mod = 1000000007
	rows, cols := len(pizza), len(pizza[0])
	apples := make([][]int, rows+1)
	for i := range apples {
		apples[i] = make([]int, cols+1)
	}
	for r := rows - 1; r >= 0; r-- {
		for c := cols - 1; c >= 0; c-- {
			add := 0
			if pizza[r][c] == 'A' {
				add = 1
			}
			apples[r][c] = add + apples[r+1][c] + apples[r][c+1] - apples[r+1][c+1]
		}
	}
	dp := make([][]int, rows)
	for r := range dp {
		dp[r] = make([]int, cols)
		for c := range dp[r] {
			if apples[r][c] > 0 {
				dp[r][c] = 1
			}
		}
	}
	for cut := 1; cut < k; cut++ {
		nxt := make([][]int, rows)
		for r := range nxt {
			nxt[r] = make([]int, cols)
		}
		for r := 0; r < rows; r++ {
			for c := 0; c < cols; c++ {
				for nr := r + 1; nr < rows; nr++ {
					if apples[r][c] > apples[nr][c] {
						nxt[r][c] += dp[nr][c]
					}
				}
				for nc := c + 1; nc < cols; nc++ {
					if apples[r][c] > apples[r][nc] {
						nxt[r][c] += dp[r][nc]
					}
				}
				nxt[r][c] %= mod
			}
		}
		dp = nxt
	}
	return dp[0][0]
}
'''

SOLUTIONS["1446_consecutive_characters"] = r'''// LeetCode 1446 - Consecutive Characters
// https://leetcode.com/problems/consecutive-characters/

func maxPower(s string) int {
	answer, run := 1, 1
	for i := 1; i < len(s); i++ {
		if s[i] == s[i-1] {
			run++
		} else {
			run = 1
		}
		if run > answer {
			answer = run
		}
	}
	return answer
}
'''

SOLUTIONS["1447_simplified_fractions"] = r'''// LeetCode 1447 - Simplified Fractions
// https://leetcode.com/problems/simplified-fractions/

import "fmt"

func simplifiedFractions(n int) []string {
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	var answer []string
	for a := 1; a < n; a++ {
		for b := a + 1; b <= n; b++ {
			if gcd(a, b) == 1 {
				answer = append(answer, fmt.Sprintf("%d/%d", a, b))
			}
		}
	}
	return answer
}
'''

SOLUTIONS["1448_count_good_nodes_in_binary_tree"] = r'''// LeetCode 1448 - Count Good Nodes in Binary Tree
// https://leetcode.com/problems/count-good-nodes-in-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func goodNodes(root *TreeNode) int {
	var visit func(*TreeNode, int) int
	visit = func(node *TreeNode, maximum int) int {
		if node == nil {
			return 0
		}
		good := 0
		if node.Val >= maximum {
			good = 1
			maximum = node.Val
		}
		return good + visit(node.Left, maximum) + visit(node.Right, maximum)
	}
	return visit(root, int(-1e9))
}
'''

SOLUTIONS["1449_form_largest_integer_with_digits_that_add_up_to_target"] = r'''// LeetCode 1449 - Form Largest Integer With Digits That Add up to Target
// https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/

func largestNumber(cost []int, target int) string {
	dp := make([]*string, target+1)
	empty := ""
	dp[0] = &empty
	for total := 1; total <= target; total++ {
		var best *string
		for digit := 1; digit <= 9; digit++ {
			price := cost[digit-1]
			if total >= price && dp[total-price] != nil {
				candidate := string(byte('0'+digit)) + *dp[total-price]
				if best == nil || len(candidate) > len(*best) || (len(candidate) == len(*best) && candidate > *best) {
					c := candidate
					best = &c
				}
			}
		}
		dp[total] = best
	}
	if dp[target] == nil {
		return "0"
	}
	return *dp[target]
}
'''

SOLUTIONS["1450_number_of_students_doing_homework_at_a_given_time"] = r'''// LeetCode 1450 - Number of Students Doing Homework at a Given Time
// https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

func busyStudent(startTime []int, endTime []int, queryTime int) int {
	ans := 0
	for i := range startTime {
		if startTime[i] <= queryTime && queryTime <= endTime[i] {
			ans++
		}
	}
	return ans
}
'''

SOLUTIONS["1451_rearrange_words_in_a_sentence"] = r'''// LeetCode 1451 - Rearrange Words in a Sentence
// https://leetcode.com/problems/rearrange-words-in-a-sentence/

import (
	"sort"
	"strings"
)

func arrangeWords(text string) string {
	words := strings.Fields(strings.ToLower(text))
	sort.SliceStable(words, func(i, j int) bool { return len(words[i]) < len(words[j]) })
	s := strings.Join(words, " ")
	if len(s) == 0 {
		return s
	}
	return strings.ToUpper(s[:1]) + s[1:]
}
'''

SOLUTIONS["1452_people_whose_list_of_favorite_companies_is_not_a_subset_of_another_list"] = r'''// LeetCode 1452 - People Whose List of Favorite Companies Is Not a Subset of Another List
// https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

func peopleIndexes(favoriteCompanies [][]string) []int {
	sets := make([]map[string]bool, len(favoriteCompanies))
	for i, comps := range favoriteCompanies {
		sets[i] = map[string]bool{}
		for _, c := range comps {
			sets[i][c] = true
		}
	}
	isSubset := func(a, b map[string]bool) bool {
		for k := range a {
			if !b[k] {
				return false
			}
		}
		return true
	}
	var answer []int
	for i, s := range sets {
		ok := true
		for j, t := range sets {
			if i != j && isSubset(s, t) {
				ok = false
				break
			}
		}
		if ok {
			answer = append(answer, i)
		}
	}
	return answer
}
'''

SOLUTIONS["1453_maximum_number_of_darts_inside_of_a_circular_dartboard"] = r'''// LeetCode 1453 - Maximum Number of Darts Inside of a Circular Dartboard
// https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/

import "math"

func numPoints(darts [][]int, r int) int {
	ans := 0
	if len(darts) > 0 {
		ans = 1
	}
	rr := float64(r)
	for i, p1 := range darts {
		x1, y1 := float64(p1[0]), float64(p1[1])
		for _, p2 := range darts[i+1:] {
			x2, y2 := float64(p2[0]), float64(p2[1])
			dx, dy := x2-x1, y2-y1
			d2 := dx*dx + dy*dy
			if d2 > 4*rr*rr || d2 == 0 {
				continue
			}
			d := math.Sqrt(d2)
			h := math.Sqrt(rr*rr - d2/4)
			mx, my := (x1+x2)/2, (y1+y2)/2
			for _, sign := range []float64{-1, 1} {
				cx := mx + sign*(-dy)*h/d
				cy := my + sign*dx*h/d
				count := 0
				for _, p := range darts {
					x, y := float64(p[0]), float64(p[1])
					if (x-cx)*(x-cx)+(y-cy)*(y-cy) <= rr*rr+1e-7 {
						count++
					}
				}
				if count > ans {
					ans = count
				}
			}
		}
	}
	return ans
}
'''

SOLUTIONS["1455_check_if_a_word_occurs_as_a_prefix_of_any_word_in_a_sentence"] = r'''// LeetCode 1455 - Check If a Word Occurs As a Prefix of Any Word in a Sentence
// https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

import "strings"

func isPrefixOfWord(sentence string, searchWord string) int {
	words := strings.Fields(sentence)
	for i, w := range words {
		if strings.HasPrefix(w, searchWord) {
			return i + 1
		}
	}
	return -1
}
'''

SOLUTIONS["1456_maximum_number_of_vowels_in_a_substring_of_given_length"] = r'''// LeetCode 1456 - Maximum Number of Vowels in a Substring of Given Length
// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

func maxVowels(s string, k int) int {
	isVowel := func(c byte) bool {
		return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
	}
	cur := 0
	for i := 0; i < k; i++ {
		if isVowel(s[i]) {
			cur++
		}
	}
	ans := cur
	for i := k; i < len(s); i++ {
		if isVowel(s[i]) {
			cur++
		}
		if isVowel(s[i-k]) {
			cur--
		}
		if cur > ans {
			ans = cur
		}
	}
	return ans
}
'''

SOLUTIONS["1457_pseudo_palindromic_paths_in_a_binary_tree"] = r'''// LeetCode 1457 - Pseudo-Palindromic Paths in a Binary Tree
// https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pseudoPalindromicPaths(root *TreeNode) int {
	var dfs func(*TreeNode, int) int
	dfs = func(node *TreeNode, mask int) int {
		if node == nil {
			return 0
		}
		mask ^= 1 << node.Val
		if node.Left == nil && node.Right == nil {
			if mask&(mask-1) == 0 {
				return 1
			}
			return 0
		}
		return dfs(node.Left, mask) + dfs(node.Right, mask)
	}
	return dfs(root, 0)
}
'''

SOLUTIONS["1458_max_dot_product_of_two_subsequences"] = r'''// LeetCode 1458 - Max Dot Product of Two Subsequences
// https://leetcode.com/problems/max-dot-product-of-two-subsequences/

func maxDotProduct(nums1 []int, nums2 []int) int {
	n := len(nums2)
	const negInf = int(-1e18)
	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = negInf
	}
	for _, a := range nums1 {
		prev := append([]int(nil), dp...)
		for j, b := range nums2 {
			jj := j + 1
			product := a * b
			best := dp[jj-1]
			if prev[jj] > best {
				best = prev[jj]
			}
			if product > best {
				best = product
			}
			alt := product
			if prev[jj-1] > 0 {
				alt += prev[jj-1]
			}
			if alt > best {
				best = alt
			}
			dp[jj] = best
		}
	}
	return dp[n]
}
'''

SOLUTIONS["1460_make_two_arrays_equal_by_reversing_subarrays"] = r'''// LeetCode 1460 - Make Two Arrays Equal by Reversing Subarrays
// https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

func canBeEqual(target []int, arr []int) bool {
	count := map[int]int{}
	for _, v := range target {
		count[v]++
	}
	for _, v := range arr {
		count[v]--
		if count[v] < 0 {
			return false
		}
	}
	return true
}
'''

SOLUTIONS["1461_check_if_a_string_contains_all_binary_codes_of_size_k"] = r'''// LeetCode 1461 - Check If a String Contains All Binary Codes of Size K
// https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

func hasAllCodes(s string, k int) bool {
	if len(s) < k {
		return false
	}
	seen := map[string]bool{}
	for i := 0; i <= len(s)-k; i++ {
		seen[s[i:i+k]] = true
	}
	return len(seen) == 1<<k
}
'''

SOLUTIONS["1462_course_schedule_iv"] = r'''// LeetCode 1462 - Course Schedule IV
// https://leetcode.com/problems/course-schedule-iv/

func checkIfPrerequisite(numCourses int, prerequisites [][]int, queries [][]int) []bool {
	reach := make([][]bool, numCourses)
	for i := range reach {
		reach[i] = make([]bool, numCourses)
	}
	for _, p := range prerequisites {
		reach[p[0]][p[1]] = true
	}
	for k := 0; k < numCourses; k++ {
		for i := 0; i < numCourses; i++ {
			if reach[i][k] {
				for j := 0; j < numCourses; j++ {
					reach[i][j] = reach[i][j] || reach[k][j]
				}
			}
		}
	}
	answer := make([]bool, len(queries))
	for i, q := range queries {
		answer[i] = reach[q[0]][q[1]]
	}
	return answer
}
'''

SOLUTIONS["1463_cherry_pickup_ii"] = r'''// LeetCode 1463 - Cherry Pickup II
// https://leetcode.com/problems/cherry-pickup-ii/

func cherryPickup(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	type key struct{ a, b int }
	dp := map[key]int{{0, n - 1}: grid[0][0]}
	if n > 1 {
		dp[key{0, n - 1}] += grid[0][n-1]
	}
	for r := 1; r < m; r++ {
		nxt := map[key]int{}
		for kb, score := range dp {
			a, b := kb.a, kb.b
			for _, da := range []int{-1, 0, 1} {
				for _, db := range []int{-1, 0, 1} {
					na, nb := a+da, b+db
					if na >= 0 && na < n && nb >= 0 && nb < n {
						val := score + grid[r][na]
						if na != nb {
							val += grid[r][nb]
						}
						k := key{na, nb}
						if v, ok := nxt[k]; !ok || val > v {
							nxt[k] = val
						}
					}
				}
			}
		}
		dp = nxt
	}
	ans := 0
	for _, v := range dp {
		if v > ans {
			ans = v
		}
	}
	return ans
}
'''

SOLUTIONS["1464_maximum_product_of_two_elements_in_an_array"] = r'''// LeetCode 1464 - Maximum Product of Two Elements in an Array
// https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

func maxProduct(nums []int) int {
	a, b := 0, 0
	for _, v := range nums {
		if v > a {
			b = a
			a = v
		} else if v > b {
			b = v
		}
	}
	return (a - 1) * (b - 1)
}
'''

SOLUTIONS["1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts"] = r'''// LeetCode 1465 - Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
// https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

import "sort"

func maxArea(h int, w int, horizontalCuts []int, verticalCuts []int) int {
	hs := append([]int{0, h}, horizontalCuts...)
	vs := append([]int{0, w}, verticalCuts...)
	sort.Ints(hs)
	sort.Ints(vs)
	maxGap := func(arr []int) int {
		best := 0
		for i := 1; i < len(arr); i++ {
			if arr[i]-arr[i-1] > best {
				best = arr[i] - arr[i-1]
			}
		}
		return best
	}
	return maxGap(hs) * maxGap(vs) % 1000000007
}
'''

SOLUTIONS["1466_reorder_routes_to_make_all_paths_lead_to_the_city_zero"] = r'''// LeetCode 1466 - Reorder Routes to Make All Paths Lead to the City Zero
// https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

func minReorder(n int, connections [][]int) int {
	type edge struct{ nei, cost int }
	graph := make([][]edge, n)
	for _, c := range connections {
		a, b := c[0], c[1]
		graph[a] = append(graph[a], edge{b, 1})
		graph[b] = append(graph[b], edge{a, 0})
	}
	ans := 0
	stack := []int{0}
	seen := map[int]bool{0: true}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for _, e := range graph[node] {
			if !seen[e.nei] {
				seen[e.nei] = true
				stack = append(stack, e.nei)
				ans += e.cost
			}
		}
	}
	return ans
}
'''

SOLUTIONS["1467_probability_of_a_two_boxes_having_the_same_number_of_distinct_balls"] = r'''// LeetCode 1467 - Probability of a Two Boxes Having the Same Number of Distinct Balls
// https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/

func getProbability(balls []int) float64 {
	half := 0
	for _, b := range balls {
		half += b
	}
	half /= 2
	comb := func(n, k int) float64 {
		if k < 0 || k > n {
			return 0
		}
		res := 1.0
		for i := 0; i < k; i++ {
			res *= float64(n - i)
			res /= float64(i + 1)
		}
		return res
	}
	var good, total float64
	var dfs func(i, left, dl int, ways float64)
	dfs = func(i, left, dl int, ways float64) {
		if i == len(balls) {
			if left == half {
				total += ways
				if dl == 0 {
					good += ways
				}
			}
			return
		}
		for x := 0; x <= balls[i]; x++ {
			if left+x <= half {
				delta := 0
				if x > 0 {
					delta++
				}
				if x < balls[i] {
					delta--
				}
				dfs(i+1, left+x, dl+delta, ways*comb(balls[i], x))
			}
		}
	}
	dfs(0, 0, 0, 1)
	return good / total
}
'''

SOLUTIONS["1469_find_all_the_lonely_nodes"] = r'''// LeetCode 1469 - Find All The Lonely Nodes
// https://leetcode.com/problems/find-all-the-lonely-nodes/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getLonelyNodes(root *TreeNode) []int {
	var ans []int
	var dfs func(*TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}
		if (node.Left == nil) != (node.Right == nil) {
			if node.Left != nil {
				ans = append(ans, node.Left.Val)
			} else {
				ans = append(ans, node.Right.Val)
			}
		}
		dfs(node.Left)
		dfs(node.Right)
	}
	dfs(root)
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
