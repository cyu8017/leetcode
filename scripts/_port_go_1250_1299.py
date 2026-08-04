#!/usr/bin/env python3
"""Write Go solutions for folders 1250-1299."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(r"c:\Users\Charlie Yu\Documents\leetcode")
SOLUTIONS: dict[str, str] = {}

SOLUTIONS["1250_check_if_it_is_a_good_array"] = r'''// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

func isGoodArray(nums []int) bool {
	g := nums[0]
	for i := 1; i < len(nums); i++ {
		g = gcd(g, nums[i])
	}
	return g == 1
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
'''

SOLUTIONS["1252_cells_with_odd_values_in_a_matrix"] = r'''// LeetCode 1252 - Cells with Odd Values in a Matrix
// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

func oddCells(m int, n int, indices [][]int) int {
	rows := make([]int, m)
	cols := make([]int, n)
	for _, idx := range indices {
		rows[idx[0]] ^= 1
		cols[idx[1]] ^= 1
	}
	ans := 0
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			ans += rows[r] ^ cols[c]
		}
	}
	return ans
}
'''

SOLUTIONS["1253_reconstruct_a_2_row_binary_matrix"] = r'''// LeetCode 1253 - Reconstruct a 2-Row Binary Matrix
// https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

func reconstructMatrix(upper int, lower int, colsum []int) [][]int {
	top := make([]int, len(colsum))
	bottom := make([]int, len(colsum))
	for i, value := range colsum {
		if value == 2 {
			top[i], bottom[i] = 1, 1
			upper--
			lower--
		}
	}
	if upper < 0 || lower < 0 {
		return [][]int{}
	}
	for i, value := range colsum {
		if value == 1 {
			if upper > 0 {
				top[i] = 1
				upper--
			} else if lower > 0 {
				bottom[i] = 1
				lower--
			} else {
				return [][]int{}
			}
		}
	}
	if upper == 0 && lower == 0 {
		return [][]int{top, bottom}
	}
	return [][]int{}
}
'''

SOLUTIONS["1254_number_of_closed_islands"] = r'''// LeetCode 1254 - Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/

func closedIsland(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	flood := func(sr, sc int) bool {
		stack := [][2]int{{sr, sc}}
		grid[sr][sc] = 1
		closed := true
		for len(stack) > 0 {
			cur := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			r, c := cur[0], cur[1]
			if r == 0 || r == m-1 || c == 0 || c == n-1 {
				closed = false
			}
			for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
				nr, nc := r+d[0], c+d[1]
				if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 0 {
					grid[nr][nc] = 1
					stack = append(stack, [2]int{nr, nc})
				}
			}
		}
		return closed
	}
	ans := 0
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			if grid[r][c] == 0 && flood(r, c) {
				ans++
			}
		}
	}
	return ans
}
'''

SOLUTIONS["1255_maximum_score_words_formed_by_letters"] = r'''// LeetCode 1255 - Maximum Score Words Formed by Letters
// https://leetcode.com/problems/maximum-score-words-formed-by-letters/

func maxScoreWords(words []string, letters []byte, score []int) int {
	available := [26]int{}
	for _, ch := range letters {
		available[ch-'a']++
	}
	counts := make([][26]int, len(words))
	values := make([]int, len(words))
	for i, word := range words {
		for j := 0; j < len(word); j++ {
			counts[i][word[j]-'a']++
			values[i] += score[word[j]-'a']
		}
	}
	var dfs func(int) int
	dfs = func(i int) int {
		if i == len(words) {
			return 0
		}
		best := dfs(i + 1)
		ok := true
		for c := 0; c < 26; c++ {
			if counts[i][c] > available[c] {
				ok = false
				break
			}
		}
		if ok {
			for c := 0; c < 26; c++ {
				available[c] -= counts[i][c]
			}
			v := values[i] + dfs(i+1)
			if v > best {
				best = v
			}
			for c := 0; c < 26; c++ {
				available[c] += counts[i][c]
			}
		}
		return best
	}
	return dfs(0)
}
'''

SOLUTIONS["1256_encode_number"] = r'''// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

func encode(num int) string {
	num++
	bits := ""
	for num > 0 {
		bits = string('0'+byte(num%2)) + bits
		num /= 2
	}
	if len(bits) <= 1 {
		return ""
	}
	return bits[1:]
}
'''

SOLUTIONS["1257_smallest_common_region"] = r'''// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

func findSmallestRegion(regions [][]string, region1 string, region2 string) string {
	parent := map[string]string{}
	for _, group := range regions {
		for _, child := range group[1:] {
			parent[child] = group[0]
		}
	}
	ancestors := map[string]bool{}
	for region1 != "" {
		ancestors[region1] = true
		region1 = parent[region1]
	}
	for !ancestors[region2] {
		region2 = parent[region2]
	}
	return region2
}
'''

SOLUTIONS["1258_synonymous_sentences"] = r'''// LeetCode 1258 - Synonymous Sentences
// https://leetcode.com/problems/synonymous-sentences/

import "sort"
import "strings"

func generateSentences(synonyms [][]string, text string) []string {
	parent := map[string]string{}
	var find func(string) string
	find = func(x string) string {
		if _, ok := parent[x]; !ok {
			parent[x] = x
		}
		if parent[x] != x {
			parent[x] = find(parent[x])
		}
		return parent[x]
	}
	for _, pair := range synonyms {
		ra, rb := find(pair[0]), find(pair[1])
		parent[ra] = rb
	}
	groups := map[string][]string{}
	for word := range parent {
		r := find(word)
		groups[r] = append(groups[r], word)
	}
	for r := range groups {
		sort.Strings(groups[r])
	}
	words := strings.Fields(text)
	choices := make([][]string, len(words))
	for i, w := range words {
		if _, ok := parent[w]; ok {
			choices[i] = groups[find(w)]
		} else {
			choices[i] = []string{w}
		}
	}
	ans := []string{}
	var dfs func(int, []string)
	dfs = func(i int, cur []string) {
		if i == len(choices) {
			ans = append(ans, strings.Join(cur, " "))
			return
		}
		for _, w := range choices[i] {
			dfs(i+1, append(cur, w))
		}
	}
	dfs(0, nil)
	return ans
}
'''

SOLUTIONS["1259_handshakes_that_dont_cross"] = r'''// LeetCode 1259 - Handshakes That Don't Cross
// https://leetcode.com/problems/handshakes-that-dont-cross/

func numberOfWays(numPeople int) int {
	const mod = 1000000007
	dp := make([]int, numPeople+1)
	dp[0] = 1
	for people := 2; people <= numPeople; people += 2 {
		sum := 0
		for left := 0; left < people; left += 2 {
			sum = (sum + dp[left]*dp[people-2-left]) % mod
		}
		dp[people] = sum
	}
	return dp[numPeople]
}
'''

SOLUTIONS["1260_shift_2d_grid"] = r'''// LeetCode 1260 - Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/

func shiftGrid(grid [][]int, k int) [][]int {
	m, n := len(grid), len(grid[0])
	flat := make([]int, 0, m*n)
	for _, row := range grid {
		flat = append(flat, row...)
	}
	k %= len(flat)
	if k > 0 {
		flat = append(flat[len(flat)-k:], flat[:len(flat)-k]...)
	}
	ans := make([][]int, m)
	for i := 0; i < m; i++ {
		ans[i] = flat[i*n : (i+1)*n]
	}
	return ans
}
'''

SOLUTIONS["1261_find_elements_in_a_contaminated_binary_tree"] = r'''// LeetCode 1261 - Find Elements in a Contaminated Binary Tree
// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type FindElements struct {
	values map[int]bool
}

func Constructor(root *TreeNode) FindElements {
	fe := FindElements{values: map[int]bool{}}
	var recover func(*TreeNode, int)
	recover = func(node *TreeNode, value int) {
		if node == nil {
			return
		}
		node.Val = value
		fe.values[value] = true
		recover(node.Left, 2*value+1)
		recover(node.Right, 2*value+2)
	}
	recover(root, 0)
	return fe
}

func (this *FindElements) Find(target int) bool {
	return this.values[target]
}
'''

SOLUTIONS["1262_greatest_sum_divisible_by_three"] = r'''// LeetCode 1262 - Greatest Sum Divisible by Three
// https://leetcode.com/problems/greatest-sum-divisible-by-three/

func maxSumDivThree(nums []int) int {
	const impossible = -1e18
	dp := [3]int{0, impossible, impossible}
	for _, value := range nums {
		old := dp
		for _, total := range old {
			if total == impossible {
				continue
			}
			rem := (total + value) % 3
			if total+value > dp[rem] {
				dp[rem] = total + value
			}
		}
	}
	return dp[0]
}
'''

SOLUTIONS["1263_minimum_moves_to_move_a_box_to_their_target_location"] = r'''// LeetCode 1263 - Minimum Moves to Move a Box to Their Target Location
// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

func minPushBox(grid [][]byte) int {
	m, n := len(grid), len(grid[0])
	var box, player, target [2]int
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			switch grid[r][c] {
			case 'B':
				box = [2]int{r, c}
			case 'S':
				player = [2]int{r, c}
			case 'T':
				target = [2]int{r, c}
			}
		}
	}
	reachable := func(start, blocked [2]int) map[[2]int]bool {
		seen := map[[2]int]bool{start: true}
		stack := [][2]int{start}
		for len(stack) > 0 {
			cur := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
				nxt := [2]int{cur[0] + d[0], cur[1] + d[1]}
				if nxt[0] >= 0 && nxt[0] < m && nxt[1] >= 0 && nxt[1] < n &&
					grid[nxt[0]][nxt[1]] != '#' && nxt != blocked && !seen[nxt] {
					seen[nxt] = true
					stack = append(stack, nxt)
				}
			}
		}
		return seen
	}
	type state struct {
		b, p [2]int
	}
	type item struct {
		b, p  [2]int
		push  int
	}
	q := []item{{box, player, 0}}
	seen := map[state]bool{{box, player}: true}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		if cur.b == target {
			return cur.push
		}
		can := reachable(cur.p, cur.b)
		for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
			stand := [2]int{cur.b[0] - d[0], cur.b[1] - d[1]}
			nb := [2]int{cur.b[0] + d[0], cur.b[1] + d[1]}
			if can[stand] && nb[0] >= 0 && nb[0] < m && nb[1] >= 0 && nb[1] < n && grid[nb[0]][nb[1]] != '#' {
				st := state{nb, cur.b}
				if !seen[st] {
					seen[st] = true
					q = append(q, item{nb, cur.b, cur.push + 1})
				}
			}
		}
	}
	return -1
}
'''

SOLUTIONS["1265_print_immutable_linked_list_in_reverse"] = r'''// LeetCode 1265 - Print Immutable Linked List in Reverse
// https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

type ImmutableListNode interface {
	GetNext() ImmutableListNode
	PrintValue()
}

func printLinkedListInReverse(head ImmutableListNode) {
	if head == nil {
		return
	}
	printLinkedListInReverse(head.GetNext())
	head.PrintValue()
}
'''

SOLUTIONS["1266_minimum_time_visiting_all_points"] = r'''// LeetCode 1266 - Minimum Time Visiting All Points
// https://leetcode.com/problems/minimum-time-visiting-all-points/

func minTimeToVisitAllPoints(points [][]int) int {
	ans := 0
	for i := 1; i < len(points); i++ {
		dx := points[i][0] - points[i-1][0]
		if dx < 0 {
			dx = -dx
		}
		dy := points[i][1] - points[i-1][1]
		if dy < 0 {
			dy = -dy
		}
		if dx > dy {
			ans += dx
		} else {
			ans += dy
		}
	}
	return ans
}
'''

SOLUTIONS["1267_count_servers_that_communicate"] = r'''// LeetCode 1267 - Count Servers that Communicate
// https://leetcode.com/problems/count-servers-that-communicate/

func countServers(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	rows := make([]int, m)
	cols := make([]int, n)
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			rows[r] += grid[r][c]
			cols[c] += grid[r][c]
		}
	}
	ans := 0
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			if grid[r][c] == 1 && (rows[r] > 1 || cols[c] > 1) {
				ans++
			}
		}
	}
	return ans
}
'''

SOLUTIONS["1268_search_suggestions_system"] = r'''// LeetCode 1268 - Search Suggestions System
// https://leetcode.com/problems/search-suggestions-system/

import "sort"
import "strings"

func suggestedProducts(products []string, searchWord string) [][]string {
	sort.Strings(products)
	ans := make([][]string, 0, len(searchWord))
	prefix := ""
	for i := 0; i < len(searchWord); i++ {
		prefix += string(searchWord[i])
		idx := sort.SearchStrings(products, prefix)
		group := []string{}
		for j := idx; j < len(products) && j < idx+3; j++ {
			if strings.HasPrefix(products[j], prefix) {
				group = append(group, products[j])
			}
		}
		ans = append(ans, group)
	}
	return ans
}
'''

SOLUTIONS["1269_number_of_ways_to_stay_in_the_same_place_after_some_steps"] = r'''// LeetCode 1269 - Number of Ways to Stay in the Same Place After Some Steps
// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

func numWays(steps int, arrLen int) int {
	const mod = 1000000007
	width := arrLen
	if steps/2+1 < width {
		width = steps/2 + 1
	}
	dp := make([]int, width)
	dp[0] = 1
	for step := 0; step < steps; step++ {
		nxt := make([]int, width)
		for i := 0; i < width; i++ {
			nxt[i] = dp[i]
			if i > 0 {
				nxt[i] = (nxt[i] + dp[i-1]) % mod
			}
			if i+1 < width {
				nxt[i] = (nxt[i] + dp[i+1]) % mod
			}
		}
		dp = nxt
	}
	return dp[0]
}
'''

SOLUTIONS["1271_hexspeak"] = r'''// LeetCode 1271 - Hexspeak
// https://leetcode.com/problems/hexspeak/

import "strconv"

func toHexspeak(num string) string {
	value, _ := strconv.ParseInt(num, 10, 64)
	digits := "0123456789ABCDEF"
	out := ""
	if value == 0 {
		return "O"
	}
	for value > 0 {
		rem := value % 16
		if rem >= 2 && rem <= 9 {
			return "ERROR"
		}
		out = string(digits[rem]) + out
		value /= 16
	}
	b := []byte(out)
	for i := range b {
		if b[i] == '0' {
			b[i] = 'O'
		} else if b[i] == '1' {
			b[i] = 'I'
		}
	}
	return string(b)
}
'''

SOLUTIONS["1272_remove_interval"] = r'''// LeetCode 1272 - Remove Interval
// https://leetcode.com/problems/remove-interval/

func removeInterval(intervals [][]int, toBeRemoved []int) [][]int {
	left, right := toBeRemoved[0], toBeRemoved[1]
	ans := [][]int{}
	for _, iv := range intervals {
		start, end := iv[0], iv[1]
		if end <= left || start >= right {
			ans = append(ans, []int{start, end})
		} else {
			if start < left {
				ans = append(ans, []int{start, left})
			}
			if end > right {
				ans = append(ans, []int{right, end})
			}
		}
	}
	return ans
}
'''

SOLUTIONS["1273_delete_tree_nodes"] = r'''// LeetCode 1273 - Delete Tree Nodes
// https://leetcode.com/problems/delete-tree-nodes/

func deleteTreeNodes(nodes int, parent []int, value []int) int {
	children := make([][]int, nodes)
	for node := 1; node < nodes; node++ {
		children[parent[node]] = append(children[parent[node]], node)
	}
	var dfs func(int) (int, int)
	dfs = func(node int) (int, int) {
		total, count := value[node], 1
		for _, child := range children[node] {
			cs, cc := dfs(child)
			total += cs
			count += cc
		}
		if total == 0 {
			return 0, 0
		}
		return total, count
	}
	_, count := dfs(0)
	return count
}
'''

SOLUTIONS["1274_number_of_ships_in_a_rectangle"] = r'''// LeetCode 1274 - Number of Ships in a Rectangle
// https://leetcode.com/problems/number-of-ships-in-a-rectangle/

type Point struct{ X, Y int }

type Sea interface {
	HasShips(topRight, bottomLeft Point) bool
}

func countShips(sea Sea, topRight Point, bottomLeft Point) int {
	tx, ty := topRight.X, topRight.Y
	bx, by := bottomLeft.X, bottomLeft.Y
	if tx < bx || ty < by || !sea.HasShips(topRight, bottomLeft) {
		return 0
	}
	if tx == bx && ty == by {
		return 1
	}
	mx, my := (tx+bx)/2, (ty+by)/2
	return countShips(sea, Point{mx, my}, Point{bx, by}) +
		countShips(sea, Point{tx, my}, Point{mx + 1, by}) +
		countShips(sea, Point{mx, ty}, Point{bx, my + 1}) +
		countShips(sea, Point{tx, ty}, Point{mx + 1, my + 1})
}
'''

SOLUTIONS["1275_find_winner_on_a_tic_tac_toe_game"] = r'''// LeetCode 1275 - Find Winner on a Tic Tac Toe Game
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

func tictactoe(moves [][]int) string {
	board := [3][3]int{}
	for i, mv := range moves {
		if i%2 == 0 {
			board[mv[0]][mv[1]] = 1
		} else {
			board[mv[0]][mv[1]] = -1
		}
	}
	lines := [][3]int{}
	for r := 0; r < 3; r++ {
		lines = append(lines, [3]int{board[r][0], board[r][1], board[r][2]})
	}
	for c := 0; c < 3; c++ {
		lines = append(lines, [3]int{board[0][c], board[1][c], board[2][c]})
	}
	lines = append(lines, [3]int{board[0][0], board[1][1], board[2][2]})
	lines = append(lines, [3]int{board[0][2], board[1][1], board[2][0]})
	for _, line := range lines {
		s := line[0] + line[1] + line[2]
		if s == 3 {
			return "A"
		}
		if s == -3 {
			return "B"
		}
	}
	if len(moves) == 9 {
		return "Draw"
	}
	return "Pending"
}
'''

SOLUTIONS["1276_number_of_burgers_with_no_waste_of_ingredients"] = r'''// LeetCode 1276 - Number of Burgers with No Waste of Ingredients
// https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

func numOfBurgers(tomatoSlices int, cheeseSlices int) []int {
	if tomatoSlices%2 != 0 {
		return []int{}
	}
	jumbo := tomatoSlices/2 - cheeseSlices
	small := cheeseSlices - jumbo
	if jumbo >= 0 && small >= 0 {
		return []int{jumbo, small}
	}
	return []int{}
}
'''

SOLUTIONS["1277_count_square_submatrices_with_all_ones"] = r'''// LeetCode 1277 - Count Square Submatrices with All Ones
// https://leetcode.com/problems/count-square-submatrices-with-all-ones/

func countSquares(matrix [][]int) int {
	answer := 0
	for r := 0; r < len(matrix); r++ {
		for c := 0; c < len(matrix[0]); c++ {
			if matrix[r][c] > 0 && r > 0 && c > 0 {
				m := matrix[r-1][c]
				if matrix[r][c-1] < m {
					m = matrix[r][c-1]
				}
				if matrix[r-1][c-1] < m {
					m = matrix[r-1][c-1]
				}
				matrix[r][c] += m
			}
			answer += matrix[r][c]
		}
	}
	return answer
}
'''

SOLUTIONS["1278_palindrome_partitioning_iii"] = r'''// LeetCode 1278 - Palindrome Partitioning III
// https://leetcode.com/problems/palindrome-partitioning-iii/

func palindromePartition(s string, k int) int {
	n := len(s)
	cost := make([][]int, n)
	for i := range cost {
		cost[i] = make([]int, n)
	}
	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			c := 0
			if s[i] != s[j] {
				c = 1
			}
			if length > 2 {
				c += cost[i+1][j-1]
			}
			cost[i][j] = c
		}
	}
	inf := n + 1
	dp := make([][]int, k+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
		for j := range dp[i] {
			dp[i][j] = inf
		}
	}
	dp[0][0] = 0
	for parts := 1; parts <= k; parts++ {
		for end := parts; end <= n; end++ {
			for start := parts - 1; start < end; start++ {
				v := dp[parts-1][start] + cost[start][end-1]
				if v < dp[parts][end] {
					dp[parts][end] = v
				}
			}
		}
	}
	return dp[k][n]
}
'''

SOLUTIONS["1279_traffic_light_controlled_intersection"] = r'''// LeetCode 1279 - Traffic Light Controlled Intersection
// https://leetcode.com/problems/traffic-light-controlled-intersection/

import "sync"

type TrafficLight struct {
	greenRoad int
	mu        sync.Mutex
}

func Constructor() TrafficLight {
	return TrafficLight{greenRoad: 1}
}

func (this *TrafficLight) CarArrived(carId int, roadId int, direction int, turnGreen func(), crossCar func()) {
	this.mu.Lock()
	defer this.mu.Unlock()
	if roadId != this.greenRoad {
		turnGreen()
		this.greenRoad = roadId
	}
	crossCar()
}
'''

SOLUTIONS["1281_subtract_the_product_and_sum_of_digits_of_an_integer"] = r'''// LeetCode 1281 - Subtract the Product and Sum of Digits of an Integer
// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

func subtractProductAndSum(n int) int {
	product, total := 1, 0
	for n > 0 {
		digit := n % 10
		n /= 10
		product *= digit
		total += digit
	}
	return product - total
}
'''

SOLUTIONS["1282_group_the_people_given_the_group_size_they_belong_to"] = r'''// LeetCode 1282 - Group the People Given the Group Size They Belong To
// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

import "sort"

func groupThePeople(groupSizes []int) [][]int {
	pending := map[int][]int{}
	answer := [][]int{}
	for person, size := range groupSizes {
		pending[size] = append(pending[size], person)
		if len(pending[size]) == size {
			answer = append(answer, pending[size])
			pending[size] = nil
		}
	}
	sort.Slice(answer, func(i, j int) bool {
		if len(answer[i]) != len(answer[j]) {
			return len(answer[i]) < len(answer[j])
		}
		for k := 0; k < len(answer[i]); k++ {
			if answer[i][k] != answer[j][k] {
				return answer[i][k] < answer[j][k]
			}
		}
		return false
	})
	return answer
}
'''

SOLUTIONS["1283_find_the_smallest_divisor_given_a_threshold"] = r'''// LeetCode 1283 - Find the Smallest Divisor Given a Threshold
// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

func smallestDivisor(nums []int, threshold int) int {
	lo, hi := 1, nums[0]
	for _, x := range nums {
		if x > hi {
			hi = x
		}
	}
	for lo < hi {
		mid := (lo + hi) / 2
		sum := 0
		for _, x := range nums {
			sum += (x + mid - 1) / mid
		}
		if sum <= threshold {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
'''

SOLUTIONS["1284_minimum_number_of_flips_to_convert_binary_matrix_to_zero_matrix"] = r'''// LeetCode 1284 - Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

func minFlips(mat [][]int) int {
	m, n := len(mat), len(mat[0])
	start := 0
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			start |= mat[r][c] << (r*n + c)
		}
	}
	masks := []int{}
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			mask := 0
			for _, d := range [][2]int{{0, 0}, {1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
				nr, nc := r+d[0], c+d[1]
				if nr >= 0 && nr < m && nc >= 0 && nc < n {
					mask ^= 1 << (nr*n + nc)
				}
			}
			masks = append(masks, mask)
		}
	}
	type item struct{ state, dist int }
	q := []item{{start, 0}}
	seen := map[int]bool{start: true}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		if cur.state == 0 {
			return cur.dist
		}
		for _, mask := range masks {
			nxt := cur.state ^ mask
			if !seen[nxt] {
				seen[nxt] = true
				q = append(q, item{nxt, cur.dist + 1})
			}
		}
	}
	return -1
}
'''

SOLUTIONS["1286_iterator_for_combination"] = r'''// LeetCode 1286 - Iterator for Combination
// https://leetcode.com/problems/iterator-for-combination/

type CombinationIterator struct {
	items []string
	idx   int
}

func Constructor(characters string, combinationLength int) CombinationIterator {
	items := []string{}
	var dfs func(int, []byte)
	dfs = func(start int, cur []byte) {
		if len(cur) == combinationLength {
			items = append(items, string(cur))
			return
		}
		for i := start; i < len(characters); i++ {
			dfs(i+1, append(cur, characters[i]))
		}
	}
	dfs(0, nil)
	return CombinationIterator{items: items}
}

func (this *CombinationIterator) Next() string {
	v := this.items[this.idx]
	this.idx++
	return v
}

func (this *CombinationIterator) HasNext() bool {
	return this.idx < len(this.items)
}
'''

SOLUTIONS["1287_element_appearing_more_than_25_in_sorted_array"] = r'''// LeetCode 1287 - Element Appearing More Than 25% In Sorted Array
// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

func findSpecialInteger(arr []int) int {
	n := len(arr)
	candidates := []int{arr[n/4], arr[n/2], arr[3*n/4]}
	for _, value := range candidates {
		count := 0
		for _, x := range arr {
			if x == value {
				count++
			}
		}
		if count > n/4 {
			return value
		}
	}
	return arr[0]
}
'''

SOLUTIONS["1288_remove_covered_intervals"] = r'''// LeetCode 1288 - Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/

import "sort"

func removeCoveredIntervals(intervals [][]int) int {
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][0] == intervals[j][0] {
			return intervals[i][1] > intervals[j][1]
		}
		return intervals[i][0] < intervals[j][0]
	})
	answer, farthest := 0, -1
	for _, iv := range intervals {
		if iv[1] > farthest {
			answer++
			farthest = iv[1]
		}
	}
	return answer
}
'''

SOLUTIONS["1289_minimum_falling_path_sum_ii"] = r'''// LeetCode 1289 - Minimum Falling Path Sum II
// https://leetcode.com/problems/minimum-falling-path-sum-ii/

func minFallingPathSum(grid [][]int) int {
	dp := append([]int{}, grid[0]...)
	for _, row := range grid[1:] {
		first := 0
		for i := 1; i < len(dp); i++ {
			if dp[i] < dp[first] {
				first = i
			}
		}
		secondValue := 0
		if len(dp) > 1 {
			secondValue = int(^uint(0) >> 1)
			for i := 0; i < len(dp); i++ {
				if i != first && dp[i] < secondValue {
					secondValue = dp[i]
				}
			}
		}
		nxt := make([]int, len(row))
		for i, value := range row {
			if i == first {
				nxt[i] = value + secondValue
			} else {
				nxt[i] = value + dp[first]
			}
		}
		dp = nxt
	}
	best := dp[0]
	for _, v := range dp[1:] {
		if v < best {
			best = v
		}
	}
	return best
}
'''

SOLUTIONS["1290_convert_binary_number_in_a_linked_list_to_integer"] = r'''// LeetCode 1290 - Convert Binary Number in a Linked List to Integer
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

type ListNode struct {
	Val  int
	Next *ListNode
}

func getDecimalValue(head *ListNode) int {
	value := 0
	for head != nil {
		value = value*2 + head.Val
		head = head.Next
	}
	return value
}
'''

SOLUTIONS["1291_sequential_digits"] = r'''// LeetCode 1291 - Sequential Digits
// https://leetcode.com/problems/sequential-digits/

func sequentialDigits(low int, high int) []int {
	digits := "123456789"
	answer := []int{}
	for length := 2; length <= 9; length++ {
		for start := 0; start <= 9-length; start++ {
			value := 0
			for i := start; i < start+length; i++ {
				value = value*10 + int(digits[i]-'0')
			}
			if value >= low && value <= high {
				answer = append(answer, value)
			}
		}
	}
	return answer
}
'''

SOLUTIONS["1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold"] = r'''// LeetCode 1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold
// https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

func maxSideLength(mat [][]int, threshold int) int {
	m, n := len(mat), len(mat[0])
	prefix := make([][]int, m+1)
	for i := range prefix {
		prefix[i] = make([]int, n+1)
	}
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			prefix[r+1][c+1] = mat[r][c] + prefix[r][c+1] + prefix[r+1][c] - prefix[r][c]
		}
	}
	possible := func(size int) bool {
		for r := size; r <= m; r++ {
			for c := size; c <= n; c++ {
				sum := prefix[r][c] - prefix[r-size][c] - prefix[r][c-size] + prefix[r-size][c-size]
				if sum <= threshold {
					return true
				}
			}
		}
		return false
	}
	lo, hi := 0, m
	if n < hi {
		hi = n
	}
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if possible(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
'''

SOLUTIONS["1293_shortest_path_in_a_grid_with_obstacles_elimination"] = r'''// LeetCode 1293 - Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

func shortestPath(grid [][]int, k int) int {
	m, n := len(grid), len(grid[0])
	if k >= m+n-2 {
		return m + n - 2
	}
	type item struct{ r, c, rem, dist int }
	q := []item{{0, 0, k, 0}}
	best := map[[2]int]int{{0, 0}: k}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		if cur.r == m-1 && cur.c == n-1 {
			return cur.dist
		}
		for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr >= 0 && nr < m && nc >= 0 && nc < n {
				nxt := cur.rem - grid[nr][nc]
				key := [2]int{nr, nc}
				if nxt >= 0 && nxt > best[key] {
					best[key] = nxt
					q = append(q, item{nr, nc, nxt, cur.dist + 1})
				}
			}
		}
	}
	return -1
}
'''

SOLUTIONS["1295_find_numbers_with_even_number_of_digits"] = r'''// LeetCode 1295 - Find Numbers with Even Number of Digits
// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

func findNumbers(nums []int) int {
	ans := 0
	for _, value := range nums {
		digits := 0
		for value > 0 {
			value /= 10
			digits++
		}
		if digits%2 == 0 {
			ans++
		}
	}
	return ans
}
'''

SOLUTIONS["1296_divide_array_in_sets_of_k_consecutive_numbers"] = r'''// LeetCode 1296 - Divide Array in Sets of K Consecutive Numbers
// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

import "sort"

func isPossibleDivide(nums []int, k int) bool {
	if len(nums)%k != 0 {
		return false
	}
	counts := map[int]int{}
	for _, x := range nums {
		counts[x]++
	}
	keys := make([]int, 0, len(counts))
	for x := range counts {
		keys = append(keys, x)
	}
	sort.Ints(keys)
	for _, start := range keys {
		amount := counts[start]
		if amount == 0 {
			continue
		}
		for value := start; value < start+k; value++ {
			if counts[value] < amount {
				return false
			}
			counts[value] -= amount
		}
	}
	return true
}
'''

SOLUTIONS["1297_maximum_number_of_occurrences_of_a_substring"] = r'''// LeetCode 1297 - Maximum Number of Occurrences of a Substring
// https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

func maxFreq(s string, maxLetters int, minSize int, maxSize int) int {
	_ = maxSize
	counts := map[string]int{}
	best := 0
	for i := 0; i+minSize <= len(s); i++ {
		sub := s[i : i+minSize]
		seen := map[byte]bool{}
		for j := 0; j < minSize; j++ {
			seen[sub[j]] = true
		}
		if len(seen) <= maxLetters {
			counts[sub]++
			if counts[sub] > best {
				best = counts[sub]
			}
		}
	}
	return best
}
'''

SOLUTIONS["1298_maximum_candies_you_can_get_from_boxes"] = r'''// LeetCode 1298 - Maximum Candies You Can Get from Boxes
// https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

func maxCandies(status []int, candies []int, keys [][]int, containedBoxes [][]int, initialBoxes []int) int {
	owned := map[int]bool{}
	opened := map[int]bool{}
	q := []int{}
	for _, box := range initialBoxes {
		owned[box] = true
		if status[box] == 1 {
			q = append(q, box)
		}
	}
	total := 0
	for len(q) > 0 {
		box := q[0]
		q = q[1:]
		if opened[box] || status[box] == 0 {
			continue
		}
		opened[box] = true
		total += candies[box]
		for _, key := range keys[box] {
			status[key] = 1
			if owned[key] && !opened[key] {
				q = append(q, key)
			}
		}
		for _, child := range containedBoxes[box] {
			owned[child] = true
			if status[child] == 1 && !opened[child] {
				q = append(q, child)
			}
		}
	}
	return total
}
'''

SOLUTIONS["1299_replace_elements_with_greatest_element_on_right_side"] = r'''// LeetCode 1299 - Replace Elements with Greatest Element on Right Side
// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

func replaceElements(arr []int) []int {
	greatest := -1
	for i := len(arr) - 1; i >= 0; i-- {
		arr[i], greatest = greatest, max(greatest, arr[i])
	}
	return arr
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
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
