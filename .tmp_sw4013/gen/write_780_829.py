#!/usr/bin/env python3
"""Write Solution.swift for problems 0780-0829."""
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

TREE = '''
class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?
    init() { self.val = 0; self.left = nil; self.right = nil }
    init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}
'''

LIST = '''
class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}
'''

def hdr(num, title, slug):
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n"

FILES = {}

FILES["0780_reaching_points"] = hdr("0780", "Reaching Points", "reaching-points") + '''
class Solution {
    func reachingPoints(_ sx: Int, _ sy: Int, _ tx: Int, _ ty: Int) -> Bool {
        var tx = tx, ty = ty
        while tx >= sx && ty >= sy {
            if tx == sx && ty == sy { return true }
            if tx == ty { break }
            if tx > ty {
                if ty > sy { tx %= ty }
                else { return (tx - sx) % ty == 0 }
            } else {
                if tx > sx { ty %= tx }
                else { return (ty - sy) % tx == 0 }
            }
        }
        return tx == sx && ty == sy
    }
}
'''

FILES["0781_rabbits_in_forest"] = hdr("0781", "Rabbits in Forest", "rabbits-in-forest") + '''
class Solution {
    func numRabbits(_ answers: [Int]) -> Int {
        var counts = [Int: Int]()
        for answer in answers { counts[answer, default: 0] += 1 }
        var total = 0
        for (x, c) in counts {
            let group = x + 1
            let groups = (c + group - 1) / group
            total += groups * group
        }
        return total
    }
}
'''

FILES["0782_transform_to_chessboard"] = hdr("0782", "Transform to Chessboard", "transform-to-chessboard") + '''
class Solution {
    func movesToChessboard(_ board: [[Int]]) -> Int {
        let n = board.count
        for i in 0..<n {
            for j in 0..<n {
                if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) != 0 { return -1 }
            }
        }
        var rowSum = 0, colSum = 0
        for i in 0..<n {
            rowSum += board[0][i]
            colSum += board[i][0]
        }
        if rowSum < n / 2 || rowSum > (n + 1) / 2 { return -1 }
        if colSum < n / 2 || colSum > (n + 1) / 2 { return -1 }
        var rowSwap = 0, colSwap = 0
        for i in 0..<n {
            if board[0][i] != i % 2 { rowSwap += 1 }
            if board[i][0] != i % 2 { colSwap += 1 }
        }
        if n % 2 == 1 {
            if rowSwap % 2 == 1 { rowSwap = n - rowSwap }
            if colSwap % 2 == 1 { colSwap = n - colSwap }
        } else {
            rowSwap = min(rowSwap, n - rowSwap)
            colSwap = min(colSwap, n - colSwap)
        }
        return (rowSwap + colSwap) / 2
    }
}
'''

FILES["0783_minimum_distance_between_bst_nodes"] = hdr("0783", "Minimum Distance Between BST Nodes", "minimum-distance-between-bst-nodes") + TREE + '''
class Solution {
    private var hasPrev = false
    private var prev = 0
    private var best = Int.max

    func minDiffInBST(_ root: TreeNode?) -> Int {
        hasPrev = false
        best = Int.max
        inorder(root)
        return best
    }

    private func inorder(_ node: TreeNode?) {
        guard let node = node else { return }
        inorder(node.left)
        if hasPrev { best = min(best, node.val - prev) }
        prev = node.val
        hasPrev = true
        inorder(node.right)
    }
}
'''

FILES["0784_letter_case_permutation"] = hdr("0784", "Letter Case Permutation", "letter-case-permutation") + '''
class Solution {
    func letterCasePermutation(_ s: String) -> [String] {
        var result = [""]
        for ch in s {
            var next = [String]()
            if ch.isLetter {
                let lower = Character(ch.lowercased())
                let upper = Character(ch.uppercased())
                for prefix in result {
                    next.append(prefix + String(lower))
                    next.append(prefix + String(upper))
                }
            } else {
                for prefix in result { next.append(prefix + String(ch)) }
            }
            result = next
        }
        return result
    }
}
'''

FILES["0785_is_graph_bipartite"] = hdr("0785", "Is Graph Bipartite?", "is-graph-bipartite") + '''
class Solution {
    func isBipartite(_ graph: [[Int]]) -> Bool {
        var color = Array(repeating: -1, count: graph.count)
        for node in 0..<graph.count {
            if color[node] == -1 && !dfs(graph, node, 0, &color) { return false }
        }
        return true
    }

    private func dfs(_ graph: [[Int]], _ node: Int, _ c: Int, _ color: inout [Int]) -> Bool {
        color[node] = c
        for nei in graph[node] {
            if color[nei] == -1 {
                if !dfs(graph, nei, c ^ 1, &color) { return false }
            } else if color[nei] == c {
                return false
            }
        }
        return true
    }
}
'''

FILES["0786_k_th_smallest_prime_fraction"] = hdr("0786", "K-th Smallest Prime Fraction", "k-th-smallest-prime-fraction") + '''
class Solution {
    func kthSmallestPrimeFraction(_ arr: [Int], _ k: Int) -> [Int] {
        let n = arr.count
        var lo = 0.0, hi = 1.0
        var best = [0, 1]
        while true {
            let mid = (lo + hi) / 2.0
            var count = 0
            var j = 1
            var num = 0, den = 1
            for i in 0..<n {
                while j < n && Double(arr[i]) > mid * Double(arr[j]) { j += 1 }
                count += n - j
                if j < n && num * arr[j] < den * arr[i] {
                    num = arr[i]
                    den = arr[j]
                }
            }
            if count == k {
                return [num, den]
            } else if count < k {
                lo = mid
            } else {
                hi = mid
                best = [num, den]
            }
            if abs(hi - lo) < 1e-12 { return best }
        }
    }
}
'''

FILES["0787_cheapest_flights_within_k_stops"] = hdr("0787", "Cheapest Flights Within K Stops", "cheapest-flights-within-k-stops") + '''
class Solution {
    func findCheapestPrice(_ n: Int, _ flights: [[Int]], _ src: Int, _ dst: Int, _ k: Int) -> Int {
        let inf = Int.max / 4
        var dist = Array(repeating: inf, count: n)
        dist[src] = 0
        for _ in 0...k {
            var nxt = dist
            for flight in flights {
                let u = flight[0], v = flight[1], price = flight[2]
                if dist[u] != inf && dist[u] + price < nxt[v] {
                    nxt[v] = dist[u] + price
                }
            }
            dist = nxt
        }
        return dist[dst] == inf ? -1 : dist[dst]
    }
}
'''

FILES["0788_rotated_digits"] = hdr("0788", "Rotated Digits", "rotated-digits") + '''
class Solution {
    func rotatedDigits(_ n: Int) -> Int {
        var count = 0
        for num in 1...n {
            let s = Array(String(num))
            var ok = true, changed = false
            for ch in s {
                if ch == "3" || ch == "4" || ch == "7" { ok = false; break }
                if ch == "2" || ch == "5" || ch == "6" || ch == "9" { changed = true }
            }
            if ok && changed { count += 1 }
        }
        return count
    }
}
'''

FILES["0789_escape_the_ghosts"] = hdr("0789", "Escape The Ghosts", "escape-the-ghosts") + '''
class Solution {
    func escapeGhosts(_ ghosts: [[Int]], _ target: [Int]) -> Bool {
        let targetDist = abs(target[0]) + abs(target[1])
        for ghost in ghosts {
            if abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) <= targetDist {
                return false
            }
        }
        return true
    }
}
'''

FILES["0790_domino_and_tromino_tiling"] = hdr("0790", "Domino and Tromino Tiling", "domino-and-tromino-tiling") + '''
class Solution {
    func numTilings(_ n: Int) -> Int {
        let mod = 1_000_000_007
        if n == 1 { return 1 }
        if n == 2 { return 2 }
        var dp = Array(repeating: 0, count: n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        if n >= 4 {
            for i in 4...n {
                dp[i] = (2 * dp[i - 1] + dp[i - 3]) % mod
            }
        }
        return dp[n]
    }
}
'''

FILES["0791_custom_sort_string"] = hdr("0791", "Custom Sort String", "custom-sort-string") + '''
class Solution {
    func customSortString(_ order: String, _ s: String) -> String {
        var count = Array(repeating: 0, count: 26)
        let a = Int(Character("a").asciiValue!)
        for ch in s {
            count[Int(ch.asciiValue!) - a] += 1
        }
        var out = ""
        for ch in order {
            let i = Int(ch.asciiValue!) - a
            while count[i] > 0 {
                out.append(ch)
                count[i] -= 1
            }
        }
        for i in 0..<26 {
            while count[i] > 0 {
                out.append(Character(UnicodeScalar(a + i)!))
                count[i] -= 1
            }
        }
        return out
    }
}
'''

FILES["0792_number_of_matching_subsequences"] = hdr("0792", "Number of Matching Subsequences", "number-of-matching-subsequences") + '''
class Solution {
    func numMatchingSubseq(_ s: String, _ words: [String]) -> Int {
        var waiting = Array(repeating: [(Int, Int)](), count: 26)
        let a = Int(Character("a").asciiValue!)
        let wordChars = words.map { Array($0) }
        for i in 0..<words.count {
            let w = wordChars[i]
            waiting[Int(w[0].asciiValue!) - a].append((i, 0))
        }
        var ans = 0
        for ch in s {
            let idx = Int(ch.asciiValue!) - a
            let cur = waiting[idx]
            waiting[idx] = []
            for (wi, pos) in cur {
                let nxt = pos + 1
                if nxt == wordChars[wi].count {
                    ans += 1
                } else {
                    waiting[Int(wordChars[wi][nxt].asciiValue!) - a].append((wi, nxt))
                }
            }
        }
        return ans
    }
}
'''

FILES["0793_preimage_size_of_factorial_zeroes_function"] = hdr("0793", "Preimage Size of Factorial Zeroes Function", "preimage-size-of-factorial-zeroes-function") + '''
class Solution {
    func preimageSizeFZF(_ k: Int) -> Int {
        return Int(firstGe(k + 1) - firstGe(k))
    }

    private func zeros(_ n: Int) -> Int {
        var n = n, z = 0
        while n > 0 {
            n /= 5
            z += n
        }
        return z
    }

    private func firstGe(_ target: Int) -> Int {
        var lo = 0, hi = 5 * target + 5
        while lo < hi {
            let mid = (lo + hi) / 2
            if zeros(mid) >= target { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }
}
'''

FILES["0794_valid_tic_tac_toe_state"] = hdr("0794", "Valid Tic-Tac-Toe State", "valid-tic-tac-toe-state") + '''
class Solution {
    func validTicTacToe(_ board: [String]) -> Bool {
        var x = 0, o = 0
        for row in board {
            for ch in row {
                if ch == "X" { x += 1 }
                else if ch == "O" { o += 1 }
            }
        }
        if o > x || x - o > 1 { return false }
        let xWin = win(board, Character("X"))
        let oWin = win(board, Character("O"))
        if xWin && oWin { return false }
        if xWin && x != o + 1 { return false }
        if oWin && x != o { return false }
        return true
    }

    private func win(_ board: [String], _ player: Character) -> Bool {
        let rows = board.map { Array($0) }
        for i in 0..<3 {
            if rows[i][0] == player && rows[i][1] == player && rows[i][2] == player { return true }
            if rows[0][i] == player && rows[1][i] == player && rows[2][i] == player { return true }
        }
        if rows[0][0] == player && rows[1][1] == player && rows[2][2] == player { return true }
        if rows[0][2] == player && rows[1][1] == player && rows[2][0] == player { return true }
        return false
    }
}
'''

FILES["0795_number_of_subarrays_with_bounded_maximum"] = hdr("0795", "Number of Subarrays with Bounded Maximum", "number-of-subarrays-with-bounded-maximum") + '''
class Solution {
    func numSubarrayBoundedMax(_ nums: [Int], _ left: Int, _ right: Int) -> Int {
        return countAtMost(nums, right) - countAtMost(nums, left - 1)
    }

    private func countAtMost(_ nums: [Int], _ bound: Int) -> Int {
        var ans = 0, cur = 0
        for num in nums {
            if num <= bound {
                cur += 1
                ans += cur
            } else {
                cur = 0
            }
        }
        return ans
    }
}
'''

FILES["0796_rotate_string"] = hdr("0796", "Rotate String", "rotate-string") + '''
class Solution {
    func rotateString(_ s: String, _ goal: String) -> Bool {
        return s.count == goal.count && (s + s).contains(goal)
    }
}
'''

FILES["0797_all_paths_from_source_to_target"] = hdr("0797", "All Paths From Source to Target", "all-paths-from-source-to-target") + '''
class Solution {
    func allPathsSourceTarget(_ graph: [[Int]]) -> [[Int]] {
        let target = graph.count - 1
        var answer = [[Int]]()
        var path = [0]
        func dfs(_ node: Int) {
            if node == target {
                answer.append(path)
                return
            }
            for nei in graph[node] {
                path.append(nei)
                dfs(nei)
                path.removeLast()
            }
        }
        dfs(0)
        return answer
    }
}
'''

FILES["0798_smallest_rotation_with_highest_score"] = hdr("0798", "Smallest Rotation with Highest Score", "smallest-rotation-with-highest-score") + '''
class Solution {
    func bestRotation(_ nums: [Int]) -> Int {
        let n = nums.count
        var change = Array(repeating: 1, count: n)
        for i in 0..<n {
            change[(i - nums[i] + 1 + n) % n] -= 1
        }
        for i in 1..<n { change[i] += change[i - 1] }
        var best = 0
        for i in 1..<n where change[i] > change[best] { best = i }
        return best
    }
}
'''

FILES["0799_champagne_tower"] = hdr("0799", "Champagne Tower", "champagne-tower") + '''
class Solution {
    func champagneTower(_ poured: Int, _ query_row: Int, _ query_glass: Int) -> Double {
        var row = [Double(poured)]
        if query_row == 0 { return min(1.0, row[query_glass]) }
        for r in 0..<query_row {
            var nextRow = Array(repeating: 0.0, count: r + 2)
            for i in 0..<row.count {
                let overflow = (row[i] - 1.0) / 2.0
                if overflow > 0 {
                    nextRow[i] += overflow
                    nextRow[i + 1] += overflow
                }
            }
            row = nextRow
        }
        return min(1.0, row[query_glass])
    }
}
'''

FILES["0800_similar_rgb_color"] = hdr("0800", "Similar RGB Color", "similar-rgb-color") + '''
class Solution {
    func similarRGB(_ color: String) -> String {
        let chars = Array(color)
        return "#" + closest(String(chars[1...2])) + closest(String(chars[3...4])) + closest(String(chars[5...6]))
    }

    private func closest(_ component: String) -> String {
        let value = Int(component, radix: 16)!
        let rounded = (value + 8) / 17
        return String(format: "%x%x", rounded, rounded)
    }
}
'''

FILES["0801_minimum_swaps_to_make_sequences_increasing"] = hdr("0801", "Minimum Swaps To Make Sequences Increasing", "minimum-swaps-to-make-sequences-increasing") + '''
class Solution {
    func minSwap(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        var swap = Array(repeating: n, count: n)
        var keep = Array(repeating: n, count: n)
        swap[0] = 1
        keep[0] = 0
        for i in 1..<n {
            if nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1] {
                keep[i] = keep[i - 1]
                swap[i] = swap[i - 1] + 1
            }
            if nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1] {
                keep[i] = min(keep[i], swap[i - 1])
                swap[i] = min(swap[i], keep[i - 1] + 1)
            }
        }
        return min(swap[n - 1], keep[n - 1])
    }
}
'''

FILES["0802_find_eventual_safe_states"] = hdr("0802", "Find Eventual Safe States", "find-eventual-safe-states") + '''
class Solution {
    func eventualSafeNodes(_ graph: [[Int]]) -> [Int] {
        let n = graph.count
        var color = Array(repeating: 0, count: n)
        var ans = [Int]()
        for i in 0..<n where dfs(graph, &color, i) { ans.append(i) }
        return ans
    }

    private func dfs(_ graph: [[Int]], _ color: inout [Int], _ node: Int) -> Bool {
        if color[node] != 0 { return color[node] == 2 }
        color[node] = 1
        for nei in graph[node] {
            if !dfs(graph, &color, nei) { return false }
        }
        color[node] = 2
        return true
    }
}
'''

FILES["0803_bricks_falling_when_hit"] = hdr("0803", "Bricks Falling When Hit", "bricks-falling-when-hit") + '''
class Solution {
    private var parent = [Int]()
    private var size = [Int]()
    private var n = 0
    private var roof = 0

    func hitBricks(_ grid: [[Int]], _ hits: [[Int]]) -> [Int] {
        let m = grid.count
        n = grid[0].count
        roof = m * n
        parent = Array(0...roof)
        size = Array(repeating: 1, count: roof + 1)
        var status = grid
        for hit in hits { status[hit[0]][hit[1]] = 0 }
        let dr = [-1, 1, 0, 0], dc = [0, 0, -1, 1]
        for r in 0..<m {
            for c in 0..<n {
                if status[r][c] == 0 { continue }
                if r == 0 { unite(idx(r, c), roof) }
                for k in 0..<4 {
                    let nr = r + dr[k], nc = c + dc[k]
                    if nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] == 1 {
                        unite(idx(r, c), idx(nr, nc))
                    }
                }
            }
        }
        var answer = Array(repeating: 0, count: hits.count)
        for i in stride(from: hits.count - 1, through: 0, by: -1) {
            let r = hits[i][0], c = hits[i][1]
            if grid[r][c] == 0 { continue }
            let prev = size[find(roof)]
            status[r][c] = 1
            if r == 0 { unite(idx(r, c), roof) }
            for k in 0..<4 {
                let nr = r + dr[k], nc = c + dc[k]
                if nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] == 1 {
                    unite(idx(r, c), idx(nr, nc))
                }
            }
            let curr = size[find(roof)]
            answer[i] = max(0, curr - prev - 1)
        }
        return answer
    }

    private func find(_ x: Int) -> Int {
        var x = x
        while parent[x] != x {
            parent[x] = parent[parent[x]]
            x = parent[x]
        }
        return x
    }

    private func unite(_ a: Int, _ b: Int) {
        let ra = find(a), rb = find(b)
        if ra == rb { return }
        parent[ra] = rb
        size[rb] += size[ra]
    }

    private func idx(_ r: Int, _ c: Int) -> Int { r * n + c }
}
'''

FILES["0804_unique_morse_code_words"] = hdr("0804", "Unique Morse Code Words", "unique-morse-code-words") + '''
class Solution {
    func uniqueMorseRepresentations(_ words: [String]) -> Int {
        let codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        let a = Int(Character("a").asciiValue!)
        var seen = Set<String>()
        for word in words {
            var code = ""
            for ch in word { code += codes[Int(ch.asciiValue!) - a] }
            seen.insert(code)
        }
        return seen.count
    }
}
'''

FILES["0805_split_array_with_same_average"] = hdr("0805", "Split Array With Same Average", "split-array-with-same-average") + '''
class Solution {
    func splitArraySameAverage(_ nums: [Int]) -> Bool {
        let n = nums.count
        let total = nums.reduce(0, +)
        let sorted = nums.sorted()
        var memo = Set<Int>()
        func find(_ target: Int, _ count: Int, _ index: Int) -> Bool {
            if count == 0 { return target == 0 }
            if index == n || count + index > n || target < 0 { return false }
            let key = (target << 20) | (count << 10) | index
            if memo.contains(key) { return false }
            if find(target - sorted[index], count - 1, index + 1) || find(target, count, index + 1) {
                return true
            }
            memo.insert(key)
            return false
        }
        for size in 1..<n {
            if (total * size) % n == 0 && find(total * size / n, size, 0) { return true }
        }
        return false
    }
}
'''

FILES["0806_number_of_lines_to_write_string"] = hdr("0806", "Number of Lines To Write String", "number-of-lines-to-write-string") + '''
class Solution {
    func numberOfLines(_ widths: [Int], _ s: String) -> [Int] {
        var lines = 1, width = 0
        let a = Int(Character("a").asciiValue!)
        for ch in s {
            let w = widths[Int(ch.asciiValue!) - a]
            if width + w > 100 {
                lines += 1
                width = w
            } else {
                width += w
            }
        }
        return [lines, width]
    }
}
'''

FILES["0807_max_increase_to_keep_city_skyline"] = hdr("0807", "Max Increase to Keep City Skyline", "max-increase-to-keep-city-skyline") + '''
class Solution {
    func maxIncreaseKeepingSkyline(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var rowMax = Array(repeating: 0, count: m)
        var colMax = Array(repeating: 0, count: n)
        for r in 0..<m {
            for c in 0..<n {
                rowMax[r] = max(rowMax[r], grid[r][c])
                colMax[c] = max(colMax[c], grid[r][c])
            }
        }
        var ans = 0
        for r in 0..<m {
            for c in 0..<n {
                ans += min(rowMax[r], colMax[c]) - grid[r][c]
            }
        }
        return ans
    }
}
'''

FILES["0808_soup_servings"] = hdr("0808", "Soup Servings", "soup-servings") + '''
class Solution {
    func soupServings(_ n: Int) -> Double {
        if n >= 4800 { return 1.0 }
        let units = (n + 24) / 25
        var memo = [Int: Double]()
        func dp(_ a: Int, _ b: Int) -> Double {
            if a <= 0 && b <= 0 { return 0.5 }
            if a <= 0 { return 1.0 }
            if b <= 0 { return 0.0 }
            let key = (a << 16) | b
            if let v = memo[key] { return v }
            let val = 0.25 * (dp(a - 4, b) + dp(a - 3, b - 1) + dp(a - 2, b - 2) + dp(a - 1, b - 3))
            memo[key] = val
            return val
        }
        return dp(units, units)
    }
}
'''

FILES["0809_expressive_words"] = hdr("0809", "Expressive Words", "expressive-words") + '''
class Solution {
    func expressiveWords(_ s: String, _ words: [String]) -> Int {
        let target = groups(s)
        var ans = 0
        for word in words {
            let source = groups(word)
            if source.count != target.count { continue }
            var ok = true
            for i in 0..<source.count {
                if source[i].0 != target[i].0 { ok = false; break }
                let c1 = source[i].1, c2 = target[i].1
                if c1 > c2 || (c1 != c2 && c2 < 3) { ok = false; break }
            }
            if ok { ans += 1 }
        }
        return ans
    }

    private func groups(_ text: String) -> [(Character, Int)] {
        let chars = Array(text)
        var result = [(Character, Int)]()
        var i = 0
        while i < chars.count {
            var j = i
            while j < chars.count && chars[j] == chars[i] { j += 1 }
            result.append((chars[i], j - i))
            i = j
        }
        return result
    }
}
'''

FILES["0810_chalkboard_xor_game"] = hdr("0810", "Chalkboard XOR Game", "chalkboard-xor-game") + '''
class Solution {
    func xorGame(_ nums: [Int]) -> Bool {
        var x = 0
        for num in nums { x ^= num }
        return x == 0 || nums.count % 2 == 0
    }
}
'''

FILES["0811_subdomain_visit_count"] = hdr("0811", "Subdomain Visit Count", "subdomain-visit-count") + '''
class Solution {
    func subdomainVisits(_ cpdomains: [String]) -> [String] {
        var counts = [String: Int]()
        for item in cpdomains {
            let parts = item.split(separator: " ", maxSplits: 1)
            let count = Int(parts[0])!
            var domain = String(parts[1])
            while true {
                counts[domain, default: 0] += count
                if let dot = domain.firstIndex(of: ".") {
                    domain = String(domain[domain.index(after: dot)...])
                } else {
                    break
                }
            }
        }
        return counts.map { "\\($0.value) \\($0.key)" }
    }
}
'''

FILES["0812_largest_triangle_area"] = hdr("0812", "Largest Triangle Area", "largest-triangle-area") + '''
class Solution {
    func largestTriangleArea(_ points: [[Int]]) -> Double {
        var best = 0.0
        let n = points.count
        for i in 0..<n {
            let x1 = points[i][0], y1 = points[i][1]
            for j in (i + 1)..<n {
                let x2 = points[j][0], y2 = points[j][1]
                for k in (j + 1)..<n {
                    let x3 = points[k][0], y3 = points[k][1]
                    let area = abs(Double(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))) / 2.0
                    best = max(best, area)
                }
            }
        }
        return best
    }
}
'''

FILES["0813_largest_sum_of_averages"] = hdr("0813", "Largest Sum of Averages", "largest-sum-of-averages") + '''
class Solution {
    func largestSumOfAverages(_ nums: [Int], _ k: Int) -> Double {
        let n = nums.count
        var prefix = Array(repeating: 0.0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + Double(nums[i]) }
        var dp = Array(repeating: 0.0, count: n)
        for i in 0..<n { dp[i] = (prefix[i + 1] - prefix[0]) / Double(i + 1) }
        if k >= 2 {
            for groups in 2...k {
                var nxt = Array(repeating: 0.0, count: n)
                for i in (groups - 1)..<n {
                    var best = 0.0
                    for j in (groups - 2)..<i {
                        best = max(best, dp[j] + (prefix[i + 1] - prefix[j + 1]) / Double(i - j))
                    }
                    nxt[i] = best
                }
                dp = nxt
            }
        }
        return dp[n - 1]
    }
}
'''

FILES["0814_binary_tree_pruning"] = hdr("0814", "Binary Tree Pruning", "binary-tree-pruning") + TREE + '''
class Solution {
    func pruneTree(_ root: TreeNode?) -> TreeNode? {
        guard let root = root else { return nil }
        root.left = pruneTree(root.left)
        root.right = pruneTree(root.right)
        if root.val == 0 && root.left == nil && root.right == nil { return nil }
        return root
    }
}
'''

FILES["0815_bus_routes"] = hdr("0815", "Bus Routes", "bus-routes") + '''
class Solution {
    func numBusesToDestination(_ routes: [[Int]], _ source: Int, _ target: Int) -> Int {
        if source == target { return 0 }
        var stopToBuses = [Int: [Int]]()
        for bus in 0..<routes.count {
            for stop in routes[bus] {
                stopToBuses[stop, default: []].append(bus)
            }
        }
        var queue = [(source, 0)]
        var seenStops: Set<Int> = [source]
        var seenBuses = Set<Int>()
        var qi = 0
        while qi < queue.count {
            let (stop, busesTaken) = queue[qi]
            qi += 1
            for bus in stopToBuses[stop, default: []] {
                if !seenBuses.insert(bus).inserted { continue }
                for nxt in routes[bus] {
                    if nxt == target { return busesTaken + 1 }
                    if seenStops.insert(nxt).inserted {
                        queue.append((nxt, busesTaken + 1))
                    }
                }
            }
        }
        return -1
    }
}
'''

FILES["0816_ambiguous_coordinates"] = hdr("0816", "Ambiguous Coordinates", "ambiguous-coordinates") + '''
class Solution {
    func ambiguousCoordinates(_ s: String) -> [String] {
        let chars = Array(s)
        let digits = String(chars[1..<(chars.count - 1)])
        var answer = [String]()
        for i in 1..<digits.count {
            let d = Array(digits)
            for left in candidates(String(d[0..<i])) {
                for right in candidates(String(d[i...])) {
                    answer.append("(" + left + ", " + right + ")")
                }
            }
        }
        return answer
    }

    private func candidates(_ frag: String) -> [String] {
        var options = [String]()
        if frag.isEmpty { return options }
        let chars = Array(frag)
        if chars.count > 1 && chars[0] == "0" && chars[chars.count - 1] == "0" { return options }
        if chars[0] == "0" && chars.count > 1 {
            if chars[chars.count - 1] != "0" { options.append("0." + String(chars[1...])) }
            return options
        }
        options.append(frag)
        if chars[chars.count - 1] == "0" { return options }
        for i in 1..<chars.count {
            options.append(String(chars[0..<i]) + "." + String(chars[i...]))
        }
        return options
    }
}
'''

FILES["0817_linked_list_components"] = hdr("0817", "Linked List Components", "linked-list-components") + LIST + '''
class Solution {
    func numComponents(_ head: ListNode?, _ nums: [Int]) -> Int {
        let present = Set(nums)
        var count = 0
        var connected = false
        var node = head
        while let cur = node {
            if present.contains(cur.val) {
                if !connected {
                    count += 1
                    connected = true
                }
            } else {
                connected = false
            }
            node = cur.next
        }
        return count
    }
}
'''

FILES["0818_race_car"] = hdr("0818", "Race Car", "race-car") + '''
class Solution {
    func racecar(_ target: Int) -> Int {
        var queue = [(0, 1, 0)]
        var seen: Set<Int> = [key(0, 1)]
        var qi = 0
        while qi < queue.count {
            let (pos, speed, steps) = queue[qi]
            qi += 1
            if pos == target { return steps }
            let nxtPos = pos + speed
            let nxtSpeed = speed * 2
            let k1 = key(nxtPos, nxtSpeed)
            if !seen.contains(k1) && abs(nxtPos) < target * 2 {
                seen.insert(k1)
                queue.append((nxtPos, nxtSpeed, steps + 1))
            }
            let revSpeed = speed > 0 ? -1 : 1
            let k2 = key(pos, revSpeed)
            if seen.insert(k2).inserted {
                queue.append((pos, revSpeed, steps + 1))
            }
        }
        return -1
    }

    private func key(_ pos: Int, _ speed: Int) -> Int {
        return (pos << 20) ^ (speed & 0xfffff)
    }
}
'''

FILES["0819_most_common_word"] = hdr("0819", "Most Common Word", "most-common-word") + '''
class Solution {
    func mostCommonWord(_ paragraph: String, _ banned: [String]) -> String {
        let bannedSet = Set(banned)
        var counts = [String: Int]()
        var word = ""
        var best = ""
        var bestCount = 0
        let text = paragraph + " "
        for ch in text {
            if ch.isLetter {
                word.append(ch.lowercased())
            } else if !word.isEmpty {
                if !bannedSet.contains(word) {
                    let c = (counts[word] ?? 0) + 1
                    counts[word] = c
                    if c > bestCount {
                        bestCount = c
                        best = word
                    }
                }
                word = ""
            }
        }
        return best
    }
}
'''

FILES["0820_short_encoding_of_words"] = hdr("0820", "Short Encoding of Words", "short-encoding-of-words") + '''
class Solution {
    func minimumLengthEncoding(_ words: [String]) -> Int {
        var good = Set(words)
        for word in words {
            let chars = Array(word)
            for i in 1..<chars.count {
                good.remove(String(chars[i...]))
            }
        }
        return good.reduce(0) { $0 + $1.count + 1 }
    }
}
'''

FILES["0821_shortest_distance_to_a_character"] = hdr("0821", "Shortest Distance to a Character", "shortest-distance-to-a-character") + '''
class Solution {
    func shortestToChar(_ s: String, _ c: Character) -> [Int] {
        let chars = Array(s)
        let n = chars.count
        var ans = Array(repeating: 0, count: n)
        var prev = -n
        for i in 0..<n {
            if chars[i] == c { prev = i }
            ans[i] = i - prev
        }
        prev = 2 * n
        for i in stride(from: n - 1, through: 0, by: -1) {
            if chars[i] == c { prev = i }
            ans[i] = min(ans[i], prev - i)
        }
        return ans
    }
}
'''

FILES["0822_card_flipping_game"] = hdr("0822", "Card Flipping Game", "card-flipping-game") + '''
class Solution {
    func flipgame(_ fronts: [Int], _ backs: [Int]) -> Int {
        var same = Set<Int>()
        for i in 0..<fronts.count where fronts[i] == backs[i] { same.insert(fronts[i]) }
        var best = Int.max
        for x in fronts where !same.contains(x) { best = min(best, x) }
        for x in backs where !same.contains(x) { best = min(best, x) }
        return best == Int.max ? 0 : best
    }
}
'''

FILES["0823_binary_trees_with_factors"] = hdr("0823", "Binary Trees With Factors", "binary-trees-with-factors") + '''
class Solution {
    func numFactoredBinaryTrees(_ arr: [Int]) -> Int {
        let mod = 1_000_000_007
        let nums = arr.sorted()
        var dp = [Int: Int]()
        for i in 0..<nums.count {
            let x = nums[i]
            var ways = 1
            for j in 0..<i {
                let left = nums[j]
                if x % left == 0 {
                    let right = x / left
                    if let wr = dp[right], let wl = dp[left] {
                        ways = (ways + wl * wr) % mod
                    }
                }
            }
            dp[x] = ways
        }
        var ans = 0
        for v in dp.values { ans = (ans + v) % mod }
        return ans
    }
}
'''

FILES["0824_goat_latin"] = hdr("0824", "Goat Latin", "goat-latin") + '''
class Solution {
    func toGoatLatin(_ sentence: String) -> String {
        let vowels: Set<Character> = ["a","e","i","o","u","A","E","I","O","U"]
        let words = sentence.split(separator: " ").map(String.init)
        var out = [String]()
        for (i, word) in words.enumerated() {
            var goat = ""
            if vowels.contains(word.first!) {
                goat = word + "ma"
            } else {
                goat = String(word.dropFirst()) + String(word.first!) + "ma"
            }
            goat += String(repeating: "a", count: i + 1)
            out.append(goat)
        }
        return out.joined(separator: " ")
    }
}
'''

FILES["0825_friends_of_appropriate_ages"] = hdr("0825", "Friends Of Appropriate Ages", "friends-of-appropriate-ages") + '''
class Solution {
    func numFriendRequests(_ ages: [Int]) -> Int {
        var count = Array(repeating: 0, count: 121)
        for age in ages { count[age] += 1 }
        var ans = 0
        for x in 1...120 {
            if count[x] == 0 { continue }
            for y in 1...120 {
                if count[y] == 0 { continue }
                if Double(y) <= 0.5 * Double(x) + 7 || y > x || (y > 100 && x < 100) { continue }
                ans += count[x] * count[y]
                if x == y { ans -= count[x] }
            }
        }
        return ans
    }
}
'''

FILES["0826_most_profit_assigning_work"] = hdr("0826", "Most Profit Assigning Work", "most-profit-assigning-work") + '''
class Solution {
    func maxProfitAssignment(_ difficulty: [Int], _ profit: [Int], _ worker: [Int]) -> Int {
        let jobs = zip(difficulty, profit).map { ($0, $1) }.sorted { $0.0 < $1.0 }
        let workers = worker.sorted()
        var ans = 0, best = 0, i = 0
        for ability in workers {
            while i < jobs.count && jobs[i].0 <= ability {
                best = max(best, jobs[i].1)
                i += 1
            }
            ans += best
        }
        return ans
    }
}
'''

FILES["0827_making_a_large_island"] = hdr("0827", "Making A Large Island", "making-a-large-island") + '''
class Solution {
    func largestIsland(_ grid: [[Int]]) -> Int {
        var grid = grid
        let n = grid.count
        var sizes = [0: 0]
        var islandId = 2
        func dfs(_ r: Int, _ c: Int, _ iid: Int) -> Int {
            if r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1 { return 0 }
            grid[r][c] = iid
            return 1 + dfs(r + 1, c, iid) + dfs(r - 1, c, iid) + dfs(r, c + 1, iid) + dfs(r, c - 1, iid)
        }
        for i in 0..<n {
            for j in 0..<n {
                if grid[i][j] == 1 {
                    sizes[islandId] = dfs(i, j, islandId)
                    islandId += 1
                }
            }
        }
        var ans = sizes.values.max() ?? 0
        let dr = [1, -1, 0, 0], dc = [0, 0, 1, -1]
        for i in 0..<n {
            for j in 0..<n {
                if grid[i][j] != 0 { continue }
                var seen = Set<Int>()
                var total = 1
                for k in 0..<4 {
                    let ni = i + dr[k], nj = j + dc[k]
                    if ni >= 0 && ni < n && nj >= 0 && nj < n {
                        let iid = grid[ni][nj]
                        if iid > 1 && seen.insert(iid).inserted {
                            total += sizes[iid] ?? 0
                        }
                    }
                }
                ans = max(ans, total)
            }
        }
        return ans
    }
}
'''

FILES["0828_count_unique_characters_of_all_substrings_of_a_given_string"] = hdr("0828", "Count Unique Characters of All Substrings of a Given String", "count-unique-characters-of-all-substrings-of-a-given-string") + '''
class Solution {
    func uniqueLetterString(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var last = [Character: [Int]]()
        for ch in chars {
            if last[ch] == nil { last[ch] = [-1] }
        }
        for i in 0..<n { last[chars[i]]!.append(i) }
        for key in last.keys { last[key]!.append(n) }
        var ans = 0
        for indices in last.values {
            for k in 1..<(indices.count - 1) {
                ans += (indices[k] - indices[k - 1]) * (indices[k + 1] - indices[k])
            }
        }
        return ans
    }
}
'''

FILES["0829_consecutive_numbers_sum"] = hdr("0829", "Consecutive Numbers Sum", "consecutive-numbers-sum") + '''
class Solution {
    func consecutiveNumbersSum(_ n: Int) -> Int {
        var ans = 0
        var k = 1
        while k * (k - 1) / 2 < n {
            if (n - k * (k - 1) / 2) % k == 0 { ans += 1 }
            k += 1
        }
        return ans
    }
}
'''

def main():
    written = 0
    for folder, body in FILES.items():
        path = ROOT / folder / "Solution.swift"
        existing = path.read_text()
        if "func solve()" not in existing:
            print(f"SKIP {folder} (already implemented)")
            continue
        path.write_text(body.lstrip("\\n") if False else body)
        # ensure starts with comment
        written += 1
        print(f"WROTE {folder}")
    print(f"written={written} total={len(FILES)}")

if __name__ == "__main__":
    main()
