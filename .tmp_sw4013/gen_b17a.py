#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def hdr(num, title, slug):
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n"

TREE = '''
public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}
'''

FILES = {}

FILES["3285_find_indices_of_stable_mountains"] = hdr("3285", "Find Indices of Stable Mountains", "find-indices-of-stable-mountains") + '''
class Solution {
    func stableMountains(_ height: [Int], _ threshold: Int) -> [Int] {
        var ans = [Int]()
        for i in 1..<height.count {
            if height[i - 1] > threshold { ans.append(i) }
        }
        return ans
    }
}
'''

FILES["3286_find_a_safe_walk_through_a_grid"] = hdr("3286", "Find a Safe Walk Through a Grid", "find-a-safe-walk-through-a-grid") + '''
class Solution {
    func findSafeWalk(_ grid: [[Int]], _ health: Int) -> Bool {
        let m = grid.count, n = grid[0].count
        var vis = Array(repeating: Array(repeating: -1, count: n), count: m)
        let qh = health - grid[0][0]
        if qh <= 0 { return false }
        var q = [(0, 0, qh)]
        vis[0][0] = qh
        let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        var qi = 0
        while qi < q.count {
            let (r, c, h) = q[qi]
            qi += 1
            if r == m - 1 && c == n - 1 { return true }
            for (dr, dc) in dirs {
                let nr = r + dr, nc = c + dc
                if nr < 0 || nc < 0 || nr >= m || nc >= n { continue }
                let nh = h - grid[nr][nc]
                if nh <= 0 { continue }
                if nh > vis[nr][nc] {
                    vis[nr][nc] = nh
                    q.append((nr, nc, nh))
                }
            }
        }
        return false
    }
}
'''

FILES["3287_find_the_maximum_sequence_value_of_array"] = hdr("3287", "Find the Maximum Sequence Value of Array", "find-the-maximum-sequence-value-of-array") + '''
class Solution {
    func maxValue(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        let MAX = 128
        var left = Array(repeating: Array(repeating: Array(repeating: false, count: MAX), count: k + 1), count: n + 1)
        left[0][0][0] = true
        for i in 0..<n {
            for j in 0...k {
                for v in 0..<MAX {
                    if !left[i][j][v] { continue }
                    left[i + 1][j][v] = true
                    if j < k { left[i + 1][j + 1][v | nums[i]] = true }
                }
            }
        }
        var right = Array(repeating: Array(repeating: Array(repeating: false, count: MAX), count: k + 1), count: n + 1)
        right[n][0][0] = true
        for i in stride(from: n - 1, through: 0, by: -1) {
            for j in 0...k {
                for v in 0..<MAX {
                    if !right[i + 1][j][v] { continue }
                    right[i][j][v] = true
                    if j < k { right[i][j + 1][v | nums[i]] = true }
                }
            }
        }
        var ans = 0
        if k <= n {
            for mid in k...(n - k) {
                for a in 0..<MAX {
                    if !left[mid][k][a] { continue }
                    for b in 0..<MAX {
                        if right[mid][k][b] && (a ^ b) > ans { ans = a ^ b }
                    }
                }
            }
        }
        return ans
    }
}
'''

FILES["3288_length_of_the_longest_increasing_path"] = hdr("3288", "Length of the Longest Increasing Path", "length-of-the-longest-increasing-path") + '''
class Solution {
    func maxPathLength(_ coordinates: [[Int]], _ k: Int) -> Int {
        let n = coordinates.count
        var arr = [[Int]]()
        for i in 0..<n {
            arr.append([coordinates[i][0], coordinates[i][1], i])
        }
        arr.sort { a, b in
            if a[0] == b[0] { return a[1] > b[1] }
            return a[0] < b[0]
        }
        let kx = coordinates[k][0], ky = coordinates[k][1]
        var left = [Int](), right = [Int]()
        for p in arr {
            if p[0] < kx && p[1] < ky { left.append(p[1]) }
            if p[0] > kx && p[1] > ky { right.append(p[1]) }
        }
        return lis(left) + 1 + lis(right)
    }

    private func lis(_ a: [Int]) -> Int {
        var tails = [Int]()
        for x in a {
            var lo = 0, hi = tails.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if tails[mid] < x { lo = mid + 1 }
                else { hi = mid }
            }
            if lo == tails.count { tails.append(x) }
            else { tails[lo] = x }
        }
        return tails.count
    }
}
'''

FILES["3289_the_two_sneaky_numbers_of_digitville"] = hdr("3289", "The Two Sneaky Numbers of Digitville", "the-two-sneaky-numbers-of-digitville") + '''
class Solution {
    func getSneakyNumbers(_ nums: [Int]) -> [Int] {
        var seen = Set<Int>()
        var ans = [Int]()
        for x in nums {
            if !seen.insert(x).inserted { ans.append(x) }
        }
        return ans
    }
}
'''

FILES["3290_maximum_multiplication_score"] = hdr("3290", "Maximum Multiplication Score", "maximum-multiplication-score") + '''
class Solution {
    func maxScore(_ a: [Int], _ b: [Int]) -> Int {
        let neg = -(1 << 62)
        var dp = [0, neg, neg, neg, neg]
        for x in b {
            for k in stride(from: 4, through: 1, by: -1) {
                if dp[k - 1] == neg { continue }
                let v = dp[k - 1] + a[k - 1] * x
                if v > dp[k] { dp[k] = v }
            }
        }
        return dp[4]
    }
}
'''

TRIE_VALID = '''
class Solution {
    func minValidStrings(_ words: [String], _ target: String) -> Int {
        let t = Array(target)
        let n = t.count
        let inf = 1_000_000_000
        var dp = Array(repeating: inf, count: n + 1)
        dp[0] = 0
        let root = TrieNode()
        for w in words {
            var cur = root
            for c in w {
                let ci = Int(c.asciiValue! - 97)
                if cur.next[ci] == nil { cur.next[ci] = TrieNode() }
                cur = cur.next[ci]!
            }
        }
        for i in 0..<n {
            if dp[i] == inf { continue }
            var cur: TrieNode? = root
            for j in i..<n {
                let ci = Int(t[j].asciiValue! - 97)
                guard let node = cur?.next[ci] else { break }
                cur = node
                if dp[i] + 1 < dp[j + 1] { dp[j + 1] = dp[i] + 1 }
            }
        }
        return dp[n] == inf ? -1 : dp[n]
    }
}

private class TrieNode {
    var next: [TrieNode?] = Array(repeating: nil, count: 26)
}
'''

FILES["3291_minimum_number_of_valid_strings_to_form_target_i"] = hdr("3291", "Minimum Number of Valid Strings to Form Target I", "minimum-number-of-valid-strings-to-form-target-i") + TRIE_VALID

FILES["3292_minimum_number_of_valid_strings_to_form_target_ii"] = hdr("3292", "Minimum Number of Valid Strings to Form Target II", "minimum-number-of-valid-strings-to-form-target-ii") + TRIE_VALID

FILES["3294_convert_doubly_linked_list_to_array_ii"] = hdr("3294", "Convert Doubly Linked List to Array II", "convert-doubly-linked-list-to-array-ii") + '''
public class Node {
    public var val: Int
    public var prev: Node?
    public var next: Node?
    public init() { self.val = 0; self.prev = nil; self.next = nil }
    public init(_ val: Int) { self.val = val; self.prev = nil; self.next = nil }
}

class Solution {
    func toArray(_ node: Node?) -> [Int] {
        var node = node
        while node?.prev != nil { node = node?.prev }
        var ans = [Int]()
        while let cur = node {
            ans.append(cur.val)
            node = cur.next
        }
        return ans
    }
}
'''

FILES["3295_report_spam_message"] = hdr("3295", "Report Spam Message", "report-spam-message") + '''
class Solution {
    func reportSpam(_ message: [String], _ bannedWords: [String]) -> Bool {
        let ban = Set(bannedWords)
        var cnt = 0
        for w in message {
            if ban.contains(w) {
                cnt += 1
                if cnt >= 2 { return true }
            }
        }
        return false
    }
}
'''

FILES["3296_minimum_number_of_seconds_to_make_mountain_height_zero"] = hdr("3296", "Minimum Number of Seconds to Make Mountain Height Zero", "minimum-number-of-seconds-to-make-mountain-height-zero") + '''
class Solution {
    func minNumberOfSeconds(_ mountainHeight: Int, _ workerTimes: [Int]) -> Int {
        var lo = 0, hi = Int(1e18)
        while lo < hi {
            let mid = (lo + hi) / 2
            if ok(mid, mountainHeight, workerTimes) { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }

    private func ok(_ t: Int, _ mountainHeight: Int, _ workerTimes: [Int]) -> Bool {
        var total = 0
        for w in workerTimes {
            var l = 0, h = mountainHeight
            while l < h {
                let mid = (l + h + 1) / 2
                if w * mid * (mid + 1) / 2 <= t { l = mid }
                else { h = mid - 1 }
            }
            total += l
            if total >= mountainHeight { return true }
        }
        return total >= mountainHeight
    }
}
'''

VALID_SUB = '''
class Solution {
    func validSubstringCount(_ word1: String, _ word2: String) -> Int {
        let w1 = Array(word1)
        var need = Array(repeating: 0, count: 26)
        var required = 0
        for c in word2 {
            let i = Int(c.asciiValue! - 97)
            if need[i] == 0 { required += 1 }
            need[i] += 1
        }
        var have = Array(repeating: 0, count: 26)
        var formed = 0
        var ans = 0
        var l = 0
        for r in 0..<w1.count {
            let c = Int(w1[r].asciiValue! - 97)
            have[c] += 1
            if have[c] == need[c] && need[c] > 0 { formed += 1 }
            while formed == required && l <= r {
                ans += w1.count - r
                let c2 = Int(w1[l].asciiValue! - 97)
                if have[c2] == need[c2] && need[c2] > 0 { formed -= 1 }
                have[c2] -= 1
                l += 1
            }
        }
        return ans
    }
}
'''

FILES["3297_count_substrings_that_can_be_rearranged_to_contain_a_string_i"] = hdr("3297", "Count Substrings That Can Be Rearranged to Contain a String I", "count-substrings-that-can-be-rearranged-to-contain-a-string-i") + VALID_SUB

FILES["3298_count_substrings_that_can_be_rearranged_to_contain_a_string_ii"] = hdr("3298", "Count Substrings That Can Be Rearranged to Contain a String II", "count-substrings-that-can-be-rearranged-to-contain-a-string-ii") + VALID_SUB

FILES["3299_sum_of_consecutive_subsequences"] = hdr("3299", "Sum of Consecutive Subsequences", "sum-of-consecutive-subsequences") + '''
class Solution {
    func rangeSum(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        var cnt = [Int: Int]()
        var sum = [Int: Int]()
        var ans = 0
        for x in nums {
            let cL = cnt[x - 1, default: 0], sL = sum[x - 1, default: 0]
            let cR = cnt[x + 1, default: 0], sR = sum[x + 1, default: 0]
            var c = (1 + cL + cR) % mod
            var s = (x + sL + cL * x % mod + sR + cR * x % mod) % mod
            if cL > 0 && cR > 0 {
                c = (c + cL * cR % mod) % mod
                s = (s + sL * cR % mod + sR * cL % mod + cL * cR % mod * x % mod) % mod
            }
            cnt[x, default: 0] = (cnt[x, default: 0] + c) % mod
            sum[x, default: 0] = (sum[x, default: 0] + s) % mod
            ans = (ans + s) % mod
        }
        return ans
    }
}
'''

FILES["3300_minimum_element_after_replacement_with_digit_sum"] = hdr("3300", "Minimum Element After Replacement With Digit Sum", "minimum-element-after-replacement-with-digit-sum") + '''
class Solution {
    func minElement(_ nums: [Int]) -> Int {
        var ans = 1_000_000_000
        for num in nums {
            var x = num, s = 0
            while x > 0 { s += x % 10; x /= 10 }
            if s < ans { ans = s }
        }
        return ans
    }
}
'''

FILES["3301_maximize_the_total_height_of_unique_towers"] = hdr("3301", "Maximize the Total Height of Unique Towers", "maximize-the-total-height-of-unique-towers") + '''
class Solution {
    func maximumTotalSum(_ maximumHeight: [Int]) -> Int {
        let heights = maximumHeight.sorted(by: >)
        var ans = 0
        var prev = Int.max
        for h in heights {
            var cur = h
            if cur >= prev { cur = prev - 1 }
            if cur <= 0 { return -1 }
            ans += cur
            prev = cur
        }
        return ans
    }
}
'''

FILES["3302_find_the_lexicographically_smallest_valid_sequence"] = hdr("3302", "Find the Lexicographically Smallest Valid Sequence", "find-the-lexicographically-smallest-valid-sequence") + '''
class Solution {
    func validSequence(_ word1: String, _ word2: String) -> [Int] {
        let w1 = Array(word1), w2 = Array(word2)
        let n = w1.count, m = w2.count
        var right = Array(repeating: -1, count: m + 1)
        right[m] = n
        var j = m - 1
        var i = n - 1
        while i >= 0 && j >= 0 {
            if w1[i] == w2[j] {
                right[j] = i
                j -= 1
            }
            i -= 1
        }
        var ans = Array(repeating: 0, count: m)
        var usedSkip = false
        i = 0
        j = 0
        while j < m {
            var found = false
            while i < n {
                if w1[i] == w2[j] {
                    if canFinish(i + 1, j + 1, usedSkip, right, n, m) {
                        ans[j] = i
                        i += 1
                        found = true
                        break
                    }
                } else if !usedSkip {
                    if canFinish(i + 1, j + 1, true, right, n, m) {
                        ans[j] = i
                        i += 1
                        usedSkip = true
                        found = true
                        break
                    }
                }
                i += 1
            }
            if !found { return [] }
            j += 1
        }
        return ans
    }

    private func canFinish(_ i: Int, _ j: Int, _ usedSkip: Bool, _ right: [Int], _ n: Int, _ m: Int) -> Bool {
        if j >= m { return true }
        if !usedSkip {
            if right[j] >= i { return true }
            if j + 1 <= m && right[j + 1] > i { return true }
            if right[j] > i { return true }
            return false
        }
        return right[j] >= i
    }
}
'''

FILES["3303_find_the_occurrence_of_first_almost_equal_substring"] = hdr("3303", "Find the Occurrence of First Almost Equal Substring", "find-the-occurrence-of-first-almost-equal-substring") + '''
class Solution {
    func minStartingIndex(_ s: String, _ pattern: String) -> Int {
        let s = Array(s), p = Array(pattern)
        let n = s.count, m = p.count
        if n < m { return -1 }
        for i in 0...(n - m) {
            var diff = 0
            for j in 0..<m {
                if s[i + j] != p[j] {
                    diff += 1
                    if diff > 1 { break }
                }
            }
            if diff <= 1 { return i }
        }
        return -1
    }
}
'''

FILES["3304_find_the_k_th_character_in_string_game_i"] = hdr("3304", "Find the K-th Character in String Game I", "find-the-k-th-character-in-string-game-i") + '''
class Solution {
    func kthCharacter(_ k: Int) -> Character {
        var s = [Character](["a"])
        while s.count < k {
            let n = s.count
            for i in 0..<n {
                let v = Int(s[i].asciiValue! - 97)
                s.append(Character(UnicodeScalar((v + 1) % 26 + 97)!))
            }
        }
        return s[k - 1]
    }
}
'''

COUNT_VOWEL = '''
class Solution {
    func countOfSubstrings(_ word: String, _ k: Int) -> Int {
        return atLeast(word, k) - atLeast(word, k + 1)
    }

    private func isVowel(_ c: Character) -> Bool {
        return c == "a" || c == "e" || c == "i" || c == "o" || c == "u"
    }

    private func atLeast(_ word: String, _ k: Int) -> Int {
        let w = Array(word)
        var cnt = [Character: Int]()
        var cons = 0, l = 0, ans = 0
        for r in 0..<w.count {
            let c = w[r]
            if isVowel(c) { cnt[c, default: 0] += 1 }
            else { cons += 1 }
            while cnt.count == 5 && cons >= k {
                ans += w.count - r
                let c2 = w[l]
                if isVowel(c2) {
                    cnt[c2, default: 0] -= 1
                    if cnt[c2] == 0 { cnt.removeValue(forKey: c2) }
                } else { cons -= 1 }
                l += 1
            }
        }
        return ans
    }
}
'''

FILES["3305_count_of_substrings_containing_every_vowel_and_k_consonants_i"] = hdr("3305", "Count of Substrings Containing Every Vowel and K Consonants I", "count-of-substrings-containing-every-vowel-and-k-consonants-i") + COUNT_VOWEL

FILES["3306_count_of_substrings_containing_every_vowel_and_k_consonants_ii"] = hdr("3306", "Count of Substrings Containing Every Vowel and K Consonants II", "count-of-substrings-containing-every-vowel-and-k-consonants-ii") + COUNT_VOWEL

FILES["3307_find_the_k_th_character_in_string_game_ii"] = hdr("3307", "Find the K-th Character in String Game II", "find-the-k-th-character-in-string-game-ii") + '''
class Solution {
    func kthCharacter(_ k: Int, _ operations: [Int]) -> Character {
        var k = k
        var shift = 0
        var ops = operations
        while !ops.isEmpty {
            let op = ops.removeLast()
            let half = 1 << ops.count
            if k > half {
                k -= half
                if op == 1 { shift += 1 }
            }
        }
        return Character(UnicodeScalar(97 + shift % 26)!)
    }
}
'''

FILES["3309_maximum_possible_number_by_binary_concatenation"] = hdr("3309", "Maximum Possible Number by Binary Concatenation", "maximum-possible-number-by-binary-concatenation") + '''
class Solution {
    func maxGoodNumber(_ nums: [Int]) -> Int {
        func toBin(_ x: Int) -> String {
            if x == 0 { return "0" }
            var x = x
            var s = ""
            while x > 0 {
                s = String(x & 1) + s
                x >>= 1
            }
            return s
        }
        let bs = nums.map { toBin($0) }
        var idx = [0, 1, 2]
        var ans = 0
        func perm(_ i: Int) {
            if i == 3 {
                let s = bs[idx[0]] + bs[idx[1]] + bs[idx[2]]
                var v = 0
                for c in s { v = v * 2 + Int(String(c))! }
                if v > ans { ans = v }
                return
            }
            for j in i..<3 {
                idx.swapAt(i, j)
                perm(i + 1)
                idx.swapAt(i, j)
            }
        }
        perm(0)
        return ans
    }
}
'''

FILES["3310_remove_methods_from_project"] = hdr("3310", "Remove Methods From Project", "remove-methods-from-project") + '''
class Solution {
    func remainingMethods(_ n: Int, _ k: Int, _ invocations: [[Int]]) -> [Int] {
        var g = Array(repeating: [Int](), count: n)
        for e in invocations { g[e[0]].append(e[1]) }
        var sus = Array(repeating: false, count: n)
        func dfs(_ u: Int) {
            if sus[u] { return }
            sus[u] = true
            for v in g[u] { dfs(v) }
        }
        dfs(k)
        for e in invocations {
            if !sus[e[0]] && sus[e[1]] {
                return Array(0..<n)
            }
        }
        return (0..<n).filter { !sus[$0] }
    }
}
'''

FILES["3311_construct_2d_grid_matching_graph_layout"] = hdr("3311", "Construct 2D Grid Matching Graph Layout", "construct-2d-grid-matching-graph-layout") + '''
class Solution {
    func constructGridLayout(_ n: Int, _ edges: [[Int]]) -> [[Int]] {
        var g = Array(repeating: [Int](), count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        let deg = g.map { $0.count }
        var start = 0
        for i in 0..<n {
            if deg[i] == 1 { start = i; break }
            if deg[i] == 2 { start = i }
        }
        var vis = Array(repeating: false, count: n)
        var row = [Int]()
        var cur = start, prev = -1
        while true {
            row.append(cur)
            vis[cur] = true
            var next = -1
            for v in g[cur] {
                if v != prev && !vis[v] && deg[v] <= 3 {
                    next = v
                    if deg[v] < 4 { break }
                }
            }
            if next == -1 { break }
            prev = cur
            cur = next
        }
        var width = row.count
        var height = width != 0 ? n / width : n
        if width == 0 || width * height != n {
            for w in 1...n where n % w == 0 {
                width = w
                height = n / w
                break
            }
        }
        var grid = Array(repeating: Array(repeating: 0, count: width), count: height)
        if row.count == width {
            for c in 0..<width { grid[0][c] = row[c] }
            var used = Array(repeating: false, count: n)
            for x in row { used[x] = true }
            for r in 1..<height {
                for c in 0..<width {
                    let up = grid[r - 1][c]
                    var chosen = -1
                    for v in g[up] {
                        if used[v] { continue }
                        if c == 0 || g[v].contains(grid[r][c - 1]) {
                            chosen = v
                            break
                        }
                    }
                    if chosen == -1 {
                        for v in g[up] where !used[v] { chosen = v; break }
                    }
                    if chosen != -1 {
                        grid[r][c] = chosen
                        used[chosen] = true
                    }
                }
            }
        } else {
            for i in 0..<n { grid[i / width][i % width] = i }
        }
        return grid
    }
}
'''

def main():
    n = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "Solution.swift"
        path.write_text(content.lstrip("\n") if content.startswith("\n") else content)
        # ensure starts with //
        text = path.read_text()
        if text.startswith("\n"):
            path.write_text(text.lstrip("\n"))
        n += 1
        print("wrote", folder)
    print("total", n)

if __name__ == "__main__":
    main()
