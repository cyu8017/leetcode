#!/usr/bin/env python3
"""Write Go solutions for LeetCode 1600-1649 (non-SQL)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

SOLUTIONS: dict[str, str] = {}

SOLUTIONS["1600_throne_inheritance"] = r'''// LeetCode 1600 - Throne Inheritance
// https://leetcode.com/problems/throne-inheritance/

type ThroneInheritance struct {
	king     string
	children map[string][]string
	dead     map[string]bool
}

func Constructor(kingName string) ThroneInheritance {
	return ThroneInheritance{
		king:     kingName,
		children: make(map[string][]string),
		dead:     make(map[string]bool),
	}
}

func (this *ThroneInheritance) Birth(parentName string, childName string) {
	this.children[parentName] = append(this.children[parentName], childName)
}

func (this *ThroneInheritance) Death(name string) {
	this.dead[name] = true
}

func (this *ThroneInheritance) GetInheritanceOrder() []string {
	order := []string{}
	var visit func(string)
	visit = func(name string) {
		if !this.dead[name] {
			order = append(order, name)
		}
		for _, child := range this.children[name] {
			visit(child)
		}
	}
	visit(this.king)
	return order
}
'''

SOLUTIONS["1601_maximum_number_of_achievable_transfer_requests"] = r'''// LeetCode 1601 - Maximum Number of Achievable Transfer Requests
// https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

func maximumRequests(n int, requests [][]int) int {
	ans := 0
	m := len(requests)
	for mask := 0; mask < 1<<m; mask++ {
		cnt := bits.OnesCount(uint(mask))
		if cnt <= ans {
			continue
		}
		bal := make([]int, n)
		for i, req := range requests {
			if mask>>i&1 == 1 {
				bal[req[0]]--
				bal[req[1]]++
			}
		}
		ok := true
		for _, v := range bal {
			if v != 0 {
				ok = false
				break
			}
		}
		if ok {
			ans = cnt
		}
	}
	return ans
}
'''
# needs import "math/bits" -> rewrite without bits package

SOLUTIONS["1601_maximum_number_of_achievable_transfer_requests"] = r'''// LeetCode 1601 - Maximum Number of Achievable Transfer Requests
// https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

func maximumRequests(n int, requests [][]int) int {
	ans := 0
	m := len(requests)
	for mask := 0; mask < 1<<m; mask++ {
		cnt := 0
		for t := mask; t > 0; t &= t - 1 {
			cnt++
		}
		if cnt <= ans {
			continue
		}
		bal := make([]int, n)
		for i, req := range requests {
			if mask>>i&1 == 1 {
				bal[req[0]]--
				bal[req[1]]++
			}
		}
		ok := true
		for _, v := range bal {
			if v != 0 {
				ok = false
				break
			}
		}
		if ok {
			ans = cnt
		}
	}
	return ans
}
'''

SOLUTIONS["1602_find_nearest_right_node_in_binary_tree"] = r'''// LeetCode 1602 - Find Nearest Right Node in Binary Tree
// https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findNearestRightNode(root *TreeNode, u *TreeNode) *TreeNode {
	if root == nil || u == nil {
		return nil
	}
	q := []*TreeNode{root}
	for len(q) > 0 {
		nxt := []*TreeNode{}
		for i, node := range q {
			if node == u || node.Val == u.Val {
				if i+1 < len(q) {
					return q[i+1]
				}
				return nil
			}
			if node.Left != nil {
				nxt = append(nxt, node.Left)
			}
			if node.Right != nil {
				nxt = append(nxt, node.Right)
			}
		}
		q = nxt
	}
	return nil
}
'''

SOLUTIONS["1603_design_parking_system"] = r'''// LeetCode 1603 - Design Parking System
// https://leetcode.com/problems/design-parking-system/

type ParkingSystem struct {
	spaces [4]int
}

func Constructor(big int, medium int, small int) ParkingSystem {
	return ParkingSystem{spaces: [4]int{0, big, medium, small}}
}

func (this *ParkingSystem) AddCar(carType int) bool {
	if this.spaces[carType] == 0 {
		return false
	}
	this.spaces[carType]--
	return true
}
'''

SOLUTIONS["1604_alert_using_same_key_card_three_or_more_times_in_a_one_hour_period"] = r'''// LeetCode 1604 - Alert Using Same Key-Card Three or More Times in a One Hour Period
// https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

import (
	"sort"
	"strconv"
	"strings"
)

func alertNames(keyName []string, keyTime []string) []string {
	times := map[string][]int{}
	for i, name := range keyName {
		parts := strings.Split(keyTime[i], ":")
		h, _ := strconv.Atoi(parts[0])
		m, _ := strconv.Atoi(parts[1])
		times[name] = append(times[name], h*60+m)
	}
	ans := []string{}
	for name, a := range times {
		sort.Ints(a)
		for i := 0; i+2 < len(a); i++ {
			if a[i+2]-a[i] <= 60 {
				ans = append(ans, name)
				break
			}
		}
	}
	sort.Strings(ans)
	return ans
}
'''

SOLUTIONS["1605_find_valid_matrix_given_row_and_column_sums"] = r'''// LeetCode 1605 - Find Valid Matrix Given Row and Column Sums
// https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

func restoreMatrix(rowSum []int, colSum []int) [][]int {
	ans := make([][]int, len(rowSum))
	for i := range ans {
		ans[i] = make([]int, len(colSum))
	}
	i, j := 0, 0
	for i < len(rowSum) && j < len(colSum) {
		x := rowSum[i]
		if colSum[j] < x {
			x = colSum[j]
		}
		ans[i][j] = x
		rowSum[i] -= x
		colSum[j] -= x
		if rowSum[i] == 0 {
			i++
		}
		if colSum[j] == 0 {
			j++
		}
	}
	return ans
}
'''

SOLUTIONS["1606_find_servers_that_handled_most_number_of_requests"] = r'''// LeetCode 1606 - Find Servers That Handled Most Number of Requests
// https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

import "container/heap"

type busyItem struct {
	end, server int
}

type busyHeap []busyItem

func (h busyHeap) Len() int            { return len(h) }
func (h busyHeap) Less(i, j int) bool  { return h[i].end < h[j].end }
func (h busyHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *busyHeap) Push(x interface{}) { *h = append(*h, x.(busyItem)) }
func (h *busyHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type freeHeap []int

func (h freeHeap) Len() int            { return len(h) }
func (h freeHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h freeHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *freeHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *freeHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func busiestServers(k int, arrival []int, load []int) []int {
	free := freeHeap{}
	for i := 0; i < k; i++ {
		heap.Push(&free, i)
	}
	busy := busyHeap{}
	count := make([]int, k)
	for i, t := range arrival {
		for busy.Len() > 0 && busy[0].end <= t {
			item := heap.Pop(&busy).(busyItem)
			heap.Push(&free, i+(item.server-i)%k)
		}
		if free.Len() == 0 {
			continue
		}
		server := heap.Pop(&free).(int) % k
		count[server]++
		heap.Push(&busy, busyItem{end: t + load[i], server: server})
	}
	best := 0
	for _, c := range count {
		if c > best {
			best = c
		}
	}
	ans := []int{}
	for i, c := range count {
		if c == best {
			ans = append(ans, i)
		}
	}
	return ans
}
'''

SOLUTIONS["1608_special_array_with_x_elements_greater_than_or_equal_x"] = r'''// LeetCode 1608 - Special Array With X Elements Greater Than or Equal X
// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

func specialArray(nums []int) int {
	for x := 0; x <= len(nums); x++ {
		cnt := 0
		for _, v := range nums {
			if v >= x {
				cnt++
			}
		}
		if cnt == x {
			return x
		}
	}
	return -1
}
'''

SOLUTIONS["1609_even_odd_tree"] = r'''// LeetCode 1609 - Even Odd Tree
// https://leetcode.com/problems/even-odd-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isEvenOddTree(root *TreeNode) bool {
	if root == nil {
		return true
	}
	q := []*TreeNode{root}
	level := 0
	for len(q) > 0 {
		prev := 0
		if level%2 == 0 {
			prev = -1 << 30
		} else {
			prev = 1 << 30
		}
		nxt := []*TreeNode{}
		for _, node := range q {
			if node.Val%2 == level%2 {
				return false
			}
			if level%2 == 0 && node.Val <= prev {
				return false
			}
			if level%2 == 1 && node.Val >= prev {
				return false
			}
			prev = node.Val
			if node.Left != nil {
				nxt = append(nxt, node.Left)
			}
			if node.Right != nil {
				nxt = append(nxt, node.Right)
			}
		}
		q = nxt
		level++
	}
	return true
}
'''

SOLUTIONS["1610_maximum_number_of_visible_points"] = r'''// LeetCode 1610 - Maximum Number of Visible Points
// https://leetcode.com/problems/maximum-number-of-visible-points/

import (
	"math"
	"sort"
)

func visiblePoints(points [][]int, angle int, location []int) int {
	same := 0
	a := []float64{}
	for _, p := range points {
		dx := float64(p[0] - location[0])
		dy := float64(p[1] - location[1])
		if dx == 0 && dy == 0 {
			same++
		} else {
			a = append(a, math.Atan2(dy, dx))
		}
	}
	sort.Float64s(a)
	ext := append([]float64{}, a...)
	for _, x := range a {
		ext = append(ext, x+2*math.Pi)
	}
	width := float64(angle)*math.Pi/180 + 1e-12
	left, best := 0, 0
	for right, value := range ext {
		for value-ext[left] > width {
			left++
		}
		cur := right - left + 1
		if cur > len(a) {
			cur = len(a)
		}
		if cur > best {
			best = cur
		}
	}
	return best + same
}
'''

SOLUTIONS["1611_minimum_one_bit_operations_to_make_integers_zero"] = r'''// LeetCode 1611 - Minimum One Bit Operations to Make Integers Zero
// https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

func minimumOneBitOperations(n int) int {
	ans := 0
	for n > 0 {
		ans ^= n
		n >>= 1
	}
	return ans
}
'''

SOLUTIONS["1612_check_if_two_expression_trees_are_equivalent"] = r'''// LeetCode 1612 - Check If Two Expression Trees are Equivalent
// https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/

type Node struct {
	Val   byte
	Left  *Node
	Right *Node
}

func checkEquivalence(root1 *Node, root2 *Node) bool {
	a := make([]int, 26)
	b := make([]int, 26)
	count(root1, a)
	count(root2, b)
	for i := 0; i < 26; i++ {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func count(node *Node, out []int) {
	if node == nil {
		return
	}
	if node.Val == '+' {
		count(node.Left, out)
		count(node.Right, out)
	} else {
		out[node.Val-'a']++
	}
}
'''

SOLUTIONS["1614_maximum_nesting_depth_of_the_parentheses"] = r'''// LeetCode 1614 - Maximum Nesting Depth of the Parentheses
// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

func maxDepth(s string) int {
	depth, ans := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			depth++
			if depth > ans {
				ans = depth
			}
		} else if s[i] == ')' {
			depth--
		}
	}
	return ans
}
'''

SOLUTIONS["1615_maximal_network_rank"] = r'''// LeetCode 1615 - Maximal Network Rank
// https://leetcode.com/problems/maximal-network-rank/

func maximalNetworkRank(n int, roads [][]int) int {
	degree := make([]int, n)
	edges := map[[2]int]bool{}
	for _, r := range roads {
		a, b := r[0], r[1]
		degree[a]++
		degree[b]++
		if a > b {
			a, b = b, a
		}
		edges[[2]int{a, b}] = true
	}
	ans := 0
	for a := 0; a < n; a++ {
		for b := a + 1; b < n; b++ {
			cur := degree[a] + degree[b]
			if edges[[2]int{a, b}] {
				cur--
			}
			if cur > ans {
				ans = cur
			}
		}
	}
	return ans
}
'''

SOLUTIONS["1616_split_two_strings_to_make_palindrome"] = r'''// LeetCode 1616 - Split Two Strings to Make Palindrome
// https://leetcode.com/problems/split-two-strings-to-make-palindrome/

func checkPalindromeFormation(a string, b string) bool {
	return check1616(a, b) || check1616(b, a)
}

func check1616(x, y string) bool {
	i, j := 0, len(x)-1
	for i < j && x[i] == y[j] {
		i++
		j--
	}
	return isPal1616(x[i:j+1]) || isPal1616(y[i:j+1])
}

func isPal1616(s string) bool {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			return false
		}
	}
	return true
}
'''

SOLUTIONS["1617_count_subtrees_with_max_distance_between_cities"] = r'''// LeetCode 1617 - Count Subtrees With Max Distance Between Cities
// https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

func countSubgraphsForEachDiameter(n int, edges [][]int) []int {
	adj := make([][]int, n)
	for _, e := range edges {
		a, b := e[0]-1, e[1]-1
		adj[a] = append(adj[a], b)
		adj[b] = append(adj[b], a)
	}
	ans := make([]int, n-1)
	bfs := func(mask, src int) (int, map[int]int) {
		dist := map[int]int{src: 0}
		q := []int{src}
		for len(q) > 0 {
			u := q[0]
			q = q[1:]
			for _, v := range adj[u] {
				if mask>>v&1 == 1 {
					if _, ok := dist[v]; !ok {
						dist[v] = dist[u] + 1
						q = append(q, v)
					}
				}
			}
		}
		far := src
		for node, d := range dist {
			if d > dist[far] {
				far = node
			}
		}
		return far, dist
	}
	bitCount := func(x int) int {
		c := 0
		for x > 0 {
			c++
			x &= x - 1
		}
		return c
	}
	for mask := 1; mask < 1<<n; mask++ {
		if mask&(mask-1) == 0 {
			continue
		}
		start := 0
		for (mask>>start)&1 == 0 {
			start++
		}
		far, seen := bfs(mask, start)
		if len(seen) == bitCount(mask) {
			_, dist := bfs(mask, far)
			mx := 0
			for _, d := range dist {
				if d > mx {
					mx = d
				}
			}
			ans[mx-1]++
		}
	}
	return ans
}
'''

SOLUTIONS["1618_maximum_font_to_fit_a_sentence_in_a_screen"] = r'''// LeetCode 1618 - Maximum Font to Fit a Sentence in a Screen
// https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/

type FontInfo interface {
	GetWidth(fontSize int, ch byte) int
	GetHeight(fontSize int) int
}

type defaultFontInfo struct{}

func (defaultFontInfo) GetWidth(fontSize int, ch byte) int { return fontSize }
func (defaultFontInfo) GetHeight(fontSize int) int         { return fontSize }

func maxFont(text string, w int, h int, fonts []int, fontInfo FontInfo) int {
	if fontInfo == nil {
		fontInfo = defaultFontInfo{}
	}
	lo, hi, ans := 0, len(fonts)-1, -1
	for lo <= hi {
		mid := (lo + hi) / 2
		f := fonts[mid]
		fits := fontInfo.GetHeight(f) <= h
		if fits {
			width := 0
			for i := 0; i < len(text); i++ {
				width += fontInfo.GetWidth(f, text[i])
			}
			fits = width <= w
		}
		if fits {
			ans = f
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return ans
}
'''

SOLUTIONS["1619_mean_of_array_after_removing_some_elements"] = r'''// LeetCode 1619 - Mean of Array After Removing Some Elements
// https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

import "sort"

func trimMean(arr []int) float64 {
	sort.Ints(arr)
	k := len(arr) / 20
	sum := 0
	for i := k; i < len(arr)-k; i++ {
		sum += arr[i]
	}
	return float64(sum) / float64(len(arr)-2*k)
}
'''

SOLUTIONS["1620_coordinate_with_maximum_network_quality"] = r'''// LeetCode 1620 - Coordinate With Maximum Network Quality
// https://leetcode.com/problems/coordinate-with-maximum-network-quality/

import "math"

func bestCoordinate(towers [][]int, radius int) []int {
	best := []int{0, 0}
	quality := -1
	for x := 0; x <= 50; x++ {
		for y := 0; y <= 50; y++ {
			q := 0
			for _, t := range towers {
				d := math.Hypot(float64(x-t[0]), float64(y-t[1]))
				if d <= float64(radius) {
					q += int(float64(t[2]) / (1 + d))
				}
			}
			if q > quality {
				quality = q
				best = []int{x, y}
			}
		}
	}
	return best
}
'''

SOLUTIONS["1621_number_of_sets_of_k_non_overlapping_line_segments"] = r'''// LeetCode 1621 - Number of Sets of K Non-Overlapping Line Segments
// https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

func numberOfSets(n int, k int) int {
	const mod = 1000000007
	return comb1621(n+k-1, 2*k, mod)
}

func comb1621(n, r, mod int) int {
	if r < 0 || r > n {
		return 0
	}
	if r > n-r {
		r = n - r
	}
	num, den := 1, 1
	for i := 0; i < r; i++ {
		num = num * (n - i) % mod
		den = den * (i + 1) % mod
	}
	return num * modInverse1621(den, mod) % mod
}

func modInverse1621(a, mod int) int {
	return modPow1621(a, mod-2, mod)
}

func modPow1621(base, exp, mod int) int {
	res := 1
	base %= mod
	for exp > 0 {
		if exp&1 == 1 {
			res = res * base % mod
		}
		base = base * base % mod
		exp >>= 1
	}
	return res
}
'''

SOLUTIONS["1622_fancy_sequence"] = r'''// LeetCode 1622 - Fancy Sequence
// https://leetcode.com/problems/fancy-sequence/

type Fancy struct {
	vals []int
	mul  int
	add  int
}

const fancyMod = 1000000007

func Constructor() Fancy {
	return Fancy{mul: 1, add: 0}
}

func (this *Fancy) Append(val int) {
	inv := fancyModPow(this.mul, fancyMod-2)
	v := ((val-this.add)%fancyMod+fancyMod)%fancyMod * inv % fancyMod
	this.vals = append(this.vals, v)
}

func (this *Fancy) AddAll(inc int) {
	if len(this.vals) > 0 {
		this.add = (this.add + inc) % fancyMod
	}
}

func (this *Fancy) MultAll(m int) {
	if len(this.vals) == 0 {
		return
	}
	this.mul = this.mul * m % fancyMod
	this.add = this.add * m % fancyMod
}

func (this *Fancy) GetIndex(idx int) int {
	if idx >= len(this.vals) {
		return -1
	}
	return (this.vals[idx]*this.mul + this.add) % fancyMod
}

func fancyModPow(base, exp int) int {
	res := 1
	base %= fancyMod
	for exp > 0 {
		if exp&1 == 1 {
			res = res * base % fancyMod
		}
		base = base * base % fancyMod
		exp >>= 1
	}
	return res
}
'''

SOLUTIONS["1624_largest_substring_between_two_equal_characters"] = r'''// LeetCode 1624 - Largest Substring Between Two Equal Characters
// https://leetcode.com/problems/largest-substring-between-two-equal-characters/

func maxLengthBetweenEqualCharacters(s string) int {
	first := map[byte]int{}
	ans := -1
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if j, ok := first[ch]; ok {
			if i-j-1 > ans {
				ans = i - j - 1
			}
		} else {
			first[ch] = i
		}
	}
	return ans
}
'''

SOLUTIONS["1625_lexicographically_smallest_string_after_applying_operations"] = r'''// LeetCode 1625 - Lexicographically Smallest String After Applying Operations
// https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

func findLexSmallestString(s string, a int, b int) string {
	seen := map[string]bool{s: true}
	q := []string{s}
	ans := s
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		if cur < ans {
			ans = cur
		}
		bytes := []byte(cur)
		for i := 1; i < len(bytes); i += 2 {
			bytes[i] = byte((int(bytes[i]-'0')+a)%10 + '0')
		}
		add := string(bytes)
		rot := cur[len(cur)-b:] + cur[:len(cur)-b]
		for _, nxt := range []string{add, rot} {
			if !seen[nxt] {
				seen[nxt] = true
				q = append(q, nxt)
			}
		}
	}
	return ans
}
'''

SOLUTIONS["1626_best_team_with_no_conflicts"] = r'''// LeetCode 1626 - Best Team With No Conflicts
// https://leetcode.com/problems/best-team-with-no-conflicts/

import "sort"

func bestTeamScore(scores []int, ages []int) int {
	n := len(scores)
	players := make([][2]int, n)
	for i := 0; i < n; i++ {
		players[i] = [2]int{ages[i], scores[i]}
	}
	sort.Slice(players, func(i, j int) bool {
		if players[i][0] == players[j][0] {
			return players[i][1] < players[j][1]
		}
		return players[i][0] < players[j][0]
	})
	dp := make([]int, n)
	ans := 0
	for i := 0; i < n; i++ {
		dp[i] = players[i][1]
		for j := 0; j < i; j++ {
			if players[j][1] <= players[i][1] && dp[j]+players[i][1] > dp[i] {
				dp[i] = dp[j] + players[i][1]
			}
		}
		if dp[i] > ans {
			ans = dp[i]
		}
	}
	return ans
}
'''

SOLUTIONS["1627_graph_connectivity_with_threshold"] = r'''// LeetCode 1627 - Graph Connectivity With Threshold
// https://leetcode.com/problems/graph-connectivity-with-threshold/

func areConnected(n int, threshold int, queries [][]int) []bool {
	parent := make([]int, n+1)
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
	for d := threshold + 1; d <= n; d++ {
		for x := 2 * d; x <= n; x += d {
			a, b := find(d), find(x)
			if a != b {
				parent[b] = a
			}
		}
	}
	ans := make([]bool, len(queries))
	for i, q := range queries {
		ans[i] = find(q[0]) == find(q[1])
	}
	return ans
}
'''

SOLUTIONS["1628_design_an_expression_tree_with_evaluate_function"] = r'''// LeetCode 1628 - Design an Expression Tree With Evaluate Function
// https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

import "strconv"

type Node struct {
	Val   string
	Left  *Node
	Right *Node
}

func (this *Node) Evaluate() int {
	if this.Val != "+" && this.Val != "-" && this.Val != "*" && this.Val != "/" {
		v, _ := strconv.Atoi(this.Val)
		return v
	}
	a, b := this.Left.Evaluate(), this.Right.Evaluate()
	switch this.Val {
	case "+":
		return a + b
	case "-":
		return a - b
	case "*":
		return a * b
	default:
		return a / b
	}
}

type TreeBuilder struct{}

func Constructor() TreeBuilder {
	return TreeBuilder{}
}

func (this *TreeBuilder) ExpTree(postfix []string) *Node {
	stack := []*Node{}
	for _, token := range postfix {
		node := &Node{Val: token}
		if token == "+" || token == "-" || token == "*" || token == "/" {
			node.Right = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			node.Left = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, node)
	}
	return stack[len(stack)-1]
}
'''

SOLUTIONS["1629_slowest_key"] = r'''// LeetCode 1629 - Slowest Key
// https://leetcode.com/problems/slowest-key/

func slowestKey(releaseTimes []int, keysPressed string) byte {
	bestDur := releaseTimes[0]
	bestKey := keysPressed[0]
	for i := 1; i < len(releaseTimes); i++ {
		dur := releaseTimes[i] - releaseTimes[i-1]
		if dur > bestDur || (dur == bestDur && keysPressed[i] > bestKey) {
			bestDur = dur
			bestKey = keysPressed[i]
		}
	}
	return bestKey
}
'''

SOLUTIONS["1630_arithmetic_subarrays"] = r'''// LeetCode 1630 - Arithmetic Subarrays
// https://leetcode.com/problems/arithmetic-subarrays/

import "sort"

func checkArithmeticSubarrays(nums []int, l []int, r []int) []bool {
	ans := make([]bool, len(l))
	for i := range l {
		a, b := l[i], r[i]
		x := append([]int{}, nums[a:b+1]...)
		sort.Ints(x)
		ok := true
		if len(x) >= 3 {
			diff := x[1] - x[0]
			for j := 2; j < len(x); j++ {
				if x[j]-x[j-1] != diff {
					ok = false
					break
				}
			}
		}
		ans[i] = ok
	}
	return ans
}
'''

SOLUTIONS["1631_path_with_minimum_effort"] = r'''// LeetCode 1631 - Path With Minimum Effort
// https://leetcode.com/problems/path-with-minimum-effort/

import "container/heap"

type effortItem struct {
	effort, i, j int
}

type effortHeap []effortItem

func (h effortHeap) Len() int            { return len(h) }
func (h effortHeap) Less(i, j int) bool  { return h[i].effort < h[j].effort }
func (h effortHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *effortHeap) Push(x interface{}) { *h = append(*h, x.(effortItem)) }
func (h *effortHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minimumEffortPath(heights [][]int) int {
	m, n := len(heights), len(heights[0])
	dist := make([][]int, m)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			dist[i][j] = 1 << 30
		}
	}
	dist[0][0] = 0
	h := &effortHeap{{0, 0, 0}}
	heap.Init(h)
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for h.Len() > 0 {
		cur := heap.Pop(h).(effortItem)
		if cur.i == m-1 && cur.j == n-1 {
			return cur.effort
		}
		if cur.effort != dist[cur.i][cur.j] {
			continue
		}
		for _, d := range dirs {
			x, y := cur.i+d[0], cur.j+d[1]
			if x >= 0 && x < m && y >= 0 && y < n {
				diff := heights[cur.i][cur.j] - heights[x][y]
				if diff < 0 {
					diff = -diff
				}
				nd := cur.effort
				if diff > nd {
					nd = diff
				}
				if nd < dist[x][y] {
					dist[x][y] = nd
					heap.Push(h, effortItem{nd, x, y})
				}
			}
		}
	}
	return 0
}
'''

SOLUTIONS["1632_rank_transform_of_a_matrix"] = r'''// LeetCode 1632 - Rank Transform of a Matrix
// https://leetcode.com/problems/rank-transform-of-a-matrix/

import "sort"

func matrixRankTransform(matrix [][]int) [][]int {
	m, n := len(matrix), len(matrix[0])
	type pair struct{ i, j int }
	groups := map[int][]pair{}
	vals := []int{}
	seen := map[int]bool{}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			v := matrix[i][j]
			groups[v] = append(groups[v], pair{i, j})
			if !seen[v] {
				seen[v] = true
				vals = append(vals, v)
			}
		}
	}
	sort.Ints(vals)
	rank := make([]int, m+n)
	ans := make([][]int, m)
	for i := range ans {
		ans[i] = make([]int, n)
	}
	for _, value := range vals {
		parent := map[int]int{}
		var find func(int) int
		find = func(x int) int {
			if _, ok := parent[x]; !ok {
				parent[x] = x
			}
			if parent[x] != x {
				parent[x] = find(parent[x])
			}
			return parent[x]
		}
		for _, p := range groups[value] {
			a, b := find(p.i), find(m+p.j)
			parent[a] = b
		}
		best := map[int]int{}
		for _, p := range groups[value] {
			r := find(p.i)
			cur := rank[p.i]
			if rank[m+p.j] > cur {
				cur = rank[m+p.j]
			}
			if cur > best[r] {
				best[r] = cur
			}
		}
		for _, p := range groups[value] {
			r := best[find(p.i)] + 1
			ans[p.i][p.j] = r
		}
		for _, p := range groups[value] {
			if ans[p.i][p.j] > rank[p.i] {
				rank[p.i] = ans[p.i][p.j]
			}
			if ans[p.i][p.j] > rank[m+p.j] {
				rank[m+p.j] = ans[p.i][p.j]
			}
		}
	}
	return ans
}
'''

SOLUTIONS["1634_add_two_polynomials_represented_as_linked_lists"] = r'''// LeetCode 1634 - Add Two Polynomials Represented as Linked Lists
// https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/

type PolyNode struct {
	Coefficient int
	Power       int
	Next        *PolyNode
}

func addPoly(poly1 *PolyNode, poly2 *PolyNode) *PolyNode {
	dummy := &PolyNode{}
	cur := dummy
	for poly1 != nil || poly2 != nil {
		var c, p int
		if poly2 == nil || (poly1 != nil && poly1.Power > poly2.Power) {
			c, p = poly1.Coefficient, poly1.Power
			poly1 = poly1.Next
		} else if poly1 == nil || poly2.Power > poly1.Power {
			c, p = poly2.Coefficient, poly2.Power
			poly2 = poly2.Next
		} else {
			c, p = poly1.Coefficient+poly2.Coefficient, poly1.Power
			poly1 = poly1.Next
			poly2 = poly2.Next
		}
		if c != 0 {
			cur.Next = &PolyNode{Coefficient: c, Power: p}
			cur = cur.Next
		}
	}
	return dummy.Next
}
'''

SOLUTIONS["1636_sort_array_by_increasing_frequency"] = r'''// LeetCode 1636 - Sort Array by Increasing Frequency
// https://leetcode.com/problems/sort-array-by-increasing-frequency/

import "sort"

func frequencySort(nums []int) []int {
	count := map[int]int{}
	for _, x := range nums {
		count[x]++
	}
	sort.Slice(nums, func(i, j int) bool {
		if count[nums[i]] == count[nums[j]] {
			return nums[i] > nums[j]
		}
		return count[nums[i]] < count[nums[j]]
	})
	return nums
}
'''

SOLUTIONS["1637_widest_vertical_area_between_two_points_containing_no_points"] = r'''// LeetCode 1637 - Widest Vertical Area Between Two Points Containing No Points
// https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

import "sort"

func maxWidthOfVerticalArea(points [][]int) int {
	xs := make([]int, len(points))
	for i, p := range points {
		xs[i] = p[0]
	}
	sort.Ints(xs)
	ans := 0
	for i := 1; i < len(xs); i++ {
		if xs[i]-xs[i-1] > ans {
			ans = xs[i] - xs[i-1]
		}
	}
	return ans
}
'''

SOLUTIONS["1638_count_substrings_that_differ_by_one_character"] = r'''// LeetCode 1638 - Count Substrings That Differ by One Character
// https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

func countSubstrings(s string, t string) int {
	ans := 0
	for i := 0; i < len(s); i++ {
		for j := 0; j < len(t); j++ {
			diff := 0
			for k := 0; i+k < len(s) && j+k < len(t); k++ {
				if s[i+k] != t[j+k] {
					diff++
				}
				if diff == 1 {
					ans++
				} else if diff > 1 {
					break
				}
			}
		}
	}
	return ans
}
'''

SOLUTIONS["1639_number_of_ways_to_form_a_target_string_given_a_dictionary"] = r'''// LeetCode 1639 - Number of Ways to Form a Target String Given a Dictionary
// https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

func numWays(words []string, target string) int {
	const mod = 1000000007
	m := len(words[0])
	dp := make([]int, len(target)+1)
	dp[0] = 1
	for j := 0; j < m; j++ {
		count := [26]int{}
		for _, word := range words {
			count[word[j]-'a']++
		}
		lim := j + 1
		if lim > len(target) {
			lim = len(target)
		}
		for i := lim; i > 0; i-- {
			dp[i] = (dp[i] + dp[i-1]*count[target[i-1]-'a']) % mod
		}
	}
	return dp[len(target)]
}
'''

SOLUTIONS["1640_check_array_formation_through_concatenation"] = r'''// LeetCode 1640 - Check Array Formation Through Concatenation
// https://leetcode.com/problems/check-array-formation-through-concatenation/

func canFormArray(arr []int, pieces [][]int) bool {
	byFirst := map[int][]int{}
	for _, p := range pieces {
		byFirst[p[0]] = p
	}
	i := 0
	for i < len(arr) {
		p, ok := byFirst[arr[i]]
		if !ok {
			return false
		}
		for _, v := range p {
			if i >= len(arr) || arr[i] != v {
				return false
			}
			i++
		}
	}
	return true
}
'''

SOLUTIONS["1641_count_sorted_vowel_strings"] = r'''// LeetCode 1641 - Count Sorted Vowel Strings
// https://leetcode.com/problems/count-sorted-vowel-strings/

func countVowelStrings(n int) int {
	return comb1641(n+4, 4)
}

func comb1641(n, r int) int {
	if r > n-r {
		r = n - r
	}
	res := 1
	for i := 0; i < r; i++ {
		res = res * (n - i) / (i + 1)
	}
	return res
}
'''

SOLUTIONS["1642_furthest_building_you_can_reach"] = r'''// LeetCode 1642 - Furthest Building You Can Reach
// https://leetcode.com/problems/furthest-building-you-can-reach/

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

func furthestBuilding(heights []int, bricks int, ladders int) int {
	climbs := &intHeap{}
	heap.Init(climbs)
	for i := 0; i+1 < len(heights); i++ {
		d := heights[i+1] - heights[i]
		if d <= 0 {
			continue
		}
		heap.Push(climbs, d)
		if climbs.Len() > ladders {
			bricks -= heap.Pop(climbs).(int)
		}
		if bricks < 0 {
			return i
		}
	}
	return len(heights) - 1
}
'''

SOLUTIONS["1643_kth_smallest_instructions"] = r'''// LeetCode 1643 - Kth Smallest Instructions
// https://leetcode.com/problems/kth-smallest-instructions/

func kthSmallestPath(destination []int, k int) string {
	v, h := destination[0], destination[1]
	ans := make([]byte, 0, v+h)
	for h+v > 0 {
		if h > 0 {
			count := comb1643(h+v-1, v)
			if k <= count {
				ans = append(ans, 'H')
				h--
				continue
			}
			k -= count
		}
		ans = append(ans, 'V')
		v--
	}
	return string(ans)
}

func comb1643(n, r int) int {
	if r < 0 || r > n {
		return 0
	}
	if r > n-r {
		r = n - r
	}
	res := 1
	for i := 0; i < r; i++ {
		res = res * (n - i) / (i + 1)
	}
	return res
}
'''

SOLUTIONS["1644_lowest_common_ancestor_of_a_binary_tree_ii"] = r'''// LeetCode 1644 - Lowest Common Ancestor of a Binary Tree II
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	found := 0
	var dfs func(*TreeNode) *TreeNode
	dfs = func(node *TreeNode) *TreeNode {
		if node == nil {
			return nil
		}
		left := dfs(node.Left)
		right := dfs(node.Right)
		if node == p || node == q {
			found++
			return node
		}
		if left != nil && right != nil {
			return node
		}
		if left != nil {
			return left
		}
		return right
	}
	ans := dfs(root)
	if found == 2 {
		return ans
	}
	return nil
}
'''

SOLUTIONS["1646_get_maximum_in_generated_array"] = r'''// LeetCode 1646 - Get Maximum in Generated Array
// https://leetcode.com/problems/get-maximum-in-generated-array/

func getMaximumGenerated(n int) int {
	if n < 2 {
		return n
	}
	a := make([]int, n+1)
	a[1] = 1
	ans := 1
	for i := 2; i <= n; i++ {
		if i%2 == 0 {
			a[i] = a[i/2]
		} else {
			a[i] = a[i/2] + a[i/2+1]
		}
		if a[i] > ans {
			ans = a[i]
		}
	}
	return ans
}
'''

SOLUTIONS["1647_minimum_deletions_to_make_character_frequencies_unique"] = r'''// LeetCode 1647 - Minimum Deletions to Make Character Frequencies Unique
// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

func minDeletions(s string) int {
	freq := [26]int{}
	for i := 0; i < len(s); i++ {
		freq[s[i]-'a']++
	}
	used := map[int]bool{}
	ans := 0
	for _, x := range freq {
		for x > 0 && used[x] {
			x--
			ans++
		}
		if x > 0 {
			used[x] = true
		}
	}
	return ans
}
'''

SOLUTIONS["1648_sell_diminishing_valued_colored_balls"] = r'''// LeetCode 1648 - Sell Diminishing-Valued Colored Balls
// https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

import "sort"

func maxProfit(inventory []int, orders int) int {
	const mod = 1000000007
	sort.Sort(sort.Reverse(sort.IntSlice(inventory)))
	inventory = append(inventory, 0)
	ans := 0
	for i := 0; i+1 < len(inventory); i++ {
		width := i + 1
		high, low := inventory[i], inventory[i+1]
		balls := width * (high - low)
		take := orders
		if balls < take {
			take = balls
		}
		full := take / width
		rem := take % width
		bottom := high - full
		ans += width*(high+bottom+1)*full/2 + rem*bottom
		ans %= mod
		orders -= take
		if orders == 0 {
			break
		}
	}
	return ans
}
'''

SOLUTIONS["1649_create_sorted_array_through_instructions"] = r'''// LeetCode 1649 - Create Sorted Array through Instructions
// https://leetcode.com/problems/create-sorted-array-through-instructions/

func createSortedArray(instructions []int) int {
	const mod = 1000000007
	mx := 0
	for _, x := range instructions {
		if x > mx {
			mx = x
		}
	}
	size := mx + 2
	bit := make([]int, size+1)
	query := func(i int) int {
		s := 0
		for i > 0 {
			s += bit[i]
			i -= i & -i
		}
		return s
	}
	update := func(j int) {
		for j <= size {
			bit[j]++
			j += j & -j
		}
	}
	ans := 0
	for i, x := range instructions {
		less := query(x - 1)
		greater := i - query(x)
		if less < greater {
			ans = (ans + less) % mod
		} else {
			ans = (ans + greater) % mod
		}
		update(x)
	}
	return ans
}
'''


def main() -> None:
    written = []
    for folder, src in sorted(SOLUTIONS.items()):
        path = ROOT / folder / "solution.go"
        if not path.parent.exists():
            raise SystemExit(f"missing folder: {folder}")
        # Match 1801 style: imports allowed without package clause.
        path.write_text(src, encoding="utf-8", newline="\n")
        written.append(folder)
    print(f"wrote {len(written)} solution.go files")
    for w in written:
        print(w)


if __name__ == "__main__":
    main()
