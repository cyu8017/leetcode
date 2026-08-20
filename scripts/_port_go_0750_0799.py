#!/usr/bin/env python3
"""Write Go solutions for folders 0750-0799."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS: dict[str, str] = {}

SOLUTIONS["0750_number_of_corner_rectangles"] = r'''// LeetCode 0750 - Number Of Corner Rectangles
// https://leetcode.com/problems/number-of-corner-rectangles/

func countCornerRectangles(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	ans := 0
	for i := 0; i < m; i++ {
		for j := i + 1; j < m; j++ {
			count := 0
			for c := 0; c < n; c++ {
				if grid[i][c] == 1 && grid[j][c] == 1 {
					count++
				}
			}
			ans += count * (count - 1) / 2
		}
	}
	return ans
}
'''

SOLUTIONS["0751_ip_to_cidr"] = r'''// LeetCode 0751 - IP to CIDR
// https://leetcode.com/problems/ip-to-cidr/

import (
	"fmt"
	"strconv"
	"strings"
)

func ipToCIDR(ip string, n int) []string {
	ipToInt := func(value string) int {
		result := 0
		for _, part := range strings.Split(value, ".") {
			v, _ := strconv.Atoi(part)
			result = result*256 + v
		}
		return result
	}
	intToIP := func(value int) string {
		return fmt.Sprintf("%d.%d.%d.%d", (value>>24)&255, (value>>16)&255, (value>>8)&255, value&255)
	}
	start := ipToInt(ip)
	answer := []string{}
	for n > 0 {
		lowbit := 1 << 32
		if start != 0 {
			lowbit = start & -start
		}
		for lowbit > n {
			lowbit >>= 1
		}
		mask := 32
		lb := lowbit
		for lb > 1 {
			lb >>= 1
			mask--
		}
		answer = append(answer, fmt.Sprintf("%s/%d", intToIP(start), mask))
		start += lowbit
		n -= lowbit
	}
	return answer
}
'''

SOLUTIONS["0752_open_the_lock"] = r'''// LeetCode 0752 - Open the Lock
// https://leetcode.com/problems/open-the-lock/

func openLock(deadends []string, target string) int {
	dead := map[string]bool{}
	for _, d := range deadends {
		dead[d] = true
	}
	if dead["0000"] {
		return -1
	}
	type item struct {
		state string
		steps int
	}
	queue := []item{{"0000", 0}}
	seen := map[string]bool{"0000": true}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur.state == target {
			return cur.steps
		}
		b := []byte(cur.state)
		for i := 0; i < 4; i++ {
			orig := b[i]
			for _, delta := range []int{-1, 1} {
				b[i] = byte('0' + (int(orig-'0')+delta+10)%10)
				nxt := string(b)
				if !seen[nxt] && !dead[nxt] {
					seen[nxt] = true
					queue = append(queue, item{nxt, cur.steps + 1})
				}
			}
			b[i] = orig
		}
	}
	return -1
}
'''

SOLUTIONS["0753_cracking_the_safe"] = r'''// LeetCode 0753 - Cracking the Safe
// https://leetcode.com/problems/cracking-the-safe/

import "strings"

func crackSafe(n int, k int) string {
	seen := map[string]bool{}
	path := []byte{}
	start := strings.Repeat("0", n-1)
	var dfs func(string)
	dfs = func(node string) {
		for d := 0; d < k; d++ {
			digit := byte('0' + d)
			edge := node + string(digit)
			if !seen[edge] {
				seen[edge] = true
				dfs(edge[1:])
				path = append(path, digit)
			}
		}
	}
	dfs(start)
	return string(path) + start
}
'''

SOLUTIONS["0754_reach_a_number"] = r'''// LeetCode 0754 - Reach a Number
// https://leetcode.com/problems/reach-a-number/

func reachNumber(target int) int {
	if target < 0 {
		target = -target
	}
	steps, total := 0, 0
	for total < target || (total-target)%2 != 0 {
		steps++
		total += steps
	}
	return steps
}
'''

SOLUTIONS["0755_pour_water"] = r'''// LeetCode 0755 - Pour Water
// https://leetcode.com/problems/pour-water/

func pourWater(heights []int, volume int, k int) []int {
	for v := 0; v < volume; v++ {
		index := k
		for i := k - 1; i >= 0; i-- {
			if heights[i] > heights[index] {
				break
			}
			if heights[i] < heights[index] {
				index = i
			}
		}
		if index != k {
			heights[index]++
			continue
		}
		index = k
		for i := k + 1; i < len(heights); i++ {
			if heights[i] > heights[index] {
				break
			}
			if heights[i] < heights[index] {
				index = i
			}
		}
		heights[index]++
	}
	return heights
}
'''

SOLUTIONS["0756_pyramid_transition_matrix"] = r'''// LeetCode 0756 - Pyramid Transition Matrix
// https://leetcode.com/problems/pyramid-transition-matrix/

func pyramidTransition(bottom string, allowed []string) bool {
	transitions := map[string][]byte{}
	for _, triple := range allowed {
		key := triple[:2]
		transitions[key] = append(transitions[key], triple[2])
	}
	memo := map[string]bool{}
	var dfs func(string) bool
	dfs = func(row string) bool {
		if len(row) == 1 {
			return true
		}
		if v, ok := memo[row]; ok {
			return v
		}
		options := make([][]byte, 0, len(row)-1)
		for i := 0; i < len(row)-1; i++ {
			choices := transitions[row[i:i+2]]
			if len(choices) == 0 {
				memo[row] = false
				return false
			}
			options = append(options, choices)
		}
		var build func(int, []byte) bool
		build = func(index int, path []byte) bool {
			if index == len(options) {
				return dfs(string(path))
			}
			for _, ch := range options[index] {
				path = append(path, ch)
				if build(index+1, path) {
					return true
				}
				path = path[:len(path)-1]
			}
			return false
		}
		ans := build(0, nil)
		memo[row] = ans
		return ans
	}
	return dfs(bottom)
}
'''

SOLUTIONS["0757_set_intersection_size_at_least_two"] = r'''// LeetCode 0757 - Set Intersection Size At Least Two
// https://leetcode.com/problems/set-intersection-size-at-least-two/

import "sort"

func intersectionSizeTwo(intervals [][]int) int {
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][1] == intervals[j][1] {
			return intervals[i][0] < intervals[j][0]
		}
		return intervals[i][1] < intervals[j][1]
	})
	size := 0
	first, second := -1, -1
	for _, iv := range intervals {
		left, right := iv[0], iv[1]
		if left <= first {
			continue
		}
		if left <= second {
			size++
			first, second = second, right
		} else {
			size += 2
			first, second = right-1, right
		}
	}
	return size
}
'''

SOLUTIONS["0758_bold_words_in_string"] = r'''// LeetCode 0758 - Bold Words in String
// https://leetcode.com/problems/bold-words-in-string/

import "strings"

func boldWords(words []string, s string) string {
	n := len(s)
	bold := make([]bool, n)
	for _, word := range words {
		start := strings.Index(s, word)
		for start != -1 {
			for i := start; i < start+len(word); i++ {
				bold[i] = true
			}
			next := strings.Index(s[start+1:], word)
			if next == -1 {
				break
			}
			start = start + 1 + next
		}
	}
	parts := []string{}
	i := 0
	for i < n {
		if bold[i] {
			parts = append(parts, "<b>")
			for i < n && bold[i] {
				parts = append(parts, string(s[i]))
				i++
			}
			parts = append(parts, "</b>")
		} else {
			parts = append(parts, string(s[i]))
			i++
		}
	}
	out := strings.Join(parts, "")
	out = strings.ReplaceAll(out, "<b>", "**")
	out = strings.ReplaceAll(out, "</b>", "**")
	return out
}
'''

SOLUTIONS["0759_employee_free_time"] = r'''// LeetCode 0759 - Employee Free Time
// https://leetcode.com/problems/employee-free-time/

import "sort"

func employeeFreeTime(schedule [][][]int) [][]int {
	intervals := [][]int{}
	for _, employee := range schedule {
		for _, item := range employee {
			intervals = append(intervals, []int{item[0], item[1]})
		}
	}
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	merged := [][]int{}
	for _, iv := range intervals {
		if len(merged) == 0 || merged[len(merged)-1][1] < iv[0] {
			merged = append(merged, []int{iv[0], iv[1]})
		} else if iv[1] > merged[len(merged)-1][1] {
			merged[len(merged)-1][1] = iv[1]
		}
	}
	ans := [][]int{}
	for i := 1; i < len(merged); i++ {
		ans = append(ans, []int{merged[i-1][1], merged[i][0]})
	}
	return ans
}
'''

SOLUTIONS["0760_find_anagram_mappings"] = r'''// LeetCode 0760 - Find Anagram Mappings
// https://leetcode.com/problems/find-anagram-mappings/

func anagramMappings(nums1 []int, nums2 []int) []int {
	positions := map[int][]int{}
	for i, v := range nums2 {
		positions[v] = append(positions[v], i)
	}
	ans := make([]int, len(nums1))
	for i, v := range nums1 {
		ans[i] = positions[v][0]
		positions[v] = positions[v][1:]
	}
	return ans
}
'''

SOLUTIONS["0761_special_binary_string"] = r'''// LeetCode 0761 - Special Binary String
// https://leetcode.com/problems/special-binary-string/

import "sort"

func makeLargestSpecial(s string) string {
	parts := []string{}
	balance, start := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			balance++
		} else {
			balance--
		}
		if balance == 0 {
			parts = append(parts, "1"+makeLargestSpecial(s[start+1:i])+"0")
			start = i + 1
		}
	}
	sort.Slice(parts, func(i, j int) bool { return parts[i] > parts[j] })
	out := ""
	for _, p := range parts {
		out += p
	}
	return out
}
'''

SOLUTIONS["0762_prime_number_of_set_bits_in_binary_representation"] = r'''// LeetCode 0762 - Prime Number of Set Bits in Binary Representation
// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

func countPrimeSetBits(left int, right int) int {
	primes := map[int]bool{2: true, 3: true, 5: true, 7: true, 11: true, 13: true, 17: true, 19: true}
	ans := 0
	for num := left; num <= right; num++ {
		bits := 0
		x := num
		for x > 0 {
			bits += x & 1
			x >>= 1
		}
		if primes[bits] {
			ans++
		}
	}
	return ans
}
'''

SOLUTIONS["0763_partition_labels"] = r'''// LeetCode 0763 - Partition Labels
// https://leetcode.com/problems/partition-labels/

func partitionLabels(s string) []int {
	last := map[byte]int{}
	for i := 0; i < len(s); i++ {
		last[s[i]] = i
	}
	start, end := 0, 0
	answer := []int{}
	for i := 0; i < len(s); i++ {
		if last[s[i]] > end {
			end = last[s[i]]
		}
		if i == end {
			answer = append(answer, end-start+1)
			start = i + 1
		}
	}
	return answer
}
'''

SOLUTIONS["0764_largest_plus_sign"] = r'''// LeetCode 0764 - Largest Plus Sign
// https://leetcode.com/problems/largest-plus-sign/

func orderOfLargestPlusSign(n int, mines [][]int) int {
	banned := map[int]bool{}
	for _, m := range mines {
		banned[m[0]*n+m[1]] = true
	}
	arms := make([][]int, n)
	for i := range arms {
		arms[i] = make([]int, n)
	}
	best := 0
	for r := 0; r < n; r++ {
		count := 0
		for c := 0; c < n; c++ {
			if banned[r*n+c] {
				count = 0
			} else {
				count++
			}
			arms[r][c] = count
		}
		count = 0
		for c := n - 1; c >= 0; c-- {
			if banned[r*n+c] {
				count = 0
			} else {
				count++
			}
			if count < arms[r][c] {
				arms[r][c] = count
			}
		}
	}
	for c := 0; c < n; c++ {
		count := 0
		for r := 0; r < n; r++ {
			if banned[r*n+c] {
				count = 0
			} else {
				count++
			}
			if count < arms[r][c] {
				arms[r][c] = count
			}
		}
		count = 0
		for r := n - 1; r >= 0; r-- {
			if banned[r*n+c] {
				count = 0
			} else {
				count++
			}
			if count < arms[r][c] {
				arms[r][c] = count
			}
			if arms[r][c] > best {
				best = arms[r][c]
			}
		}
	}
	return best
}
'''

SOLUTIONS["0765_couples_holding_hands"] = r'''// LeetCode 0765 - Couples Holding Hands
// https://leetcode.com/problems/couples-holding-hands/

func minSwapsCouples(row []int) int {
	pos := map[int]int{}
	for i, person := range row {
		pos[person] = i
	}
	swaps := 0
	for i := 0; i < len(row); i += 2 {
		partner := row[i] ^ 1
		if row[i+1] == partner {
			continue
		}
		j := pos[partner]
		pos[row[i+1]] = j
		row[j] = row[i+1]
		row[i+1] = partner
		pos[partner] = i + 1
		swaps++
	}
	return swaps
}
'''

SOLUTIONS["0766_toeplitz_matrix"] = r'''// LeetCode 0766 - Toeplitz Matrix
// https://leetcode.com/problems/toeplitz-matrix/

func isToeplitzMatrix(matrix [][]int) bool {
	for r := 1; r < len(matrix); r++ {
		for c := 1; c < len(matrix[0]); c++ {
			if matrix[r][c] != matrix[r-1][c-1] {
				return false
			}
		}
	}
	return true
}
'''

SOLUTIONS["0767_reorganize_string"] = r'''// LeetCode 0767 - Reorganize String
// https://leetcode.com/problems/reorganize-string/

import "container/heap"

type charCount struct {
	count int
	ch    byte
}
type maxHeap []charCount

func (h maxHeap) Len() int            { return len(h) }
func (h maxHeap) Less(i, j int) bool  { return h[i].count > h[j].count }
func (h maxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x interface{}) { *h = append(*h, x.(charCount)) }
func (h *maxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func reorganizeString(s string) string {
	freq := map[byte]int{}
	for i := 0; i < len(s); i++ {
		freq[s[i]]++
	}
	h := &maxHeap{}
	heap.Init(h)
	for ch, count := range freq {
		heap.Push(h, charCount{count, ch})
	}
	if (*h)[0].count > (len(s)+1)/2 {
		return ""
	}
	result := make([]byte, 0, len(s))
	for h.Len() >= 2 {
		a := heap.Pop(h).(charCount)
		b := heap.Pop(h).(charCount)
		result = append(result, a.ch, b.ch)
		if a.count-1 > 0 {
			heap.Push(h, charCount{a.count - 1, a.ch})
		}
		if b.count-1 > 0 {
			heap.Push(h, charCount{b.count - 1, b.ch})
		}
	}
	if h.Len() > 0 {
		result = append(result, (*h)[0].ch)
	}
	return string(result)
}
'''

SOLUTIONS["0768_max_chunks_to_make_sorted_ii"] = r'''// LeetCode 0768 - Max Chunks To Make Sorted II
// https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

func maxChunksToSorted(arr []int) int {
	n := len(arr)
	maxLeft := make([]int, n)
	minRight := make([]int, n)
	maxLeft[0] = arr[0]
	for i := 1; i < n; i++ {
		maxLeft[i] = arr[i]
		if maxLeft[i-1] > maxLeft[i] {
			maxLeft[i] = maxLeft[i-1]
		}
	}
	minRight[n-1] = arr[n-1]
	for i := n - 2; i >= 0; i-- {
		minRight[i] = arr[i]
		if minRight[i+1] < minRight[i] {
			minRight[i] = minRight[i+1]
		}
	}
	chunks := 1
	for i := 0; i < n-1; i++ {
		if maxLeft[i] <= minRight[i+1] {
			chunks++
		}
	}
	return chunks
}
'''

SOLUTIONS["0769_max_chunks_to_make_sorted"] = r'''// LeetCode 0769 - Max Chunks To Make Sorted
// https://leetcode.com/problems/max-chunks-to-make-sorted/

func maxChunksToSorted(arr []int) int {
	chunks, maxSoFar := 0, 0
	for i, value := range arr {
		if value > maxSoFar {
			maxSoFar = value
		}
		if maxSoFar == i {
			chunks++
		}
	}
	return chunks
}
'''

SOLUTIONS["0770_basic_calculator_iv"] = r'''// LeetCode 0770 - Basic Calculator IV
// https://leetcode.com/problems/basic-calculator-iv/

import (
	"sort"
	"strconv"
	"strings"
)

func basicCalculatorIV(expression string, evalvars []string, evalints []int) []string {
	values := map[string]int{}
	for i, v := range evalvars {
		values[v] = evalints[i]
	}
	expr := strings.ReplaceAll(expression, "(", " ( ")
	expr = strings.ReplaceAll(expr, ")", " ) ")
	tokens := strings.Fields(expr)
	pos := 0

	type key []string
	type poly map[string]int

	keyStr := func(k []string) string {
		return strings.Join(k, "\x00")
	}
	parseKey := func(s string) []string {
		if s == "" {
			return nil
		}
		return strings.Split(s, "\x00")
	}

	add := func(left, right poly) poly {
		result := poly{}
		for k, v := range left {
			result[k] += v
		}
		for k, v := range right {
			result[k] += v
		}
		out := poly{}
		for k, v := range result {
			if v != 0 {
				out[k] = v
			}
		}
		return out
	}
	negate := func(p poly) poly {
		out := poly{}
		for k, v := range p {
			out[k] = -v
		}
		return out
	}
	mul := func(left, right poly) poly {
		result := poly{}
		for lk, lv := range left {
			for rk, rv := range right {
				parts := append(append([]string{}, parseKey(lk)...), parseKey(rk)...)
				sort.Strings(parts)
				ks := keyStr(parts)
				result[ks] += lv * rv
			}
		}
		out := poly{}
		for k, v := range result {
			if v != 0 {
				out[k] = v
			}
		}
		return out
	}
	atom := func(token string) poly {
		p := poly{}
		if token[0] >= 'a' && token[0] <= 'z' {
			if v, ok := values[token]; ok {
				p[""] = v
			} else {
				p[keyStr([]string{token})] = 1
			}
		} else {
			v, _ := strconv.Atoi(token)
			p[""] = v
		}
		return p
	}

	var parseExpr func() poly
	var parseTerm func() poly
	var parseFactor func() poly

	parseFactor = func() poly {
		token := tokens[pos]
		if token == "(" {
			pos++
			p := parseExpr()
			pos++ // ')'
			return p
		}
		pos++
		return atom(token)
	}
	parseTerm = func() poly {
		p := parseFactor()
		for pos < len(tokens) && tokens[pos] == "*" {
			pos++
			p = mul(p, parseFactor())
		}
		return p
	}
	parseExpr = func() poly {
		p := parseTerm()
		for pos < len(tokens) && (tokens[pos] == "+" || tokens[pos] == "-") {
			op := tokens[pos]
			pos++
			right := parseTerm()
			if op == "+" {
				p = add(p, right)
			} else {
				p = add(p, negate(right))
			}
		}
		return p
	}

	p := parseExpr()
	keys := make([]string, 0, len(p))
	for k := range p {
		keys = append(keys, k)
	}
	sort.Slice(keys, func(i, j int) bool {
		ki, kj := parseKey(keys[i]), parseKey(keys[j])
		if len(ki) != len(kj) {
			return len(ki) > len(kj)
		}
		for t := 0; t < len(ki); t++ {
			if ki[t] != kj[t] {
				return ki[t] < kj[t]
			}
		}
		return false
	})
	answer := []string{}
	for _, k := range keys {
		coef := p[k]
		parts := parseKey(k)
		if len(parts) == 0 {
			answer = append(answer, strconv.Itoa(coef))
		} else {
			answer = append(answer, strconv.Itoa(coef)+"*"+strings.Join(parts, "*"))
		}
	}
	return answer
}
'''

SOLUTIONS["0771_jewels_and_stones"] = r'''// LeetCode 0771 - Jewels and Stones
// https://leetcode.com/problems/jewels-and-stones/

func numJewelsInStones(jewels string, stones string) int {
	set := map[byte]bool{}
	for i := 0; i < len(jewels); i++ {
		set[jewels[i]] = true
	}
	ans := 0
	for i := 0; i < len(stones); i++ {
		if set[stones[i]] {
			ans++
		}
	}
	return ans
}
'''

SOLUTIONS["0772_basic_calculator_iii"] = r'''// LeetCode 0772 - Basic Calculator III
// https://leetcode.com/problems/basic-calculator-iii/

func calculate(s string) int {
	expr := make([]byte, 0, len(s))
	for i := 0; i < len(s); i++ {
		if s[i] != ' ' {
			expr = append(expr, s[i])
		}
	}
	var parse func(int) (int, int)
	parse = func(i int) (int, int) {
		stack := []int{}
		num := 0
		sign := byte('+')
		for i < len(expr) {
			ch := expr[i]
			if ch >= '0' && ch <= '9' {
				num = num*10 + int(ch-'0')
			}
			if ch == '(' {
				num, i = parse(i + 1)
			}
			if ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == ')' || i == len(expr)-1 {
				if sign == '+' {
					stack = append(stack, num)
				} else if sign == '-' {
					stack = append(stack, -num)
				} else if sign == '*' {
					stack[len(stack)-1] *= num
				} else {
					top := stack[len(stack)-1]
					stack[len(stack)-1] = top / num
				}
				if ch == ')' {
					sum := 0
					for _, v := range stack {
						sum += v
					}
					return sum, i
				}
				sign = ch
				num = 0
			}
			i++
		}
		sum := 0
		for _, v := range stack {
			sum += v
		}
		return sum, i
	}
	ans, _ := parse(0)
	return ans
}
'''

SOLUTIONS["0773_sliding_puzzle"] = r'''// LeetCode 0773 - Sliding Puzzle
// https://leetcode.com/problems/sliding-puzzle/

func slidingPuzzle(board [][]int) int {
	start := make([]byte, 0, 6)
	for _, row := range board {
		for _, cell := range row {
			start = append(start, byte('0'+cell))
		}
	}
	target := "123450"
	neighbors := [][]int{
		{1, 3},
		{0, 2, 4},
		{1, 5},
		{0, 4},
		{1, 3, 5},
		{2, 4},
	}
	type item struct {
		state string
		steps int
	}
	queue := []item{{string(start), 0}}
	seen := map[string]bool{string(start): true}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur.state == target {
			return cur.steps
		}
		zero := 0
		for i := 0; i < 6; i++ {
			if cur.state[i] == '0' {
				zero = i
				break
			}
		}
		for _, nei := range neighbors[zero] {
			chars := []byte(cur.state)
			chars[zero], chars[nei] = chars[nei], chars[zero]
			nxt := string(chars)
			if !seen[nxt] {
				seen[nxt] = true
				queue = append(queue, item{nxt, cur.steps + 1})
			}
		}
	}
	return -1
}
'''

SOLUTIONS["0774_minimize_max_distance_to_gas_station"] = r'''// LeetCode 0774 - Minimize Max Distance to Gas Station
// https://leetcode.com/problems/minimize-max-distance-to-gas-station/

func minmaxGasDist(stations []int, k int) float64 {
	can := func(dist float64) bool {
		needed := 0
		for i := 1; i < len(stations); i++ {
			needed += int(float64(stations[i]-stations[i-1]) / dist)
		}
		return needed <= k
	}
	lo, hi := 0.0, float64(stations[len(stations)-1]-stations[0])
	for hi-lo > 1e-6 {
		mid := (lo + hi) / 2
		if can(mid) {
			hi = mid
		} else {
			lo = mid
		}
	}
	return hi
}
'''

SOLUTIONS["0775_global_and_local_inversions"] = r'''// LeetCode 0775 - Global and Local Inversions
// https://leetcode.com/problems/global-and-local-inversions/

func isIdealPermutation(nums []int) bool {
	for i, v := range nums {
		diff := v - i
		if diff < 0 {
			diff = -diff
		}
		if diff > 1 {
			return false
		}
	}
	return true
}
'''

SOLUTIONS["0776_split_bst"] = r'''// LeetCode 0776 - Split BST
// https://leetcode.com/problems/split-bst/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func splitBST(root *TreeNode, target int) []*TreeNode {
	if root == nil {
		return []*TreeNode{nil, nil}
	}
	if root.Val <= target {
		parts := splitBST(root.Right, target)
		root.Right = parts[0]
		return []*TreeNode{root, parts[1]}
	}
	parts := splitBST(root.Left, target)
	root.Left = parts[1]
	return []*TreeNode{parts[0], root}
}
'''

SOLUTIONS["0777_swap_adjacent_in_lr_string"] = r'''// LeetCode 0777 - Swap Adjacent in LR String
// https://leetcode.com/problems/swap-adjacent-in-lr-string/

import "strings"

func canTransform(start string, result string) bool {
	if strings.ReplaceAll(start, "X", "") != strings.ReplaceAll(result, "X", "") {
		return false
	}
	i, j, n := 0, 0, len(start)
	for i < n && j < n {
		for i < n && start[i] == 'X' {
			i++
		}
		for j < n && result[j] == 'X' {
			j++
		}
		if i == n || j == n {
			break
		}
		if start[i] != result[j] {
			return false
		}
		if start[i] == 'L' && i < j {
			return false
		}
		if start[i] == 'R' && i > j {
			return false
		}
		i++
		j++
	}
	return true
}
'''

SOLUTIONS["0778_swim_in_rising_water"] = r'''// LeetCode 0778 - Swim in Rising Water
// https://leetcode.com/problems/swim-in-rising-water/

import "container/heap"

type cell struct {
	time, r, c int
}
type cellHeap []cell

func (h cellHeap) Len() int            { return len(h) }
func (h cellHeap) Less(i, j int) bool  { return h[i].time < h[j].time }
func (h cellHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *cellHeap) Push(x interface{}) { *h = append(*h, x.(cell)) }
func (h *cellHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func swimInWater(grid [][]int) int {
	n := len(grid)
	h := &cellHeap{{grid[0][0], 0, 0}}
	heap.Init(h)
	seen := map[[2]int]bool{{0, 0}: true}
	dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	for h.Len() > 0 {
		cur := heap.Pop(h).(cell)
		if cur.r == n-1 && cur.c == n-1 {
			return cur.time
		}
		for _, d := range dirs {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr >= 0 && nr < n && nc >= 0 && nc < n && !seen[[2]int{nr, nc}] {
				seen[[2]int{nr, nc}] = true
				t := cur.time
				if grid[nr][nc] > t {
					t = grid[nr][nc]
				}
				heap.Push(h, cell{t, nr, nc})
			}
		}
	}
	return -1
}
'''

SOLUTIONS["0779_k_th_symbol_in_grammar"] = r'''// LeetCode 0779 - K-th Symbol in Grammar
// https://leetcode.com/problems/k-th-symbol-in-grammar/

func kthGrammar(n int, k int) int {
	if n == 1 {
		return 0
	}
	mid := 1 << (n - 2)
	if k <= mid {
		return kthGrammar(n-1, k)
	}
	return 1 - kthGrammar(n-1, k-mid)
}
'''

SOLUTIONS["0780_reaching_points"] = r'''// LeetCode 0780 - Reaching Points
// https://leetcode.com/problems/reaching-points/

func reachingPoints(sx int, sy int, tx int, ty int) bool {
	for tx >= sx && ty >= sy {
		if tx == sx && ty == sy {
			return true
		}
		if tx == ty {
			break
		}
		if tx > ty {
			if ty > sy {
				tx %= ty
			} else {
				return (tx-sx)%ty == 0
			}
		} else {
			if tx > sx {
				ty %= tx
			} else {
				return (ty-sy)%tx == 0
			}
		}
	}
	return tx == sx && ty == sy
}
'''

SOLUTIONS["0781_rabbits_in_forest"] = r'''// LeetCode 0781 - Rabbits in Forest
// https://leetcode.com/problems/rabbits-in-forest/

func numRabbits(answers []int) int {
	freq := map[int]int{}
	for _, a := range answers {
		freq[a]++
	}
	total := 0
	for answer, count := range freq {
		group := answer + 1
		groups := (count + group - 1) / group
		total += groups * group
	}
	return total
}
'''

SOLUTIONS["0782_transform_to_chessboard"] = r'''// LeetCode 0782 - Transform to Chessboard
// https://leetcode.com/problems/transform-to-chessboard/

func movesToChessboard(board [][]int) int {
	n := len(board)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if board[0][0]^board[i][0]^board[0][j]^board[i][j] == 1 {
				return -1
			}
		}
	}
	rowSum, colSum := 0, 0
	for j := 0; j < n; j++ {
		rowSum += board[0][j]
	}
	for i := 0; i < n; i++ {
		colSum += board[i][0]
	}
	if rowSum < n/2 || rowSum > (n+1)/2 {
		return -1
	}
	if colSum < n/2 || colSum > (n+1)/2 {
		return -1
	}
	rowSwap, colSwap := 0, 0
	for i := 0; i < n; i++ {
		if board[0][i] != i%2 {
			rowSwap++
		}
		if board[i][0] != i%2 {
			colSwap++
		}
	}
	if n%2 == 1 {
		if rowSwap%2 == 1 {
			rowSwap = n - rowSwap
		}
		if colSwap%2 == 1 {
			colSwap = n - colSwap
		}
	} else {
		if n-rowSwap < rowSwap {
			rowSwap = n - rowSwap
		}
		if n-colSwap < colSwap {
			colSwap = n - colSwap
		}
	}
	return (rowSwap + colSwap) / 2
}
'''

SOLUTIONS["0783_minimum_distance_between_bst_nodes"] = r'''// LeetCode 0783 - Minimum Distance Between BST Nodes
// https://leetcode.com/problems/minimum-distance-between-bst-nodes/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func minDiffInBST(root *TreeNode) int {
	prev := -1
	best := int(^uint(0) >> 1)
	var inorder func(*TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inorder(node.Left)
		if prev != -1 {
			diff := node.Val - prev
			if diff < best {
				best = diff
			}
		}
		prev = node.Val
		inorder(node.Right)
	}
	inorder(root)
	return best
}
'''

SOLUTIONS["0784_letter_case_permutation"] = r'''// LeetCode 0784 - Letter Case Permutation
// https://leetcode.com/problems/letter-case-permutation/

func letterCasePermutation(s string) []string {
	result := []string{""}
	for i := 0; i < len(s); i++ {
		ch := s[i]
		next := []string{}
		if (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') {
			lower := ch | 32
			upper := ch &^ 32
			for _, prefix := range result {
				next = append(next, prefix+string(lower), prefix+string(upper))
			}
		} else {
			for _, prefix := range result {
				next = append(next, prefix+string(ch))
			}
		}
		result = next
	}
	return result
}
'''

SOLUTIONS["0785_is_graph_bipartite"] = r'''// LeetCode 0785 - Is Graph Bipartite?
// https://leetcode.com/problems/is-graph-bipartite/

func isBipartite(graph [][]int) bool {
	color := make([]int, len(graph))
	for i := range color {
		color[i] = -1
	}
	var dfs func(int, int) bool
	dfs = func(node, c int) bool {
		color[node] = c
		for _, nei := range graph[node] {
			if color[nei] == -1 {
				if !dfs(nei, c^1) {
					return false
				}
			} else if color[nei] == c {
				return false
			}
		}
		return true
	}
	for node := 0; node < len(graph); node++ {
		if color[node] == -1 && !dfs(node, 0) {
			return false
		}
	}
	return true
}
'''

SOLUTIONS["0786_k_th_smallest_prime_fraction"] = r'''// LeetCode 0786 - K-th Smallest Prime Fraction
// https://leetcode.com/problems/k-th-smallest-prime-fraction/

import "container/heap"

type frac struct {
	val float64
	i, j int
}
type fracHeap []frac

func (h fracHeap) Len() int            { return len(h) }
func (h fracHeap) Less(i, j int) bool  { return h[i].val < h[j].val }
func (h fracHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *fracHeap) Push(x interface{}) { *h = append(*h, x.(frac)) }
func (h *fracHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func kthSmallestPrimeFraction(arr []int, k int) []int {
	n := len(arr)
	h := &fracHeap{}
	heap.Init(h)
	for i := 0; i < n-1; i++ {
		heap.Push(h, frac{float64(arr[i]) / float64(arr[n-1]), i, n - 1})
	}
	for t := 0; t < k-1; t++ {
		cur := heap.Pop(h).(frac)
		if cur.j-1 > cur.i {
			heap.Push(h, frac{float64(arr[cur.i]) / float64(arr[cur.j-1]), cur.i, cur.j - 1})
		}
	}
	cur := heap.Pop(h).(frac)
	return []int{arr[cur.i], arr[cur.j]}
}
'''

SOLUTIONS["0787_cheapest_flights_within_k_stops"] = r'''// LeetCode 0787 - Cheapest Flights Within K Stops
// https://leetcode.com/problems/cheapest-flights-within-k-stops/

func findCheapestPrice(n int, flights [][]int, src int, dst int, k int) int {
	const inf = int(^uint(0) >> 1)
	dist := make([]int, n)
	for i := range dist {
		dist[i] = inf
	}
	dist[src] = 0
	for t := 0; t <= k; t++ {
		nxt := append([]int{}, dist...)
		for _, f := range flights {
			u, v, price := f[0], f[1], f[2]
			if dist[u] != inf && dist[u]+price < nxt[v] {
				nxt[v] = dist[u] + price
			}
		}
		dist = nxt
	}
	if dist[dst] == inf {
		return -1
	}
	return dist[dst]
}
'''

SOLUTIONS["0788_rotated_digits"] = r'''// LeetCode 0788 - Rotated Digits
// https://leetcode.com/problems/rotated-digits/

import "strconv"

func rotatedDigits(n int) int {
	valid := map[byte]bool{'0': true, '1': true, '2': true, '5': true, '6': true, '8': true, '9': true}
	changing := map[byte]bool{'2': true, '5': true, '6': true, '9': true}
	count := 0
	for num := 1; num <= n; num++ {
		s := strconv.Itoa(num)
		ok, changed := true, false
		for i := 0; i < len(s); i++ {
			if !valid[s[i]] {
				ok = false
				break
			}
			if changing[s[i]] {
				changed = true
			}
		}
		if ok && changed {
			count++
		}
	}
	return count
}
'''

SOLUTIONS["0789_escape_the_ghosts"] = r'''// LeetCode 0789 - Escape The Ghosts
// https://leetcode.com/problems/escape-the-ghosts/

func escapeGhosts(ghosts [][]int, target []int) bool {
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	targetDist := abs(target[0]) + abs(target[1])
	for _, g := range ghosts {
		if abs(g[0]-target[0])+abs(g[1]-target[1]) <= targetDist {
			return false
		}
	}
	return true
}
'''

SOLUTIONS["0790_domino_and_tromino_tiling"] = r'''// LeetCode 0790 - Domino and Tromino Tiling
// https://leetcode.com/problems/domino-and-tromino-tiling/

func numTilings(n int) int {
	mod := 1000000007
	if n == 1 {
		return 1
	}
	if n == 2 {
		return 2
	}
	dp := make([]int, n+1)
	dp[1], dp[2], dp[3] = 1, 2, 5
	for i := 4; i <= n; i++ {
		dp[i] = (2*dp[i-1] + dp[i-3]) % mod
	}
	return dp[n]
}
'''

SOLUTIONS["0791_custom_sort_string"] = r'''// LeetCode 0791 - Custom Sort String
// https://leetcode.com/problems/custom-sort-string/

func customSortString(order string, s string) string {
	counts := map[byte]int{}
	for i := 0; i < len(s); i++ {
		counts[s[i]]++
	}
	parts := make([]byte, 0, len(s))
	for i := 0; i < len(order); i++ {
		ch := order[i]
		for counts[ch] > 0 {
			parts = append(parts, ch)
			counts[ch]--
		}
	}
	for ch, count := range counts {
		for c := 0; c < count; c++ {
			parts = append(parts, ch)
		}
	}
	return string(parts)
}
'''

SOLUTIONS["0792_number_of_matching_subsequences"] = r'''// LeetCode 0792 - Number of Matching Subsequences
// https://leetcode.com/problems/number-of-matching-subsequences/

func numMatchingSubseq(s string, words []string) int {
	waiting := map[byte][]string{}
	for _, word := range words {
		waiting[word[0]] = append(waiting[word[0]], word[1:])
	}
	count := 0
	for i := 0; i < len(s); i++ {
		ch := s[i]
		advance := waiting[ch]
		waiting[ch] = nil
		for _, rest := range advance {
			if rest == "" {
				count++
			} else {
				waiting[rest[0]] = append(waiting[rest[0]], rest[1:])
			}
		}
	}
	return count
}
'''

SOLUTIONS["0793_preimage_size_of_factorial_zeroes_function"] = r'''// LeetCode 0793 - Preimage Size of Factorial Zeroes Function
// https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

func preimageSizeFZF(k int) int {
	zeros := func(x int) int {
		count := 0
		for x > 0 {
			x /= 5
			count += x
		}
		return count
	}
	firstGE := func(target int) int {
		lo, hi := 0, 5*(target+1)
		for lo < hi {
			mid := (lo + hi) / 2
			if zeros(mid) < target {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		return lo
	}
	if zeros(firstGE(k)) == k {
		return 5
	}
	return 0
}
'''

SOLUTIONS["0794_valid_tic_tac_toe_state"] = r'''// LeetCode 0794 - Valid Tic-Tac-Toe State
// https://leetcode.com/problems/valid-tic-tac-toe-state/

func validTicTacToe(board []string) bool {
	flat := board[0] + board[1] + board[2]
	xCount, oCount := 0, 0
	for i := 0; i < len(flat); i++ {
		if flat[i] == 'X' {
			xCount++
		} else if flat[i] == 'O' {
			oCount++
		}
	}
	if oCount != xCount && oCount != xCount-1 {
		return false
	}
	win := func(player byte) bool {
		p := string([]byte{player, player, player})
		lines := []string{board[0], board[1], board[2]}
		for c := 0; c < 3; c++ {
			lines = append(lines, string([]byte{board[0][c], board[1][c], board[2][c]}))
		}
		lines = append(lines, string([]byte{board[0][0], board[1][1], board[2][2]}))
		lines = append(lines, string([]byte{board[0][2], board[1][1], board[2][0]}))
		for _, line := range lines {
			if line == p {
				return true
			}
		}
		return false
	}
	xWin, oWin := win('X'), win('O')
	if xWin && oWin {
		return false
	}
	if xWin && xCount != oCount+1 {
		return false
	}
	if oWin && xCount != oCount {
		return false
	}
	return true
}
'''

SOLUTIONS["0795_number_of_subarrays_with_bounded_maximum"] = r'''// LeetCode 0795 - Number of Subarrays with Bounded Maximum
// https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

func numSubarrayBoundedMax(nums []int, left int, right int) int {
	countAtMost := func(bound int) int {
		ans, cur := 0, 0
		for _, num := range nums {
			if num <= bound {
				cur++
				ans += cur
			} else {
				cur = 0
			}
		}
		return ans
	}
	return countAtMost(right) - countAtMost(left-1)
}
'''

SOLUTIONS["0796_rotate_string"] = r'''// LeetCode 0796 - Rotate String
// https://leetcode.com/problems/rotate-string/

import "strings"

func rotateString(s string, goal string) bool {
	return len(s) == len(goal) && strings.Contains(s+s, goal)
}
'''

SOLUTIONS["0797_all_paths_from_source_to_target"] = r'''// LeetCode 0797 - All Paths From Source to Target
// https://leetcode.com/problems/all-paths-from-source-to-target/

func allPathsSourceTarget(graph [][]int) [][]int {
	target := len(graph) - 1
	answer := [][]int{}
	var dfs func(int, []int)
	dfs = func(node int, path []int) {
		if node == target {
			cp := append([]int{}, path...)
			answer = append(answer, cp)
			return
		}
		for _, nei := range graph[node] {
			path = append(path, nei)
			dfs(nei, path)
			path = path[:len(path)-1]
		}
	}
	dfs(0, []int{0})
	return answer
}
'''

SOLUTIONS["0798_smallest_rotation_with_highest_score"] = r'''// LeetCode 0798 - Smallest Rotation with Highest Score
// https://leetcode.com/problems/smallest-rotation-with-highest-score/

func bestRotation(nums []int) int {
	n := len(nums)
	change := make([]int, n)
	for i := range change {
		change[i] = 1
	}
	for i, value := range nums {
		change[(i-value+1+n)%n]--
	}
	for i := 1; i < n; i++ {
		change[i] += change[i-1]
	}
	best, idx := change[0], 0
	for i := 1; i < n; i++ {
		if change[i] > best {
			best = change[i]
			idx = i
		}
	}
	return idx
}
'''

SOLUTIONS["0799_champagne_tower"] = r'''// LeetCode 0799 - Champagne Tower
// https://leetcode.com/problems/champagne-tower/

func champagneTower(poured int, query_row int, query_glass int) float64 {
	row := []float64{float64(poured)}
	for r := 0; r < query_row; r++ {
		next := make([]float64, r+2)
		for i, amount := range row {
			overflow := (amount - 1.0) / 2.0
			if overflow > 0 {
				next[i] += overflow
				next[i+1] += overflow
			}
		}
		row = next
	}
	if row[query_glass] > 1.0 {
		return 1.0
	}
	return row[query_glass]
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
