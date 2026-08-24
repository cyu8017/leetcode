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


write("3780_maximum_sum_of_three_numbers_divisible_by_three", """// LeetCode 3780 - Maximum Sum Of Three Numbers Divisible By Three
// https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/

class Solution {
    func maximumSum(_ nums: [Int]) -> Int {
        let a = nums.sorted()
        var g = [[Int]](repeating: [], count: 3)
        for x in a { g[x % 3].append(x) }
        var ans = 0
        for aa in 0..<3 {
            if !g[aa].isEmpty {
                let x = g[aa].removeLast()
                for b in 0..<3 {
                    if !g[b].isEmpty {
                        let y = g[b].removeLast()
                        let c = (3 - (aa + b) % 3) % 3
                        if !g[c].isEmpty {
                            let z = g[c][g[c].count - 1]
                            ans = max(ans, x + y + z)
                        }
                        g[b].append(y)
                    }
                }
                g[aa].append(x)
            }
        }
        return ans
    }
}
""")

write("3781_maximum_score_after_binary_swaps", """// LeetCode 3781 - Maximum Score After Binary Swaps
// https://leetcode.com/problems/maximum-score-after-binary-swaps/

class Solution {
    func maximumScore(_ nums: [Int], _ s: String) -> Int {
        let chars = Array(s)
        var ans = 0
        var pq = [Int]()
        for i in 0..<nums.count {
            pq.append(nums[i])
            pq.sort(by: >)
            if chars[i] == "1" {
                ans += pq.removeFirst()
            }
        }
        return ans
    }
}
""")

write("3782_last_remaining_integer_after_alternating_deletion_operations", """// LeetCode 3782 - Last Remaining Integer After Alternating Deletion Operations
// https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/

class Solution {
    func lastRemaining(_ n: Int) -> Int {
        var n = n
        var first = 1, step = 2
        var left = true
        while n > 1 {
            if !left && n % 2 == 0 { first += step }
            n = (n + 1) / 2
            step *= 2
            left = !left
        }
        return first
    }
}
""")

write("3783_mirror_distance_of_an_integer", """// LeetCode 3783 - Mirror Distance Of An Integer
// https://leetcode.com/problems/mirror-distance-of-an-integer/

class Solution {
    func mirrorDistance(_ n: Int) -> Int {
        return abs(n - reverse(n))
    }

    private func reverse(_ x: Int) -> Int {
        var x = x, y = 0
        while x > 0 {
            y = y * 10 + x % 10
            x /= 10
        }
        return y
    }
}
""")

write("3784_minimum_deletion_cost_to_make_all_characters_equal", """// LeetCode 3784 - Minimum Deletion Cost To Make All Characters Equal
// https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/

class Solution {
    func minCost(_ s: String, _ cost: [Int]) -> Int {
        let chars = Array(s)
        var tot = 0
        var g = [Character: Int]()
        for i in 0..<cost.count {
            tot += cost[i]
            g[chars[i], default: 0] += cost[i]
        }
        var ans = tot
        for x in g.values { ans = min(ans, tot - x) }
        return ans
    }
}
""")

write("3785_minimum_swaps_to_avoid_forbidden_values", """// LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
// https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

class Solution {
    func minSwaps(_ nums: [Int], _ forbidden: [Int]) -> Int {
        let n = nums.count
        var freq = [Int: Int]()
        for x in nums { freq[x, default: 0] += 1 }
        for x in forbidden { freq[x, default: 0] += 1 }
        for c in freq.values {
            if c > n { return -1 }
        }
        var bad = [Int: Int]()
        var total = 0, largest = 0
        for i in 0..<n {
            if nums[i] == forbidden[i] {
                bad[nums[i], default: 0] += 1
                total += 1
                if bad[nums[i]]! > largest { largest = bad[nums[i]]! }
            }
        }
        if (total + 1) / 2 > largest { return (total + 1) / 2 }
        return largest
    }
}
""")

write("3786_total_sum_of_interaction_cost_in_tree_groups", """// LeetCode 3786 - Total Sum Of Interaction Cost In Tree Groups
// https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/

class Solution {
    func interactionCost(_ n: Int, _ edges: [[Int]], _ group: [Int]) -> Int {
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var total = [Int](repeating: 0, count: 21)
        for x in group { total[x] += 1 }
        var parent = [Int](repeating: -2, count: n)
        parent[0] = -1
        var order = [0]
        var i = 0
        while i < order.count {
            let u = order[i]
            for v in g[u] {
                if parent[v] == -2 {
                    parent[v] = u
                    order.append(v)
                }
            }
            i += 1
        }
        var count = Array(repeating: [Int](repeating: 0, count: 21), count: n)
        var ans = 0
        for i in stride(from: n - 1, through: 0, by: -1) {
            let u = order[i]
            count[u][group[u]] += 1
            for v in g[u] {
                if parent[v] != u { continue }
                for c in 1...20 {
                    let x = count[v][c]
                    ans += x * (total[c] - x)
                    count[u][c] += x
                }
            }
        }
        return ans
    }
}
""")

write("3787_find_diameter_endpoints_of_a_tree", """// LeetCode 3787 - Find Diameter Endpoints Of A Tree
// https://leetcode.com/problems/find-diameter-endpoints-of-a-tree/

class Solution {
    private var g = [[Int]]()
    private var n = 0

    func findSpecialNodes(_ n: Int, _ edges: [[Int]]) -> String {
        self.n = n
        g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        let r0 = bfs(0)
        let a = r0.0
        let r1 = bfs(a)
        let b = r1.0
        let dist1 = r1.1
        let r2 = bfs(b)
        let dist2 = r2.1
        let d = dist1[b]
        var ans = [Character](repeating: "0", count: n)
        for i in 0..<n {
            if dist1[i] == d || dist2[i] == d { ans[i] = "1" }
        }
        return String(ans)
    }

    private func bfs(_ start: Int) -> (Int, [Int]) {
        var dist = [Int](repeating: -1, count: n)
        dist[start] = 0
        var q = [start]
        var far = start
        var head = 0
        while head < q.count {
            let u = q[head]
            head += 1
            if dist[u] > dist[far] { far = u }
            for v in g[u] {
                if dist[v] == -1 {
                    dist[v] = dist[u] + 1
                    q.append(v)
                }
            }
        }
        return (far, dist)
    }
}
""")

write("3788_maximum_score_of_a_split", """// LeetCode 3788 - Maximum Score Of A Split
// https://leetcode.com/problems/maximum-score-of-a-split/

class Solution {
    func maximumScore(_ nums: [Int]) -> Int {
        let n = nums.count
        var suf = [Int](repeating: 0, count: n)
        suf[n - 1] = nums[n - 1]
        if n >= 2 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                suf[i] = min(nums[i], suf[i + 1])
            }
        }
        var pre = 0
        var ans = Int.min
        for i in 0..<(n - 1) {
            pre += nums[i]
            ans = max(ans, pre - suf[i + 1])
        }
        return ans
    }
}
""")

write("3789_minimum_cost_to_acquire_required_items", """// LeetCode 3789 - Minimum Cost To Acquire Required Items
// https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

class Solution {
    func minimumCost(_ cost1: Int, _ cost2: Int, _ costBoth: Int, _ need1: Int, _ need2: Int) -> Int {
        let a = need1 * cost1 + need2 * cost2
        let b = costBoth * max(need1, need2)
        let mn = min(need1, need2)
        let c = costBoth * mn + (need1 - mn) * cost1 + (need2 - mn) * cost2
        return min(a, min(b, c))
    }
}
""")

write("3790_smallest_all_ones_multiple", """// LeetCode 3790 - Smallest All Ones Multiple
// https://leetcode.com/problems/smallest-all-ones-multiple/

class Solution {
    func minAllOneMultiple(_ k: Int) -> Int {
        if (k & 1) == 0 { return -1 }
        var x = 1 % k
        var ans = 1
        for _ in 0..<k {
            x = (x * 10 + 1) % k
            ans += 1
            if x == 0 { return ans }
        }
        return -1
    }
}
""")

write("3791_number_of_balanced_integers_in_a_range", """// LeetCode 3791 - Number Of Balanced Integers In A Range
// https://leetcode.com/problems/number-of-balanced-integers-in-a-range/

class Solution {
    private let BASE = 90
    private var num = [Character]()
    private var f = Array(repeating: [Int](repeating: -1, count: 181), count: 20)

    private func dfs(_ pos: Int, _ diff: Int, _ lim: Bool) -> Int {
        if pos >= num.count { return diff == 0 ? 1 : 0 }
        if !lim && f[pos][diff + BASE] != -1 { return f[pos][diff + BASE] }
        let up = lim ? Int(num[pos].asciiValue! - 48) : 9
        var res = 0
        for i in 0...up {
            if pos % 2 == 0 { res += dfs(pos + 1, diff + i, lim && i == up) }
            else { res += dfs(pos + 1, diff - i, lim && i == up) }
        }
        if !lim { f[pos][diff + BASE] = res }
        return res
    }

    func countBalanced(_ low: Int, _ high: Int) -> Int {
        if high < 11 { return 0 }
        var low = low
        if low < 11 { low = 11 }
        num = Array(String(low - 1))
        f = Array(repeating: [Int](repeating: -1, count: 181), count: 20)
        let a = dfs(0, 0, true)
        num = Array(String(high))
        f = Array(repeating: [Int](repeating: -1, count: 181), count: 20)
        let b = dfs(0, 0, true)
        return b - a
    }
}
""")

write("3792_sum_of_increasing_product_blocks", """// LeetCode 3792 - Sum Of Increasing Product Blocks
// https://leetcode.com/problems/sum-of-increasing-product-blocks/

class Solution {
    func sumOfBlocks(_ n: Int) -> Int {
        let MOD = 1_000_000_007
        var ans = 0, k = 1
        for i in 1...n {
            var x = 1
            for j in k..<(k + i) { x = x * j % MOD }
            ans = (ans + x) % MOD
            k += i
        }
        return ans
    }
}
""")

write("3794_reverse_string_prefix", """// LeetCode 3794 - Reverse String Prefix
// https://leetcode.com/problems/reverse-string-prefix/

class Solution {
    func reversePrefix(_ s: String, _ k: Int) -> String {
        var arr = Array(s)
        var i = 0, j = k - 1
        while i < j {
            arr.swapAt(i, j)
            i += 1
            j -= 1
        }
        return String(arr)
    }
}
""")

write("3795_minimum_subarray_length_with_distinct_sum_at_least_k", """// LeetCode 3795 - Minimum Subarray Length With Distinct Sum At Least K
// https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k/

class Solution {
    func minLength(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var ans = n + 1, l = 0
        var cnt = [Int: Int]()
        var s = 0
        for r in 0..<n {
            cnt[nums[r], default: 0] += 1
            if cnt[nums[r]] == 1 { s += nums[r] }
            while s >= k {
                if r - l + 1 < ans { ans = r - l + 1 }
                let left = nums[l]
                cnt[left]! -= 1
                if cnt[left] == 0 {
                    cnt.removeValue(forKey: left)
                    s -= left
                }
                l += 1
            }
        }
        return ans > n ? -1 : ans
    }
}
""")

write("3796_find_maximum_value_in_a_constrained_sequence", """// LeetCode 3796 - Find Maximum Value in a Constrained Sequence
// https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

class Solution {
    func maxValue(_ n: Int, _ restrictions: [[Int]], _ diff: [Int]) -> Int {
        let INF = Int.max / 4
        var bound = [Int](repeating: INF, count: n)
        bound[0] = 0
        for r in restrictions { bound[r[0]] = r[1] }
        if n > 1 {
            for i in 1..<n { bound[i] = min(bound[i], bound[i - 1] + diff[i - 1]) }
            for i in stride(from: n - 2, through: 0, by: -1) {
                bound[i] = min(bound[i], bound[i + 1] + diff[i])
            }
        }
        var ans = bound[0]
        if n > 1 {
            for i in 1..<n { ans = max(ans, bound[i]) }
        }
        return ans
    }
}
""")

write("3797_count_routes_to_climb_a_rectangular_grid", """// LeetCode 3797 - Count Routes To Climb A Rectangular Grid
// https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/

class Solution {
    func countRoutes(_ grid: [String], _ d: Int) -> Int {
        let MOD = 1_000_000_007
        let n = grid.count
        let m = grid[0].count
        let rows = grid.map { Array($0) }
        var upRadius = 0
        while (upRadius + 1) * (upRadius + 1) + 1 <= d * d { upRadius += 1 }
        var arrived = [Int](repeating: 0, count: m)
        for c in 0..<m {
            if rows[n - 1][c] == "." { arrived[c] = 1 }
        }
        for r in stride(from: n - 1, through: 0, by: -1) {
            var pref = [Int](repeating: 0, count: m + 1)
            for i in 0..<m { pref[i + 1] = (pref[i] + arrived[i]) % MOD }
            var horizontal = [Int](repeating: 0, count: m)
            for c in 0..<m {
                if rows[r][c] == "#" { continue }
                let l = max(0, c - d), rr = min(m - 1, c + d)
                horizontal[c] = (pref[rr + 1] - pref[l] - arrived[c]) % MOD
                if horizontal[c] < 0 { horizontal[c] += MOD }
            }
            if r == 0 {
                var ans = 0
                for c in 0..<m { ans = (ans + arrived[c] + horizontal[c]) % MOD }
                return ans
            }
            var pref2 = [Int](repeating: 0, count: m + 1)
            for c in 0..<m { pref2[c + 1] = (pref2[c] + arrived[c] + horizontal[c]) % MOD }
            var next = [Int](repeating: 0, count: m)
            for c in 0..<m {
                if rows[r - 1][c] == "#" { continue }
                let l = max(0, c - upRadius), rr = min(m - 1, c + upRadius)
                next[c] = pref2[rr + 1] - pref2[l]
                if next[c] < 0 { next[c] += MOD }
            }
            arrived = next
        }
        return 0
    }
}
""")

write("3798_largest_even_number", """// LeetCode 3798 - Largest Even Number
// https://leetcode.com/problems/largest-even-number/

class Solution {
    func largestEven(_ s: String) -> String {
        var s = s
        while !s.isEmpty && s.last == "1" { s.removeLast() }
        return s
    }
}
""")

write("3799_word_squares_ii", """// LeetCode 3799 - Word Squares II
// https://leetcode.com/problems/word-squares-ii/

class Solution {
    func wordSquares(_ words: [String]) -> [[String]] {
        let words = words.sorted()
        let n = words.count
        var ans = [[String]]()
        for i in 0..<n {
            let top = Array(words[i])
            for j in 0..<n where j != i {
                let left = Array(words[j])
                for k in 0..<n where k != j && k != i {
                    let right = Array(words[k])
                    for h in 0..<n where h != k && h != j && h != i {
                        let bottom = Array(words[h])
                        if top[0] == left[0] && top[3] == right[0] &&
                            bottom[0] == left[3] && bottom[3] == right[3] {
                            ans.append([words[i], words[j], words[k], words[h]])
                        }
                    }
                }
            }
        }
        return ans
    }
}
""")

write("3800_minimum_cost_to_make_two_binary_strings_equal", """// LeetCode 3800 - Minimum Cost To Make Two Binary Strings Equal
// https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

class Solution {
    func minimumCost(_ s: String, _ t: String, _ flipCost: Int, _ swapCost: Int, _ crossCost: Int) -> Int {
        let sc = Array(s), tc = Array(t)
        var diff = [0, 0]
        for i in 0..<sc.count {
            if sc[i] != tc[i] { diff[Int(sc[i].asciiValue! - 48)] += 1 }
        }
        var ans = (diff[0] + diff[1]) * flipCost
        let mx = max(diff[0], diff[1])
        let mn = min(diff[0], diff[1])
        ans = min(ans, mn * swapCost + (mx - mn) * flipCost)
        let avg = (mx + mn) / 2
        ans = min(ans, (avg - mn) * crossCost + avg * swapCost + (mx + mn - avg * 2) * flipCost)
        return ans
    }
}
""")
