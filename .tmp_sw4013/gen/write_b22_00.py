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


write("3822_design_order_management_system", """// LeetCode 3822 - Design Order Management System
// https://leetcode.com/problems/design-order-management-system/

class OrderManagementSystem {
    private var orderTypeMap = [Int: String]()
    private var priceMap = [Int: Int]()
    private var t = [String: [Int]]()

    private func key(_ orderType: String, _ price: Int) -> String {
        return "\\(orderType)#\\(price)"
    }

    init() {}

    func addOrder(_ orderId: Int, _ orderType: String, _ price: Int) {
        orderTypeMap[orderId] = orderType
        priceMap[orderId] = price
        t[key(orderType, price), default: []].append(orderId)
    }

    func modifyOrder(_ orderId: Int, _ newPrice: Int) {
        let orderType = orderTypeMap[orderId]!
        let oldPrice = priceMap[orderId]!
        priceMap[orderId] = newPrice
        let oldKey = key(orderType, oldPrice)
        if var oldList = t[oldKey] {
            if let i = oldList.firstIndex(of: orderId) { oldList.remove(at: i) }
            t[oldKey] = oldList
        }
        t[key(orderType, newPrice), default: []].append(orderId)
    }

    func cancelOrder(_ orderId: Int) {
        let orderType = orderTypeMap[orderId]!
        let price = priceMap[orderId]!
        orderTypeMap.removeValue(forKey: orderId)
        priceMap.removeValue(forKey: orderId)
        let k = key(orderType, price)
        if var list = t[k] {
            if let i = list.firstIndex(of: orderId) { list.remove(at: i) }
            t[k] = list
        }
    }

    func getOrdersAtPrice(_ orderType: String, _ price: Int) -> [Int] {
        return t[key(orderType, price)] ?? []
    }
}
""")

write("3823_reverse_letters_then_special_characters_in_a_string", """// LeetCode 3823 - Reverse Letters Then Special Characters In A String
// https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

class Solution {
    func reverseByType(_ s: String) -> String {
        var a = [Character]()
        var b = [Character]()
        for c in s {
            if c.isLetter { a.append(c) } else { b.append(c) }
        }
        var j = a.count, k = b.count
        var arr = Array(s)
        for i in 0..<arr.count {
            if arr[i].isLetter {
                j -= 1
                arr[i] = a[j]
            } else {
                k -= 1
                arr[i] = b[k]
            }
        }
        return String(arr)
    }
}
""")

write("3824_minimum_k_to_reduce_array_within_limit", """// LeetCode 3824 - Minimum K To Reduce Array Within Limit
// https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/

class Solution {
    func minimumK(_ nums: [Int]) -> Int {
        var lo = 1, hi = 100000
        while lo < hi {
            let mid = (lo + hi) / 2
            if check(nums, mid) { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }

    private func check(_ nums: [Int], _ k: Int) -> Bool {
        var t = 0
        for x in nums { t += (x + k - 1) / k }
        return t <= k * k
    }
}
""")

write("3825_longest_strictly_increasing_subsequence_with_non_zero_bitwise_and", """// LeetCode 3825 - Longest Strictly Increasing Subsequence With Non Zero Bitwise And
// https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/

class Solution {
    private func bitLen(_ x: Int) -> Int {
        if x == 0 { return 0 }
        var x = x, n = 0
        while x > 0 { n += 1; x >>= 1 }
        return n
    }

    private func lis(_ arr: [Int]) -> Int {
        var g = [Int]()
        for x in arr {
            var lo = 0, hi = g.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if g[mid] < x { lo = mid + 1 }
                else { hi = mid }
            }
            if lo == g.count { g.append(x) }
            else { g[lo] = x }
        }
        return g.count
    }

    func longestSubsequence(_ nums: [Int]) -> Int {
        var ans = 0, mx = 0
        for x in nums { mx = max(mx, x) }
        let m = bitLen(mx)
        for i in 0..<m {
            var arr = [Int]()
            for x in nums where ((x >> i) & 1) != 0 { arr.append(x) }
            ans = max(ans, lis(arr))
        }
        return ans
    }
}
""")

write("3826_minimum_partition_score", """// LeetCode 3826 - Minimum Partition Score
// https://leetcode.com/problems/minimum-partition-score/

class Solution {
    private var prefix = [Int]()
    private var previous = [Int]()
    private var current = [Int]()
    private let INF = 1 << 62

    func minPartitionScore(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        prefix = [Int](repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + nums[i] }
        previous = [Int](repeating: INF, count: n + 1)
        previous[0] = 0
        for parts in 1...k {
            current = [Int](repeating: INF, count: n + 1)
            compute(parts, n, parts - 1, n - 1)
            previous = current
        }
        return previous[n]
    }

    private func value(_ left: Int, _ right: Int) -> Int {
        let sum = prefix[right] - prefix[left]
        return sum * (sum + 1) / 2
    }

    private func compute(_ lo: Int, _ hi: Int, _ optLo: Int, _ optHi: Int) {
        if lo > hi { return }
        let mid = (lo + hi) / 2
        var bestIndex = -1
        let end = min(optHi, mid - 1)
        if optLo <= end {
            for split in optLo...end {
                if previous[split] == INF { continue }
                let candidate = previous[split] + value(split, mid)
                if candidate < current[mid] {
                    current[mid] = candidate
                    bestIndex = split
                }
            }
        }
        if bestIndex == -1 { bestIndex = optLo }
        compute(lo, mid - 1, optLo, bestIndex)
        compute(mid + 1, hi, bestIndex, optHi)
    }
}
""")

write("3827_count_monobit_integers", """// LeetCode 3827 - Count Monobit Integers
// https://leetcode.com/problems/count-monobit-integers/

class Solution {
    func countMonobit(_ n: Int) -> Int {
        var ans = 1
        var i = 1, x = 1
        while x <= n {
            ans += 1
            x += (1 << i)
            i += 1
        }
        return ans
    }
}
""")

write("3828_final_element_after_subarray_deletions", """// LeetCode 3828 - Final Element After Subarray Deletions
// https://leetcode.com/problems/final-element-after-subarray-deletions/

class Solution {
    func finalElement(_ nums: [Int]) -> Int {
        return max(nums[0], nums[nums.count - 1])
    }
}
""")

write("3829_design_ride_sharing_system", """// LeetCode 3829 - Design Ride Sharing System
// https://leetcode.com/problems/design-ride-sharing-system/

class RideSharingSystem {
    private var t = 0
    private var riders = [(Int, Int)]()
    private var drivers = [(Int, Int)]()
    private var d = [Int: Int]()

    init() {}

    func addRider(_ riderId: Int) {
        d[riderId] = t
        riders.append((t, riderId))
        t += 1
    }

    func addDriver(_ driverId: Int) {
        drivers.append((t, driverId))
        t += 1
    }

    func matchDriverWithRider() -> [Int] {
        riders = riders.filter { d[$0.1] == $0.0 }
        if riders.isEmpty || drivers.isEmpty { return [-1, -1] }
        riders.sort { $0.0 < $1.0 }
        drivers.sort { $0.0 < $1.0 }
        let driver = drivers.removeFirst()
        let rider = riders.removeFirst()
        d.removeValue(forKey: rider.1)
        return [driver.1, rider.1]
    }

    func cancelRider(_ riderId: Int) {
        d.removeValue(forKey: riderId)
    }
}
""")

write("3830_longest_alternating_subarray_after_removing_at_most_one_element", """// LeetCode 3830 - Longest Alternating Subarray After Removing At Most One Element
// https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/

class Solution {
    func longestAlternating(_ nums: [Int]) -> Int {
        let n = nums.count
        var l1 = [Int](repeating: 1, count: n)
        var l2 = [Int](repeating: 1, count: n)
        var r1 = [Int](repeating: 1, count: n)
        var r2 = [Int](repeating: 1, count: n)
        var ans = 0
        if n > 1 {
            for i in 1..<n {
                if nums[i - 1] < nums[i] { l1[i] = l2[i - 1] + 1 }
                else if nums[i - 1] > nums[i] { l2[i] = l1[i - 1] + 1 }
                ans = max(ans, max(l1[i], l2[i]))
            }
            for i in stride(from: n - 2, through: 0, by: -1) {
                if nums[i + 1] > nums[i] { r1[i] = r2[i + 1] + 1 }
                else if nums[i + 1] < nums[i] { r2[i] = r1[i + 1] + 1 }
            }
        }
        if n > 2 {
            for i in 1..<(n - 1) {
                if nums[i - 1] < nums[i + 1] { ans = max(ans, l2[i - 1] + r2[i + 1]) }
                else if nums[i - 1] > nums[i + 1] { ans = max(ans, l1[i - 1] + r1[i + 1]) }
            }
        }
        return ans
    }
}
""")

write("3831_median_of_a_binary_search_tree_level", """// LeetCode 3831 - Median Of A Binary Search Tree Level
// https://leetcode.com/problems/median-of-a-binary-search-tree-level/
""" + TREE + """
class Solution {
    private var nums = [Int]()

    func levelMedian(_ root: TreeNode?, _ level: Int) -> Int {
        nums = []
        dfs(root, 0, level)
        if nums.isEmpty { return -1 }
        return nums[nums.count / 2]
    }

    private func dfs(_ node: TreeNode?, _ i: Int, _ level: Int) {
        guard let node = node else { return }
        dfs(node.left, i + 1, level)
        if i == level { nums.append(node.val) }
        dfs(node.right, i + 1, level)
    }
}
""")

write("3833_count_dominant_indices", """// LeetCode 3833 - Count Dominant Indices
// https://leetcode.com/problems/count-dominant-indices/

class Solution {
    func dominantIndices(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0, suf = nums[n - 1]
        if n >= 2 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                if nums[i] * (n - i - 1) > suf { ans += 1 }
                suf += nums[i]
            }
        }
        return ans
    }
}
""")

write("3834_merge_adjacent_equal_elements", """// LeetCode 3834 - Merge Adjacent Equal Elements
// https://leetcode.com/problems/merge-adjacent-equal-elements/

class Solution {
    func mergeAdjacent(_ nums: [Int]) -> [Int] {
        var stk = [Int]()
        for x in nums {
            stk.append(x)
            while stk.count > 1 && stk[stk.count - 1] == stk[stk.count - 2] {
                let a = stk.removeLast()
                let b = stk.removeLast()
                stk.append(a + b)
            }
        }
        return stk
    }
}
""")

write("3835_count_subarrays_with_cost_less_than_or_equal_to_k", """// LeetCode 3835 - Count Subarrays With Cost Less Than Or Equal To K
// https://leetcode.com/problems/count-subarrays-with-cost-less-than-or-equal-to-k/

class Solution {
    func countSubarrays(_ nums: [Int], _ k: Int) -> Int {
        var ans = 0
        var q1 = [Int]()
        var q2 = [Int]()
        var l = 0
        for r in 0..<nums.count {
            let x = nums[r]
            while !q1.isEmpty && nums[q1.last!] <= x { q1.removeLast() }
            while !q2.isEmpty && nums[q2.last!] >= x { q2.removeLast() }
            q1.append(r)
            q2.append(r)
            while l < r && (nums[q1[0]] - nums[q2[0]]) * (r - l + 1) > k {
                l += 1
                if q1[0] < l { q1.removeFirst() }
                if q2[0] < l { q2.removeFirst() }
            }
            ans += r - l + 1
        }
        return ans
    }
}
""")

write("3836_maximum_score_using_exactly_k_pairs", """// LeetCode 3836 - Maximum Score Using Exactly K Pairs
// https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/

class Solution {
    func maxScore(_ nums1: [Int], _ nums2: [Int], _ K: Int) -> Int {
        let n = nums1.count, m = nums2.count
        let NEG = Int.min / 4
        var f = Array(repeating: Array(repeating: [Int](repeating: NEG, count: K + 1), count: m + 1), count: n + 1)
        f[0][0][0] = 0
        for i in 0...n {
            for j in 0...m {
                for k in 0...K {
                    if i > 0 { f[i][j][k] = max(f[i][j][k], f[i - 1][j][k]) }
                    if j > 0 { f[i][j][k] = max(f[i][j][k], f[i][j - 1][k]) }
                    if i > 0 && j > 0 && k > 0 {
                        f[i][j][k] = max(f[i][j][k], f[i - 1][j - 1][k - 1] + nums1[i - 1] * nums2[j - 1])
                    }
                }
            }
        }
        return f[n][m][K]
    }
}
""")

write("3837_delayed_count_of_equal_elements", """// LeetCode 3837 - Delayed Count Of Equal Elements
// https://leetcode.com/problems/delayed-count-of-equal-elements/

class Solution {
    func delayedCount(_ nums: [Int], _ k: Int) -> [Int] {
        let n = nums.count
        var cnt = [Int: Int]()
        var ans = [Int](repeating: 0, count: n)
        let start = n - k - 2
        if start >= 0 {
            for i in stride(from: start, through: 0, by: -1) {
                let key = nums[i + k + 1]
                cnt[key, default: 0] += 1
                ans[i] = cnt[nums[i], default: 0]
            }
        }
        return ans
    }
}
""")

write("3838_weighted_word_mapping", """// LeetCode 3838 - Weighted Word Mapping
// https://leetcode.com/problems/weighted-word-mapping/

class Solution {
    func mapWordWeights(_ words: [String], _ weights: [Int]) -> String {
        var ans = ""
        for w in words {
            var s = 0
            for c in w { s = (s + weights[Int(c.asciiValue! - 97)]) % 26 }
            ans.append(Character(UnicodeScalar(97 + (25 - s))!))
        }
        return ans
    }
}
""")

write("3839_number_of_prefix_connected_groups", """// LeetCode 3839 - Number Of Prefix Connected Groups
// https://leetcode.com/problems/number-of-prefix-connected-groups/

class Solution {
    func prefixConnected(_ words: [String], _ k: Int) -> Int {
        var cnt = [String: Int]()
        for w in words {
            if w.count >= k {
                let p = String(w.prefix(k))
                cnt[p, default: 0] += 1
            }
        }
        var ans = 0
        for v in cnt.values where v > 1 { ans += 1 }
        return ans
    }
}
""")

write("3840_house_robber_v", """// LeetCode 3840 - House Robber V
// https://leetcode.com/problems/house-robber-v/

class Solution {
    func rob(_ nums: [Int], _ colors: [Int]) -> Int {
        let n = nums.count
        var f = 0, g = nums[0]
        if n > 1 {
            for i in 1..<n {
                if colors[i - 1] == colors[i] {
                    let nf = max(f, g)
                    g = f + nums[i]
                    f = nf
                } else {
                    let nf = max(f, g)
                    g = nf + nums[i]
                    f = nf
                }
            }
        }
        return max(f, g)
    }
}
""")

write("3841_palindromic_path_queries_in_a_tree", """// LeetCode 3841 - Palindromic Path Queries in a Tree
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

class Solution {
    private var bit = [Int]()
    private var n = 0
    private var parent = [Int]()
    private var depth = [Int]()
    private var size = [Int]()
    private var heavy = [Int]()
    private var head = [Int]()
    private var position = [Int]()
    private var graph = [[Int]]()

    func palindromicPathQueries(_ n: Int, _ edges: [[Int]], _ s: String, _ queries: [String]) -> [Bool] {
        self.n = n
        graph = [[Int]](repeating: [], count: n)
        for edge in edges {
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        }
        parent = [Int](repeating: -2, count: n)
        depth = [Int](repeating: 0, count: n)
        parent[0] = -1
        var order = [0]
        var i = 0
        while i < order.count {
            let u = order[i]
            for v in graph[u] {
                if parent[v] == -2 {
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)
                }
            }
            i += 1
        }
        size = [Int](repeating: 0, count: n)
        heavy = [Int](repeating: -1, count: n)
        for i in stride(from: n - 1, through: 0, by: -1) {
            let u = order[i]
            size[u] = 1
            for v in graph[u] {
                if parent[v] == u {
                    size[u] += size[v]
                    if heavy[u] == -1 || size[v] > size[heavy[u]] { heavy[u] = v }
                }
            }
        }
        head = [Int](repeating: 0, count: n)
        position = [Int](repeating: 0, count: n)
        var stack = [[0, 0]]
        var nextPosition = 0
        while !stack.isEmpty {
            let chain = stack.removeLast()
            var u = chain[0]
            while u != -1 {
                head[u] = chain[1]
                position[u] = nextPosition
                nextPosition += 1
                for v in graph[u] {
                    if parent[v] == u && v != heavy[u] { stack.append([v, v]) }
                }
                u = heavy[u]
            }
        }
        bit = [Int](repeating: 0, count: n + 1)
        var current = Array(s)
        for node in 0..<n {
            update(position[node], 1 << Int(current[node].asciiValue! - 97))
        }
        var answer = [Bool]()
        for query in queries {
            let parts = query.split(separator: " ").map(String.init)
            let op = parts[0]
            let node = Int(parts[1])!
            if op == "update" {
                let newCharacter = parts[2].first!
                let delta = (1 << Int(current[node].asciiValue! - 97)) ^ (1 << Int(newCharacter.asciiValue! - 97))
                update(position[node], delta)
                current[node] = newCharacter
            } else {
                let other = Int(parts[2])!
                let mask = pathMask(node, other)
                answer.append((mask & (mask - 1)) == 0)
            }
        }
        return answer
    }

    private func update(_ index: Int, _ value: Int) {
        var index = index + 1
        while index <= n {
            bit[index] ^= value
            index += index & -index
        }
    }

    private func prefix(_ index: Int) -> Int {
        var index = index, result = 0
        while index > 0 {
            result ^= bit[index]
            index -= index & -index
        }
        return result
    }

    private func pathMask(_ u: Int, _ v: Int) -> Int {
        var u = u, v = v, result = 0
        while head[u] != head[v] {
            if depth[head[u]] < depth[head[v]] { swap(&u, &v) }
            result ^= prefix(position[u] + 1) ^ prefix(position[head[u]])
            u = parent[head[u]]
        }
        if position[u] > position[v] { swap(&u, &v) }
        return result ^ prefix(position[v] + 1) ^ prefix(position[u])
    }
}
""")

write("3842_toggle_light_bulbs", """// LeetCode 3842 - Toggle Light Bulbs
// https://leetcode.com/problems/toggle-light-bulbs/

class Solution {
    func toggleLightBulbs(_ bulbs: [Int]) -> [Int] {
        var st = [Int](repeating: 0, count: 101)
        for x in bulbs { st[x] ^= 1 }
        var ans = [Int]()
        for i in 0..<101 where st[i] == 1 { ans.append(i) }
        return ans
    }
}
""")
