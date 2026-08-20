#!/usr/bin/env python3
"""Write Go solutions for folders 0800-0849."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
S: dict[str, str] = {}

def add(name: str, body: str) -> None:
    S[name] = body.strip() + "\n"

add("0800_similar_rgb_color", r'''
// LeetCode 0800 - Similar RGB Color
// https://leetcode.com/problems/similar-rgb-color/

import "fmt"

func similarRGB(color string) string {
	closest := func(component string) string {
		var value int
		fmt.Sscanf(component, "%x", &value)
		rounded := (value + 8) / 17
		return fmt.Sprintf("%x%x", rounded, rounded)
	}
	return "#" + closest(color[1:3]) + closest(color[3:5]) + closest(color[5:7])
}
''')

add("0801_minimum_swaps_to_make_sequences_increasing", r'''
// LeetCode 0801 - Minimum Swaps To Make Sequences Increasing
// https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

func minSwap(nums1 []int, nums2 []int) int {
	n := len(nums1)
	swap := make([]int, n)
	keep := make([]int, n)
	for i := range swap {
		swap[i], keep[i] = n, n
	}
	swap[0], keep[0] = 1, 0
	for i := 1; i < n; i++ {
		if nums1[i] > nums1[i-1] && nums2[i] > nums2[i-1] {
			keep[i] = keep[i-1]
			swap[i] = swap[i-1] + 1
		}
		if nums1[i] > nums2[i-1] && nums2[i] > nums1[i-1] {
			if swap[i-1] < keep[i] {
				keep[i] = swap[i-1]
			}
			if keep[i-1]+1 < swap[i] {
				swap[i] = keep[i-1] + 1
			}
		}
	}
	if swap[n-1] < keep[n-1] {
		return swap[n-1]
	}
	return keep[n-1]
}
''')

add("0802_find_eventual_safe_states", r'''
// LeetCode 0802 - Find Eventual Safe States
// https://leetcode.com/problems/find-eventual-safe-states/

func eventualSafeNodes(graph [][]int) []int {
	n := len(graph)
	color := make([]int, n)
	var dfs func(int) bool
	dfs = func(node int) bool {
		if color[node] != 0 {
			return color[node] == 2
		}
		color[node] = 1
		for _, nei := range graph[node] {
			if !dfs(nei) {
				return false
			}
		}
		color[node] = 2
		return true
	}
	ans := []int{}
	for i := 0; i < n; i++ {
		if dfs(i) {
			ans = append(ans, i)
		}
	}
	return ans
}
''')

add("0803_bricks_falling_when_hit", r'''
// LeetCode 0803 - Bricks Falling When Hit
// https://leetcode.com/problems/bricks-falling-when-hit/

func hitBricks(grid [][]int, hits [][]int) []int {
	m, n := len(grid), len(grid[0])
	roof := m * n
	parent := make([]int, roof+1)
	size := make([]int, roof+1)
	for i := range parent {
		parent[i] = i
		size[i] = 1
	}
	find := func(x int) int {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	union := func(a, b int) {
		ra, rb := find(a), find(b)
		if ra == rb {
			return
		}
		parent[ra] = rb
		size[rb] += size[ra]
	}
	idx := func(r, c int) int { return r*n + c }
	status := make([][]int, m)
	for i := range grid {
		status[i] = append([]int{}, grid[i]...)
	}
	for _, h := range hits {
		status[h[0]][h[1]] = 0
	}
	dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			if status[r][c] == 0 {
				continue
			}
			if r == 0 {
				union(idx(r, c), roof)
			}
			for _, d := range dirs {
				nr, nc := r+d[0], c+d[1]
				if nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] == 1 {
					union(idx(r, c), idx(nr, nc))
				}
			}
		}
	}
	answer := make([]int, len(hits))
	for i := len(hits) - 1; i >= 0; i-- {
		r, c := hits[i][0], hits[i][1]
		if grid[r][c] == 0 {
			continue
		}
		prev := size[find(roof)]
		status[r][c] = 1
		if r == 0 {
			union(idx(r, c), roof)
		}
		for _, d := range dirs {
			nr, nc := r+d[0], c+d[1]
			if nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] == 1 {
				union(idx(r, c), idx(nr, nc))
			}
		}
		curr := size[find(roof)]
		diff := curr - prev - 1
		if diff > 0 {
			answer[i] = diff
		}
	}
	return answer
}
''')

add("0804_unique_morse_code_words", r'''
// LeetCode 0804 - Unique Morse Code Words
// https://leetcode.com/problems/unique-morse-code-words/

func uniqueMorseRepresentations(words []string) int {
	codes := []string{".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."}
	seen := map[string]bool{}
	for _, word := range words {
		var b []byte
		for i := 0; i < len(word); i++ {
			b = append(b, codes[word[i]-'a']...)
		}
		seen[string(b)] = true
	}
	return len(seen)
}
''')

add("0805_split_array_with_same_average", r'''
// LeetCode 0805 - Split Array With Same Average
// https://leetcode.com/problems/split-array-with-same-average/

import "sort"

func splitArraySameAverage(nums []int) bool {
	n := len(nums)
	total := 0
	for _, v := range nums {
		total += v
	}
	sort.Ints(nums)
	type key struct{ target, count, index int }
	memo := map[key]bool{}
	var find func(int, int, int) bool
	find = func(target, count, index int) bool {
		k := key{target, count, index}
		if v, ok := memo[k]; ok {
			return v
		}
		if count == 0 {
			return target == 0
		}
		if index == n || count+index > n || target < 0 {
			return false
		}
		ans := find(target-nums[index], count-1, index+1) || find(target, count, index+1)
		memo[k] = ans
		return ans
	}
	for size := 1; size < n; size++ {
		if total*size%n == 0 && find(total*size/n, size, 0) {
			return true
		}
	}
	return false
}
''')

add("0806_number_of_lines_to_write_string", r'''
// LeetCode 0806 - Number of Lines To Write String
// https://leetcode.com/problems/number-of-lines-to-write-string/

func numberOfLines(widths []int, s string) []int {
	lines, width := 1, 0
	for i := 0; i < len(s); i++ {
		w := widths[s[i]-'a']
		if width+w > 100 {
			lines++
			width = w
		} else {
			width += w
		}
	}
	return []int{lines, width}
}
''')

add("0807_max_increase_to_keep_city_skyline", r'''
// LeetCode 0807 - Max Increase to Keep City Skyline
// https://leetcode.com/problems/max-increase-to-keep-city-skyline/

func maxIncreaseKeepingSkyline(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	rowMax := make([]int, m)
	colMax := make([]int, n)
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			if grid[r][c] > rowMax[r] {
				rowMax[r] = grid[r][c]
			}
			if grid[r][c] > colMax[c] {
				colMax[c] = grid[r][c]
			}
		}
	}
	ans := 0
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			limit := rowMax[r]
			if colMax[c] < limit {
				limit = colMax[c]
			}
			ans += limit - grid[r][c]
		}
	}
	return ans
}
''')

add("0808_soup_servings", r'''
// LeetCode 0808 - Soup Servings
// https://leetcode.com/problems/soup-servings/

func soupServings(n int) float64 {
	if n >= 4800 {
		return 1.0
	}
	units := (n + 24) / 25
	memo := map[[2]int]float64{}
	var dp func(int, int) float64
	dp = func(a, b int) float64 {
		if a <= 0 && b <= 0 {
			return 0.5
		}
		if a <= 0 {
			return 1.0
		}
		if b <= 0 {
			return 0.0
		}
		key := [2]int{a, b}
		if v, ok := memo[key]; ok {
			return v
		}
		ans := 0.25 * (dp(a-4, b) + dp(a-3, b-1) + dp(a-2, b-2) + dp(a-1, b-3))
		memo[key] = ans
		return ans
	}
	return dp(units, units)
}
''')

add("0809_expressive_words", r'''
// LeetCode 0809 - Expressive Words
// https://leetcode.com/problems/expressive-words/

func expressiveWords(s string, words []string) int {
	groups := func(text string) [][2]int {
		result := [][2]int{}
		i := 0
		for i < len(text) {
			j := i
			for j < len(text) && text[j] == text[i] {
				j++
			}
			result = append(result, [2]int{int(text[i]), j - i})
			i = j
		}
		return result
	}
	target := groups(s)
	stretchy := func(word string) bool {
		source := groups(word)
		if len(source) != len(target) {
			return false
		}
		for i := range source {
			if source[i][0] != target[i][0] {
				return false
			}
			c1, c2 := source[i][1], target[i][1]
			if c1 > c2 || (c1 != c2 && c2 < 3) {
				return false
			}
		}
		return true
	}
	ans := 0
	for _, word := range words {
		if stretchy(word) {
			ans++
		}
	}
	return ans
}
''')

add("0810_chalkboard_xor_game", r'''
// LeetCode 0810 - Chalkboard XOR Game
// https://leetcode.com/problems/chalkboard-xor-game/

func xorGame(nums []int) bool {
	x := 0
	for _, v := range nums {
		x ^= v
	}
	return x == 0 || len(nums)%2 == 0
}
''')

add("0811_subdomain_visit_count", r'''
// LeetCode 0811 - Subdomain Visit Count
// https://leetcode.com/problems/subdomain-visit-count/

import (
	"fmt"
	"strconv"
	"strings"
)

func subdomainVisits(cpdomains []string) []string {
	counts := map[string]int{}
	for _, item := range cpdomains {
		parts := strings.Fields(item)
		count, _ := strconv.Atoi(parts[0])
		domain := parts[1]
		segs := strings.Split(domain, ".")
		for i := 0; i < len(segs); i++ {
			counts[strings.Join(segs[i:], ".")] += count
		}
	}
	ans := make([]string, 0, len(counts))
	for domain, count := range counts {
		ans = append(ans, fmt.Sprintf("%d %s", count, domain))
	}
	return ans
}
''')

add("0812_largest_triangle_area", r'''
// LeetCode 0812 - Largest Triangle Area
// https://leetcode.com/problems/largest-triangle-area/

func largestTriangleArea(points [][]int) float64 {
	best := 0.0
	n := len(points)
	for i := 0; i < n; i++ {
		x1, y1 := points[i][0], points[i][1]
		for j := i + 1; j < n; j++ {
			x2, y2 := points[j][0], points[j][1]
			for k := j + 1; k < n; k++ {
				x3, y3 := points[k][0], points[k][1]
				area := float64(abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))) / 2.0
				if area > best {
					best = area
				}
			}
		}
	}
	return best
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
''')

add("0813_largest_sum_of_averages", r'''
// LeetCode 0813 - Largest Sum of Averages
// https://leetcode.com/problems/largest-sum-of-averages/

func largestSumOfAverages(nums []int, k int) float64 {
	n := len(nums)
	prefix := make([]float64, n+1)
	for i, num := range nums {
		prefix[i+1] = prefix[i] + float64(num)
	}
	average := func(i, j int) float64 {
		return (prefix[j] - prefix[i]) / float64(j-i)
	}
	dp := make([]float64, n)
	for i := 0; i < n; i++ {
		dp[i] = average(0, i+1)
	}
	for groups := 2; groups <= k; groups++ {
		nxt := make([]float64, n)
		for i := groups - 1; i < n; i++ {
			best := 0.0
			for j := groups - 2; j < i; j++ {
				cand := dp[j] + average(j+1, i+1)
				if cand > best {
					best = cand
				}
			}
			nxt[i] = best
		}
		dp = nxt
	}
	return dp[n-1]
}
''')

add("0814_binary_tree_pruning", r'''
// LeetCode 0814 - Binary Tree Pruning
// https://leetcode.com/problems/binary-tree-pruning/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pruneTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	root.Left = pruneTree(root.Left)
	root.Right = pruneTree(root.Right)
	if root.Val == 0 && root.Left == nil && root.Right == nil {
		return nil
	}
	return root
}
''')

# continuation for _port_go_0800_0849.py — append before main

add("0815_bus_routes", r'''
// LeetCode 0815 - Bus Routes
// https://leetcode.com/problems/bus-routes/

func numBusesToDestination(routes [][]int, source int, target int) int {
	if source == target {
		return 0
	}
	stopToBuses := map[int][]int{}
	for bus, stops := range routes {
		for _, stop := range stops {
			stopToBuses[stop] = append(stopToBuses[stop], bus)
		}
	}
	type item struct{ stop, buses int }
	queue := []item{{source, 0}}
	seenStops := map[int]bool{source: true}
	seenBuses := map[int]bool{}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		for _, bus := range stopToBuses[cur.stop] {
			if seenBuses[bus] {
				continue
			}
			seenBuses[bus] = true
			for _, nxt := range routes[bus] {
				if nxt == target {
					return cur.buses + 1
				}
				if !seenStops[nxt] {
					seenStops[nxt] = true
					queue = append(queue, item{nxt, cur.buses + 1})
				}
			}
		}
	}
	return -1
}
''')

add("0816_ambiguous_coordinates", r'''
// LeetCode 0816 - Ambiguous Coordinates
// https://leetcode.com/problems/ambiguous-coordinates/

func ambiguousCoordinates(s string) []string {
	digits := s[1 : len(s)-1]
	candidates := func(frag string) []string {
		options := []string{}
		if frag == "" || (len(frag) > 1 && frag[0] == '0' && frag[len(frag)-1] == '0') {
			return options
		}
		if frag[0] == '0' && len(frag) > 1 {
			if frag[len(frag)-1] != '0' {
				return []string{"0." + frag[1:]}
			}
			return options
		}
		options = append(options, frag)
		if frag[len(frag)-1] == '0' {
			return options
		}
		for i := 1; i < len(frag); i++ {
			options = append(options, frag[:i]+"."+frag[i:])
		}
		return options
	}
	answer := []string{}
	for i := 1; i < len(digits); i++ {
		for _, left := range candidates(digits[:i]) {
			for _, right := range candidates(digits[i:]) {
				answer = append(answer, "("+left+", "+right+")")
			}
		}
	}
	return answer
}
''')

add("0817_linked_list_components", r'''
// LeetCode 0817 - Linked List Components
// https://leetcode.com/problems/linked-list-components/

type ListNode struct {
	Val  int
	Next *ListNode
}

func numComponents(head *ListNode, nums []int) int {
	present := map[int]bool{}
	for _, v := range nums {
		present[v] = true
	}
	count := 0
	connected := false
	for head != nil {
		if present[head.Val] {
			if !connected {
				count++
				connected = true
			}
		} else {
			connected = false
		}
		head = head.Next
	}
	return count
}
''')

add("0818_race_car", r'''
// LeetCode 0818 - Race Car
// https://leetcode.com/problems/race-car/

func racecar(target int) int {
	type state struct{ pos, speed, steps int }
	queue := []state{{0, 1, 0}}
	seen := map[[2]int]bool{{0, 1}: true}
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur.pos == target {
			return cur.steps
		}
		nxtPos, nxtSpeed := cur.pos+cur.speed, cur.speed*2
		if !seen[[2]int{nxtPos, nxtSpeed}] && abs(nxtPos) < target*2 {
			seen[[2]int{nxtPos, nxtSpeed}] = true
			queue = append(queue, state{nxtPos, nxtSpeed, cur.steps + 1})
		}
		rev := -1
		if cur.speed <= 0 {
			rev = 1
		}
		if !seen[[2]int{cur.pos, rev}] {
			seen[[2]int{cur.pos, rev}] = true
			queue = append(queue, state{cur.pos, rev, cur.steps + 1})
		}
	}
	return -1
}
''')

add("0819_most_common_word", r'''
// LeetCode 0819 - Most Common Word
// https://leetcode.com/problems/most-common-word/

import "unicode"

func mostCommonWord(paragraph string, banned []string) string {
	bannedSet := map[string]bool{}
	for _, w := range banned {
		bannedSet[w] = true
	}
	counts := map[string]int{}
	var word []byte
	flush := func() {
		if len(word) == 0 {
			return
		}
		s := string(word)
		word = word[:0]
		if !bannedSet[s] {
			counts[s]++
		}
	}
	for i := 0; i < len(paragraph); i++ {
		ch := rune(paragraph[i])
		if unicode.IsLetter(ch) {
			word = append(word, byte(unicode.ToLower(ch)))
		} else {
			flush()
		}
	}
	flush()
	best, ans := -1, ""
	for w, c := range counts {
		if c > best {
			best, ans = c, w
		}
	}
	return ans
}
''')

add("0820_short_encoding_of_words", r'''
// LeetCode 0820 - Short Encoding of Words
// https://leetcode.com/problems/short-encoding-of-words/

func minimumLengthEncoding(words []string) int {
	good := map[string]bool{}
	for _, w := range words {
		good[w] = true
	}
	for _, word := range words {
		for i := 1; i < len(word); i++ {
			delete(good, word[i:])
		}
	}
	ans := 0
	for word := range good {
		ans += len(word) + 1
	}
	return ans
}
''')

add("0821_shortest_distance_to_a_character", r'''
// LeetCode 0821 - Shortest Distance to a Character
// https://leetcode.com/problems/shortest-distance-to-a-character/

func shortestToChar(s string, c byte) []int {
	n := len(s)
	ans := make([]int, n)
	prev := -n
	for i := 0; i < n; i++ {
		if s[i] == c {
			prev = i
		}
		ans[i] = i - prev
	}
	prev = 2 * n
	for i := n - 1; i >= 0; i-- {
		if s[i] == c {
			prev = i
		}
		if prev-i < ans[i] {
			ans[i] = prev - i
		}
	}
	return ans
}
''')

add("0822_card_flipping_game", r'''
// LeetCode 0822 - Card Flipping Game
// https://leetcode.com/problems/card-flipping-game/

func flipgame(fronts []int, backs []int) int {
	same := map[int]bool{}
	for i := range fronts {
		if fronts[i] == backs[i] {
			same[fronts[i]] = true
		}
	}
	best := int(^uint(0) >> 1)
	for _, x := range fronts {
		if !same[x] && x < best {
			best = x
		}
	}
	for _, x := range backs {
		if !same[x] && x < best {
			best = x
		}
	}
	if best == int(^uint(0)>>1) {
		return 0
	}
	return best
}
''')

add("0823_binary_trees_with_factors", r'''
// LeetCode 0823 - Binary Trees With Factors
// https://leetcode.com/problems/binary-trees-with-factors/

import "sort"

func numFactoredBinaryTrees(arr []int) int {
	const MOD = 1000000007
	sort.Ints(arr)
	dp := map[int]int{}
	for i, x := range arr {
		ways := 1
		for j := 0; j < i; j++ {
			left := arr[j]
			if x%left == 0 {
				right := x / left
				if _, ok := dp[right]; ok {
					ways = (ways + dp[left]*dp[right]) % MOD
				}
			}
		}
		dp[x] = ways
	}
	ans := 0
	for _, v := range dp {
		ans = (ans + v) % MOD
	}
	return ans
}
''')

add("0824_goat_latin", r'''
// LeetCode 0824 - Goat Latin
// https://leetcode.com/problems/goat-latin/

import "strings"

func toGoatLatin(sentence string) string {
	vowels := map[byte]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'A': true, 'E': true, 'I': true, 'O': true, 'U': true}
	words := strings.Fields(sentence)
	out := make([]string, len(words))
	for i, word := range words {
		var goat string
		if vowels[word[0]] {
			goat = word + "ma"
		} else {
			goat = word[1:] + string(word[0]) + "ma"
		}
		out[i] = goat + strings.Repeat("a", i+1)
	}
	return strings.Join(out, " ")
}
''')

add("0825_friends_of_appropriate_ages", r'''
// LeetCode 0825 - Friends Of Appropriate Ages
// https://leetcode.com/problems/friends-of-appropriate-ages/

func numFriendRequests(ages []int) int {
	count := make([]int, 121)
	for _, age := range ages {
		count[age]++
	}
	ans := 0
	for x := 1; x <= 120; x++ {
		if count[x] == 0 {
			continue
		}
		for y := 1; y <= 120; y++ {
			if count[y] == 0 {
				continue
			}
			if float64(y) <= 0.5*float64(x)+7 || y > x || (y > 100 && x < 100) {
				continue
			}
			ans += count[x] * count[y]
			if x == y {
				ans -= count[x]
			}
		}
	}
	return ans
}
''')

add("0826_most_profit_assigning_work", r'''
// LeetCode 0826 - Most Profit Assigning Work
// https://leetcode.com/problems/most-profit-assigning-work/

import "sort"

func maxProfitAssignment(difficulty []int, profit []int, worker []int) int {
	type job struct{ d, p int }
	jobs := make([]job, len(difficulty))
	for i := range difficulty {
		jobs[i] = job{difficulty[i], profit[i]}
	}
	sort.Slice(jobs, func(i, j int) bool { return jobs[i].d < jobs[j].d })
	sort.Ints(worker)
	ans, best, i := 0, 0, 0
	for _, ability := range worker {
		for i < len(jobs) && jobs[i].d <= ability {
			if jobs[i].p > best {
				best = jobs[i].p
			}
			i++
		}
		ans += best
	}
	return ans
}
''')

add("0827_making_a_large_island", r'''
// LeetCode 0827 - Making A Large Island
// https://leetcode.com/problems/making-a-large-island/

func largestIsland(grid [][]int) int {
	n := len(grid)
	sizes := map[int]int{0: 0}
	islandID := 2
	var dfs func(int, int, int) int
	dfs = func(r, c, iid int) int {
		if r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1 {
			return 0
		}
		grid[r][c] = iid
		return 1 + dfs(r+1, c, iid) + dfs(r-1, c, iid) + dfs(r, c+1, iid) + dfs(r, c-1, iid)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				sizes[islandID] = dfs(i, j, islandID)
				islandID++
			}
		}
	}
	ans := 0
	for _, v := range sizes {
		if v > ans {
			ans = v
		}
	}
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] != 0 {
				continue
			}
			seen := map[int]bool{}
			total := 1
			for _, d := range dirs {
				ni, nj := i+d[0], j+d[1]
				if ni >= 0 && ni < n && nj >= 0 && nj < n {
					iid := grid[ni][nj]
					if iid > 1 && !seen[iid] {
						seen[iid] = true
						total += sizes[iid]
					}
				}
			}
			if total > ans {
				ans = total
			}
		}
	}
	return ans
}
''')

add("0828_count_unique_characters_of_all_substrings_of_a_given_string", r'''
// LeetCode 0828 - Count Unique Characters of All Substrings of a Given String
// https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

func uniqueLetterString(s string) int {
	n := len(s)
	last := map[byte][]int{}
	for i := 0; i < n; i++ {
		ch := s[i]
		if _, ok := last[ch]; !ok {
			last[ch] = []int{-1}
		}
	}
	for i := 0; i < n; i++ {
		last[s[i]] = append(last[s[i]], i)
	}
	for ch := range last {
		last[ch] = append(last[ch], n)
	}
	ans := 0
	for _, indices := range last {
		for k := 1; k < len(indices)-1; k++ {
			ans += (indices[k] - indices[k-1]) * (indices[k+1] - indices[k])
		}
	}
	return ans
}
''')

add("0829_consecutive_numbers_sum", r'''
// LeetCode 0829 - Consecutive Numbers Sum
// https://leetcode.com/problems/consecutive-numbers-sum/

func consecutiveNumbersSum(n int) int {
	ans, k := 0, 1
	for k*(k-1)/2 < n {
		if (n-k*(k-1)/2)%k == 0 {
			ans++
		}
		k++
	}
	return ans
}
''')

add("0830_positions_of_large_groups", r'''
// LeetCode 0830 - Positions of Large Groups
// https://leetcode.com/problems/positions-of-large-groups/

func largeGroupPositions(s string) [][]int {
	ans := [][]int{}
	i, n := 0, len(s)
	for i < n {
		j := i
		for j < n && s[j] == s[i] {
			j++
		}
		if j-i >= 3 {
			ans = append(ans, []int{i, j - 1})
		}
		i = j
	}
	return ans
}
''')

add("0831_masking_personal_information", r'''
// LeetCode 0831 - Masking Personal Information
// https://leetcode.com/problems/masking-personal-information/

import (
	"strings"
	"unicode"
)

func maskPII(s string) string {
	if strings.Contains(s, "@") {
		parts := strings.Split(strings.ToLower(s), "@")
		name, domain := parts[0], parts[1]
		return string(name[0]) + "*****" + string(name[len(name)-1]) + "@" + domain
	}
	digits := []byte{}
	for i := 0; i < len(s); i++ {
		if unicode.IsDigit(rune(s[i])) {
			digits = append(digits, s[i])
		}
	}
	local := string(digits[len(digits)-4:])
	country := len(digits) - 10
	if country == 0 {
		return "***-***-" + local
	}
	return "+" + strings.Repeat("*", country) + "-***-***-" + local
}
''')

add("0832_flipping_an_image", r'''
// LeetCode 0832 - Flipping an Image
// https://leetcode.com/problems/flipping-an-image/

func flipAndInvertImage(image [][]int) [][]int {
	for _, row := range image {
		for i, j := 0, len(row)-1; i <= j; i, j = i+1, j-1 {
			row[i], row[j] = 1-row[j], 1-row[i]
		}
	}
	return image
}
''')

add("0833_find_and_replace_in_string", r'''
// LeetCode 0833 - Find And Replace in String
// https://leetcode.com/problems/find-and-replace-in-string/

func findReplaceString(s string, indices []int, sources []string, targets []string) string {
	type rep struct {
		length int
		target string
	}
	replace := map[int]rep{}
	for i := range indices {
		idx, src, tgt := indices[i], sources[i], targets[i]
		if idx+len(src) <= len(s) && s[idx:idx+len(src)] == src {
			replace[idx] = rep{len(src), tgt}
		}
	}
	out := []byte{}
	i := 0
	for i < len(s) {
		if v, ok := replace[i]; ok {
			out = append(out, v.target...)
			i += v.length
		} else {
			out = append(out, s[i])
			i++
		}
	}
	return string(out)
}
''')

add("0834_sum_of_distances_in_tree", r'''
// LeetCode 0834 - Sum of Distances in Tree
// https://leetcode.com/problems/sum-of-distances-in-tree/

func sumOfDistancesInTree(n int, edges [][]int) []int {
	graph := make([][]int, n)
	for _, e := range edges {
		graph[e[0]] = append(graph[e[0]], e[1])
		graph[e[1]] = append(graph[e[1]], e[0])
	}
	count := make([]int, n)
	ans := make([]int, n)
	for i := range count {
		count[i] = 1
	}
	var post func(int, int)
	post = func(node, parent int) {
		for _, child := range graph[node] {
			if child == parent {
				continue
			}
			post(child, node)
			count[node] += count[child]
			ans[node] += ans[child] + count[child]
		}
	}
	var reroot func(int, int)
	reroot = func(node, parent int) {
		for _, child := range graph[node] {
			if child == parent {
				continue
			}
			ans[child] = ans[node] - count[child] + (n - count[child])
			reroot(child, node)
		}
	}
	post(0, -1)
	reroot(0, -1)
	return ans
}
''')

add("0835_image_overlap", r'''
// LeetCode 0835 - Image Overlap
// https://leetcode.com/problems/image-overlap/

func largestOverlap(img1 [][]int, img2 [][]int) int {
	n := len(img1)
	ones1, ones2 := [][2]int{}, [][2]int{}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if img1[i][j] == 1 {
				ones1 = append(ones1, [2]int{i, j})
			}
			if img2[i][j] == 1 {
				ones2 = append(ones2, [2]int{i, j})
			}
		}
	}
	if len(ones1) == 0 || len(ones2) == 0 {
		return 0
	}
	shifts := map[[2]int]int{}
	best := 0
	for _, a := range ones1 {
		for _, b := range ones2 {
			key := [2]int{a[0] - b[0], a[1] - b[1]}
			shifts[key]++
			if shifts[key] > best {
				best = shifts[key]
			}
		}
	}
	return best
}
''')

add("0836_rectangle_overlap", r'''
// LeetCode 0836 - Rectangle Overlap
// https://leetcode.com/problems/rectangle-overlap/

func isRectangleOverlap(rec1 []int, rec2 []int) bool {
	return !(rec1[2] <= rec2[0] || rec1[0] >= rec2[2] || rec1[3] <= rec2[1] || rec1[1] >= rec2[3])
}
''')

add("0837_new_21_game", r'''
// LeetCode 0837 - New 21 Game
// https://leetcode.com/problems/new-21-game/

func new21Game(n int, k int, maxPts int) float64 {
	if k == 0 || n >= k-1+maxPts {
		return 1.0
	}
	dp := make([]float64, n+1)
	dp[0] = 1.0
	window := 1.0
	ans := 0.0
	for i := 1; i <= n; i++ {
		dp[i] = window / float64(maxPts)
		if i < k {
			window += dp[i]
		} else {
			ans += dp[i]
		}
		if i-maxPts >= 0 && i-maxPts < k {
			window -= dp[i-maxPts]
		}
	}
	return ans
}
''')

add("0838_push_dominoes", r'''
// LeetCode 0838 - Push Dominoes
// https://leetcode.com/problems/push-dominoes/

func pushDominoes(dominoes string) string {
	n := len(dominoes)
	force := make([]int, n)
	f := 0
	for i := 0; i < n; i++ {
		if dominoes[i] == 'R' {
			f = n
		} else if dominoes[i] == 'L' {
			f = 0
		} else if f > 0 {
			f--
		}
		force[i] += f
	}
	f = 0
	for i := n - 1; i >= 0; i-- {
		if dominoes[i] == 'L' {
			f = n
		} else if dominoes[i] == 'R' {
			f = 0
		} else if f > 0 {
			f--
		}
		force[i] -= f
	}
	out := make([]byte, n)
	for i, x := range force {
		if x > 0 {
			out[i] = 'R'
		} else if x < 0 {
			out[i] = 'L'
		} else {
			out[i] = '.'
		}
	}
	return string(out)
}
''')

add("0839_similar_string_groups", r'''
// LeetCode 0839 - Similar String Groups
// https://leetcode.com/problems/similar-string-groups/

func numSimilarGroups(strs []string) int {
	n := len(strs)
	parent := make([]int, n)
	for i := range parent {
		parent[i] = i
	}
	find := func(x int) int {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	similar := func(a, b string) bool {
		diff := []int{}
		for i := 0; i < len(a); i++ {
			if a[i] != b[i] {
				diff = append(diff, i)
			}
		}
		return len(diff) == 0 || (len(diff) == 2 && a[diff[0]] == b[diff[1]] && a[diff[1]] == b[diff[0]])
	}
	groups := n
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if similar(strs[i], strs[j]) {
				pi, pj := find(i), find(j)
				if pi != pj {
					parent[pi] = pj
					groups--
				}
			}
		}
	}
	return groups
}
''')

add("0840_magic_squares_in_grid", r'''
// LeetCode 0840 - Magic Squares In Grid
// https://leetcode.com/problems/magic-squares-in-grid/

import "sort"

func numMagicSquaresInside(grid [][]int) int {
	rows, cols := len(grid), len(grid[0])
	if rows < 3 || cols < 3 {
		return 0
	}
	magic := func(r, c int) bool {
		vals := make([]int, 0, 9)
		for i := 0; i < 3; i++ {
			for j := 0; j < 3; j++ {
				vals = append(vals, grid[r+i][c+j])
			}
		}
		sorted := append([]int{}, vals...)
		sort.Ints(sorted)
		for i := 0; i < 9; i++ {
			if sorted[i] != i+1 {
				return false
			}
		}
		a := grid
		return a[r][c]+a[r][c+1]+a[r][c+2] == 15 &&
			a[r+1][c]+a[r+1][c+1]+a[r+1][c+2] == 15 &&
			a[r+2][c]+a[r+2][c+1]+a[r+2][c+2] == 15 &&
			a[r][c]+a[r+1][c]+a[r+2][c] == 15 &&
			a[r][c+1]+a[r+1][c+1]+a[r+2][c+1] == 15 &&
			a[r][c+2]+a[r+1][c+2]+a[r+2][c+2] == 15 &&
			a[r][c]+a[r+1][c+1]+a[r+2][c+2] == 15 &&
			a[r][c+2]+a[r+1][c+1]+a[r+2][c] == 15
	}
	ans := 0
	for i := 0; i < rows-2; i++ {
		for j := 0; j < cols-2; j++ {
			if magic(i, j) {
				ans++
			}
		}
	}
	return ans
}
''')

add("0841_keys_and_rooms", r'''
// LeetCode 0841 - Keys and Rooms
// https://leetcode.com/problems/keys-and-rooms/

func canVisitAllRooms(rooms [][]int) bool {
	seen := map[int]bool{0: true}
	stack := []int{0}
	for len(stack) > 0 {
		room := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for _, key := range rooms[room] {
			if !seen[key] {
				seen[key] = true
				stack = append(stack, key)
			}
		}
	}
	return len(seen) == len(rooms)
}
''')

add("0842_split_array_into_fibonacci_sequence", r'''
// LeetCode 0842 - Split Array into Fibonacci Sequence
// https://leetcode.com/problems/split-array-into-fibonacci-sequence/

func splitIntoFibonacci(num string) []int {
	n := len(num)
	path := []int{}
	var dfs func(int) bool
	dfs = func(start int) bool {
		if start == n {
			return len(path) >= 3
		}
		for end := start; end < n; end++ {
			if num[start] == '0' && end > start {
				break
			}
			val := 0
			ok := true
			for i := start; i <= end; i++ {
				val = val*10 + int(num[i]-'0')
				if val > 1<<31-1 {
					ok = false
					break
				}
			}
			if !ok {
				break
			}
			if len(path) >= 2 {
				total := path[len(path)-1] + path[len(path)-2]
				if val < total {
					continue
				}
				if val > total {
					break
				}
			}
			path = append(path, val)
			if dfs(end + 1) {
				return true
			}
			path = path[:len(path)-1]
		}
		return false
	}
	dfs(0)
	return path
}
''')

add("0843_guess_the_word", r'''
// LeetCode 0843 - Guess the Word
// https://leetcode.com/problems/guess-the-word/

type Master interface {
	Guess(word string) int
}

func findSecretWord(words []string, master Master) {
	match := func(a, b string) int {
		cnt := 0
		for i := 0; i < len(a); i++ {
			if a[i] == b[i] {
				cnt++
			}
		}
		return cnt
	}
	candidates := append([]string{}, words...)
	for len(candidates) > 0 {
		best := candidates[0]
		bestScore := int(^uint(0) >> 1)
		for _, w := range candidates {
			buckets := make([]int, 7)
			for _, c := range candidates {
				buckets[match(w, c)]++
			}
			maxBucket := 0
			for _, b := range buckets {
				if b > maxBucket {
					maxBucket = b
				}
			}
			if maxBucket < bestScore {
				bestScore = maxBucket
				best = w
			}
		}
		score := master.Guess(best)
		if score == 6 {
			return
		}
		next := []string{}
		for _, c := range candidates {
			if match(c, best) == score {
				next = append(next, c)
			}
		}
		candidates = next
	}
}
''')

add("0844_backspace_string_compare", r'''
// LeetCode 0844 - Backspace String Compare
// https://leetcode.com/problems/backspace-string-compare/

func backspaceCompare(s string, t string) bool {
	build := func(text string) string {
		stack := []byte{}
		for i := 0; i < len(text); i++ {
			if text[i] == '#' {
				if len(stack) > 0 {
					stack = stack[:len(stack)-1]
				}
			} else {
				stack = append(stack, text[i])
			}
		}
		return string(stack)
	}
	return build(s) == build(t)
}
''')

add("0845_longest_mountain_in_array", r'''
// LeetCode 0845 - Longest Mountain in Array
// https://leetcode.com/problems/longest-mountain-in-array/

func longestMountain(arr []int) int {
	n := len(arr)
	ans, i := 0, 0
	for i < n {
		j := i
		if j+1 < n && arr[j] < arr[j+1] {
			for j+1 < n && arr[j] < arr[j+1] {
				j++
			}
			if j+1 < n && arr[j] > arr[j+1] {
				for j+1 < n && arr[j] > arr[j+1] {
					j++
				}
				if j-i+1 > ans {
					ans = j - i + 1
				}
				i = j
				continue
			}
		}
		i++
	}
	return ans
}
''')

add("0846_hand_of_straights", r'''
// LeetCode 0846 - Hand of Straights
// https://leetcode.com/problems/hand-of-straights/

import "sort"

func isNStraightHand(hand []int, groupSize int) bool {
	if len(hand)%groupSize != 0 {
		return false
	}
	count := map[int]int{}
	for _, v := range hand {
		count[v]++
	}
	keys := make([]int, 0, len(count))
	for k := range count {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	for _, start := range keys {
		for count[start] > 0 {
			for x := start; x < start+groupSize; x++ {
				if count[x] == 0 {
					return false
				}
				count[x]--
			}
		}
	}
	return true
}
''')

add("0847_shortest_path_visiting_all_nodes", r'''
// LeetCode 0847 - Shortest Path Visiting All Nodes
// https://leetcode.com/problems/shortest-path-visiting-all-nodes/

func shortestPathLength(graph [][]int) int {
	n := len(graph)
	target := (1 << n) - 1
	type item struct{ node, mask, dist int }
	queue := []item{}
	seen := map[[2]int]bool{}
	for i := 0; i < n; i++ {
		queue = append(queue, item{i, 1 << i, 0})
		seen[[2]int{i, 1 << i}] = true
	}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur.mask == target {
			return cur.dist
		}
		for _, nxt := range graph[cur.node] {
			nmask := cur.mask | (1 << nxt)
			state := [2]int{nxt, nmask}
			if !seen[state] {
				seen[state] = true
				queue = append(queue, item{nxt, nmask, cur.dist + 1})
			}
		}
	}
	return -1
}
''')

add("0848_shifting_letters", r'''
// LeetCode 0848 - Shifting Letters
// https://leetcode.com/problems/shifting-letters/

func shiftingLetters(s string, shifts []int) string {
	total := 0
	chars := []byte(s)
	for i := len(s) - 1; i >= 0; i-- {
		total = (total + shifts[i]) % 26
		chars[i] = byte((int(chars[i]-'a')+total)%26 + 'a')
	}
	return string(chars)
}
''')

add("0849_maximize_distance_to_closest_person", r'''
// LeetCode 0849 - Maximize Distance to Closest Person
// https://leetcode.com/problems/maximize-distance-to-closest-person/

func maxDistToClosest(seats []int) int {
	n := len(seats)
	prev, ans := -1, 0
	for i, occupied := range seats {
		if occupied == 1 {
			if prev == -1 {
				ans = i
			} else if (i-prev)/2 > ans {
				ans = (i - prev) / 2
			}
			prev = i
		}
	}
	if n-1-prev > ans {
		ans = n - 1 - prev
	}
	return ans
}
''')


def main() -> None:
    written = []
    for name, content in sorted(S.items()):
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
