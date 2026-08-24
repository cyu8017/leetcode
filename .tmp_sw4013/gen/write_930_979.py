#!/usr/bin/env python3
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

def hdr(num, title, slug):
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n"

FILES = {}

FILES["0930_binary_subarrays_with_sum"] = hdr("0930", "Binary Subarrays With Sum", "binary-subarrays-with-sum") + '''
class Solution {
    func numSubarraysWithSum(_ nums: [Int], _ goal: Int) -> Int {
        var count = [0: 1]
        var prefix = 0, ans = 0
        for x in nums {
            prefix += x
            ans += count[prefix - goal, default: 0]
            count[prefix, default: 0] += 1
        }
        return ans
    }
}
'''

FILES["0931_minimum_falling_path_sum"] = hdr("0931", "Minimum Falling Path Sum", "minimum-falling-path-sum") + '''
class Solution {
    func minFallingPathSum(_ matrix: [[Int]]) -> Int {
        var dp = matrix[0]
        if matrix.count > 1 {
            for r in 1..<matrix.count {
                var ndp = Array(repeating: 0, count: dp.count)
                for c in 0..<dp.count {
                    var best = dp[c]
                    if c > 0 { best = min(best, dp[c - 1]) }
                    if c + 1 < dp.count { best = min(best, dp[c + 1]) }
                    ndp[c] = matrix[r][c] + best
                }
                dp = ndp
            }
        }
        return dp.min() ?? 0
    }
}
'''

FILES["0932_beautiful_array"] = hdr("0932", "Beautiful Array", "beautiful-array") + '''
class Solution {
    func beautifulArray(_ n: Int) -> [Int] {
        if n == 1 { return [1] }
        let left = beautifulArray((n + 1) / 2)
        let right = beautifulArray(n / 2)
        return left.map { 2 * $0 - 1 } + right.map { 2 * $0 }
    }
}
'''

FILES["0933_number_of_recent_calls"] = hdr("0933", "Number of Recent Calls", "number-of-recent-calls") + '''
class RecentCounter {
    private var q = [Int]()

    init() {}

    func ping(_ t: Int) -> Int {
        q.append(t)
        while !q.isEmpty && q[0] < t - 3000 { q.removeFirst() }
        return q.count
    }
}
'''

FILES["0934_shortest_bridge"] = hdr("0934", "Shortest Bridge", "shortest-bridge") + '''
class Solution {
    func shortestBridge(_ grid: [[Int]]) -> Int {
        var grid = grid
        let n = grid.count
        let dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        func dfs(_ r: Int, _ c: Int) {
            if r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1 { return }
            grid[r][c] = 2
            for d in dirs { dfs(r + d[0], c + d[1]) }
        }
        var found = false
        for i in 0..<n {
            if found { break }
            for j in 0..<n where grid[i][j] == 1 {
                dfs(i, j)
                found = true
                break
            }
        }
        var q = [(Int, Int, Int)]()
        for i in 0..<n {
            for j in 0..<n where grid[i][j] == 2 { q.append((i, j, 0)) }
        }
        var qi = 0
        while qi < q.count {
            let (r, c, dist) = q[qi]
            qi += 1
            for d in dirs {
                let nr = r + d[0], nc = c + d[1]
                if nr < 0 || nr >= n || nc < 0 || nc >= n { continue }
                if grid[nr][nc] == 1 { return dist }
                if grid[nr][nc] == 0 {
                    grid[nr][nc] = 2
                    q.append((nr, nc, dist + 1))
                }
            }
        }
        return -1
    }
}
'''

FILES["0935_knight_dialer"] = hdr("0935", "Knight Dialer", "knight-dialer") + '''
class Solution {
    func knightDialer(_ n: Int) -> Int {
        let mod = 1_000_000_007
        let moves = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        var dp = Array(repeating: 1, count: 10)
        if n > 1 {
            for _ in 0..<(n - 1) {
                var ndp = Array(repeating: 0, count: 10)
                for i in 0..<10 {
                    for j in moves[i] { ndp[j] = (ndp[j] + dp[i]) % mod }
                }
                dp = ndp
            }
        }
        return dp.reduce(0, +) % mod
    }
}
'''

FILES["0936_stamping_the_sequence"] = hdr("0936", "Stamping The Sequence", "stamping-the-sequence") + '''
class Solution {
    func movesToStamp(_ stamp: String, _ target: String) -> [Int] {
        let stamp = Array(stamp), target = Array(target)
        let n = target.count, m = stamp.count
        var done = Array(repeating: false, count: n)
        var ans = [Int]()
        var changed = true
        while changed {
            changed = false
            if n >= m {
                for i in stride(from: n - m, through: 0, by: -1) {
                    var ok = true, any = false
                    for j in 0..<m {
                        if !done[i + j] && target[i + j] != stamp[j] { ok = false; break }
                        if !done[i + j] { any = true }
                    }
                    if ok && any {
                        for j in 0..<m { done[i + j] = true }
                        ans.append(i)
                        changed = true
                        break
                    }
                }
            }
        }
        if done.contains(false) { return [] }
        return ans.reversed()
    }
}
'''

FILES["0937_reorder_data_in_log_files"] = hdr("0937", "Reorder Data in Log Files", "reorder-data-in-log-files") + '''
class Solution {
    func reorderLogFiles(_ logs: [String]) -> [String] {
        var letter = [String]()
        var digit = [String]()
        for log in logs {
            let sp = log.firstIndex(of: " ")!
            let restStart = log.index(after: sp)
            if log[restStart].isLetter { letter.append(log) }
            else { digit.append(log) }
        }
        letter.sort { a, b in
            let spa = a.firstIndex(of: " ")!
            let spb = b.firstIndex(of: " ")!
            let resta = a[a.index(after: spa)...]
            let restb = b[b.index(after: spb)...]
            if resta != restb { return resta < restb }
            return a[..<spa] < b[..<spb]
        }
        return letter + digit
    }
}
'''

FILES["0938_range_sum_of_bst"] = hdr("0938", "Range Sum of BST", "range-sum-of-bst") + TREE + '''
class Solution {
    func rangeSumBST(_ root: TreeNode?, _ low: Int, _ high: Int) -> Int {
        guard let root = root else { return 0 }
        if root.val < low { return rangeSumBST(root.right, low, high) }
        if root.val > high { return rangeSumBST(root.left, low, high) }
        return root.val + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high)
    }
}
'''

FILES["0939_minimum_area_rectangle"] = hdr("0939", "Minimum Area Rectangle", "minimum-area-rectangle") + '''
class Solution {
    func minAreaRect(_ points: [[Int]]) -> Int {
        var byX = [Int: [Int]]()
        for p in points { byX[p[0], default: []].append(p[1]) }
        var last = [String: Int]()
        var ans = Int.max
        for x in byX.keys.sorted() {
            let ys = byX[x]!.sorted()
            for i in 0..<ys.count {
                for j in (i + 1)..<ys.count {
                    let key = "\\(ys[i])#\\(ys[j])"
                    if let prev = last[key] {
                        ans = min(ans, abs(x - prev) * (ys[j] - ys[i]))
                    }
                    last[key] = x
                }
            }
        }
        return ans == Int.max ? 0 : ans
    }
}
'''

FILES["0940_distinct_subsequences_ii"] = hdr("0940", "Distinct Subsequences II", "distinct-subsequences-ii") + '''
class Solution {
    func distinctSubseqII(_ s: String) -> Int {
        let mod = 1_000_000_007
        var ends = Array(repeating: 0, count: 26)
        var total = 1
        let a = Int(Character("a").asciiValue!)
        for ch in s {
            let i = Int(ch.asciiValue!) - a
            let prev = ends[i]
            ends[i] = total
            total = (total - prev + ends[i] + mod) % mod
        }
        return (total - 1 + mod) % mod
    }
}
'''

FILES["0941_valid_mountain_array"] = hdr("0941", "Valid Mountain Array", "valid-mountain-array") + '''
class Solution {
    func validMountainArray(_ arr: [Int]) -> Bool {
        let n = arr.count
        if n < 3 { return false }
        var i = 0
        while i + 1 < n && arr[i] < arr[i + 1] { i += 1 }
        if i == 0 || i == n - 1 { return false }
        while i + 1 < n && arr[i] > arr[i + 1] { i += 1 }
        return i == n - 1
    }
}
'''

FILES["0942_di_string_match"] = hdr("0942", "DI String Match", "di-string-match") + '''
class Solution {
    func diStringMatch(_ s: String) -> [Int] {
        var lo = 0, hi = s.count
        var ans = Array(repeating: 0, count: s.count + 1)
        var k = 0
        for ch in s {
            if ch == "I" { ans[k] = lo; lo += 1 }
            else { ans[k] = hi; hi -= 1 }
            k += 1
        }
        ans[k] = lo
        return ans
    }
}
'''

FILES["0943_find_the_shortest_superstring"] = hdr("0943", "Find the Shortest Superstring", "find-the-shortest-superstring") + '''
class Solution {
    func shortestSuperstring(_ words: [String]) -> String {
        let n = words.count
        var overlap = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n {
            for j in 0..<n where i != j {
                let a = words[i], b = words[j]
                for k in stride(from: min(a.count, b.count), through: 1, by: -1) {
                    if a.suffix(k) == b.prefix(k) {
                        overlap[i][j] = k
                        break
                    }
                }
            }
        }
        let N = 1 << n
        var dp = Array(repeating: Array(repeating: nil as String?, count: n), count: N)
        for i in 0..<n { dp[1 << i][i] = words[i] }
        for mask in 0..<N {
            for last in 0..<n {
                guard (mask & (1 << last)) != 0, let cur = dp[mask][last] else { continue }
                for nxt in 0..<n where (mask & (1 << nxt)) == 0 {
                    let ov = overlap[last][nxt]
                    let cand = cur + String(words[nxt].dropFirst(ov))
                    let nmask = mask | (1 << nxt)
                    if dp[nmask][nxt] == nil || cand.count < dp[nmask][nxt]!.count {
                        dp[nmask][nxt] = cand
                    }
                }
            }
        }
        let full = N - 1
        var best: String?
        for i in 0..<n {
            if let s = dp[full][i], best == nil || s.count < best!.count { best = s }
        }
        return best ?? ""
    }
}
'''

FILES["0944_delete_columns_to_make_sorted"] = hdr("0944", "Delete Columns to Make Sorted", "delete-columns-to-make-sorted") + '''
class Solution {
    func minDeletionSize(_ strs: [String]) -> Int {
        let rows = strs.map { Array($0) }
        let m = rows[0].count, n = rows.count
        var ans = 0
        for c in 0..<m {
            for r in 0..<(n - 1) {
                if rows[r][c] > rows[r + 1][c] { ans += 1; break }
            }
        }
        return ans
    }
}
'''

FILES["0945_minimum_increment_to_make_array_unique"] = hdr("0945", "Minimum Increment to Make Array Unique", "minimum-increment-to-make-array-unique") + '''
class Solution {
    func minIncrementForUnique(_ nums: [Int]) -> Int {
        var a = nums.sorted()
        var ans = 0
        for i in 1..<a.count {
            if a[i] <= a[i - 1] {
                let need = a[i - 1] + 1
                ans += need - a[i]
                a[i] = need
            }
        }
        return ans
    }
}
'''

FILES["0946_validate_stack_sequences"] = hdr("0946", "Validate Stack Sequences", "validate-stack-sequences") + '''
class Solution {
    func validateStackSequences(_ pushed: [Int], _ popped: [Int]) -> Bool {
        var stack = [Int]()
        var j = 0
        for x in pushed {
            stack.append(x)
            while !stack.isEmpty && stack.last! == popped[j] {
                stack.removeLast()
                j += 1
            }
        }
        return stack.isEmpty
    }
}
'''

FILES["0947_most_stones_removed_with_same_row_or_column"] = hdr("0947", "Most Stones Removed with Same Row or Column", "most-stones-removed-with-same-row-or-column") + '''
class Solution {
    func removeStones(_ stones: [[Int]]) -> Int {
        var parent = [Int: Int]()
        func find(_ x: Int) -> Int {
            if parent[x] == nil { parent[x] = x }
            if parent[x]! != x { parent[x] = find(parent[x]!) }
            return parent[x]!
        }
        func unite(_ a: Int, _ b: Int) {
            parent[find(a)] = find(b)
        }
        for s in stones { unite(s[0], ~s[1]) }
        var roots = Set<Int>()
        for s in stones { roots.insert(find(s[0])) }
        return stones.count - roots.count
    }
}
'''

FILES["0948_bag_of_tokens"] = hdr("0948", "Bag of Tokens", "bag-of-tokens") + '''
class Solution {
    func bagOfTokensScore(_ tokens: [Int], _ power: Int) -> Int {
        let t = tokens.sorted()
        var i = 0, j = t.count - 1, score = 0, ans = 0, power = power
        while i <= j {
            if power >= t[i] {
                power -= t[i]
                i += 1
                score += 1
                ans = max(ans, score)
            } else if score > 0 {
                power += t[j]
                j -= 1
                score -= 1
            } else {
                break
            }
        }
        return ans
    }
}
'''

FILES["0949_largest_time_for_given_digits"] = hdr("0949", "Largest Time for Given Digits", "largest-time-for-given-digits") + '''
class Solution {
    func largestTimeFromDigits(_ arr: [Int]) -> String {
        var a = arr.sorted()
        var best = ""
        func nextPermutation(_ a: inout [Int]) -> Bool {
            var i = a.count - 2
            while i >= 0 && a[i] >= a[i + 1] { i -= 1 }
            if i < 0 { return false }
            var j = a.count - 1
            while a[j] <= a[i] { j -= 1 }
            a.swapAt(i, j)
            var l = i + 1, r = a.count - 1
            while l < r { a.swapAt(l, r); l += 1; r -= 1 }
            return true
        }
        repeat {
            let hours = 10 * a[0] + a[1]
            let minutes = 10 * a[2] + a[3]
            if hours < 24 && minutes < 60 {
                let cand = String(format: "%02d:%02d", hours, minutes)
                if cand > best { best = cand }
            }
        } while nextPermutation(&a)
        return best
    }
}
'''

FILES["0950_reveal_cards_in_increasing_order"] = hdr("0950", "Reveal Cards In Increasing Order", "reveal-cards-in-increasing-order") + '''
class Solution {
    func deckRevealedIncreasing(_ deck: [Int]) -> [Int] {
        let cards = deck.sorted()
        var idx = Array(0..<deck.count)
        var ans = Array(repeating: 0, count: deck.count)
        for card in cards {
            ans[idx.removeFirst()] = card
            if !idx.isEmpty { idx.append(idx.removeFirst()) }
        }
        return ans
    }
}
'''

FILES["0951_flip_equivalent_binary_trees"] = hdr("0951", "Flip Equivalent Binary Trees", "flip-equivalent-binary-trees") + TREE + '''
class Solution {
    func flipEquiv(_ root1: TreeNode?, _ root2: TreeNode?) -> Bool {
        if root1 == nil && root2 == nil { return true }
        guard let a = root1, let b = root2, a.val == b.val else { return false }
        return (flipEquiv(a.left, b.left) && flipEquiv(a.right, b.right))
            || (flipEquiv(a.left, b.right) && flipEquiv(a.right, b.left))
    }
}
'''

FILES["0952_largest_component_size_by_common_factor"] = hdr("0952", "Largest Component Size by Common Factor", "largest-component-size-by-common-factor") + '''
class Solution {
    func largestComponentSize(_ nums: [Int]) -> Int {
        let mx = nums.max() ?? 0
        var parent = Array(0...mx)
        func find(_ x: Int) -> Int {
            if parent[x] != x { parent[x] = find(parent[x]) }
            return parent[x]
        }
        func unite(_ a: Int, _ b: Int) { parent[find(a)] = find(b) }
        func factors(_ x: Int) -> [Int] {
            var x = x, res = [Int]()
            var d = 2
            while d * d <= x {
                if x % d == 0 {
                    res.append(d)
                    while x % d == 0 { x /= d }
                }
                d += 1
            }
            if x > 1 { res.append(x) }
            return res
        }
        for num in nums {
            for f in factors(num) { unite(num, f) }
        }
        var cnt = [Int: Int]()
        var ans = 0
        for num in nums {
            let r = find(num)
            cnt[r, default: 0] += 1
            ans = max(ans, cnt[r]!)
        }
        return ans
    }
}
'''

FILES["0953_verifying_an_alien_dictionary"] = hdr("0953", "Verifying an Alien Dictionary", "verifying-an-alien-dictionary") + '''
class Solution {
    func isAlienSorted(_ words: [String], _ order: String) -> Bool {
        var rank = Array(repeating: 0, count: 26)
        let a = Int(Character("a").asciiValue!)
        for (i, ch) in order.enumerated() { rank[Int(ch.asciiValue!) - a] = i }
        func lessEq(_ aS: String, _ bS: String) -> Bool {
            let ca = Array(aS), cb = Array(bS)
            let n = min(ca.count, cb.count)
            for i in 0..<n {
                let ra = rank[Int(ca[i].asciiValue!) - a]
                let rb = rank[Int(cb[i].asciiValue!) - a]
                if ra != rb { return ra < rb }
            }
            return ca.count <= cb.count
        }
        for i in 0..<(words.count - 1) {
            if !lessEq(words[i], words[i + 1]) { return false }
        }
        return true
    }
}
'''

FILES["0954_array_of_doubled_pairs"] = hdr("0954", "Array of Doubled Pairs", "array-of-doubled-pairs") + '''
class Solution {
    func canReorderDoubled(_ arr: [Int]) -> Bool {
        var count = [Int: Int]()
        for x in arr { count[x, default: 0] += 1 }
        let keys = count.keys.sorted { abs($0) < abs($1) }
        for x in keys {
            let need = count[x] ?? 0
            if need == 0 { continue }
            if (count[2 * x] ?? 0) < need { return false }
            count[2 * x]! -= need
        }
        return true
    }
}
'''

FILES["0955_delete_columns_to_make_sorted_ii"] = hdr("0955", "Delete Columns to Make Sorted II", "delete-columns-to-make-sorted-ii") + '''
class Solution {
    func minDeletionSize(_ strs: [String]) -> Int {
        let rows = strs.map { Array($0) }
        let n = rows.count, m = rows[0].count
        var deleted = 0
        var sortedPair = Array(repeating: false, count: max(0, n - 1))
        for c in 0..<m {
            var bad = false
            for r in 0..<(n - 1) {
                if !sortedPair[r] && rows[r][c] > rows[r + 1][c] { bad = true; break }
            }
            if bad { deleted += 1; continue }
            for r in 0..<(n - 1) {
                if rows[r][c] < rows[r + 1][c] { sortedPair[r] = true }
            }
        }
        return deleted
    }
}
'''

FILES["0956_tallest_billboard"] = hdr("0956", "Tallest Billboard", "tallest-billboard") + '''
class Solution {
    func tallestBillboard(_ rods: [Int]) -> Int {
        var dp = [0: 0]
        for rod in rods {
            let cur = dp
            for (diff, taller) in cur {
                let key1 = diff + rod
                dp[key1] = max(dp[key1] ?? 0, taller + rod)
                let nd = abs(diff - rod)
                let nt = diff >= rod ? taller : taller - diff + rod
                dp[nd] = max(dp[nd] ?? 0, nt)
            }
        }
        return dp[0] ?? 0
    }
}
'''

FILES["0957_prison_cells_after_n_days"] = hdr("0957", "Prison Cells After N Days", "prison-cells-after-n-days") + '''
class Solution {
    func prisonAfterNDays(_ cells: [Int], _ n: Int) -> [Int] {
        var seen = [String: Int]()
        var state = cells
        var n = n
        while n > 0 {
            let key = state.map(String.init).joined(separator: ",")
            if let prev = seen[key] {
                let cycle = prev - n
                if cycle > 0 { n %= cycle }
                if n == 0 { break }
            }
            seen[key] = n
            var nxt = Array(repeating: 0, count: 8)
            for i in 1...6 { nxt[i] = state[i - 1] == state[i + 1] ? 1 : 0 }
            state = nxt
            n -= 1
        }
        return state
    }
}
'''

FILES["0958_check_completeness_of_a_binary_tree"] = hdr("0958", "Check Completeness of a Binary Tree", "check-completeness-of-a-binary-tree") + TREE + '''
class Solution {
    func isCompleteTree(_ root: TreeNode?) -> Bool {
        var q: [TreeNode?] = [root]
        var end = false
        var qi = 0
        while qi < q.count {
            let node = q[qi]
            qi += 1
            if node == nil {
                end = true
            } else {
                if end { return false }
                q.append(node!.left)
                q.append(node!.right)
            }
        }
        return true
    }
}
'''

FILES["0959_regions_cut_by_slashes"] = hdr("0959", "Regions Cut By Slashes", "regions-cut-by-slashes") + '''
class Solution {
    func regionsBySlashes(_ grid: [String]) -> Int {
        let n = grid.count
        var parent = Array(0..<(n * n * 4))
        func find(_ x: Int) -> Int {
            if parent[x] != x { parent[x] = find(parent[x]) }
            return parent[x]
        }
        func unite(_ a: Int, _ b: Int) { parent[find(a)] = find(b) }
        let rows = grid.map { Array($0) }
        for r in 0..<n {
            for c in 0..<n {
                let root = 4 * (r * n + c)
                let ch = rows[r][c]
                if ch == "/" {
                    unite(root + 0, root + 3)
                    unite(root + 1, root + 2)
                } else if ch == "\\\\" {
                    unite(root + 0, root + 1)
                    unite(root + 2, root + 3)
                } else {
                    unite(root + 0, root + 1)
                    unite(root + 1, root + 2)
                    unite(root + 2, root + 3)
                }
                if r + 1 < n { unite(root + 2, root + 4 * n + 0) }
                if c + 1 < n { unite(root + 1, root + 4 + 3) }
            }
        }
        var ans = 0
        for i in 0..<parent.count where find(i) == i { ans += 1 }
        return ans
    }
}
'''

FILES["0960_delete_columns_to_make_sorted_iii"] = hdr("0960", "Delete Columns to Make Sorted III", "delete-columns-to-make-sorted-iii") + '''
class Solution {
    func minDeletionSize(_ strs: [String]) -> Int {
        let rows = strs.map { Array($0) }
        let m = rows[0].count
        var dp = Array(repeating: 1, count: m)
        for j in 0..<m {
            for i in 0..<j {
                var ok = true
                for row in rows where row[i] > row[j] { ok = false; break }
                if ok { dp[j] = max(dp[j], dp[i] + 1) }
            }
        }
        return m - (dp.max() ?? 0)
    }
}
'''

FILES["0961_n_repeated_element_in_size_2n_array"] = hdr("0961", "N-Repeated Element in Size 2N Array", "n-repeated-element-in-size-2n-array") + '''
class Solution {
    func repeatedNTimes(_ nums: [Int]) -> Int {
        var seen = Set<Int>()
        for x in nums {
            if seen.contains(x) { return x }
            seen.insert(x)
        }
        return -1
    }
}
'''

FILES["0962_maximum_width_ramp"] = hdr("0962", "Maximum Width Ramp", "maximum-width-ramp") + '''
class Solution {
    func maxWidthRamp(_ nums: [Int]) -> Int {
        var stack = [Int]()
        for i in 0..<nums.count {
            if stack.isEmpty || nums[stack.last!] > nums[i] { stack.append(i) }
        }
        var ans = 0
        for j in stride(from: nums.count - 1, through: 0, by: -1) {
            while !stack.isEmpty && nums[stack.last!] <= nums[j] {
                ans = max(ans, j - stack.last!)
                stack.removeLast()
            }
        }
        return ans
    }
}
'''

FILES["0963_minimum_area_rectangle_ii"] = hdr("0963", "Minimum Area Rectangle II", "minimum-area-rectangle-ii") + '''
class Solution {
    func minAreaFreeRect(_ points: [[Int]]) -> Double {
        let n = points.count
        var groups = [String: [(Int, Int)]]()
        for i in 0..<n {
            for j in (i + 1)..<n {
                let cx = points[i][0] + points[j][0]
                let cy = points[i][1] + points[j][1]
                let dx = points[i][0] - points[j][0]
                let dy = points[i][1] - points[j][1]
                let dist = dx * dx + dy * dy
                let key = "\\(cx)#\\(cy)#\\(dist)"
                groups[key, default: []].append((i, j))
            }
        }
        var ans = Double.greatestFiniteMagnitude
        for pairs in groups.values {
            for a in 0..<pairs.count {
                for b in (a + 1)..<pairs.count {
                    let p1 = pairs[a].0, p2 = pairs[b].0, q2 = pairs[b].1
                    let d1 = hypot(Double(points[p1][0] - points[p2][0]), Double(points[p1][1] - points[p2][1]))
                    let d2 = hypot(Double(points[p1][0] - points[q2][0]), Double(points[p1][1] - points[q2][1]))
                    let area = d1 * d2
                    if area > 0 { ans = min(ans, area) }
                }
            }
        }
        return ans == Double.greatestFiniteMagnitude ? 0.0 : ans
    }
}
'''

FILES["0964_least_operators_to_express_number"] = hdr("0964", "Least Operators to Express Number", "least-operators-to-express-number") + '''
class Solution {
    func leastOpsExpressTarget(_ x: Int, _ target: Int) -> Int {
        var memo = [Int: Int]()
        func dfs(_ t: Int) -> Int {
            if let v = memo[t] { return v }
            if x > t {
                let ans = min(2 * t - 1, 2 * (x - t))
                memo[t] = ans
                return ans
            }
            if x == t {
                memo[t] = 0
                return 0
            }
            var prod = x
            var n = 0
            while prod < t {
                prod *= x
                n += 1
            }
            if prod == t {
                memo[t] = n
                return n
            }
            var ans = dfs(t - prod / x) + n
            if prod < 2 * t { ans = min(ans, dfs(prod - t) + n + 1) }
            memo[t] = ans
            return ans
        }
        return dfs(target)
    }
}
'''

FILES["0965_univalued_binary_tree"] = hdr("0965", "Univalued Binary Tree", "univalued-binary-tree") + TREE + '''
class Solution {
    func isUnivalTree(_ root: TreeNode?) -> Bool {
        guard let root = root else { return true }
        func dfs(_ node: TreeNode?, _ v: Int) -> Bool {
            guard let node = node else { return true }
            if node.val != v { return false }
            return dfs(node.left, v) && dfs(node.right, v)
        }
        return dfs(root, root.val)
    }
}
'''

FILES["0966_vowel_spellchecker"] = hdr("0966", "Vowel Spellchecker", "vowel-spellchecker") + '''
class Solution {
    func spellchecker(_ wordlist: [String], _ queries: [String]) -> [String] {
        let exact = Set(wordlist)
        var lowerMap = [String: String]()
        var vowelMap = [String: String]()
        func devowel(_ w: String) -> String {
            return String(w.lowercased().map { "aeiou".contains($0) ? "*" : $0 })
        }
        for w in wordlist {
            let low = w.lowercased()
            if lowerMap[low] == nil { lowerMap[low] = w }
            let dv = devowel(w)
            if vowelMap[dv] == nil { vowelMap[dv] = w }
        }
        return queries.map { q in
            if exact.contains(q) { return q }
            if let w = lowerMap[q.lowercased()] { return w }
            if let w = vowelMap[devowel(q)] { return w }
            return ""
        }
    }
}
'''

FILES["0967_numbers_with_same_consecutive_differences"] = hdr("0967", "Numbers With Same Consecutive Differences", "numbers-with-same-consecutive-differences") + '''
class Solution {
    func numsSameConsecDiff(_ n: Int, _ k: Int) -> [Int] {
        var ans = [Int]()
        func dfs(_ num: Int, _ length: Int) {
            if length == n {
                ans.append(num)
                return
            }
            let last = num % 10
            var nexts = Set<Int>([last + k, last - k])
            for nxt in nexts where nxt >= 0 && nxt <= 9 {
                dfs(num * 10 + nxt, length + 1)
            }
        }
        for start in 1...9 { dfs(start, 1) }
        return ans
    }
}
'''

FILES["0968_binary_tree_cameras"] = hdr("0968", "Binary Tree Cameras", "binary-tree-cameras") + TREE + '''
class Solution {
    private var cameras = 0

    func minCameraCover(_ root: TreeNode?) -> Int {
        cameras = 0
        let rootState = dfs(root)
        return cameras + (rootState == 0 ? 1 : 0)
    }

    private func dfs(_ node: TreeNode?) -> Int {
        guard let node = node else { return 1 }
        let left = dfs(node.left)
        let right = dfs(node.right)
        if left == 0 || right == 0 {
            cameras += 1
            return 2
        }
        if left == 2 || right == 2 { return 1 }
        return 0
    }
}
'''

FILES["0969_pancake_sorting"] = hdr("0969", "Pancake Sorting", "pancake-sorting") + '''
class Solution {
    func pancakeSort(_ arr: [Int]) -> [Int] {
        var a = arr
        var ans = [Int]()
        for size in stride(from: a.count, through: 2, by: -1) {
            let i = a.firstIndex(of: size)!
            if i == size - 1 { continue }
            if i > 0 {
                ans.append(i + 1)
                a[0...i].reverse()
            }
            ans.append(size)
            a[0...(size - 1)].reverse()
        }
        return ans
    }
}
'''

FILES["0970_powerful_integers"] = hdr("0970", "Powerful Integers", "powerful-integers") + '''
class Solution {
    func powerfulIntegers(_ x: Int, _ y: Int, _ bound: Int) -> [Int] {
        var ans = Set<Int>()
        var a = 1
        while a < bound {
            var b = 1
            while a + b <= bound {
                ans.insert(a + b)
                if y == 1 { break }
                b *= y
            }
            if x == 1 { break }
            a *= x
        }
        return Array(ans)
    }
}
'''

FILES["0971_flip_binary_tree_to_match_preorder_traversal"] = hdr("0971", "Flip Binary Tree To Match Preorder Traversal", "flip-binary-tree-to-match-preorder-traversal") + TREE + '''
class Solution {
    func flipMatchVoyage(_ root: TreeNode?, _ voyage: [Int]) -> [Int] {
        var i = 0
        var ans = [Int]()
        func dfs(_ node: TreeNode?) -> Bool {
            guard let node = node else { return true }
            if node.val != voyage[i] { return false }
            i += 1
            if let left = node.left, left.val != voyage[i] {
                ans.append(node.val)
                return dfs(node.right) && dfs(node.left)
            }
            return dfs(node.left) && dfs(node.right)
        }
        return dfs(root) ? ans : [-1]
    }
}
'''

FILES["0972_equal_rational_numbers"] = hdr("0972", "Equal Rational Numbers", "equal-rational-numbers") + '''
class Solution {
    func isRationalEqual(_ s: String, _ t: String) -> Bool {
        return abs(parse(s) - parse(t)) < 1e-12
    }

    private func parse(_ x: String) -> Double {
        if !x.contains("(") { return x.isEmpty ? 0.0 : Double(x)! }
        let lp = x.firstIndex(of: "(")!
        var nonRep = String(x[..<lp])
        let rp = x.index(before: x.endIndex)
        let rep = String(x[x.index(after: lp)..<rp])
        if !nonRep.contains(".") { nonRep += "." }
        let dot = nonRep.firstIndex(of: ".")!
        let integer = String(nonRep[..<dot])
        let frac = String(nonRep[nonRep.index(after: dot)...])
        var bas = integer.isEmpty ? 0.0 : Double(integer)!
        if !frac.isEmpty {
            var denom = 1.0
            for _ in 0..<frac.count { denom *= 10 }
            bas += Double(frac)! / denom
        }
        if !rep.isEmpty {
            let repVal = Double(rep)!
            var cycle = 1.0
            for _ in 0..<rep.count { cycle *= 10 }
            var denom = cycle - 1
            for _ in 0..<frac.count { denom *= 10 }
            bas += repVal / denom
        }
        return bas
    }
}
'''

FILES["0973_k_closest_points_to_origin"] = hdr("0973", "K Closest Points to Origin", "k-closest-points-to-origin") + '''
class Solution {
    func kClosest(_ points: [[Int]], _ k: Int) -> [[Int]] {
        return Array(points.sorted { $0[0] * $0[0] + $0[1] * $0[1] < $1[0] * $1[0] + $1[1] * $1[1] }.prefix(k))
    }
}
'''

FILES["0974_subarray_sums_divisible_by_k"] = hdr("0974", "Subarray Sums Divisible by K", "subarray-sums-divisible-by-k") + '''
class Solution {
    func subarraysDivByK(_ nums: [Int], _ k: Int) -> Int {
        var count = [0: 1]
        var prefix = 0, ans = 0
        for x in nums {
            prefix = ((prefix + x) % k + k) % k
            ans += count[prefix, default: 0]
            count[prefix, default: 0] += 1
        }
        return ans
    }
}
'''

FILES["0975_odd_even_jump"] = hdr("0975", "Odd Even Jump", "odd-even-jump") + '''
class Solution {
    func oddEvenJumps(_ arr: [Int]) -> Int {
        let n = arr.count
        var nextHigher = Array(repeating: 0, count: n)
        var nextLower = Array(repeating: 0, count: n)
        var order = Array(0..<n)
        order.sort { arr[$0] == arr[$1] ? $0 < $1 : arr[$0] < arr[$1] }
        var stack = [Int]()
        for i in order {
            while !stack.isEmpty && stack.last! < i {
                nextHigher[stack.removeLast()] = i
            }
            stack.append(i)
        }
        stack.removeAll()
        order.sort { arr[$0] == arr[$1] ? $0 < $1 : arr[$0] > arr[$1] }
        for i in order {
            while !stack.isEmpty && stack.last! < i {
                nextLower[stack.removeLast()] = i
            }
            stack.append(i)
        }
        var odd = Array(repeating: false, count: n)
        var even = Array(repeating: false, count: n)
        odd[n - 1] = true
        even[n - 1] = true
        for i in stride(from: n - 2, through: 0, by: -1) {
            if nextHigher[i] != 0 { odd[i] = even[nextHigher[i]] }
            if nextLower[i] != 0 { even[i] = odd[nextLower[i]] }
        }
        return odd.filter { $0 }.count
    }
}
'''

FILES["0976_largest_perimeter_triangle"] = hdr("0976", "Largest Perimeter Triangle", "largest-perimeter-triangle") + '''
class Solution {
    func largestPerimeter(_ nums: [Int]) -> Int {
        let a = nums.sorted()
        for i in stride(from: a.count - 1, through: 2, by: -1) {
            if a[i] < a[i - 1] + a[i - 2] { return a[i] + a[i - 1] + a[i - 2] }
        }
        return 0
    }
}
'''

FILES["0977_squares_of_a_sorted_array"] = hdr("0977", "Squares of a Sorted Array", "squares-of-a-sorted-array") + '''
class Solution {
    func sortedSquares(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var ans = Array(repeating: 0, count: n)
        var i = 0, j = n - 1
        for k in stride(from: n - 1, through: 0, by: -1) {
            if abs(nums[i]) > abs(nums[j]) {
                ans[k] = nums[i] * nums[i]
                i += 1
            } else {
                ans[k] = nums[j] * nums[j]
                j -= 1
            }
        }
        return ans
    }
}
'''

FILES["0978_longest_turbulent_subarray"] = hdr("0978", "Longest Turbulent Subarray", "longest-turbulent-subarray") + '''
class Solution {
    func maxTurbulenceSize(_ arr: [Int]) -> Int {
        var ans = 1, cur = 1
        if arr.count > 1 {
            for i in 1..<arr.count {
                if arr[i] == arr[i - 1] {
                    cur = 1
                } else if i == 1 || (arr[i] - arr[i - 1]) * (arr[i - 1] - arr[i - 2]) < 0 {
                    cur += 1
                } else {
                    cur = 2
                }
                ans = max(ans, cur)
            }
        }
        return ans
    }
}
'''

FILES["0979_distribute_coins_in_binary_tree"] = hdr("0979", "Distribute Coins in Binary Tree", "distribute-coins-in-binary-tree") + TREE + '''
class Solution {
    private var ans = 0

    func distributeCoins(_ root: TreeNode?) -> Int {
        ans = 0
        _ = dfs(root)
        return ans
    }

    private func dfs(_ node: TreeNode?) -> Int {
        guard let node = node else { return 0 }
        let left = dfs(node.left)
        let right = dfs(node.right)
        ans += abs(left) + abs(right)
        return node.val + left + right - 1
    }
}
'''

def main():
    written = 0
    for folder, body in FILES.items():
        path = ROOT / folder / "Solution.swift"
        existing = path.read_text()
        if "func solve()" not in existing:
            print(f"SKIP {folder}")
            continue
        path.write_text(body)
        written += 1
        print(f"WROTE {folder}")
    print(f"written={written} total={len(FILES)}")

if __name__ == "__main__":
    main()
