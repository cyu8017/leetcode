#!/usr/bin/env python3
"""Port Go solutions 1389-1428 (batch C)."""
import os

ROOT = r"c:\Users\Charlie Yu\Documents\leetcode"

SOLUTIONS = {}

SOLUTIONS["1389_create_target_array_in_the_given_order"] = r'''// LeetCode 1389 - Create Target Array in the Given Order
// https://leetcode.com/problems/create-target-array-in-the-given-order/

func createTargetArray(nums []int, index []int) []int {
	out := []int{}
	for i, x := range nums {
		idx := index[i]
		out = append(out, 0)
		copy(out[idx+1:], out[idx:])
		out[idx] = x
	}
	return out
}
'''

SOLUTIONS["1390_four_divisors"] = r'''// LeetCode 1390 - Four Divisors
// https://leetcode.com/problems/four-divisors/

func sumFourDivisors(nums []int) int {
	ans := 0
	for _, x := range nums {
		ds := map[int]bool{}
		for d := 1; d*d <= x; d++ {
			if x%d == 0 {
				ds[d] = true
				ds[x/d] = true
			}
			if len(ds) > 4 {
				break
			}
		}
		if len(ds) == 4 {
			for v := range ds {
				ans += v
			}
		}
	}
	return ans
}
'''

SOLUTIONS["1391_check_if_there_is_a_valid_path_in_a_grid"] = r'''// LeetCode 1391 - Check if There is a Valid Path in a Grid
// https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

func hasValidPath(grid [][]int) bool {
	dirs := map[int][][2]int{
		1: {{0, -1}, {0, 1}},
		2: {{-1, 0}, {1, 0}},
		3: {{0, -1}, {1, 0}},
		4: {{0, 1}, {1, 0}},
		5: {{0, -1}, {-1, 0}},
		6: {{0, 1}, {-1, 0}},
	}
	m, n := len(grid), len(grid[0])
	seen := map[[2]int]bool{{0, 0}: true}
	st := [][2]int{{0, 0}}
	for len(st) > 0 {
		cur := st[len(st)-1]
		st = st[:len(st)-1]
		r, c := cur[0], cur[1]
		if r == m-1 && c == n-1 {
			return true
		}
		for _, d := range dirs[grid[r][c]] {
			x, y := r+d[0], c+d[1]
			if x >= 0 && x < m && y >= 0 && y < n && !seen[[2]int{x, y}] {
				ok := false
				for _, back := range dirs[grid[x][y]] {
					if back[0] == -d[0] && back[1] == -d[1] {
						ok = true
						break
					}
				}
				if ok {
					seen[[2]int{x, y}] = true
					st = append(st, [2]int{x, y})
				}
			}
		}
	}
	return false
}
'''

SOLUTIONS["1392_longest_happy_prefix"] = r'''// LeetCode 1392 - Longest Happy Prefix
// https://leetcode.com/problems/longest-happy-prefix/

func longestPrefix(s string) string {
	if len(s) == 0 {
		return ""
	}
	pi := make([]int, len(s))
	for i := 1; i < len(s); i++ {
		j := pi[i-1]
		for j > 0 && s[i] != s[j] {
			j = pi[j-1]
		}
		if s[i] == s[j] {
			j++
		}
		pi[i] = j
	}
	return s[:pi[len(s)-1]]
}
'''

SOLUTIONS["1394_find_lucky_integer_in_an_array"] = r'''// LeetCode 1394 - Find Lucky Integer in an Array
// https://leetcode.com/problems/find-lucky-integer-in-an-array/

func findLucky(arr []int) int {
	count := map[int]int{}
	for _, x := range arr {
		count[x]++
	}
	ans := -1
	for x, c := range count {
		if x == c && x > ans {
			ans = x
		}
	}
	return ans
}
'''

SOLUTIONS["1395_count_number_of_teams"] = r'''// LeetCode 1395 - Count Number of Teams
// https://leetcode.com/problems/count-number-of-teams/

func numTeams(rating []int) int {
	ans := 0
	for j, x := range rating {
		ll, lg, rl, rg := 0, 0, 0, 0
		for i := 0; i < j; i++ {
			if rating[i] < x {
				ll++
			} else {
				lg++
			}
		}
		for i := j + 1; i < len(rating); i++ {
			if rating[i] > x {
				rg++
			} else {
				rl++
			}
		}
		ans += ll*rg + lg*rl
	}
	return ans
}
'''

SOLUTIONS["1396_design_underground_system"] = r'''// LeetCode 1396 - Design Underground System
// https://leetcode.com/problems/design-underground-system/

type UndergroundSystem struct {
	ins   map[int]checkIn
	stats map[[2]string][2]int
}

type checkIn struct {
	station string
	t       int
}

func Constructor() UndergroundSystem {
	return UndergroundSystem{ins: map[int]checkIn{}, stats: map[[2]string][2]int{}}
}

func (this *UndergroundSystem) CheckIn(id int, stationName string, t int) {
	this.ins[id] = checkIn{stationName, t}
}

func (this *UndergroundSystem) CheckOut(id int, stationName string, t int) {
	in := this.ins[id]
	delete(this.ins, id)
	key := [2]string{in.station, stationName}
	st := this.stats[key]
	this.stats[key] = [2]int{st[0] + t - in.t, st[1] + 1}
}

func (this *UndergroundSystem) GetAverageTime(startStation string, endStation string) float64 {
	st := this.stats[[2]string{startStation, endStation}]
	return float64(st[0]) / float64(st[1])
}
'''

SOLUTIONS["1397_find_all_good_strings"] = r'''// LeetCode 1397 - Find All Good Strings
// https://leetcode.com/problems/find-all-good-strings/

func findGoodStrings(n int, s1 string, s2 string, evil string) int {
	const mod = 1000000007
	m := len(evil)
	pi := make([]int, m)
	for i := 1; i < m; i++ {
		j := pi[i-1]
		for j > 0 && evil[i] != evil[j] {
			j = pi[j-1]
		}
		if evil[i] == evil[j] {
			j++
		}
		pi[i] = j
	}
	trans := make([][26]int, m)
	for j := 0; j < m; j++ {
		for x := 0; x < 26; x++ {
			c := byte('a' + x)
			k := j
			for k > 0 && evil[k] != c {
				k = pi[k-1]
			}
			if evil[k] == c {
				k++
			}
			trans[j][x] = k
		}
	}
	type key struct {
		i, j    int
		lo, hi  bool
	}
	memo := map[key]int{}
	var dp func(i, j int, lo, hi bool) int
	dp = func(i, j int, lo, hi bool) int {
		if j == m {
			return 0
		}
		if i == n {
			return 1
		}
		k := key{i, j, lo, hi}
		if v, ok := memo[k]; ok {
			return v
		}
		a, b := 0, 25
		if lo {
			a = int(s1[i] - 'a')
		}
		if hi {
			b = int(s2[i] - 'a')
		}
		ans := 0
		for x := a; x <= b; x++ {
			ans = (ans + dp(i+1, trans[j][x], lo && x == a, hi && x == b)) % mod
		}
		memo[k] = ans
		return ans
	}
	return dp(0, 0, true, true)
}
'''

SOLUTIONS["1399_count_largest_group"] = r'''// LeetCode 1399 - Count Largest Group
// https://leetcode.com/problems/count-largest-group/

func countLargestGroup(n int) int {
	digitSum := func(x int) int {
		s := 0
		for x > 0 {
			s += x % 10
			x /= 10
		}
		return s
	}
	c := map[int]int{}
	mx := 0
	for x := 1; x <= n; x++ {
		ds := digitSum(x)
		c[ds]++
		if c[ds] > mx {
			mx = c[ds]
		}
	}
	ans := 0
	for _, v := range c {
		if v == mx {
			ans++
		}
	}
	return ans
}
'''

SOLUTIONS["1400_construct_k_palindrome_strings"] = r'''// LeetCode 1400 - Construct K Palindrome Strings
// https://leetcode.com/problems/construct-k-palindrome-strings/

func canConstruct(s string, k int) bool {
	if k > len(s) {
		return false
	}
	count := [26]int{}
	for i := 0; i < len(s); i++ {
		count[s[i]-'a']++
	}
	odd := 0
	for _, v := range count {
		odd += v % 2
	}
	return odd <= k
}
'''

SOLUTIONS["1401_circle_and_rectangle_overlapping"] = r'''// LeetCode 1401 - Circle and Rectangle Overlapping
// https://leetcode.com/problems/circle-and-rectangle-overlapping/

func checkOverlap(radius int, xCenter int, yCenter int, x1 int, y1 int, x2 int, y2 int) bool {
	x := xCenter
	if x < x1 {
		x = x1
	} else if x > x2 {
		x = x2
	}
	y := yCenter
	if y < y1 {
		y = y1
	} else if y > y2 {
		y = y2
	}
	dx, dy := x-xCenter, y-yCenter
	return dx*dx+dy*dy <= radius*radius
}
'''

SOLUTIONS["1402_reducing_dishes"] = r'''// LeetCode 1402 - Reducing Dishes
// https://leetcode.com/problems/reducing-dishes/

import "sort"

func maxSatisfaction(satisfaction []int) int {
	sort.Sort(sort.Reverse(sort.IntSlice(satisfaction)))
	total, answer := 0, 0
	for _, value := range satisfaction {
		if total+value <= 0 {
			break
		}
		total += value
		answer += total
	}
	return answer
}
'''

SOLUTIONS["1403_minimum_subsequence_in_non_increasing_order"] = r'''// LeetCode 1403 - Minimum Subsequence in Non-Increasing Order
// https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

import "sort"

func minSubsequence(nums []int) []int {
	sort.Sort(sort.Reverse(sort.IntSlice(nums)))
	total := 0
	for _, v := range nums {
		total += v
	}
	answer := []int{}
	chosen := 0
	for _, value := range nums {
		answer = append(answer, value)
		chosen += value
		if chosen > total-chosen {
			return answer
		}
	}
	return answer
}
'''

SOLUTIONS["1404_number_of_steps_to_reduce_a_number_in_binary_representation_to_one"] = r'''// LeetCode 1404 - Number of Steps to Reduce a Number in Binary Representation to One
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

func numSteps(s string) int {
	steps, carry := 0, 0
	for i := len(s) - 1; i >= 1; i-- {
		value := int(s[i]-'0') + carry
		if value == 1 {
			steps += 2
			carry = 1
		} else {
			steps++
		}
	}
	return steps + carry
}
'''

SOLUTIONS["1405_longest_happy_string"] = r'''// LeetCode 1405 - Longest Happy String
// https://leetcode.com/problems/longest-happy-string/

import "container/heap"

type item struct {
	count int
	char  byte
}
type maxHeap []item

func (h maxHeap) Len() int            { return len(h) }
func (h maxHeap) Less(i, j int) bool  { return h[i].count > h[j].count }
func (h maxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *maxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func longestDiverseString(a int, b int, c int) string {
	h := &maxHeap{}
	heap.Init(h)
	for _, p := range []item{{a, 'a'}, {b, 'b'}, {c, 'c'}} {
		if p.count > 0 {
			heap.Push(h, p)
		}
	}
	answer := []byte{}
	for h.Len() > 0 {
		cur := heap.Pop(h).(item)
		n := len(answer)
		if n >= 2 && answer[n-1] == cur.char && answer[n-2] == cur.char {
			if h.Len() == 0 {
				break
			}
			cur2 := heap.Pop(h).(item)
			answer = append(answer, cur2.char)
			if cur2.count-1 > 0 {
				heap.Push(h, item{cur2.count - 1, cur2.char})
			}
			heap.Push(h, cur)
		} else {
			answer = append(answer, cur.char)
			if cur.count-1 > 0 {
				heap.Push(h, item{cur.count - 1, cur.char})
			}
		}
	}
	return string(answer)
}
'''

SOLUTIONS["1406_stone_game_iii"] = r'''// LeetCode 1406 - Stone Game III
// https://leetcode.com/problems/stone-game-iii/

func stoneGameIII(stoneValue []int) string {
	n := len(stoneValue)
	dp := make([]int, n+1)
	const negInf = int(-1e18)
	for i := n - 1; i >= 0; i-- {
		take := 0
		dp[i] = negInf
		for j := i; j < i+3 && j < n; j++ {
			take += stoneValue[j]
			if take-dp[j+1] > dp[i] {
				dp[i] = take - dp[j+1]
			}
		}
	}
	if dp[0] > 0 {
		return "Alice"
	}
	if dp[0] < 0 {
		return "Bob"
	}
	return "Tie"
}
'''

SOLUTIONS["1408_string_matching_in_an_array"] = r'''// LeetCode 1408 - String Matching in an Array
// https://leetcode.com/problems/string-matching-in-an-array/

import "strings"

func stringMatching(words []string) []string {
	var answer []string
	for i, word := range words {
		for j, other := range words {
			if i != j && strings.Contains(other, word) {
				answer = append(answer, word)
				break
			}
		}
	}
	return answer
}
'''

SOLUTIONS["1409_queries_on_a_permutation_with_key"] = r'''// LeetCode 1409 - Queries on a Permutation With Key
// https://leetcode.com/problems/queries-on-a-permutation-with-key/

func processQueries(queries []int, m int) []int {
	values := make([]int, m)
	for i := 0; i < m; i++ {
		values[i] = i + 1
	}
	answer := make([]int, len(queries))
	for qi, query := range queries {
		index := 0
		for i, v := range values {
			if v == query {
				index = i
				break
			}
		}
		answer[qi] = index
		val := values[index]
		copy(values[1:index+1], values[:index])
		values[0] = val
	}
	return answer
}
'''

SOLUTIONS["1410_html_entity_parser"] = r'''// LeetCode 1410 - HTML Entity Parser
// https://leetcode.com/problems/html-entity-parser/

import "strings"

func entityParser(text string) string {
	entities := [][2]string{
		{"&quot;", `"`},
		{"&apos;", "'"},
		{"&gt;", ">"},
		{"&lt;", "<"},
		{"&frasl;", "/"},
		{"&amp;", "&"},
	}
	// Replace &amp; last
	for _, e := range entities[:5] {
		text = strings.ReplaceAll(text, e[0], e[1])
	}
	text = strings.ReplaceAll(text, "&amp;", "&")
	return text
}
'''

SOLUTIONS["1411_number_of_ways_to_paint_n_3_grid"] = r'''// LeetCode 1411 - Number of Ways to Paint N × 3 Grid
// https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

func numOfWays(n int) int {
	const mod = 1000000007
	aba, abc := 6, 6
	for i := 1; i < n; i++ {
		aba, abc = (3*aba+2*abc)%mod, (2*aba+2*abc)%mod
	}
	return (aba + abc) % mod
}
'''

SOLUTIONS["1413_minimum_value_to_get_positive_step_by_step_sum"] = r'''// LeetCode 1413 - Minimum Value to Get Positive Step by Step Sum
// https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

func minStartValue(nums []int) int {
	prefix, lowest := 0, 0
	for _, value := range nums {
		prefix += value
		if prefix < lowest {
			lowest = prefix
		}
	}
	return 1 - lowest
}
'''

SOLUTIONS["1414_find_the_minimum_number_of_fibonacci_numbers_whose_sum_is_k"] = r'''// LeetCode 1414 - Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
// https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

func findMinFibonacciNumbers(k int) int {
	fib := []int{1, 1}
	for fib[len(fib)-1] < k {
		fib = append(fib, fib[len(fib)-1]+fib[len(fib)-2])
	}
	answer := 0
	for i := len(fib) - 1; i >= 0; i-- {
		if fib[i] <= k {
			k -= fib[i]
			answer++
		}
	}
	return answer
}
'''

SOLUTIONS["1415_the_k_th_lexicographical_string_of_all_happy_strings_of_length_n"] = r'''// LeetCode 1415 - The k-th Lexicographical String of All Happy Strings of Length n
// https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

func getHappyString(n int, k int) string {
	var answer []string
	var build func(path string)
	build = func(path string) {
		if len(path) == n {
			answer = append(answer, path)
			return
		}
		for _, char := range "abc" {
			if len(path) == 0 || path[len(path)-1] != byte(char) {
				build(path + string(char))
			}
		}
	}
	build("")
	if k <= len(answer) {
		return answer[k-1]
	}
	return ""
}
'''

SOLUTIONS["1416_restore_the_array"] = r'''// LeetCode 1416 - Restore The Array
// https://leetcode.com/problems/restore-the-array/

func numberOfArrays(s string, k int) int {
	const mod = 1000000007
	n := len(s)
	dp := make([]int, n+1)
	dp[n] = 1
	for i := n - 1; i >= 0; i-- {
		if s[i] == '0' {
			continue
		}
		value := 0
		for j := i; j < n; j++ {
			value = value*10 + int(s[j]-'0')
			if value > k {
				break
			}
			dp[i] = (dp[i] + dp[j+1]) % mod
		}
	}
	return dp[0]
}
'''

SOLUTIONS["1417_reformat_the_string"] = r'''// LeetCode 1417 - Reformat The String
// https://leetcode.com/problems/reformat-the-string/

func reformat(s string) string {
	var letters, digits []byte
	for i := 0; i < len(s); i++ {
		if s[i] >= '0' && s[i] <= '9' {
			digits = append(digits, s[i])
		} else {
			letters = append(letters, s[i])
		}
	}
	diff := len(letters) - len(digits)
	if diff < 0 {
		diff = -diff
	}
	if diff > 1 {
		return ""
	}
	if len(digits) > len(letters) {
		letters, digits = digits, letters
	}
	answer := make([]byte, 0, len(s))
	for i, char := range letters {
		answer = append(answer, char)
		if i < len(digits) {
			answer = append(answer, digits[i])
		}
	}
	return string(answer)
}
'''

SOLUTIONS["1418_display_table_of_food_orders_in_a_restaurant"] = r'''// LeetCode 1418 - Display Table of Food Orders in a Restaurant
// https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

import (
	"sort"
	"strconv"
)

func displayTable(orders [][]string) [][]string {
	foodSet := map[string]bool{}
	tableSet := map[int]bool{}
	counts := map[[2]interface{}]int{}
	type key struct {
		table int
		food  string
	}
	counts2 := map[key]int{}
	for _, o := range orders {
		table, _ := strconv.Atoi(o[1])
		food := o[2]
		foodSet[food] = true
		tableSet[table] = true
		counts2[key{table, food}]++
	}
	_ = counts
	foods := make([]string, 0, len(foodSet))
	for f := range foodSet {
		foods = append(foods, f)
	}
	sort.Strings(foods)
	tables := make([]int, 0, len(tableSet))
	for t := range tableSet {
		tables = append(tables, t)
	}
	sort.Ints(tables)
	result := [][]string{append([]string{"Table"}, foods...)}
	for _, table := range tables {
		row := []string{strconv.Itoa(table)}
		for _, food := range foods {
			row = append(row, strconv.Itoa(counts2[key{table, food}]))
		}
		result = append(result, row)
	}
	return result
}
'''

SOLUTIONS["1419_minimum_number_of_frogs_croaking"] = r'''// LeetCode 1419 - Minimum Number of Frogs Croaking
// https://leetcode.com/problems/minimum-number-of-frogs-croaking/

func minNumberOfFrogs(croakOfFrogs string) int {
	order := map[byte]int{'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
	counts := [5]int{}
	active, answer := 0, 0
	for i := 0; i < len(croakOfFrogs); i++ {
		idx, ok := order[croakOfFrogs[i]]
		if !ok || (idx > 0 && counts[idx-1] == 0) {
			return -1
		}
		if idx > 0 {
			counts[idx-1]--
		}
		counts[idx]++
		if idx == 0 {
			active++
			if active > answer {
				answer = active
			}
		} else if idx == 4 {
			counts[4]--
			active--
		}
	}
	if active == 0 {
		return answer
	}
	return -1
}
'''

SOLUTIONS["1420_build_array_where_you_can_find_the_maximum_exactly_k_comparisons"] = r'''// LeetCode 1420 - Build Array Where You Can Find The Maximum Exactly K Comparisons
// https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/

func numOfArrays(n int, m int, k int) int {
	const mod = 1000000007
	dp := make([][]int, k+1)
	for i := range dp {
		dp[i] = make([]int, m+1)
	}
	for maximum := 1; maximum <= m; maximum++ {
		dp[1][maximum] = 1
	}
	for length := 1; length < n; length++ {
		nxt := make([][]int, k+1)
		for i := range nxt {
			nxt[i] = make([]int, m+1)
		}
		for cost := 1; cost <= k; cost++ {
			prefix := 0
			for maximum := 1; maximum <= m; maximum++ {
				prefix = (prefix + dp[cost-1][maximum-1]) % mod
				nxt[cost][maximum] = (maximum*dp[cost][maximum] + prefix) % mod
			}
		}
		dp = nxt
	}
	ans := 0
	for _, v := range dp[k] {
		ans = (ans + v) % mod
	}
	return ans
}
'''

SOLUTIONS["1422_maximum_score_after_splitting_a_string"] = r'''// LeetCode 1422 - Maximum Score After Splitting a String
// https://leetcode.com/problems/maximum-score-after-splitting-a-string/

func maxScore(s string) int {
	ones := 0
	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			ones++
		}
	}
	leftZeros, answer := 0, 0
	for i := 0; i < len(s)-1; i++ {
		if s[i] == '0' {
			leftZeros++
		} else {
			ones--
		}
		if leftZeros+ones > answer {
			answer = leftZeros + ones
		}
	}
	return answer
}
'''

SOLUTIONS["1423_maximum_points_you_can_obtain_from_cards"] = r'''// LeetCode 1423 - Maximum Points You Can Obtain from Cards
// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

func maxScore(cardPoints []int, k int) int {
	total := 0
	for _, v := range cardPoints {
		total += v
	}
	if k == len(cardPoints) {
		return total
	}
	window := len(cardPoints) - k
	current := 0
	for i := 0; i < window; i++ {
		current += cardPoints[i]
	}
	smallest := current
	for i := window; i < len(cardPoints); i++ {
		current += cardPoints[i] - cardPoints[i-window]
		if current < smallest {
			smallest = current
		}
	}
	return total - smallest
}
'''

SOLUTIONS["1424_diagonal_traverse_ii"] = r'''// LeetCode 1424 - Diagonal Traverse II
// https://leetcode.com/problems/diagonal-traverse-ii/

import "sort"

func findDiagonalOrder(nums [][]int) []int {
	diagonals := map[int][]int{}
	keys := []int{}
	for row, values := range nums {
		for col, value := range values {
			if _, ok := diagonals[row+col]; !ok {
				keys = append(keys, row+col)
			}
			diagonals[row+col] = append(diagonals[row+col], value)
		}
	}
	sort.Ints(keys)
	var answer []int
	for _, key := range keys {
		vals := diagonals[key]
		for i := len(vals) - 1; i >= 0; i-- {
			answer = append(answer, vals[i])
		}
	}
	return answer
}
'''

SOLUTIONS["1425_constrained_subsequence_sum"] = r'''// LeetCode 1425 - Constrained Subsequence Sum
// https://leetcode.com/problems/constrained-subsequence-sum/

func constrainedSubsetSum(nums []int, k int) int {
	best := append([]int(nil), nums...)
	queue := []int{}
	for i, value := range nums {
		for len(queue) > 0 && queue[0] < i-k {
			queue = queue[1:]
		}
		if len(queue) > 0 && best[queue[0]] > 0 {
			best[i] = value + best[queue[0]]
		} else {
			best[i] = value
		}
		for len(queue) > 0 && best[queue[len(queue)-1]] <= best[i] {
			queue = queue[:len(queue)-1]
		}
		queue = append(queue, i)
	}
	ans := best[0]
	for _, v := range best {
		if v > ans {
			ans = v
		}
	}
	return ans
}
'''

SOLUTIONS["1426_counting_elements"] = r'''// LeetCode 1426 - Counting Elements
// https://leetcode.com/problems/counting-elements/

func countElements(arr []int) int {
	values := map[int]bool{}
	for _, v := range arr {
		values[v] = true
	}
	ans := 0
	for _, v := range arr {
		if values[v+1] {
			ans++
		}
	}
	return ans
}
'''

SOLUTIONS["1427_perform_string_shifts"] = r'''// LeetCode 1427 - Perform String Shifts
// https://leetcode.com/problems/perform-string-shifts/

func stringShift(s string, shift [][]int) string {
	offset := 0
	for _, sh := range shift {
		if sh[0] == 1 {
			offset += sh[1]
		} else {
			offset -= sh[1]
		}
	}
	n := len(s)
	offset %= n
	if offset < 0 {
		offset += n
	}
	if offset == 0 {
		return s
	}
	return s[n-offset:] + s[:n-offset]
}
'''

SOLUTIONS["1428_leftmost_column_with_at_least_a_one"] = r'''// LeetCode 1428 - Leftmost Column with at Least a One
// https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

type BinaryMatrix interface {
	Get(row, col int) int
	Dimensions() []int
}

func leftMostColumnWithOne(binaryMatrix BinaryMatrix) int {
	dims := binaryMatrix.Dimensions()
	rows, cols := dims[0], dims[1]
	row, col, answer := 0, cols-1, -1
	for row < rows && col >= 0 {
		if binaryMatrix.Get(row, col) == 1 {
			answer = col
			col--
		} else {
			row++
		}
	}
	return answer
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
