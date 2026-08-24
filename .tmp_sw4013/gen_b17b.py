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

FILES["3312_sorted_gcd_pair_queries"] = hdr("3312", "Sorted GCD Pair Queries", "sorted-gcd-pair-queries") + '''
class Solution {
    func gcdValues(_ nums: [Int], _ queries: [Int]) -> [Int] {
        var maxV = 0
        for x in nums where x > maxV { maxV = x }
        var cnt = Array(repeating: 0, count: maxV + 1)
        for x in nums { cnt[x] += 1 }
        var divCnt = Array(repeating: 0, count: maxV + 1)
        for g in 1...maxV {
            var c = 0
            var m = g
            while m <= maxV {
                c += cnt[m]
                m += g
            }
            divCnt[g] = c * (c - 1) / 2
        }
        var exact = Array(repeating: 0, count: maxV + 1)
        for g in stride(from: maxV, through: 1, by: -1) {
            exact[g] = divCnt[g]
            var m = 2 * g
            while m <= maxV {
                exact[g] -= exact[m]
                m += g
            }
        }
        var pref = Array(repeating: 0, count: maxV + 1)
        for g in 1...maxV { pref[g] = pref[g - 1] + exact[g] }
        var ans = Array(repeating: 0, count: queries.count)
        for i in 0..<queries.count {
            let q = queries[i]
            var lo = 1, hi = maxV
            while lo < hi {
                let mid = (lo + hi) / 2
                if pref[mid] > q { hi = mid }
                else { lo = mid + 1 }
            }
            ans[i] = lo
        }
        return ans
    }
}
'''

FILES["3313_find_the_last_marked_nodes_in_tree"] = hdr("3313", "Find the Last Marked Nodes in Tree", "find-the-last-marked-nodes-in-tree") + '''
class Solution {
    func lastMarkedNodes(_ edges: [[Int]]) -> [Int] {
        let n = edges.count + 1
        var g = Array(repeating: [Int](), count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        func bfs(_ start: Int) -> (Int, [Int]) {
            var dist = Array(repeating: -1, count: n)
            var q = [start]
            dist[start] = 0
            var far = start
            var qi = 0
            while qi < q.count {
                let u = q[qi]; qi += 1
                if dist[u] > dist[far] { far = u }
                for v in g[u] where dist[v] == -1 {
                    dist[v] = dist[u] + 1
                    q.append(v)
                }
            }
            return (far, dist)
        }
        let u = bfs(0).0
        let (v, du) = bfs(u)
        let dv = bfs(v).1
        var ans = Array(repeating: 0, count: n)
        for i in 0..<n { ans[i] = du[i] >= dv[i] ? u : v }
        return ans
    }
}
'''

MIN_BIT = '''
class Solution {
    func minBitwiseArray(_ nums: [Int]) -> [Int] {
        var ans = Array(repeating: -1, count: nums.count)
        for i in 0..<nums.count {
            let n = nums[i]
            if n == 2 { continue }
            var x = 0
            while x < n {
                if (x | (x + 1)) == n { ans[i] = x; break }
                x += 1
            }
        }
        return ans
    }
}
'''

FILES["3314_construct_the_minimum_bitwise_array_i"] = hdr("3314", "Construct the Minimum Bitwise Array I", "construct-the-minimum-bitwise-array-i") + MIN_BIT

FILES["3315_construct_the_minimum_bitwise_array_ii"] = hdr("3315", "Construct the Minimum Bitwise Array II", "construct-the-minimum-bitwise-array-ii") + '''
class Solution {
    func minBitwiseArray(_ nums: [Int]) -> [Int] {
        var ans = Array(repeating: -1, count: nums.count)
        for i in 0..<nums.count {
            let n = nums[i]
            if n == 2 { continue }
            for b in 0..<31 {
                if ((n >> b) & 1) == 0 { continue }
                let x = n ^ (1 << b)
                if (x | (x + 1)) == n { ans[i] = x; break }
            }
        }
        return ans
    }
}
'''

FILES["3316_find_maximum_removals_from_source_string"] = hdr("3316", "Find Maximum Removals From Source String", "find-maximum-removals-from-source-string") + '''
class Solution {
    func maxRemovals(_ source: String, _ pattern: String, _ targetIndices: [Int]) -> Int {
        let s = Array(source), p = Array(pattern)
        let n = s.count
        var lo = 0, hi = targetIndices.count
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if ok(mid, s, p, targetIndices, n) { lo = mid }
            else { hi = mid - 1 }
        }
        return lo
    }

    private func ok(_ removeFirst: Int, _ s: [Character], _ p: [Character], _ targetIndices: [Int], _ n: Int) -> Bool {
        var mark = Array(repeating: false, count: n)
        for i in 0..<removeFirst { mark[targetIndices[i]] = true }
        var j = 0
        for i in 0..<n where j < p.count {
            if mark[i] { continue }
            if s[i] == p[j] { j += 1 }
        }
        return j == p.count
    }
}
'''

FILES["3317_find_the_number_of_possible_ways_for_an_event"] = hdr("3317", "Find the Number of Possible Ways for an Event", "find-the-number-of-possible-ways-for-an-event") + '''
class Solution {
    func numberOfWays(_ n: Int, _ x: Int, _ y: Int) -> Int {
        let mod = 1_000_000_007
        var dp = Array(repeating: Array(repeating: 0, count: x + 1), count: n + 1)
        dp[0][0] = 1
        for i in 1...n {
            for j in 1...min(x, i) {
                dp[i][j] = (dp[i - 1][j - 1] + j * dp[i - 1][j] % mod) % mod
            }
        }
        var fact = Array(repeating: 1, count: x + 1)
        if x >= 1 {
            for i in 1...x { fact[i] = fact[i - 1] * i % mod }
        }
        var ans = 0, ypow = 1
        for k in 1...min(x, n) {
            ypow = ypow * y % mod
            let perm = fact[x] * modPow(fact[x - k], mod - 2, mod) % mod
            ans = (ans + dp[n][k] * perm % mod * ypow % mod) % mod
        }
        return ans
    }

    private func modPow(_ a: Int, _ e: Int, _ mod: Int) -> Int {
        var r = 1, a = a % mod, e = e
        while e > 0 {
            if e & 1 != 0 { r = r * a % mod }
            a = a * a % mod
            e >>= 1
        }
        return r
    }
}
'''

XSUM = '''
class Solution {
    func findXSum(_ nums: [Int], _ k: Int, _ x: Int) -> [Int] {
        let n = nums.count
        var ans = Array(repeating: 0, count: n - k + 1)
        for i in 0...(n - k) {
            var freq = [Int: Int]()
            for j in i..<(i + k) { freq[nums[j], default: 0] += 1 }
            var arr = freq.map { ($0.key, $0.value) }
            arr.sort { a, b in
                if a.1 != b.1 { return a.1 > b.1 }
                return a.0 > b.0
            }
            let lim = min(x, arr.count)
            var keep = Set<Int>()
            for t in 0..<lim { keep.insert(arr[t].0) }
            var sum = 0
            for j in i..<(i + k) where keep.contains(nums[j]) { sum += nums[j] }
            ans[i] = sum
        }
        return ans
    }
}
'''

FILES["3318_find_x_sum_of_all_k_long_subarrays_i"] = hdr("3318", "Find X-Sum of All K-Long Subarrays I", "find-x-sum-of-all-k-long-subarrays-i") + XSUM

FILES["3319_k_th_largest_perfect_subtree_size_in_binary_tree"] = hdr("3319", "K-th Largest Perfect Subtree Size in Binary Tree", "k-th-largest-perfect-subtree-size-in-binary-tree") + TREE + '''
class Solution {
    func kthLargestPerfectSubtree(_ root: TreeNode?, _ k: Int) -> Int {
        var sizes = [Int]()
        @discardableResult
        func dfs(_ node: TreeNode?) -> (Int, Int, Bool) {
            guard let node else { return (0, 0, true) }
            let L = dfs(node.left)
            let R = dfs(node.right)
            let sz = L.1 + R.1 + 1
            let perf = L.2 && R.2 && L.0 == R.0
            if perf { sizes.append(sz) }
            return (max(L.0, R.0) + 1, sz, perf)
        }
        _ = dfs(root)
        sizes.sort(by: >)
        if k > sizes.count { return -1 }
        return sizes[k - 1]
    }
}
'''

FILES["3320_count_the_number_of_winning_sequences"] = hdr("3320", "Count the Number of Winning Sequences", "count-the-number-of-winning-sequences") + '''
class Solution {
    func countWinningSequences(_ s: String) -> Int {
        let mod = 1_000_000_007
        let chars = Array(s)
        let n = chars.count
        var mp = [Character: Int]()
        mp["F"] = 0; mp["W"] = 1; mp["E"] = 2
        let beat = [2, 0, 1]
        var score = Array(repeating: Array(repeating: 0, count: 3), count: 3)
        for a in 0..<3 {
            for b in 0..<3 {
                if a == b { score[a][b] = 0 }
                else if beat[a] == b { score[a][b] = 1 }
                else { score[a][b] = -1 }
            }
        }
        let offset = n
        var dp = Array(repeating: Array(repeating: 0, count: 2 * n + 1), count: 3)
        let b0 = mp[chars[0]]!
        for a in 0..<3 { dp[a][score[a][b0] + offset] = 1 }
        if n > 1 {
            for i in 1..<n {
                var ndp = Array(repeating: Array(repeating: 0, count: 2 * n + 1), count: 3)
                let b = mp[chars[i]]!
                for last in 0..<3 {
                    for d in 0...(2 * n) {
                        if dp[last][d] == 0 { continue }
                        for a in 0..<3 where a != last {
                            let nd = d + score[a][b]
                            if nd < 0 || nd > 2 * n { continue }
                            ndp[a][nd] = (ndp[a][nd] + dp[last][d]) % mod
                        }
                    }
                }
                dp = ndp
            }
        }
        var ans = 0
        for a in 0..<3 {
            if offset + 1 <= 2 * n {
                for d in (offset + 1)...(2 * n) { ans = (ans + dp[a][d]) % mod }
            }
        }
        return ans
    }
}
'''

FILES["3321_find_x_sum_of_all_k_long_subarrays_ii"] = hdr("3321", "Find X-Sum of All K-Long Subarrays II", "find-x-sum-of-all-k-long-subarrays-ii") + XSUM

FILES["3323_minimize_connected_groups_by_inserting_interval"] = hdr("3323", "Minimize Connected Groups by Inserting Interval", "minimize-connected-groups-by-inserting-interval") + '''
class Solution {
    func minConnectedGroups(_ intervals: [[Int]], _ k: Int) -> Int {
        let intervals = intervals.sorted { $0[0] < $1[0] }
        var merged = [[Int]]()
        for it in intervals {
            if merged.isEmpty || it[0] > merged[merged.count - 1][1] {
                merged.append(it)
            } else if it[1] > merged[merged.count - 1][1] {
                merged[merged.count - 1][1] = it[1]
            }
        }
        let m = merged.count
        var ans = m
        for i in 0..<m {
            let end = merged[i][1] + k
            var j = i
            while j < m && merged[j][0] <= end { j += 1 }
            let groups = i + 1 + (m - j)
            if groups < ans { ans = groups }
        }
        return ans
    }
}
'''

FILES["3324_find_the_sequence_of_strings_appeared_on_the_screen"] = hdr("3324", "Find the Sequence of Strings Appeared on the Screen", "find-the-sequence-of-strings-appeared-on-the-screen") + '''
class Solution {
    func stringSequence(_ target: String) -> [String] {
        var ans = [String]()
        var cur = [Character]()
        for ch in target {
            cur.append("a")
            ans.append(String(cur))
            while cur[cur.count - 1] != ch {
                let v = Int(cur[cur.count - 1].asciiValue!) + 1
                cur[cur.count - 1] = Character(UnicodeScalar(v)!)
                ans.append(String(cur))
            }
        }
        return ans
    }
}
'''

K_FREQ = '''
class Solution {
    func numberOfSubstrings(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var ans = 0
        for i in 0..<n {
            var freq = Array(repeating: 0, count: 26)
            for j in i..<n {
                freq[Int(chars[j].asciiValue! - 97)] += 1
                var ok = false
                for f in freq where f >= k { ok = true; break }
                if ok { ans += n - j; break }
            }
        }
        return ans
    }
}
'''

FILES["3325_count_substrings_with_k_frequency_characters_i"] = hdr("3325", "Count Substrings With K-Frequency Characters I", "count-substrings-with-k-frequency-characters-i") + K_FREQ

FILES["3326_minimum_division_operations_to_make_array_non_decreasing"] = hdr("3326", "Minimum Division Operations to Make Array Non Decreasing", "minimum-division-operations-to-make-array-non-decreasing") + '''
class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var nums = nums
        var ops = 0
        for i in stride(from: nums.count - 2, through: 0, by: -1) {
            if nums[i] <= nums[i + 1] { continue }
            while nums[i] > nums[i + 1] {
                let d = smallestProperDivisor(nums[i])
                if d == nums[i] { return -1 }
                nums[i] /= d
                ops += 1
                if nums[i] > nums[i + 1] && smallestProperDivisor(nums[i]) == nums[i] { return -1 }
            }
        }
        return ops
    }

    private func smallestProperDivisor(_ x: Int) -> Int {
        var d = 2
        while d * d <= x {
            if x % d == 0 { return d }
            d += 1
        }
        return x
    }
}
'''

FILES["3327_check_if_dfs_strings_are_palindromes"] = hdr("3327", "Check if DFS Strings Are Palindromes", "check-if-dfs-strings-are-palindromes") + '''
class Solution {
    func findAnswer(_ parent: [Int], _ s: String) -> [Bool] {
        let chars = Array(s)
        let n = parent.count
        var g = Array(repeating: [Int](), count: n)
        for i in 1..<n { g[parent[i]].append(i) }
        var ans = Array(repeating: false, count: n)
        func isPal(_ t: [Character]) -> Bool {
            var i = 0, j = t.count - 1
            while i < j {
                if t[i] != t[j] { return false }
                i += 1; j -= 1
            }
            return true
        }
        func dfsStr(_ u: Int) -> [Character] {
            var out = [Character]()
            for v in g[u] { out.append(contentsOf: dfsStr(v)) }
            out.append(chars[u])
            ans[u] = isPal(out)
            return out
        }
        _ = dfsStr(0)
        return ans
    }
}
'''

FILES["3329_count_substrings_with_k_frequency_characters_ii"] = hdr("3329", "Count Substrings With K-Frequency Characters II", "count-substrings-with-k-frequency-characters-ii") + K_FREQ

FILES["3330_find_the_original_typed_string_i"] = hdr("3330", "Find the Original Typed String I", "find-the-original-typed-string-i") + '''
class Solution {
    func possibleStringCount(_ word: String) -> Int {
        let w = Array(word)
        var ans = 1
        for i in 1..<w.count where w[i] == w[i - 1] { ans += 1 }
        return ans
    }
}
'''

FILES["3331_find_subtree_sizes_after_changes"] = hdr("3331", "Find Subtree Sizes After Changes", "find-subtree-sizes-after-changes") + '''
class Solution {
    func findSubtreeSizes(_ parent: [Int], _ s: String) -> [Int] {
        let chars = Array(s)
        let n = parent.count
        var g = Array(repeating: [Int](), count: n)
        for i in 1..<n { g[parent[i]].append(i) }
        var newParent = parent
        var last = Array(repeating: -1, count: 26)
        func dfs1(_ u: Int) {
            let c = Int(chars[u].asciiValue! - 97)
            let prev = last[c]
            if prev != -1 { newParent[u] = prev }
            last[c] = u
            for v in g[u] { dfs1(v) }
            last[c] = prev
        }
        dfs1(0)
        var ng = Array(repeating: [Int](), count: n)
        for i in 1..<n { ng[newParent[i]].append(i) }
        var ans = Array(repeating: 0, count: n)
        func dfs2(_ u: Int) -> Int {
            var sz = 1
            for v in ng[u] { sz += dfs2(v) }
            ans[u] = sz
            return sz
        }
        _ = dfs2(0)
        return ans
    }
}
'''

FILES["3332_maximum_points_tourist_can_earn"] = hdr("3332", "Maximum Points Tourist Can Earn", "maximum-points-tourist-can-earn") + '''
class Solution {
    func maxScore(_ n: Int, _ k: Int, _ stayScore: [[Int]], _ travelScore: [[Int]]) -> Int {
        var dp = Array(repeating: 0, count: n)
        for day in 0..<k {
            var ndp = Array(repeating: -(1 << 30), count: n)
            for dest in 0..<n {
                var best = -(1 << 30)
                for src in 0..<n {
                    var val = dp[src]
                    if src == dest { val += stayScore[day][dest] }
                    else { val += travelScore[src][dest] }
                    if val > best { best = val }
                }
                ndp[dest] = best
            }
            dp = ndp
        }
        return dp.max() ?? 0
    }
}
'''

FILES["3333_find_the_original_typed_string_ii"] = hdr("3333", "Find the Original Typed String II", "find-the-original-typed-string-ii") + '''
class Solution {
    func possibleStringCount(_ word: String, _ k: Int) -> Int {
        let mod = 1_000_000_007
        let w = Array(word)
        var groups = [Int]()
        var i = 0
        while i < w.count {
            var j = i
            while j < w.count && w[j] == w[i] { j += 1 }
            groups.append(j - i)
            i = j
        }
        var total = 1
        for g in groups { total = total * g % mod }
        if k <= groups.count { return total }
        let need = k - 1
        var dp = Array(repeating: 0, count: need)
        dp[0] = 1
        for g in groups {
            var ndp = Array(repeating: 0, count: need)
            var pref = Array(repeating: 0, count: need + 1)
            for i in 0..<need { pref[i + 1] = (pref[i] + dp[i]) % mod }
            for s in 0..<need {
                var lo = s - g
                if lo < 0 { lo = 0 }
                let hi = s - 1
                if hi >= 0 { ndp[s] = (pref[hi + 1] - pref[lo] + mod) % mod }
            }
            dp = ndp
        }
        var bad = 0
        for v in dp { bad = (bad + v) % mod }
        return (total - bad + mod) % mod
    }
}
'''

FILES["3334_find_the_maximum_factor_score_of_array"] = hdr("3334", "Find the Maximum Factor Score of Array", "find-the-maximum-factor-score-of-array") + '''
class Solution {
    func maxScore(_ nums: [Int]) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        func lcm(_ a: Int, _ b: Int) -> Int {
            if a == 0 || b == 0 { return 0 }
            return a / gcd(a, b) * b
        }
        let n = nums.count
        var gcdAll = nums[0], lcmAll = nums[0]
        for i in 1..<n {
            gcdAll = gcd(gcdAll, nums[i])
            lcmAll = lcm(lcmAll, nums[i])
        }
        var ans = gcdAll * lcmAll
        for skip in 0..<n {
            var g = 0, l = 1
            var first = true
            for i in 0..<n where i != skip {
                if first { g = nums[i]; l = nums[i]; first = false }
                else { g = gcd(g, nums[i]); l = lcm(l, nums[i]) }
            }
            if first { continue }
            let v = g * l
            if v > ans { ans = v }
        }
        return ans
    }
}
'''

FILES["3335_total_characters_in_string_after_transformations_i"] = hdr("3335", "Total Characters in String After Transformations I", "total-characters-in-string-after-transformations-i") + '''
class Solution {
    func lengthAfterTransformations(_ s: String, _ t: Int) -> Int {
        let mod = 1_000_000_007
        var cnt = Array(repeating: 0, count: 26)
        for c in s { cnt[Int(c.asciiValue! - 97)] += 1 }
        for _ in 0..<t {
            var ncnt = Array(repeating: 0, count: 26)
            for i in 0..<25 { ncnt[i + 1] = (ncnt[i + 1] + cnt[i]) % mod }
            ncnt[0] = (ncnt[0] + cnt[25]) % mod
            ncnt[1] = (ncnt[1] + cnt[25]) % mod
            cnt = ncnt
        }
        return cnt.reduce(0, +) % mod
    }
}
'''

FILES["3336_find_the_number_of_subsequences_with_equal_gcd"] = hdr("3336", "Find the Number of Subsequences With Equal GCD", "find-the-number-of-subsequences-with-equal-gcd") + '''
class Solution {
    func subsequencePairCount(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            if a == 0 { return b }
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        var maxV = 0
        for x in nums where x > maxV { maxV = x }
        var dp = Array(repeating: Array(repeating: 0, count: maxV + 1), count: maxV + 1)
        dp[0][0] = 1
        for x in nums {
            var ndp = dp
            for a in 0...maxV {
                for b in 0...maxV {
                    if dp[a][b] == 0 { continue }
                    let na = a == 0 ? x : gcd(a, x)
                    let nb = b == 0 ? x : gcd(b, x)
                    ndp[na][b] = (ndp[na][b] + dp[a][b]) % mod
                    ndp[a][nb] = (ndp[a][nb] + dp[a][b]) % mod
                }
            }
            dp = ndp
        }
        var ans = 0
        if maxV >= 1 {
            for g in 1...maxV { ans = (ans + dp[g][g]) % mod }
        }
        return ans
    }
}
'''

FILES["3337_total_characters_in_string_after_transformations_ii"] = hdr("3337", "Total Characters in String After Transformations II", "total-characters-in-string-after-transformations-ii") + '''
class Solution {
    func lengthAfterTransformations(_ s: String, _ t: Int, _ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        var mat = Array(repeating: Array(repeating: 0, count: 26), count: 26)
        for i in 0..<26 {
            if nums[i] >= 1 {
                for j in 1...nums[i] { mat[i][(i + j) % 26] = 1 }
            }
        }
        mat = matPow(mat, t, mod)
        var cnt = Array(repeating: 0, count: 26)
        for c in s { cnt[Int(c.asciiValue! - 97)] += 1 }
        var ans = 0
        for i in 0..<26 {
            for j in 0..<26 {
                ans = (ans + cnt[i] * mat[i][j] % mod) % mod
            }
        }
        return ans
    }

    private func matMul(_ a: [[Int]], _ b: [[Int]], _ mod: Int) -> [[Int]] {
        let n = a.count
        var c = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n {
            for k in 0..<n {
                if a[i][k] == 0 { continue }
                for j in 0..<n {
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j] % mod) % mod
                }
            }
        }
        return c
    }

    private func matPow(_ a: [[Int]], _ e: Int, _ mod: Int) -> [[Int]] {
        let n = a.count
        var r = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n { r[i][i] = 1 }
        var a = a, e = e
        while e > 0 {
            if e & 1 != 0 { r = matMul(r, a, mod) }
            a = matMul(a, a, mod)
            e >>= 1
        }
        return r
    }
}
'''

FILES["3339_find_the_number_of_k_even_arrays"] = hdr("3339", "Find the Number of K-Even Arrays", "find-the-number-of-k-even-arrays") + '''
class Solution {
    func countOfArrays(_ n: Int, _ m: Int, _ k: Int) -> Int {
        let mod = 1_000_000_007
        let even = m / 2, odd = m - even
        var dp = Array(repeating: Array(repeating: Array(repeating: 0, count: 2), count: k + 1), count: n + 1)
        dp[1][0][0] = odd
        dp[1][0][1] = even
        if n >= 2 {
            for i in 1..<n {
                for j in 0...k {
                    dp[i + 1][j][0] = (dp[i + 1][j][0] + ((dp[i][j][0] + dp[i][j][1]) % mod) * odd % mod) % mod
                    dp[i + 1][j][1] = (dp[i + 1][j][1] + dp[i][j][0] * even % mod) % mod
                    if j < k {
                        dp[i + 1][j + 1][1] = (dp[i + 1][j + 1][1] + dp[i][j][1] * even % mod) % mod
                    }
                }
            }
        }
        return (dp[n][k][0] + dp[n][k][1]) % mod
    }
}
'''

def main():
    for folder, content in FILES.items():
        path = ROOT / folder / "Solution.swift"
        text = content.lstrip("\n")
        path.write_text(text)
        print("wrote", folder)
    print("total", len(FILES))

if __name__ == "__main__":
    main()
