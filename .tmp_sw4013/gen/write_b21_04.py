#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")


def write(folder, content):
    p = ROOT / folder / "Solution.swift"
    if "func solve()" not in p.read_text():
        print("SKIP", folder)
        return
    p.write_text(content)
    print("WROTE", folder)


write("3801_minimum_cost_to_merge_sorted_lists", """// LeetCode 3801 - Minimum Cost To Merge Sorted Lists
// https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/

class Solution {
    func minMergeCost(_ lists: [[Int]]) -> Int {
        let m = lists.count
        let totalMasks = 1 << m
        var merged = [[Int]](repeating: [], count: totalMasks)
        var length = [Int](repeating: 0, count: totalMasks)
        var median = [Int](repeating: 0, count: totalMasks)
        if totalMasks > 1 {
            for mask in 1..<totalMasks {
                let bit = mask & -mask
                let index = trailingZeros(bit)
                let previous = merged[mask ^ bit]
                let current = lists[index]
                var out = [Int]()
                var i = 0, j = 0
                while i < previous.count || j < current.count {
                    if j == current.count || (i < previous.count && previous[i] <= current[j]) {
                        out.append(previous[i])
                        i += 1
                    } else {
                        out.append(current[j])
                        j += 1
                    }
                }
                merged[mask] = out
                length[mask] = out.count
                median[mask] = out[(out.count - 1) / 2]
            }
        }
        let INF = 1 << 62
        var dp = [Int](repeating: 0, count: totalMasks)
        if totalMasks > 1 {
            for mask in 1..<totalMasks {
                if (mask & (mask - 1)) == 0 { continue }
                dp[mask] = INF
                let firstBit = mask & -mask
                var left = (mask - 1) & mask
                while left > 0 {
                    if (left & firstBit) != 0 {
                        let right = mask ^ left
                        if right != 0 {
                            var diff = median[left] - median[right]
                            if diff < 0 { diff = -diff }
                            let candidate = dp[left] + dp[right] + length[mask] + diff
                            if candidate < dp[mask] { dp[mask] = candidate }
                        }
                    }
                    left = (left - 1) & mask
                }
            }
        }
        return dp[totalMasks - 1]
    }

    private func trailingZeros(_ x: Int) -> Int {
        var x = x, n = 0
        while x > 0 && (x & 1) == 0 { x >>= 1; n += 1 }
        return n
    }
}
""")

write("3802_number_of_ways_to_paint_sheets", """// LeetCode 3802 - Number Of Ways To Paint Sheets
// https://leetcode.com/problems/number-of-ways-to-paint-sheets/

class Solution {
    func numberOfWays(_ n: Int, _ limit: [Int]) -> Int {
        let MOD = 1_000_000_007
        let limit = limit.sorted()
        var points = [1, n]
        for x in limit {
            if x + 1 > 1 && x + 1 < n { points.append(x + 1) }
            if n - x > 1 && n - x < n { points.append(n - x) }
        }
        points.sort()
        var u = 0
        for i in 0..<points.count {
            if u == 0 || points[i] != points[u - 1] {
                points[u] = points[i]
                u += 1
            }
        }
        points = Array(points.prefix(u))
        var ans = 0
        if points.count >= 2 {
            for i in 0..<(points.count - 1) {
                let x = points[i]
                let a = countGE(limit, x), b = countGE(limit, n - x)
                let same = countGE(limit, max(x, n - x))
                var ways = (a * b - same) % MOD
                let length = points[i + 1] - x
                ans = (ans + ways * length) % MOD
            }
        }
        if ans < 0 { ans += MOD }
        return ans
    }

    private func countGE(_ limit: [Int], _ x: Int) -> Int {
        var lo = 0, hi = limit.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if limit[mid] < x { lo = mid + 1 }
            else { hi = mid }
        }
        return limit.count - lo
    }
}
""")

write("3803_count_residue_prefixes", """// LeetCode 3803 - Count Residue Prefixes
// https://leetcode.com/problems/count-residue-prefixes/

class Solution {
    func residuePrefixes(_ s: String) -> Int {
        var st = Set<Character>()
        var ans = 0
        var i = 0
        for c in s {
            st.insert(c)
            if st.count == (i + 1) % 3 { ans += 1 }
            i += 1
        }
        return ans
    }
}
""")

write("3804_number_of_centered_subarrays", """// LeetCode 3804 - Number Of Centered Subarrays
// https://leetcode.com/problems/number-of-centered-subarrays/

class Solution {
    func centeredSubarrays(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var st = Set<Int>()
            var s = 0
            for j in i..<n {
                s += nums[j]
                st.insert(nums[j])
                if st.contains(s) { ans += 1 }
            }
        }
        return ans
    }
}
""")

write("3805_count_caesar_cipher_pairs", """// LeetCode 3805 - Count Caesar Cipher Pairs
// https://leetcode.com/problems/count-caesar-cipher-pairs/

class Solution {
    func countPairs(_ words: [String]) -> Int {
        var cnt = [String: Int]()
        for word in words {
            var s = Array(word)
            let k = Int(Character("z").asciiValue! - s[0].asciiValue!)
            if s.count > 1 {
                for i in 1..<s.count {
                    let v = Int(s[i].asciiValue! - 97)
                    s[i] = Character(UnicodeScalar(97 + (v + k) % 26)!)
                }
            }
            s[0] = "z"
            let key = String(s)
            cnt[key, default: 0] += 1
        }
        var ans = 0
        for v in cnt.values { ans += v * (v - 1) / 2 }
        return ans
    }
}
""")

write("3806_maximum_bitwise_and_after_increment_operations", """// LeetCode 3806 - Maximum Bitwise And After Increment Operations
// https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

class Solution {
    private func bitLen(_ x: Int) -> Int {
        if x == 0 { return 0 }
        var x = x, n = 0
        while x > 0 { n += 1; x >>= 1 }
        return n
    }

    func maximumAND(_ nums: [Int], _ k: Int, _ m: Int) -> Int {
        var mxVal = nums[0]
        for v in nums where v > mxVal { mxVal = v }
        mxVal += k
        let mx = bitLen(mxVal)
        var ans = 0
        var cost = [Int](repeating: 0, count: nums.count)
        if mx > 0 {
            for bit in stride(from: mx - 1, through: 0, by: -1) {
                let target = ans | (1 << bit)
                for i in 0..<nums.count {
                    let x = nums[i]
                    let j = bitLen(target & ~x)
                    let mask = (1 << j) - 1
                    cost[i] = (target & mask) - (x & mask)
                }
                cost.sort()
                var sum = 0
                for i in 0..<m { sum += cost[i] }
                if sum <= k { ans = target }
            }
        }
        return ans
    }
}
""")

write("3807_minimum_cost_to_repair_edges_to_traverse_a_graph", """// LeetCode 3807 - Minimum Cost To Repair Edges To Traverse A Graph
// https://leetcode.com/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/

class Solution {
    private var edges = [[Int]]()
    private var n = 0, k = 0

    func minCost(_ n: Int, _ edges: [[Int]], _ k: Int) -> Int {
        self.n = n
        self.k = k
        self.edges = edges.sorted { $0[2] < $1[2] }
        let m = self.edges.count
        if m == 0 { return -1 }
        var l = 0, r = m - 1
        while l < r {
            let mid = (l + r) >> 1
            if check(mid) { r = mid }
            else { l = mid + 1 }
        }
        if check(l) { return self.edges[l][2] }
        return -1
    }

    private func check(_ idx: Int) -> Bool {
        var g = [[Int]](repeating: [], count: n)
        for i in 0...idx {
            g[edges[i][0]].append(edges[i][1])
            g[edges[i][1]].append(edges[i][0])
        }
        var q = [0]
        var vis = [Bool](repeating: false, count: n)
        vis[0] = true
        var dist = 0
        while !q.isEmpty {
            var nq = [Int]()
            for u in q {
                if u == n - 1 { return dist <= k }
                for v in g[u] where !vis[v] {
                    vis[v] = true
                    nq.append(v)
                }
            }
            q = nq
            dist += 1
        }
        return false
    }
}
""")

write("3809_best_reachable_tower", """// LeetCode 3809 - Best Reachable Tower
// https://leetcode.com/problems/best-reachable-tower/

class Solution {
    func bestTower(_ towers: [[Int]], _ center: [Int], _ radius: Int) -> [Int] {
        let cx = center[0], cy = center[1]
        var idx = -1
        for i in 0..<towers.count {
            let x = towers[i][0], y = towers[i][1], q = towers[i][2]
            let dist = abs(x - cx) + abs(y - cy)
            if dist > radius { continue }
            if idx == -1 || towers[idx][2] < q ||
                (towers[idx][2] == q &&
                 (x < towers[idx][0] || (x == towers[idx][0] && y < towers[idx][1]))) {
                idx = i
            }
        }
        if idx == -1 { return [-1, -1] }
        return [towers[idx][0], towers[idx][1]]
    }
}
""")

write("3810_minimum_operations_to_reach_target_array", """// LeetCode 3810 - Minimum Operations To Reach Target Array
// https://leetcode.com/problems/minimum-operations-to-reach-target-array/

class Solution {
    func minOperations(_ nums: [Int], _ target: [Int]) -> Int {
        var s = Set<Int>()
        for i in 0..<nums.count {
            if nums[i] != target[i] { s.insert(nums[i]) }
        }
        return s.count
    }
}
""")

write("3811_number_of_alternating_xor_partitions", """// LeetCode 3811 - Number Of Alternating Xor Partitions
// https://leetcode.com/problems/number-of-alternating-xor-partitions/

class Solution {
    func alternatingXOR(_ nums: [Int], _ target1: Int, _ target2: Int) -> Int {
        let MOD = 1_000_000_007
        var cnt1 = [Int: Int]()
        var cnt2 = [0: 1]
        var pre = 0, ans = 0
        for x in nums {
            pre ^= x
            let a = cnt2[pre ^ target1, default: 0]
            let b = cnt1[pre ^ target2, default: 0]
            ans = (a + b) % MOD
            cnt1[pre, default: 0] = (cnt1[pre, default: 0] + a) % MOD
            cnt2[pre, default: 0] = (cnt2[pre, default: 0] + b) % MOD
        }
        return ans
    }
}
""")

write("3812_minimum_edge_toggles_on_a_tree", """// LeetCode 3812 - Minimum Edge Toggles On A Tree
// https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/

class Solution {
    private var g = [[[Int]]]()
    private var start = [Character]()
    private var target = [Character]()
    private var ans = [Int]()

    func minimumFlips(_ n: Int, _ edges: [[Int]], _ start: String, _ target: String) -> [Int] {
        self.start = Array(start)
        self.target = Array(target)
        g = [[[Int]]](repeating: [], count: n)
        if n > 1 {
            for i in 0..<(n - 1) {
                let a = edges[i][0], b = edges[i][1]
                g[a].append([b, i])
                g[b].append([a, i])
            }
        }
        ans = []
        if dfs(0, -1) { return [-1] }
        return ans.sorted()
    }

    private func dfs(_ a: Int, _ fa: Int) -> Bool {
        var rev = start[a] != target[a]
        for e in g[a] {
            let b = e[0], i = e[1]
            if b != fa && dfs(b, a) {
                ans.append(i)
                rev = !rev
            }
        }
        return rev
    }
}
""")

write("3813_vowel_consonant_score", """// LeetCode 3813 - Vowel Consonant Score
// https://leetcode.com/problems/vowel-consonant-score/

class Solution {
    func vowelConsonantScore(_ s: String) -> Int {
        var v = 0, c = 0
        for ch in s where ch.isLetter {
            c += 1
            if "aeiou".contains(ch) { v += 1 }
        }
        c -= v
        if c == 0 { return 0 }
        return v / c
    }
}
""")

write("3814_maximum_capacity_within_budget", """// LeetCode 3814 - Maximum Capacity Within Budget
// https://leetcode.com/problems/maximum-capacity-within-budget/

class Solution {
    func maxCapacity(_ costs: [Int], _ capacity: [Int], _ budget: Int) -> Int {
        var arr = [[Int]]()
        for k in 0..<costs.count {
            if costs[k] < budget { arr.append([costs[k], capacity[k]]) }
        }
        if arr.isEmpty { return 0 }
        arr.sort { $0[0] < $1[0] }
        let m = arr.count
        var alive = [Bool](repeating: true, count: m)
        var h = [(Int, Int)]()
        for i in 0..<m { h.append((arr[i][1], i)) }
        h.sort { $0.0 != $1.0 ? $0.0 > $1.0 : $0.1 > $1.1 }
        while !h.isEmpty && !alive[h[0].1] { h.removeFirst() }
        var ans = h[0].0
        var i = 0, j = m - 1
        while i < j {
            alive[i] = false
            while i < j && arr[i][0] + arr[j][0] >= budget {
                alive[j] = false
                j -= 1
            }
            while !h.isEmpty && !alive[h[0].1] { h.removeFirst() }
            if !h.isEmpty { ans = max(ans, arr[i][1] + h[0].0) }
            i += 1
        }
        return ans
    }
}
""")

write("3815_design_auction_system", """// LeetCode 3815 - Design Auction System
// https://leetcode.com/problems/design-auction-system/

class AuctionSystem {
    private class Bid {
        var amount: Int
        var userId: Int
        init(_ amount: Int, _ userId: Int) {
            self.amount = amount
            self.userId = userId
        }
    }

    private var bids = [Int: [Int: Int]]()
    private var heaps = [Int: [Bid]]()

    init() {}

    func addBid(_ userId: Int, _ itemId: Int, _ bidAmount: Int) {
        if bids[itemId] == nil { bids[itemId] = [:] }
        bids[itemId]![userId] = bidAmount
        if heaps[itemId] == nil { heaps[itemId] = [] }
        heaps[itemId]!.append(Bid(bidAmount, userId))
        heaps[itemId]!.sort { a, b in
            if a.amount != b.amount { return a.amount > b.amount }
            return a.userId > b.userId
        }
    }

    func updateBid(_ userId: Int, _ itemId: Int, _ newAmount: Int) {
        addBid(userId, itemId, newAmount)
    }

    func removeBid(_ userId: Int, _ itemId: Int) {
        bids[itemId]?.removeValue(forKey: userId)
    }

    func getHighestBidder(_ itemId: Int) -> Int {
        guard var h = heaps[itemId] else { return -1 }
        let m = bids[itemId] ?? [:]
        while !h.isEmpty {
            let top = h[0]
            if let cur = m[top.userId], cur == top.amount {
                heaps[itemId] = h
                return top.userId
            }
            h.removeFirst()
        }
        heaps[itemId] = h
        return -1
    }
}
""")

write("3816_lexicographically_smallest_string_after_deleting_duplicate_characters", """// LeetCode 3816 - Lexicographically Smallest String After Deleting Duplicate Characters
// https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/

class Solution {
    func lexSmallestAfterDeletion(_ s: String) -> String {
        var cnt = [Int](repeating: 0, count: 26)
        for c in s { cnt[Int(c.asciiValue! - 97)] += 1 }
        var stk = [Character]()
        for c in s {
            while !stk.isEmpty && stk.last! > c && cnt[Int(stk.last!.asciiValue! - 97)] > 1 {
                cnt[Int(stk.last!.asciiValue! - 97)] -= 1
                stk.removeLast()
            }
            stk.append(c)
        }
        while !stk.isEmpty && cnt[Int(stk.last!.asciiValue! - 97)] > 1 {
            cnt[Int(stk.last!.asciiValue! - 97)] -= 1
            stk.removeLast()
        }
        return String(stk)
    }
}
""")

write("3817_good_indices_in_a_digit_string", """// LeetCode 3817 - Good Indices In A Digit String
// https://leetcode.com/problems/good-indices-in-a-digit-string/

class Solution {
    func goodIndices(_ s: String) -> [Int] {
        let chars = Array(s)
        var ans = [Int]()
        for i in 0..<chars.count {
            let t = String(i)
            let k = t.count
            if i + 1 - k >= 0 && String(chars[(i + 1 - k)..<(i + 1)]) == t {
                ans.append(i)
            }
        }
        return ans
    }
}
""")

write("3818_minimum_prefix_removal_to_make_array_strictly_increasing", """// LeetCode 3818 - Minimum Prefix Removal To Make Array Strictly Increasing
// https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/

class Solution {
    func minimumPrefixLength(_ nums: [Int]) -> Int {
        for i in stride(from: nums.count - 1, through: 1, by: -1) {
            if nums[i - 1] >= nums[i] { return i }
        }
        return 0
    }
}
""")

write("3819_rotate_non_negative_elements", """// LeetCode 3819 - Rotate Non Negative Elements
// https://leetcode.com/problems/rotate-non-negative-elements/

class Solution {
    func rotateElements(_ nums: [Int], _ k: Int) -> [Int] {
        var nums = nums
        var t = [Int]()
        for x in nums where x >= 0 { t.append(x) }
        let m = t.count
        if m == 0 { return nums }
        var d = [Int](repeating: 0, count: m)
        for i in 0..<m { d[((i - k) % m + m) % m] = t[i] }
        var j = 0
        for i in 0..<nums.count {
            if nums[i] >= 0 {
                nums[i] = d[j]
                j += 1
            }
        }
        return nums
    }
}
""")

write("3820_pythagorean_distance_nodes_in_a_tree", """// LeetCode 3820 - Pythagorean Distance Nodes In A Tree
// https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/

class Solution {
    private var g = [[Int]]()
    private var n = 0

    func specialNodes(_ n: Int, _ edges: [[Int]], _ x: Int, _ y: Int, _ z: Int) -> Int {
        self.n = n
        g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        let d1 = bfs(x), d2 = bfs(y), d3 = bfs(z)
        var ans = 0
        for i in 0..<n {
            var a = [d1[i], d2[i], d3[i]]
            a.sort()
            if a[0] * a[0] + a[1] * a[1] == a[2] * a[2] { ans += 1 }
        }
        return ans
    }

    private func bfs(_ start: Int) -> [Int] {
        var dist = [Int](repeating: 1_000_000_000, count: n)
        var q = [start]
        dist[start] = 0
        var head = 0
        while head < q.count {
            let u = q[head]
            head += 1
            for v in g[u] {
                if dist[v] > dist[u] + 1 {
                    dist[v] = dist[u] + 1
                    q.append(v)
                }
            }
        }
        return dist
    }
}
""")

write("3821_find_nth_smallest_integer_with_k_one_bits", """// LeetCode 3821 - Find Nth Smallest Integer With K One Bits
// https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/

class Solution {
    private static let C: [[Int]] = {
        let MX = 50
        var c = Array(repeating: [Int](repeating: 0, count: MX + 1), count: MX)
        for i in 0..<MX {
            c[i][0] = 1
            if i >= 1 {
                for j in 1...i { c[i][j] = c[i - 1][j - 1] + c[i - 1][j] }
            }
        }
        return c
    }()

    func nthSmallest(_ n: Int, _ k: Int) -> Int {
        var n = n, k = k
        var ans = 0
        for i in stride(from: 49, through: 0, by: -1) {
            if n > Solution.C[i][k] {
                n -= Solution.C[i][k]
                ans |= 1 << i
                k -= 1
                if k == 0 { break }
            }
        }
        return ans
    }
}
""")
