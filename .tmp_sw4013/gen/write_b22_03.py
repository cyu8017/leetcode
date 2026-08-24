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


def write(folder, content):
    p = ROOT / folder / "Solution.swift"
    if "func solve()" not in p.read_text():
        print("SKIP", folder)
        return
    p.write_text(content)
    print("WROTE", folder)


write("3883_count_non_decreasing_arrays_with_given_digit_sums", """// LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

class Solution {
    func countNonDecreasingArrays(_ digitSum: [Int]) -> Int {
        let mod = 1_000_000_007
        var groups = [[Int]](repeating: [], count: 51)
        for x in 0...5000 {
            var s = 0, y = x
            while y > 0 { s += y % 10; y /= 10 }
            groups[s].append(x)
        }
        var prevVals = groups[digitSum[0]]
        var dp = [Int](repeating: 1, count: prevVals.count)
        if digitSum.count > 1 {
            for pos in 1..<digitSum.count {
                let curVals = groups[digitSum[pos]]
                var next = [Int](repeating: 0, count: curVals.count)
                var j = 0, prefix = 0
                for i in 0..<curVals.count {
                    let x = curVals[i]
                    while j < prevVals.count && prevVals[j] <= x {
                        prefix += dp[j]
                        if prefix >= mod { prefix -= mod }
                        j += 1
                    }
                    next[i] = prefix
                }
                prevVals = curVals
                dp = next
            }
        }
        var ans = 0
        for x in dp {
            ans += x
            if ans >= mod { ans -= mod }
        }
        return ans
    }
}
""")

write("3884_first_matching_character_from_both_ends", """// LeetCode 3884 - First Matching Character From Both Ends
// https://leetcode.com/problems/first-matching-character-from-both-ends/

class Solution {
    func firstMatchingIndex(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        for i in 0..<(n / 2 + 1) {
            if chars[i] == chars[n - i - 1] { return i }
        }
        return -1
    }
}
""")

write("3885_design_event_manager", """// LeetCode 3885 - Design Event Manager
// https://leetcode.com/problems/design-event-manager/

class EventManager {
    private var sl = [(Int, Int)]()
    private var d = [Int: Int]()

    init(_ events: [[Int]]) {
        for e in events {
            sl.append((-e[1], e[0]))
            d[e[0]] = e[1]
        }
        sl.sort { $0.0 != $1.0 ? $0.0 < $1.0 : $0.1 < $1.1 }
    }

    func updatePriority(_ eventId: Int, _ newPriority: Int) {
        let old = d[eventId]!
        if let i = sl.firstIndex(where: { $0.0 == -old && $0.1 == eventId }) {
            sl.remove(at: i)
        }
        sl.append((-newPriority, eventId))
        sl.sort { $0.0 != $1.0 ? $0.0 < $1.0 : $0.1 < $1.1 }
        d[eventId] = newPriority
    }

    func pollHighest() -> Int {
        if sl.isEmpty { return -1 }
        let top = sl.removeFirst()
        d.removeValue(forKey: top.1)
        return top.1
    }
}
""")

write("3886_sum_of_sortable_integers", """// LeetCode 3886 - Sum of Sortable Integers
// https://leetcode.com/problems/sum-of-sortable-integers/

class Solution {
    private func rotationMatches(_ block: [Int], _ target: [Int]) -> Bool {
        let k = block.count
        var prefix = [Int](repeating: 0, count: k)
        if k > 1 {
            for i in 1..<k {
                var j = prefix[i - 1]
                while j > 0 && target[i] != target[j] { j = prefix[j - 1] }
                if target[i] == target[j] { j += 1 }
                prefix[i] = j
            }
        }
        var matched = 0
        for i in 0..<(2 * k - 1) {
            let x = block[i % k]
            while matched > 0 && x != target[matched] { matched = prefix[matched - 1] }
            if x == target[matched] { matched += 1 }
            if matched == k { return true }
        }
        return false
    }

    func sumOfSortableIntegers(_ nums: [Int]) -> Int {
        let n = nums.count
        let sorted = nums.sorted()
        var divisors = [Int]()
        var d = 1
        while d * d <= n {
            if n % d == 0 {
                divisors.append(d)
                if d * d != n { divisors.append(n / d) }
            }
            d += 1
        }
        var answer = 0
        for k in divisors {
            var ok = true
            var start = 0
            while start < n {
                let block = Array(nums[start..<(start + k)])
                let target = Array(sorted[start..<(start + k)])
                if !rotationMatches(block, target) { ok = false; break }
                start += k
            }
            if ok { answer += k }
        }
        return answer
    }
}
""")

write("3887_incremental_even_weighted_cycle_queries", """// LeetCode 3887 - Incremental Even-Weighted Cycle Queries
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

class Solution {
    private var parent = [Int]()
    private var size = [Int]()
    private var parity = [Int]()

    private func find(_ x: Int) -> (Int, Int) {
        if parent[x] == x { return (x, 0) }
        let res = find(parent[x])
        parity[x] ^= res.1
        parent[x] = res.0
        return (res.0, parity[x])
    }

    func countValidEdges(_ n: Int, _ edges: [[Int]]) -> Int {
        parent = Array(0..<n)
        size = [Int](repeating: 1, count: n)
        parity = [Int](repeating: 0, count: n)
        var ans = 0
        for e in edges {
            var fu = find(e[0])
            var fv = find(e[1])
            var ru = fu.0, pu = fu.1, rv = fv.0, pv = fv.1
            if ru == rv {
                if (pu ^ pv) == e[2] { ans += 1 }
                continue
            }
            if size[ru] < size[rv] {
                swap(&ru, &rv)
                swap(&pu, &pv)
            }
            parent[rv] = ru
            parity[rv] = pu ^ pv ^ e[2]
            size[ru] += size[rv]
            ans += 1
        }
        return ans
    }
}
""")

write("3888_minimum_operations_to_make_all_grid_elements_equal", """// LeetCode 3888 - Minimum Operations To Make All Grid Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

class Solution {
    private var grid = [[Int]]()
    private var k = 0, m = 0, n = 0

    func minOperations(_ grid: [[Int]], _ k: Int) -> Int {
        self.grid = grid
        self.k = k
        m = grid.count
        n = grid[0].count
        var maxVal = grid[0][0]
        for row in grid {
            for x in row { maxVal = max(maxVal, x) }
        }
        for t in maxVal...(maxVal + 1) {
            let res = check(t)
            if res != -1 { return res }
        }
        return -1
    }

    private func check(_ target: Int) -> Int {
        var diff = Array(repeating: [Int](repeating: 0, count: n + 2), count: m + 2)
        var totalOps = 0
        for i in 1...m {
            for j in 1...n {
                diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
                let curVal = grid[i - 1][j - 1] + diff[i][j]
                if curVal > target { return -1 }
                if curVal < target {
                    if i + k - 1 > m || j + k - 1 > n { return -1 }
                    let needed = target - curVal
                    totalOps += needed
                    diff[i][j] += needed
                    diff[i + k][j] -= needed
                    diff[i][j + k] -= needed
                    diff[i + k][j + k] += needed
                }
            }
        }
        return totalOps
    }
}
""")

write("3889_mirror_frequency_distance", """// LeetCode 3889 - Mirror Frequency Distance
// https://leetcode.com/problems/mirror-frequency-distance/

class Solution {
    func mirrorFrequency(_ s: String) -> Int {
        var freq = [Character: Int]()
        for c in s { freq[c, default: 0] += 1 }
        var ans = 0
        var vis = [Character: Bool]()
        for (c, v) in freq {
            let m: Character
            if c >= "a" && c <= "z" {
                m = Character(UnicodeScalar(97 + 25 - Int(c.asciiValue! - 97))!)
            } else {
                m = Character(UnicodeScalar(48 + (9 - Int(c.asciiValue! - 48)))!)
            }
            if vis[m] == true { continue }
            vis[c] = true
            let mv = freq[m, default: 0]
            ans += abs(v - mv)
        }
        return ans
    }
}
""")

write("3890_integers_with_multiple_sum_of_two_cubes", """// LeetCode 3890 - Integers With Multiple Sum Of Two Cubes
// https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

class Solution {
    private static let GOOD: [Int] = {
        let LIMIT = 1_000_000_000
        var cnt = [Int: Int]()
        var cubes = [Int](repeating: 0, count: 1001)
        for i in 0...1000 { cubes[i] = i * i * i }
        for a in 1...1000 {
            for b in a...1000 {
                let x = cubes[a] + cubes[b]
                if x > LIMIT { break }
                cnt[x, default: 0] += 1
            }
        }
        return cnt.filter { $0.value > 1 }.map { $0.key }.sorted()
    }()

    func findGoodIntegers(_ n: Int) -> [Int] {
        var lo = 0, hi = Solution.GOOD.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if Solution.GOOD[mid] <= n { lo = mid + 1 }
            else { hi = mid }
        }
        return Array(Solution.GOOD.prefix(lo))
    }
}
""")

write("3891_minimum_increase_to_maximize_special_indices", """// LeetCode 3891 - Minimum Increase To Maximize Special Indices
// https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

class Solution {
    private var nums = [Int]()
    private var f = [[Int]]()
    private var n = 0

    func minIncrease(_ nums: [Int]) -> Int {
        self.nums = nums
        n = nums.count
        f = Array(repeating: [-1, -1], count: n)
        return dfs(1, (n & 1) ^ 1)
    }

    private func dfs(_ i: Int, _ j: Int) -> Int {
        if i >= n - 1 { return 0 }
        if f[i][j] != -1 { return f[i][j] }
        let cost = max(0, max(nums[i - 1], nums[i + 1]) + 1 - nums[i])
        var ans = cost + dfs(i + 2, j)
        if j > 0 { ans = min(ans, dfs(i + 1, 0)) }
        f[i][j] = ans
        return ans
    }
}
""")

write("3892_minimum_operations_to_achieve_at_least_k_peaks", """// LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
// https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

class Solution {
    private var cost = [Int]()
    private let INF = 1 << 60

    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        if k == 0 { return 0 }
        if k > n / 2 { return -1 }
        cost = [Int](repeating: 0, count: n)
        for i in 0..<n {
            let left = nums[(i + n - 1) % n], right = nums[(i + 1) % n]
            let need = max(left, right)
            if need >= nums[i] { cost[i] = need - nums[i] + 1 }
        }
        var answer = line(1, n - 1, k)
        var withFirst = line(2, n - 2, k - 1)
        if withFirst != INF {
            withFirst += cost[0]
            answer = min(answer, withFirst)
        }
        if answer == INF { return -1 }
        return answer
    }

    private func line(_ left: Int, _ right: Int, _ choose: Int) -> Int {
        if choose == 0 { return 0 }
        if left > right || choose > (right - left + 2) / 2 { return INF }
        var prev2 = [Int](repeating: INF, count: choose + 1)
        var prev1 = [Int](repeating: INF, count: choose + 1)
        prev2[0] = 0
        prev1[0] = 0
        if left <= right {
            for i in left...right {
                var current = prev1
                for j in 1...choose {
                    if prev2[j - 1] != INF && prev2[j - 1] + cost[i] < current[j] {
                        current[j] = prev2[j - 1] + cost[i]
                    }
                }
                prev2 = prev1
                prev1 = current
            }
        }
        return prev1[choose]
    }
}
""")

write("3893_maximum_team_size_with_overlapping_intervals", """// LeetCode 3893 - Maximum Team Size With Overlapping Intervals
// https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

class Solution {
    func maximumTeamSize(_ startTime: [Int], _ endTime: [Int]) -> Int {
        let n = startTime.count
        let st = startTime.sorted()
        let en = endTime.sorted()
        var ans = 0
        for t in 0..<n {
            let l = startTime[t], r = endTime[t]
            let i = upperBound(en, l - 1)
            let j = upperBound(st, r)
            ans = max(ans, j - i)
        }
        return ans
    }

    private func upperBound(_ a: [Int], _ x: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] <= x { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }
}
""")

write("3894_traffic_signal_color", """// LeetCode 3894 - Traffic Signal Color
// https://leetcode.com/problems/traffic-signal-color/

class Solution {
    func trafficSignal(_ timer: Int) -> String {
        if timer == 0 { return "Green" }
        if timer == 30 { return "Orange" }
        if timer > 30 && timer <= 90 { return "Red" }
        return "Invalid"
    }
}
""")

write("3895_count_digit_appearances", """// LeetCode 3895 - Count Digit Appearances
// https://leetcode.com/problems/count-digit-appearances/

class Solution {
    func countDigitOccurrences(_ nums: [Int], _ digit: Int) -> Int {
        var ans = 0
        for num in nums {
            var x = num
            while x > 0 {
                if x % 10 == digit { ans += 1 }
                x /= 10
            }
        }
        return ans
    }
}
""")

write("3896_minimum_operations_to_transform_array_into_alternating_prime", """// LeetCode 3896 - Minimum Operations To Transform Array Into Alternating Prime
// https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

class Solution {
    private static let MX = 200000
    private static let isPrime: [Bool] = {
        var ip = [Bool](repeating: true, count: MX + 1)
        ip[0] = false
        ip[1] = false
        var i = 2
        while i <= MX / i {
            if ip[i] {
                var j = i * i
                while j <= MX {
                    ip[j] = false
                    j += i
                }
            }
            i += 1
        }
        return ip
    }()
    private static let primes: [Int] = {
        var p = [Int]()
        for i in 2...MX where isPrime[i] { p.append(i) }
        return p
    }()

    func minOperations(_ nums: [Int]) -> Int {
        var ans = 0
        for i in 0..<nums.count {
            let x = nums[i]
            if i % 2 == 0 {
                var lo = 0, hi = Solution.primes.count
                while lo < hi {
                    let mid = (lo + hi) / 2
                    if Solution.primes[mid] < x { lo = mid + 1 }
                    else { hi = mid }
                }
                ans += Solution.primes[lo] - x
            } else if Solution.isPrime[x] {
                ans += (x == 2) ? 2 : 1
            }
        }
        return ans
    }
}
""")

write("3897_maximum_value_of_concatenated_binary_segments", """// LeetCode 3897 - Maximum Value Of Concatenated Binary Segments
// https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

class Solution {
    private let MOD = 1_000_000_007

    private func group(_ p: [Int]) -> Int {
        if p[1] == 0 { return 0 }
        if p[0] > 0 { return 1 }
        return 2
    }

    func maxValue(_ nums1: [Int], _ nums0: [Int]) -> Int {
        let n = nums1.count
        var pairs = [[Int]]()
        var b = 0
        for i in 0..<n {
            pairs.append([nums1[i], nums0[i]])
            b += nums1[i] + nums0[i]
        }
        pairs.sort { a, c in
            let g1 = group(a), g2 = group(c)
            if g1 != g2 { return g1 < g2 }
            if g1 == 0 { return a[0] > c[0] }
            if g1 == 1 {
                if a[0] != c[0] { return a[0] > c[0] }
                return a[1] < c[1]
            }
            return a[1] < c[1]
        }
        var p = [Int](repeating: 0, count: max(b, 1))
        if b > 0 { p[0] = 1 }
        if b > 1 {
            for i in 1..<b { p[i] = 2 * p[i - 1] % MOD }
        }
        var ans = 0
        b -= 1
        for pr in pairs {
            var cnt1 = pr[0], cnt0 = pr[1]
            while cnt1 > 0 {
                ans = (ans + p[b]) % MOD
                b -= 1
                cnt1 -= 1
            }
            b -= cnt0
        }
        return ans
    }
}
""")

write("3898_find_the_degree_of_each_vertex", """// LeetCode 3898 - Find The Degree Of Each Vertex
// https://leetcode.com/problems/find-the-degree-of-each-vertex/

class Solution {
    func findDegrees(_ matrix: [[Int]]) -> [Int] {
        var ans = [Int](repeating: 0, count: matrix.count)
        for i in 0..<matrix.count {
            for x in matrix[i] { ans[i] += x }
        }
        return ans
    }
}
""")

write("3899_angles_of_a_triangle", """// LeetCode 3899 - Angles Of A Triangle
// https://leetcode.com/problems/angles-of-a-triangle/

import Foundation

class Solution {
    func internalAngles(_ sides: [Int]) -> [Double] {
        let s = sides.sorted()
        let a = Double(s[0]), b = Double(s[1]), c = Double(s[2])
        if a + b <= c { return [] }
        let PI = acos(-1.0)
        let A = acos((b * b + c * c - a * a) / (2.0 * b * c)) * 180.0 / PI
        let B = acos((a * a + c * c - b * b) / (2.0 * a * c)) * 180.0 / PI
        let C = 180.0 - A - B
        return [A, B, C]
    }
}
""")

write("3900_longest_balanced_substring_after_one_swap", """// LeetCode 3900 - Longest Balanced Substring After One Swap
// https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

class Solution {
    func longestBalanced(_ s: String) -> Int {
        let chars = Array(s)
        var cnt0 = 0
        for c in chars where c == "0" { cnt0 += 1 }
        let cnt1 = chars.count - cnt0
        var pos = [Int: [Int]]()
        pos[0] = [-1]
        var ans = 0, pre = 0
        for i in 0..<chars.count {
            if chars[i] == "1" { pre += 1 } else { pre -= 1 }
            pos[pre, default: []].append(i)
            ans = max(ans, i - pos[pre]![0])
            if let p = pos[pre - 2] {
                if (i - p[0] - 2) / 2 < cnt0 { ans = max(ans, i - p[0]) }
                else if p.count > 1 { ans = max(ans, i - p[1]) }
            }
            if let p = pos[pre + 2] {
                if (i - p[0] - 2) / 2 < cnt1 { ans = max(ans, i - p[0]) }
                else if p.count > 1 { ans = max(ans, i - p[1]) }
            }
        }
        return ans
    }
}
""")

write("3901_good_subsequence_queries", """// LeetCode 3901 - Good Subsequence Queries
// https://leetcode.com/problems/good-subsequence-queries/

class Solution {
    private class Node {
        var l = 0, r = 0, g = 0
    }

    private class SegmentTree {
        var tr: [Node]
        init(_ n: Int) {
            tr = (0..<(n << 2)).map { _ in Node() }
            build(1, 1, n)
        }
        func build(_ u: Int, _ l: Int, _ r: Int) {
            tr[u].l = l; tr[u].r = r; tr[u].g = 0
            if l == r { return }
            let mid = (l + r) >> 1
            build(u << 1, l, mid)
            build(u << 1 | 1, mid + 1, r)
        }
        func pushup(_ u: Int) { tr[u].g = gcd(tr[u << 1].g, tr[u << 1 | 1].g) }
        func modify(_ u: Int, _ x: Int, _ v: Int) {
            if tr[u].l == tr[u].r { tr[u].g = v; return }
            let mid = (tr[u].l + tr[u].r) >> 1
            if x <= mid { modify(u << 1, x, v) }
            else { modify(u << 1 | 1, x, v) }
            pushup(u)
        }
        func query(_ u: Int, _ l: Int, _ r: Int) -> Int {
            if l > r { return 0 }
            if tr[u].l >= l && tr[u].r <= r { return tr[u].g }
            let mid = (tr[u].l + tr[u].r) >> 1
            if r <= mid { return query(u << 1, l, r) }
            if l > mid { return query(u << 1 | 1, l, r) }
            return gcd(query(u << 1, l, mid), query(u << 1 | 1, mid + 1, r))
        }
        static func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        func gcd(_ a: Int, _ b: Int) -> Int { SegmentTree.gcd(a, b) }
    }

    func countGoodSubseq(_ nums: [Int], _ p: Int, _ queries: [[Int]]) -> Int {
        var nums = nums
        let n = nums.count
        let tree = SegmentTree(n)
        var cnt = 0
        for i in 0..<n {
            if nums[i] % p == 0 {
                tree.modify(1, i + 1, nums[i])
                cnt += 1
            }
        }
        var ans = 0
        for q in queries {
            let idx = q[0], val = q[1]
            if nums[idx] % p == 0 {
                tree.modify(1, idx + 1, 0)
                cnt -= 1
            }
            if val % p == 0 {
                tree.modify(1, idx + 1, val)
                cnt += 1
            }
            nums[idx] = val
            if tree.tr[1].g != p { continue }
            if cnt < n || n > 6 {
                ans += 1
                continue
            }
            for i in 1...n {
                let leftG = tree.query(1, 1, i - 1)
                let rightG = tree.query(1, i + 1, n)
                var g = leftG, b = rightG
                while b != 0 { let t = g % b; g = b; b = t }
                if g == p { ans += 1; break }
            }
        }
        return ans
    }
}
""")

write("3902_zigzag_level_sum_of_binary_tree", """// LeetCode 3902 - Zigzag Level Sum Of Binary Tree
// https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/
""" + TREE + """
class Solution {
    func zigzagLevelSum(_ root: TreeNode?) -> [Int] {
        guard let root = root else { return [] }
        var ans = [Int]()
        var q = [root]
        var left = true
        while !q.isEmpty {
            var nq = [TreeNode]()
            for node in q {
                if let l = node.left { nq.append(l) }
                if let r = node.right { nq.append(r) }
            }
            let m = q.count
            var s = 0
            for i in 0..<m {
                let node = left ? q[i] : q[m - i - 1]
                let child = left ? node.left : node.right
                if child == nil { break }
                s += node.val
            }
            ans.append(s)
            left = !left
            q = nq
        }
        return ans
    }
}
""")
