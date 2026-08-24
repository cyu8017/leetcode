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


write("3863_minimum_operations_to_sort_a_string", """// LeetCode 3863 - Minimum Operations To Sort A String
// https://leetcode.com/problems/minimum-operations-to-sort-a-string/

class Solution {
    func minOperations(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var sorted = true
        if n > 1 {
            for i in 1..<n {
                if chars[i] < chars[i - 1] { sorted = false; break }
            }
        }
        if sorted { return 0 }
        if n == 2 { return -1 }
        var mn = chars[0], mx = chars[0]
        for c in chars {
            if c < mn { mn = c }
            if c > mx { mx = c }
        }
        if chars[0] == mn || chars[n - 1] == mx { return 1 }
        if n > 2 {
            for i in 1..<(n - 1) {
                if chars[i] == mn || chars[i] == mx { return 2 }
            }
        }
        return 3
    }
}
""")

write("3864_minimum_cost_to_partition_a_binary_string", """// LeetCode 3864 - Minimum Cost To Partition A Binary String
// https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/

class Solution {
    private var pre = [Int]()
    private var encCost = 0, flatCost = 0

    func minCost(_ s: String, _ encCost: Int, _ flatCost: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        self.encCost = encCost
        self.flatCost = flatCost
        pre = [Int](repeating: 0, count: n + 1)
        for i in 1...n { pre[i] = pre[i - 1] + Int(chars[i - 1].asciiValue! - 48) }
        return dfs(0, n)
    }

    private func dfs(_ l: Int, _ r: Int) -> Int {
        let x = pre[r] - pre[l]
        var res = x != 0 ? (r - l) * x * encCost : flatCost
        if (r - l) % 2 == 0 {
            let m = (l + r) / 2
            res = min(res, dfs(l, m) + dfs(m, r))
        }
        return res
    }
}
""")

write("3865_reverse_k_subarrays", """// LeetCode 3865 - Reverse K Subarrays
// https://leetcode.com/problems/reverse-k-subarrays/

class Solution {
    func reverseSubarrays(_ nums: [Int], _ k: Int) -> [Int] {
        var nums = nums
        let n = nums.count
        let m = n / k
        var i = 0
        while i < n {
            var lo = i, hi = i + m - 1
            while lo < hi {
                nums.swapAt(lo, hi)
                lo += 1
                hi -= 1
            }
            i += m
        }
        return nums
    }
}
""")

write("3866_first_unique_even_element", """// LeetCode 3866 - First Unique Even Element
// https://leetcode.com/problems/first-unique-even-element/

class Solution {
    func firstUniqueEven(_ nums: [Int]) -> Int {
        var cnt = [Int](repeating: 0, count: 101)
        for x in nums { cnt[x] += 1 }
        for x in nums {
            if x % 2 == 0 && cnt[x] == 1 { return x }
        }
        return -1
    }
}
""")

write("3867_sum_of_gcd_of_formed_pairs", """// LeetCode 3867 - Sum Of Gcd Of Formed Pairs
// https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

class Solution {
    private func gcd(_ a: Int, _ b: Int) -> Int {
        var a = a, b = b
        while b != 0 {
            let t = a % b
            a = b
            b = t
        }
        return a
    }

    func gcdSum(_ nums: [Int]) -> Int {
        let n = nums.count
        var prefixGcd = [Int](repeating: 0, count: n)
        var mx = 0
        for i in 0..<n {
            mx = max(mx, nums[i])
            prefixGcd[i] = gcd(nums[i], mx)
        }
        prefixGcd.sort()
        var ans = 0
        for i in 0..<(n / 2) { ans += gcd(prefixGcd[i], prefixGcd[n - i - 1]) }
        return ans
    }
}
""")

write("3868_minimum_cost_to_equalize_arrays_using_swaps", """// LeetCode 3868 - Minimum Cost To Equalize Arrays Using Swaps
// https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

class Solution {
    func minCost(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var cnt2 = [Int: Int]()
        for x in nums2 { cnt2[x, default: 0] += 1 }
        var cnt1 = [Int: Int]()
        for x in nums1 {
            if let c = cnt2[x], c > 0 { cnt2[x] = c - 1 }
            else { cnt1[x, default: 0] += 1 }
        }
        var ans = 0
        for v in cnt1.values {
            if v % 2 == 1 { return -1 }
            ans += v / 2
        }
        for v in cnt2.values {
            if v % 2 == 1 { return -1 }
        }
        return ans
    }
}
""")

write("3869_count_fancy_numbers_in_a_range", """// LeetCode 3869 - Count Fancy Numbers In A Range
// https://leetcode.com/problems/count-fancy-numbers-in-a-range/

class Solution {
    private var num = [Character]()
    private var f = [[[[Int]]]]()
    private var n = 0

    private func check(_ s: Int) -> Bool {
        if s < 100 { return s % 11 != 0 }
        let mid = (s / 10) % 10
        let last = s % 10
        return mid > 1 && mid < last
    }

    func countFancy(_ l: Int, _ r: Int) -> Int {
        return calc(r) - calc(l - 1)
    }

    private func calc(_ x: Int) -> Int {
        num = Array(String(x))
        n = num.count
        f = Array(repeating: Array(repeating: Array(repeating: [Int](repeating: -1, count: 4), count: 10), count: 9 * n + 1), count: n)
        return dfs(0, 0, 0, 0, true)
    }

    private func dfs(_ pos: Int, _ s: Int, _ prev: Int, _ st: Int, _ lim: Bool) -> Int {
        if pos >= n {
            if st != 3 { return 1 }
            return check(s) ? 1 : 0
        }
        if !lim && f[pos][s][prev][st] != -1 { return f[pos][s][prev][st] }
        let up = lim ? Int(num[pos].asciiValue! - 48) : 9
        var res = 0
        for i in 0...up {
            var nxtSt = st
            if st == 0 {
                if prev == 0 { nxtSt = 0 }
                else if i > prev { nxtSt = 1 }
                else if i < prev { nxtSt = 2 }
                else { nxtSt = 3 }
            } else if st == 1 {
                nxtSt = i > prev ? 1 : 3
            } else if st == 2 {
                nxtSt = i < prev ? 2 : 3
            } else {
                nxtSt = 3
            }
            res += dfs(pos + 1, s + i, i, nxtSt, lim && i == up)
        }
        if !lim { f[pos][s][prev][st] = res }
        return res
    }
}
""")

write("3870_count_commas_in_range", """// LeetCode 3870 - Count Commas In Range
// https://leetcode.com/problems/count-commas-in-range/

class Solution {
    func countCommas(_ n: Int) -> Int {
        return max(0, n - 999)
    }
}
""")

write("3871_count_commas_in_range_ii", """// LeetCode 3871 - Count Commas In Range II
// https://leetcode.com/problems/count-commas-in-range-ii/

class Solution {
    func countCommas(_ n: Int) -> Int {
        var ans = 0
        var x = 1000
        while x <= n {
            ans += n - x + 1
            if x > n / 1000 { break }
            x *= 1000
        }
        return ans
    }
}
""")

write("3872_longest_arithmetic_sequence_after_changing_at_most_one_element", """// LeetCode 3872 - Longest Arithmetic Sequence After Changing At Most One Element
// https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/

class Solution {
    func longestArithmetic(_ nums: [Int]) -> Int {
        let n = nums.count
        var d = [Int](repeating: 0, count: n)
        if n > 1 {
            for i in 1..<n { d[i] = nums[i] - nums[i - 1] }
        }
        var f = [Int](repeating: 2, count: n)
        var g = [Int](repeating: 2, count: n)
        f[0] = 1
        g[n - 1] = 1
        if n > 2 {
            for i in 2..<n {
                if d[i] == d[i - 1] { f[i] = f[i - 1] + 1 }
            }
            for i in stride(from: n - 3, through: 0, by: -1) {
                if d[i + 1] == d[i + 2] { g[i] = g[i + 1] + 1 }
            }
        }
        var ans = 3
        for i in 0..<n {
            ans = max(ans, max(f[i], g[i]))
            if i > 0 { ans = max(ans, f[i - 1] + 1) }
            if i + 1 < n { ans = max(ans, g[i + 1] + 1) }
            if i > 0 && i < n - 1 {
                var diff = nums[i + 1] - nums[i - 1]
                if diff % 2 == 0 {
                    diff /= 2
                    var k = 3
                    if i > 1 && diff == d[i - 1] { k += f[i - 1] - 1 }
                    if i < n - 2 && diff == d[i + 2] { k += g[i + 1] - 1 }
                    ans = max(ans, k)
                }
            }
        }
        return ans
    }
}
""")

write("3873_maximum_points_activated_with_one_addition", """// LeetCode 3873 - Maximum Points Activated With One Addition
// https://leetcode.com/problems/maximum-points-activated-with-one-addition/

class Solution {
    private class UnionFind {
        var p = [Int: Int]()
        var size = [Int: Int]()

        func find(_ x: Int) -> Int {
            if p[x] == nil {
                p[x] = x
                size[x] = 1
            }
            if p[x] != x { p[x] = find(p[x]!) }
            return p[x]!
        }

        func unite(_ a: Int, _ b: Int) -> Bool {
            var pa = find(a), pb = find(b)
            if pa == pb { return false }
            if size[pa]! > size[pb]! {
                p[pb] = pa
                size[pa]! += size[pb]!
            } else {
                p[pa] = pb
                size[pb]! += size[pa]!
            }
            return true
        }
    }

    func maxActivated(_ points: [[Int]]) -> Int {
        let uf = UnionFind()
        let m = 3000000000
        for pt in points { _ = uf.unite(pt[0], pt[1] + m) }
        var cnt = [Int: Int]()
        for pt in points {
            let r = uf.find(pt[0])
            cnt[r, default: 0] += 1
        }
        var mx1 = 0, mx2 = 0
        for x in cnt.values {
            if mx1 < x { mx2 = mx1; mx1 = x }
            else if mx2 < x { mx2 = x }
        }
        return mx1 + mx2 + 1
    }
}
""")

write("3874_valid_subarrays_with_exactly_one_peak", """// LeetCode 3874 - Valid Subarrays With Exactly One Peak
// https://leetcode.com/problems/valid-subarrays-with-exactly-one-peak/

class Solution {
    func validSubarrays(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var peaks = [Int]()
        if n > 2 {
            for i in 1..<(n - 1) {
                if nums[i] > nums[i - 1] && nums[i] > nums[i + 1] { peaks.append(i) }
            }
        }
        var ans = 0
        for j in 0..<peaks.count {
            let p = peaks[j]
            var leftMin = max(p - k, 0)
            if j > 0 { leftMin = max(leftMin, peaks[j - 1] + 1) }
            var rightMax = min(p + k, n - 1)
            if j < peaks.count - 1 { rightMax = min(rightMax, peaks[j + 1] - 1) }
            ans += (p - leftMin + 1) * (rightMax - p + 1)
        }
        return ans
    }
}
""")

write("3875_construct_uniform_parity_array_i", """// LeetCode 3875 - Construct Uniform Parity Array I
// https://leetcode.com/problems/construct-uniform-parity-array-i/

class Solution {
    func uniformArray(_ nums1: [Int]) -> Bool {
        return true
    }
}
""")

write("3876_construct_uniform_parity_array_ii", """// LeetCode 3876 - Construct Uniform Parity Array II
// https://leetcode.com/problems/construct-uniform-parity-array-ii/

class Solution {
    func uniformArray(_ nums1: [Int]) -> Bool {
        var mn = Int.max
        for x in nums1 {
            if x % 2 == 1 && x < mn { mn = x }
        }
        for x in nums1 {
            if x % 2 == 0 && mn != Int.max && x < mn { return false }
        }
        return true
    }
}
""")

write("3877_minimum_removals_to_achieve_target_xor", """// LeetCode 3877 - Minimum Removals To Achieve Target Xor
// https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

class Solution {
    func minRemovals(_ nums: [Int], _ target: Int) -> Int {
        var mx = 0
        for x in nums { mx = max(mx, x) }
        var m = 0
        if mx > 0 {
            var u = mx
            while u != 0 { m += 1; u >>= 1 }
        }
        if (1 << m) <= target { return -1 }
        let n = nums.count
        let N = 1 << m
        var f = Array(repeating: [Int](repeating: Int.min, count: N), count: n + 1)
        f[0][0] = 0
        for i in 1...n {
            let x = nums[i - 1]
            for j in 0..<N {
                f[i][j] = f[i - 1][j]
                if f[i - 1][j ^ x] != Int.min {
                    f[i][j] = max(f[i][j], f[i - 1][j ^ x] + 1)
                }
            }
        }
        if f[n][target] < 0 { return -1 }
        return n - f[n][target]
    }
}
""")

write("3878_count_good_subarrays", """// LeetCode 3878 - Count Good Subarrays
// https://leetcode.com/problems/count-good-subarrays/

class Solution {
    func countGoodSubarrays(_ nums: [Int]) -> Int {
        let n = nums.count
        var l = [Int](repeating: -1, count: n)
        var stk = [Int]()
        for i in 0..<n {
            let x = nums[i]
            while !stk.isEmpty && nums[stk.last!] < x && (nums[stk.last!] | x) == x {
                stk.removeLast()
            }
            if !stk.isEmpty { l[i] = stk.last! }
            stk.append(i)
        }
        var r = [Int](repeating: n, count: n)
        stk = []
        for i in stride(from: n - 1, through: 0, by: -1) {
            while !stk.isEmpty && (nums[stk.last!] | nums[i]) == nums[i] {
                stk.removeLast()
            }
            if !stk.isEmpty { r[i] = stk.last! }
            stk.append(i)
        }
        var ans = 0
        for i in 0..<n { ans += (i - l[i]) * (r[i] - i) }
        return ans
    }
}
""")

write("3879_maximum_distinct_path_sum_in_a_binary_tree", """// LeetCode 3879 - Maximum Distinct Path Sum In A Binary Tree
// https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/
""" + TREE + """
class Solution {
    private var g = [ObjectIdentifier: [TreeNode?]]()
    private var vis = [Int: Bool]()
    private var nodes = [TreeNode]()

    private func dfs(_ node: TreeNode?, _ p: TreeNode?) {
        guard let node = node else { return }
        g[ObjectIdentifier(node)] = [p, node.left, node.right]
        nodes.append(node)
        dfs(node.left, node)
        dfs(node.right, node)
    }

    private func dfs2(_ node: TreeNode?) -> Int {
        guard let node = node, vis[node.val] != true else { return 0 }
        vis[node.val] = true
        var best = 0
        if let nbrs = g[ObjectIdentifier(node)] {
            for nxt in nbrs { best = max(best, dfs2(nxt)) }
        }
        vis[node.val] = false
        return node.val + best
    }

    func maxSum(_ root: TreeNode?) -> Int {
        g = [:]
        vis = [:]
        nodes = []
        dfs(root, nil)
        var ans = Int.min
        for node in nodes {
            ans = max(ans, dfs2(node))
            vis = [:]
        }
        return ans
    }
}
""")

write("3880_minimum_absolute_difference_between_two_values", """// LeetCode 3880 - Minimum Absolute Difference Between Two Values
// https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

class Solution {
    func minAbsoluteDifference(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = n + 1
        var last = [-ans, -ans, -ans]
        for i in 0..<n {
            let x = nums[i]
            if x != 0 {
                ans = min(ans, i - last[3 - x])
                last[x] = i
            }
        }
        if ans > n { return -1 }
        return ans
    }
}
""")

write("3881_direction_assignments_with_exactly_k_visible_people", """// LeetCode 3881 - Direction Assignments With Exactly K Visible People
// https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

class Solution {
    private static let N = 100001
    private static let MOD = 1_000_000_007
    private static let fact: [Int] = {
        var f = [Int](repeating: 1, count: N)
        for i in 1..<N { f[i] = f[i - 1] * i % MOD }
        return f
    }()
    private static let invFact: [Int] = {
        var inv = [Int](repeating: 1, count: N)
        inv[N - 1] = qmi(fact[N - 1], MOD - 2, MOD)
        for i in stride(from: N - 2, through: 1, by: -1) {
            inv[i] = inv[i + 1] * (i + 1) % MOD
        }
        return inv
    }()

    private static func qmi(_ a: Int, _ k: Int, _ p: Int) -> Int {
        var a = a, k = k, res = 1
        while k != 0 {
            if (k & 1) != 0 { res = res * a % p }
            k >>= 1
            a = a * a % p
        }
        return res
    }

    private func comb(_ n: Int, _ k: Int) -> Int {
        return Solution.fact[n] * Solution.invFact[k] % Solution.MOD * Solution.invFact[n - k] % Solution.MOD
    }

    func countVisiblePeople(_ n: Int, _ pos: Int, _ k: Int) -> Int {
        let l = pos, r = n - pos - 1
        var ans = 0
        let lim = min(k, l)
        if lim >= 0 {
            for a in 0...lim {
                let b = k - a
                if b <= r {
                    ans = (ans + 2 * comb(l, a) % Solution.MOD * comb(r, b) % Solution.MOD) % Solution.MOD
                }
            }
        }
        return ans
    }
}
""")

write("3882_minimum_xor_path_in_a_grid", """// LeetCode 3882 - Minimum XOR Path in a Grid
// https://leetcode.com/problems/minimum-xor-path-in-a-grid/

class Solution {
    func minXor(_ grid: [[Int]]) -> Int {
        let rows = grid.count, cols = grid[0].count
        var dp = Array(repeating: [Bool](repeating: false, count: 1024), count: cols)
        for row in 0..<rows {
            var left = [Bool](repeating: false, count: 1024)
            for col in 0..<cols {
                var next = [Bool](repeating: false, count: 1024)
                let value = grid[row][col]
                if row == 0 && col == 0 {
                    next[value] = true
                } else {
                    for xorv in 0..<1024 {
                        if dp[col][xorv] || left[xorv] { next[xorv ^ value] = true }
                    }
                }
                dp[col] = next
                left = next
            }
        }
        for xorv in 0..<1024 {
            if dp[cols - 1][xorv] { return xorv }
        }
        return -1
    }
}
""")
