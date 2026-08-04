#!/usr/bin/env python3
"""Port Go solutions 1324-1359 range (batch A)."""
import os

ROOT = r"c:\Users\Charlie Yu\Documents\leetcode"

SOLUTIONS = {}

SOLUTIONS["1324_print_words_vertically"] = r'''// LeetCode 1324 - Print Words Vertically
// https://leetcode.com/problems/print-words-vertically/

import "strings"

func printVertically(s string) []string {
	words := strings.Fields(s)
	maxLen := 0
	for _, w := range words {
		if len(w) > maxLen {
			maxLen = len(w)
		}
	}
	answer := make([]string, maxLen)
	for i := 0; i < maxLen; i++ {
		var b strings.Builder
		for _, w := range words {
			if i < len(w) {
				b.WriteByte(w[i])
			} else {
				b.WriteByte(' ')
			}
		}
		answer[i] = strings.TrimRight(b.String(), " ")
	}
	return answer
}
'''

SOLUTIONS["1325_delete_leaves_with_a_given_value"] = r'''// LeetCode 1325 - Delete Leaves With a Given Value
// https://leetcode.com/problems/delete-leaves-with-a-given-value/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func removeLeafNodes(root *TreeNode, target int) *TreeNode {
	if root == nil {
		return nil
	}
	root.Left = removeLeafNodes(root.Left, target)
	root.Right = removeLeafNodes(root.Right, target)
	if root.Left == nil && root.Right == nil && root.Val == target {
		return nil
	}
	return root
}
'''

SOLUTIONS["1326_minimum_number_of_taps_to_open_to_water_a_garden"] = r'''// LeetCode 1326 - Minimum Number of Taps to Open to Water a Garden
// https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

func minTaps(n int, ranges []int) int {
	farthest := make([]int, n+1)
	for center, radius := range ranges {
		left := center - radius
		if left < 0 {
			left = 0
		}
		right := center + radius
		if right > n {
			right = n
		}
		if right > farthest[left] {
			farthest[left] = right
		}
	}
	taps, end, reach := 0, 0, 0
	for position := 0; position < n; position++ {
		if farthest[position] > reach {
			reach = farthest[position]
		}
		if position == end {
			if reach <= position {
				return -1
			}
			taps++
			end = reach
		}
	}
	return taps
}
'''

SOLUTIONS["1328_break_a_palindrome"] = r'''// LeetCode 1328 - Break a Palindrome
// https://leetcode.com/problems/break-a-palindrome/

func breakPalindrome(palindrome string) string {
	if len(palindrome) == 1 {
		return ""
	}
	chars := []byte(palindrome)
	for i := 0; i < len(chars)/2; i++ {
		if chars[i] != 'a' {
			chars[i] = 'a'
			return string(chars)
		}
	}
	chars[len(chars)-1] = 'b'
	return string(chars)
}
'''

SOLUTIONS["1329_sort_the_matrix_diagonally"] = r'''// LeetCode 1329 - Sort the Matrix Diagonally
// https://leetcode.com/problems/sort-the-matrix-diagonally/

import "sort"

func diagonalSort(mat [][]int) [][]int {
	diagonals := map[int][]int{}
	for r, row := range mat {
		for c, value := range row {
			diagonals[r-c] = append(diagonals[r-c], value)
		}
	}
	for k := range diagonals {
		sort.Sort(sort.Reverse(sort.IntSlice(diagonals[k])))
	}
	for r, row := range mat {
		for c := range row {
			vals := diagonals[r-c]
			mat[r][c] = vals[len(vals)-1]
			diagonals[r-c] = vals[:len(vals)-1]
		}
	}
	return mat
}
'''

SOLUTIONS["1330_reverse_subarray_to_maximize_array_value"] = r'''// LeetCode 1330 - Reverse Subarray To Maximize Array Value
// https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/

func maxValueAfterReverse(nums []int) int {
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	base := 0
	for i := 0; i+1 < len(nums); i++ {
		base += abs(nums[i] - nums[i+1])
	}
	gain := 0
	low, high := int(1e9), int(-1e9)
	for i := 0; i+1 < len(nums); i++ {
		a, b := nums[i], nums[i+1]
		g1 := abs(nums[0]-b) - abs(a-b)
		g2 := abs(nums[len(nums)-1]-a) - abs(a-b)
		if g1 > gain {
			gain = g1
		}
		if g2 > gain {
			gain = g2
		}
		mx, mn := a, b
		if b > a {
			mx, mn = b, a
		}
		if mx < low {
			low = mx
		}
		if mn > high {
			high = mn
		}
	}
	alt := 2 * (high - low)
	if alt > gain {
		gain = alt
	}
	return base + gain
}
'''

SOLUTIONS["1331_rank_transform_of_an_array"] = r'''// LeetCode 1331 - Rank Transform of an Array
// https://leetcode.com/problems/rank-transform-of-an-array/

import "sort"

func arrayRankTransform(arr []int) []int {
	uniq := append([]int(nil), arr...)
	sort.Ints(uniq)
	rank := map[int]int{}
	r := 1
	for _, v := range uniq {
		if _, ok := rank[v]; !ok {
			rank[v] = r
			r++
		}
	}
	answer := make([]int, len(arr))
	for i, v := range arr {
		answer[i] = rank[v]
	}
	return answer
}
'''

SOLUTIONS["1332_remove_palindromic_subsequences"] = r'''// LeetCode 1332 - Remove Palindromic Subsequences
// https://leetcode.com/problems/remove-palindromic-subsequences/

func removePalindromeSub(s string) int {
	if len(s) == 0 {
		return 0
	}
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			return 2
		}
	}
	return 1
}
'''

SOLUTIONS["1333_filter_restaurants_by_vegan_friendly_price_and_distance"] = r'''// LeetCode 1333 - Filter Restaurants by Vegan-Friendly, Price and Distance
// https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

import "sort"

func filterRestaurants(restaurants [][]int, veganFriendly int, maxPrice int, maxDistance int) []int {
	var valid [][]int
	for _, row := range restaurants {
		if (veganFriendly == 0 || row[2] == 1) && row[3] <= maxPrice && row[4] <= maxDistance {
			valid = append(valid, row)
		}
	}
	sort.Slice(valid, func(i, j int) bool {
		if valid[i][1] != valid[j][1] {
			return valid[i][1] > valid[j][1]
		}
		return valid[i][0] > valid[j][0]
	})
	answer := make([]int, len(valid))
	for i, row := range valid {
		answer[i] = row[0]
	}
	return answer
}
'''

SOLUTIONS["1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance"] = r'''// LeetCode 1334 - Find the City With the Smallest Number of Neighbors at a Threshold Distance
// https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

func findTheCity(n int, edges [][]int, distanceThreshold int) int {
	const inf = int64(1e15)
	dist := make([][]int64, n)
	for i := range dist {
		dist[i] = make([]int64, n)
		for j := range dist[i] {
			dist[i][j] = inf
		}
		dist[i][i] = 0
	}
	for _, e := range edges {
		a, b, w := e[0], e[1], int64(e[2])
		dist[a][b], dist[b][a] = w, w
	}
	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if dist[i][k]+dist[k][j] < dist[i][j] {
					dist[i][j] = dist[i][k] + dist[k][j]
				}
			}
		}
	}
	bestCity, bestCount := -1, n+1
	for city := 0; city < n; city++ {
		count := 0
		for _, d := range dist[city] {
			if d <= int64(distanceThreshold) {
				count++
			}
		}
		if count <= bestCount {
			bestCount = count
			bestCity = city
		}
	}
	return bestCity
}
'''

SOLUTIONS["1335_minimum_difficulty_of_a_job_schedule"] = r'''// LeetCode 1335 - Minimum Difficulty of a Job Schedule
// https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

func minDifficulty(jobDifficulty []int, d int) int {
	n := len(jobDifficulty)
	if n < d {
		return -1
	}
	const inf = int(1e9)
	dp := make([]int, n)
	hardest := 0
	for i, value := range jobDifficulty {
		if value > hardest {
			hardest = value
		}
		dp[i] = hardest
	}
	for day := 1; day < d; day++ {
		nxt := make([]int, n)
		for i := range nxt {
			nxt[i] = inf
		}
		for end := day; end < n; end++ {
			hardest = 0
			for start := end; start >= day; start-- {
				if jobDifficulty[start] > hardest {
					hardest = jobDifficulty[start]
				}
				if dp[start-1]+hardest < nxt[end] {
					nxt[end] = dp[start-1] + hardest
				}
			}
		}
		dp = nxt
	}
	return dp[n-1]
}
'''

SOLUTIONS["1337_the_k_weakest_rows_in_a_matrix"] = r'''// LeetCode 1337 - The K Weakest Rows in a Matrix
// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

import "sort"

func kWeakestRows(mat [][]int, k int) []int {
	type pair struct{ soldiers, idx int }
	rows := make([]pair, len(mat))
	for i, row := range mat {
		s := 0
		for _, v := range row {
			s += v
		}
		rows[i] = pair{s, i}
	}
	sort.Slice(rows, func(i, j int) bool {
		if rows[i].soldiers != rows[j].soldiers {
			return rows[i].soldiers < rows[j].soldiers
		}
		return rows[i].idx < rows[j].idx
	})
	answer := make([]int, k)
	for i := 0; i < k; i++ {
		answer[i] = rows[i].idx
	}
	return answer
}
'''

SOLUTIONS["1338_reduce_array_size_to_the_half"] = r'''// LeetCode 1338 - Reduce Array Size to The Half
// https://leetcode.com/problems/reduce-array-size-to-the-half/

import "sort"

func minSetSize(arr []int) int {
	counts := map[int]int{}
	for _, v := range arr {
		counts[v]++
	}
	freqs := make([]int, 0, len(counts))
	for _, f := range counts {
		freqs = append(freqs, f)
	}
	sort.Sort(sort.Reverse(sort.IntSlice(freqs)))
	removed := 0
	for i, frequency := range freqs {
		removed += frequency
		if removed*2 >= len(arr) {
			return i + 1
		}
	}
	return 0
}
'''

SOLUTIONS["1339_maximum_product_of_splitted_binary_tree"] = r'''// LeetCode 1339 - Maximum Product of Splitted Binary Tree
// https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxProduct(root *TreeNode) int {
	var sums []int64
	var total func(*TreeNode) int64
	total = func(node *TreeNode) int64 {
		if node == nil {
			return 0
		}
		value := int64(node.Val) + total(node.Left) + total(node.Right)
		sums = append(sums, value)
		return value
	}
	whole := total(root)
	var best int64
	for _, value := range sums {
		prod := value * (whole - value)
		if prod > best {
			best = prod
		}
	}
	return int(best % 1000000007)
}
'''

SOLUTIONS["1340_jump_game_v"] = r'''// LeetCode 1340 - Jump Game V
// https://leetcode.com/problems/jump-game-v/

import "sort"

func maxJumps(arr []int, d int) int {
	n := len(arr)
	dp := make([]int, n)
	for i := range dp {
		dp[i] = 1
	}
	order := make([]int, n)
	for i := range order {
		order[i] = i
	}
	sort.Slice(order, func(i, j int) bool { return arr[order[i]] < arr[order[j]] })
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	for _, i := range order {
		for _, step := range []int{-1, 1} {
			j := i + step
			for j >= 0 && j < n && abs(j-i) <= d && arr[j] < arr[i] {
				if 1+dp[j] > dp[i] {
					dp[i] = 1 + dp[j]
				}
				j += step
			}
		}
	}
	best := 0
	for _, v := range dp {
		if v > best {
			best = v
		}
	}
	return best
}
'''

SOLUTIONS["1342_number_of_steps_to_reduce_a_number_to_zero"] = r'''// LeetCode 1342 - Number of Steps to Reduce a Number to Zero
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

func numberOfSteps(num int) int {
	steps := 0
	for num > 0 {
		if num%2 == 0 {
			num /= 2
		} else {
			num--
		}
		steps++
	}
	return steps
}
'''

SOLUTIONS["1343_number_of_sub_arrays_of_size_k_and_average_greater_than_or_equal_to_threshold"] = r'''// LeetCode 1343 - Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
// https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

func numOfSubarrays(arr []int, k int, threshold int) int {
	window := 0
	for i := 0; i < k; i++ {
		window += arr[i]
	}
	answer := 0
	if window >= k*threshold {
		answer = 1
	}
	for i := k; i < len(arr); i++ {
		window += arr[i] - arr[i-k]
		if window >= k*threshold {
			answer++
		}
	}
	return answer
}
'''

SOLUTIONS["1344_angle_between_hands_of_a_clock"] = r'''// LeetCode 1344 - Angle Between Hands of a Clock
// https://leetcode.com/problems/angle-between-hands-of-a-clock/

func angleClock(hour int, minutes int) float64 {
	diff := float64((hour%12)*30) + float64(minutes)*0.5 - float64(minutes)*6
	if diff < 0 {
		diff = -diff
	}
	if diff > 360-diff {
		return 360 - diff
	}
	return diff
}
'''

SOLUTIONS["1345_jump_game_iv"] = r'''// LeetCode 1345 - Jump Game IV
// https://leetcode.com/problems/jump-game-iv/

func minJumps(arr []int) int {
	positions := map[int][]int{}
	for i, value := range arr {
		positions[value] = append(positions[value], i)
	}
	queue := []int{0}
	seen := map[int]bool{0: true}
	steps := 0
	for len(queue) > 0 {
		for sz := len(queue); sz > 0; sz-- {
			i := queue[0]
			queue = queue[1:]
			if i == len(arr)-1 {
				return steps
			}
			cands := append(append([]int{}, positions[arr[i]]...), i-1, i+1)
			delete(positions, arr[i])
			for _, j := range cands {
				if j >= 0 && j < len(arr) && !seen[j] {
					seen[j] = true
					queue = append(queue, j)
				}
			}
		}
		steps++
	}
	return -1
}
'''

SOLUTIONS["1346_check_if_n_and_its_double_exist"] = r'''// LeetCode 1346 - Check If N and Its Double Exist
// https://leetcode.com/problems/check-if-n-and-its-double-exist/

func checkIfExist(arr []int) bool {
	seen := map[int]bool{}
	for _, value := range arr {
		if seen[2*value] || (value%2 == 0 && seen[value/2]) {
			return true
		}
		seen[value] = true
	}
	return false
}
'''

SOLUTIONS["1347_minimum_number_of_steps_to_make_two_strings_anagram"] = r'''// LeetCode 1347 - Minimum Number of Steps to Make Two Strings Anagram
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

func minSteps(s string, t string) int {
	count := [26]int{}
	for i := 0; i < len(s); i++ {
		count[s[i]-'a']++
		count[t[i]-'a']--
	}
	answer := 0
	for _, c := range count {
		if c > 0 {
			answer += c
		}
	}
	return answer
}
'''

SOLUTIONS["1348_tweet_counts_per_frequency"] = r'''// LeetCode 1348 - Tweet Counts Per Frequency
// https://leetcode.com/problems/tweet-counts-per-frequency/

import "sort"

type TweetCounts struct {
	times map[string][]int
}

func Constructor() TweetCounts {
	return TweetCounts{times: map[string][]int{}}
}

func (this *TweetCounts) RecordTweet(tweetName string, time int) {
	this.times[tweetName] = append(this.times[tweetName], time)
}

func (this *TweetCounts) GetTweetCountsPerFrequency(freq string, tweetName string, startTime int, endTime int) []int {
	delta := 60
	if freq == "hour" {
		delta = 3600
	} else if freq == "day" {
		delta = 86400
	}
	n := (endTime-startTime)/delta + 1
	answer := make([]int, n)
	arr := this.times[tweetName]
	sort.Ints(arr)
	for _, t := range arr {
		if t < startTime || t > endTime {
			continue
		}
		answer[(t-startTime)/delta]++
	}
	return answer
}
'''

SOLUTIONS["1349_maximum_students_taking_exam"] = r'''// LeetCode 1349 - Maximum Students Taking Exam
// https://leetcode.com/problems/maximum-students-taking-exam/

func maxStudents(seats [][]byte) int {
	m, n := len(seats), len(seats[0])
	valid := make([]int, m)
	for r := 0; r < m; r++ {
		mask := 0
		for c := 0; c < n; c++ {
			if seats[r][c] == '.' {
				mask |= 1 << c
			}
		}
		valid[r] = mask
	}
	dp := map[int]int{0: 0}
	for r := 0; r < m; r++ {
		nxt := map[int]int{}
		for cur := 0; cur < (1 << n); cur++ {
			if cur&valid[r] != cur {
				continue
			}
			if cur&(cur<<1) != 0 {
				continue
			}
			bits := 0
			for x := cur; x > 0; x &= x - 1 {
				bits++
			}
			for prev, best := range dp {
				if (cur<<1)&prev == 0 && (cur>>1)&prev == 0 {
					if v := best + bits; v > nxt[cur] {
						nxt[cur] = v
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

SOLUTIONS["1351_count_negative_numbers_in_a_sorted_matrix"] = r'''// LeetCode 1351 - Count Negative Numbers in a Sorted Matrix
// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

func countNegatives(grid [][]int) int {
	answer := 0
	for _, row := range grid {
		lo, hi := 0, len(row)
		for lo < hi {
			mid := (lo + hi) / 2
			if row[mid] < 0 {
				hi = mid
			} else {
				lo = mid + 1
			}
		}
		answer += len(row) - lo
	}
	return answer
}
'''

SOLUTIONS["1352_product_of_the_last_k_numbers"] = r'''// LeetCode 1352 - Product of the Last K Numbers
// https://leetcode.com/problems/product-of-the-last-k-numbers/

type ProductOfNumbers struct {
	p []int
}

func Constructor() ProductOfNumbers {
	return ProductOfNumbers{p: []int{1}}
}

func (this *ProductOfNumbers) Add(num int) {
	if num == 0 {
		this.p = []int{1}
	} else {
		this.p = append(this.p, this.p[len(this.p)-1]*num)
	}
}

func (this *ProductOfNumbers) GetProduct(k int) int {
	if k >= len(this.p) {
		return 0
	}
	return this.p[len(this.p)-1] / this.p[len(this.p)-1-k]
}
'''

SOLUTIONS["1353_maximum_number_of_events_that_can_be_attended"] = r'''// LeetCode 1353 - Maximum Number of Events That Can Be Attended
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

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

func maxEvents(events [][]int) int {
	sort.Slice(events, func(i, j int) bool { return events[i][0] < events[j][0] })
	h := &minHeap{}
	heap.Init(h)
	i, ans, day := 0, 0, 0
	for i < len(events) || h.Len() > 0 {
		if h.Len() == 0 {
			if day < events[i][0] {
				day = events[i][0]
			}
		}
		for i < len(events) && events[i][0] <= day {
			heap.Push(h, events[i][1])
			i++
		}
		for h.Len() > 0 && (*h)[0] < day {
			heap.Pop(h)
		}
		if h.Len() > 0 {
			heap.Pop(h)
			ans++
			day++
		}
	}
	return ans
}
'''

SOLUTIONS["1354_construct_target_array_with_multiple_sums"] = r'''// LeetCode 1354 - Construct Target Array With Multiple Sums
// https://leetcode.com/problems/construct-target-array-with-multiple-sums/

import "container/heap"

type maxHeap []int

func (h maxHeap) Len() int            { return len(h) }
func (h maxHeap) Less(i, j int) bool  { return h[i] > h[j] }
func (h maxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *maxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func isPossible(target []int) bool {
	if len(target) == 1 {
		return target[0] == 1
	}
	total := 0
	h := &maxHeap{}
	for _, x := range target {
		total += x
		heap.Push(h, x)
	}
	for {
		x := heap.Pop(h).(int)
		rest := total - x
		if x == 1 || rest == 1 {
			return true
		}
		if rest == 0 || x <= rest {
			return false
		}
		prev := x % rest
		if prev == 0 {
			return false
		}
		total = rest + prev
		heap.Push(h, prev)
	}
}
'''

SOLUTIONS["1356_sort_integers_by_the_number_of_1_bits"] = r'''// LeetCode 1356 - Sort Integers by The Number of 1 Bits
// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

import "sort"

func sortByBits(arr []int) []int {
	bits := func(x int) int {
		c := 0
		for x > 0 {
			c += x & 1
			x >>= 1
		}
		return c
	}
	sort.Slice(arr, func(i, j int) bool {
		bi, bj := bits(arr[i]), bits(arr[j])
		if bi != bj {
			return bi < bj
		}
		return arr[i] < arr[j]
	})
	return arr
}
'''

SOLUTIONS["1357_apply_discount_every_n_orders"] = r'''// LeetCode 1357 - Apply Discount Every n Orders
// https://leetcode.com/problems/apply-discount-every-n-orders/

type Cashier struct {
	n, discount, count int
	prices             map[int]int
}

func Constructor(n int, discount int, products []int, prices []int) Cashier {
	m := map[int]int{}
	for i, p := range products {
		m[p] = prices[i]
	}
	return Cashier{n: n, discount: discount, prices: m}
}

func (this *Cashier) GetBill(product []int, amount []int) float64 {
	this.count++
	total := 0.0
	for i, p := range product {
		total += float64(this.prices[p] * amount[i])
	}
	if this.count%this.n == 0 {
		total = total * float64(100-this.discount) / 100.0
	}
	return total
}
'''

SOLUTIONS["1358_number_of_substrings_containing_all_three_characters"] = r'''// LeetCode 1358 - Number of Substrings Containing All Three Characters
// https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

func numberOfSubstrings(s string) int {
	count := [3]int{}
	left, answer := 0, 0
	for right := 0; right < len(s); right++ {
		count[s[right]-'a']++
		for count[0] > 0 && count[1] > 0 && count[2] > 0 {
			answer += len(s) - right
			count[s[left]-'a']--
			left++
		}
	}
	return answer
}
'''

SOLUTIONS["1359_count_all_valid_pickup_and_delivery_options"] = r'''// LeetCode 1359 - Count All Valid Pickup and Delivery Options
// https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

func countOrders(n int) int {
	const mod = 1000000007
	ans := 1
	for i := 1; i <= n; i++ {
		ans = ans * i % mod
		ans = ans * (2*i - 1) % mod
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
