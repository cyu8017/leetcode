#!/usr/bin/env python3
"""Write Solution.swift for LeetCode 1801-1850 (non-SQL)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SOLUTIONS: dict[str, str] = {}

SOLUTIONS["1801_number_of_orders_in_the_backlog"] = r'''// LeetCode 1801 - Number of Orders in the Backlog
// https://leetcode.com/problems/number-of-orders-in-the-backlog/

class Solution {
    func getNumberOfBacklogOrders(_ orders: [[Int]]) -> Int {
        let mod = 1_000_000_007
        var buy: [(Int, Int)] = []
        var sell: [(Int, Int)] = []

        func pushBuy(_ price: Int, _ amount: Int) {
            buy.append((price, amount))
            var i = buy.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if buy[p].0 >= buy[i].0 { break }
                buy.swapAt(p, i)
                i = p
            }
        }
        func popBuy() -> (Int, Int) {
            let top = buy[0]
            let last = buy.removeLast()
            if !buy.isEmpty {
                buy[0] = last
                var i = 0
                while true {
                    var largest = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < buy.count && buy[l].0 > buy[largest].0 { largest = l }
                    if r < buy.count && buy[r].0 > buy[largest].0 { largest = r }
                    if largest == i { break }
                    buy.swapAt(i, largest)
                    i = largest
                }
            }
            return top
        }
        func pushSell(_ price: Int, _ amount: Int) {
            sell.append((price, amount))
            var i = sell.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if sell[p].0 <= sell[i].0 { break }
                sell.swapAt(p, i)
                i = p
            }
        }
        func popSell() -> (Int, Int) {
            let top = sell[0]
            let last = sell.removeLast()
            if !sell.isEmpty {
                sell[0] = last
                var i = 0
                while true {
                    var smallest = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < sell.count && sell[l].0 < sell[smallest].0 { smallest = l }
                    if r < sell.count && sell[r].0 < sell[smallest].0 { smallest = r }
                    if smallest == i { break }
                    sell.swapAt(i, smallest)
                    i = smallest
                }
            }
            return top
        }

        for order in orders {
            let price = order[0]
            let amount = order[1]
            let orderType = order[2]
            if orderType == 0 {
                pushBuy(price, amount)
            } else {
                pushSell(price, amount)
            }
            while !buy.isEmpty && !sell.isEmpty && buy[0].0 >= sell[0].0 {
                let (bp, ba) = popBuy()
                let (sp, sa) = popSell()
                let matched = min(ba, sa)
                let buyLeft = ba - matched
                let sellLeft = sa - matched
                if buyLeft > 0 { pushBuy(bp, buyLeft) }
                if sellLeft > 0 { pushSell(sp, sellLeft) }
            }
        }

        var total = 0
        for (_, amount) in buy { total = (total + amount) % mod }
        for (_, amount) in sell { total = (total + amount) % mod }
        return total
    }
}
'''

SOLUTIONS["1802_maximum_value_at_a_given_index_in_a_bounded_array"] = r'''// LeetCode 1802 - Maximum Value at a Given Index in a Bounded Array
// https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

class Solution {
    func maxValue(_ n: Int, _ index: Int, _ maxSum: Int) -> Int {
        func minSideSum(_ value: Int, _ count: Int) -> Int {
            if value > count {
                return (value - 1 + value - count) * count / 2
            }
            return value * (value - 1) / 2 + (count - value + 1)
        }

        var lo = 1
        var hi = maxSum
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            let total = minSideSum(mid, index) + mid + minSideSum(mid, n - index - 1)
            if total <= maxSum {
                lo = mid
            } else {
                hi = mid - 1
            }
        }
        return lo
    }
}
'''

SOLUTIONS["1803_count_pairs_with_xor_in_a_range"] = r'''// LeetCode 1803 - Count Pairs With XOR in a Range
// https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

private class XORTrieNode {
    var count = 0
    var children: [XORTrieNode?] = [nil, nil]
}

class Solution {
    func countPairs(_ nums: [Int], _ low: Int, _ high: Int) -> Int {
        return countSmallerThan(nums, high + 1) - countSmallerThan(nums, low)
    }

    private func countSmallerThan(_ nums: [Int], _ limit: Int) -> Int {
        if limit <= 0 { return 0 }
        let root = XORTrieNode()
        var total = 0
        let maxBit = 15
        for num in nums {
            total += query(root, num, limit, maxBit)
            insert(root, num, maxBit)
        }
        return total
    }

    private func insert(_ root: XORTrieNode, _ num: Int, _ bit: Int) {
        var node = root
        var i = bit
        while i >= 0 {
            let b = (num >> i) & 1
            if node.children[b] == nil {
                node.children[b] = XORTrieNode()
            }
            node = node.children[b]!
            node.count += 1
            i -= 1
        }
    }

    private func query(_ root: XORTrieNode?, _ num: Int, _ limit: Int, _ bit: Int) -> Int {
        guard let root = root, bit >= 0 else { return 0 }
        let numBit = (num >> bit) & 1
        let limitBit = (limit >> bit) & 1
        let child = root.children[numBit]
        if limitBit == 1 {
            let same = child?.count ?? 0
            return same + query(root.children[1 - numBit], num, limit, bit - 1)
        }
        return query(child, num, limit, bit - 1)
    }
}
'''

SOLUTIONS["1804_implement_trie_ii_prefix_tree"] = r'''// LeetCode 1804 - Implement Trie II (Prefix Tree)
// https://leetcode.com/problems/implement-trie-ii-prefix-tree/

private class TrieIINode {
    var children = [Character: TrieIINode]()
    var wordCount = 0
    var prefixCount = 0
}

class Trie {
    private let root = TrieIINode()

    func insert(_ word: String) {
        var node = root
        for ch in word {
            if node.children[ch] == nil {
                node.children[ch] = TrieIINode()
            }
            node = node.children[ch]!
            node.prefixCount += 1
        }
        node.wordCount += 1
    }

    func countWordsEqualTo(_ word: String) -> Int {
        return find(word)?.wordCount ?? 0
    }

    func countWordsStartingWith(_ prefix: String) -> Int {
        return find(prefix)?.prefixCount ?? 0
    }

    func erase(_ word: String) {
        var node = root
        for ch in word {
            node = node.children[ch]!
            node.prefixCount -= 1
        }
        node.wordCount -= 1
    }

    private func find(_ text: String) -> TrieIINode? {
        var node = root
        for ch in text {
            guard let next = node.children[ch] else { return nil }
            node = next
        }
        return node
    }
}
'''

SOLUTIONS["1805_number_of_different_integers_in_a_string"] = r'''// LeetCode 1805 - Number of Different Integers in a String
// https://leetcode.com/problems/number-of-different-integers-in-a-string/

class Solution {
    func numDifferentIntegers(_ word: String) -> Int {
        var seen = Set<String>()
        var current = ""
        for ch in word {
            if ch.isNumber {
                current.append(ch)
            } else if !current.isEmpty {
                seen.insert(normalize(current))
                current = ""
            }
        }
        if !current.isEmpty {
            seen.insert(normalize(current))
        }
        return seen.count
    }

    private func normalize(_ s: String) -> String {
        var i = s.startIndex
        while i < s.endIndex && s[i] == "0" {
            i = s.index(after: i)
        }
        if i == s.endIndex { return "0" }
        return String(s[i...])
    }
}
'''

SOLUTIONS["1806_minimum_number_of_operations_to_reinitialize_a_permutation"] = r'''// LeetCode 1806 - Minimum Number of Operations to Reinitialize a Permutation
// https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

class Solution {
    func reinitializePermutation(_ n: Int) -> Int {
        var perm = Array(0..<n)
        let target = perm
        var operations = 0
        while true {
            var newPerm = Array(repeating: 0, count: n)
            for i in 0..<n {
                if i % 2 == 0 {
                    newPerm[i] = perm[i / 2]
                } else {
                    newPerm[i] = perm[n / 2 + (i - 1) / 2]
                }
            }
            perm = newPerm
            operations += 1
            if perm == target {
                return operations
            }
        }
    }
}
'''

SOLUTIONS["1807_evaluate_the_bracket_pairs_of_a_string"] = r'''// LeetCode 1807 - Evaluate the Bracket Pairs of a String
// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

class Solution {
    func evaluate(_ s: String, _ knowledge: [[String]]) -> String {
        var lookup = [String: String]()
        for pair in knowledge {
            lookup[pair[0]] = pair[1]
        }
        var result = ""
        let chars = Array(s)
        var i = 0
        while i < chars.count {
            if chars[i] == "(" {
                var j = i + 1
                while chars[j] != ")" { j += 1 }
                let key = String(chars[(i + 1)..<j])
                result += lookup[key] ?? "?"
                i = j + 1
            } else {
                result.append(chars[i])
                i += 1
            }
        }
        return result
    }
}
'''

SOLUTIONS["1808_maximize_number_of_nice_divisors"] = r'''// LeetCode 1808 - Maximize Number of Nice Divisors
// https://leetcode.com/problems/maximize-number-of-nice-divisors/

class Solution {
    func maxNiceDivisors(_ primeFactors: Int) -> Int {
        let mod = 1_000_000_007
        if primeFactors <= 3 { return primeFactors }
        if primeFactors % 3 == 0 {
            return modPow(3, primeFactors / 3, mod)
        }
        if primeFactors % 3 == 1 {
            return Int((Int64(modPow(3, primeFactors / 3 - 1, mod)) * 4) % Int64(mod))
        }
        return Int((Int64(modPow(3, primeFactors / 3, mod)) * 2) % Int64(mod))
    }

    private func modPow(_ base: Int, _ exp: Int, _ mod: Int) -> Int {
        var b = Int64(base % mod)
        var e = exp
        var res: Int64 = 1
        let m = Int64(mod)
        while e > 0 {
            if e & 1 == 1 { res = res * b % m }
            b = b * b % m
            e >>= 1
        }
        return Int(res)
    }
}
'''

SOLUTIONS["1810_minimum_path_cost_in_a_hidden_grid"] = r'''// LeetCode 1810 - Minimum Path Cost in a Hidden Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/

class Solution {
    // Test harness passes the revealed grid plus start/target coordinates.
    func findShortestPath(_ grid: [[Int]], _ r1: Int, _ c1: Int, _ r2: Int, _ c2: Int) -> Int {
        if r1 == r2 && c1 == c2 { return 0 }
        let m = grid.count
        let n = grid[0].count
        let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        var dist = Array(repeating: Array(repeating: Int.max, count: n), count: m)
        var heap: [(Int, Int, Int)] = [(0, r1, c1)]
        dist[r1][c1] = 0

        func push(_ item: (Int, Int, Int)) {
            heap.append(item)
            var i = heap.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if heap[p].0 <= heap[i].0 { break }
                heap.swapAt(p, i)
                i = p
            }
        }
        func pop() -> (Int, Int, Int) {
            let top = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                var i = 0
                while true {
                    var smallest = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < heap.count && heap[l].0 < heap[smallest].0 { smallest = l }
                    if r < heap.count && heap[r].0 < heap[smallest].0 { smallest = r }
                    if smallest == i { break }
                    heap.swapAt(i, smallest)
                    i = smallest
                }
            }
            return top
        }

        while !heap.isEmpty {
            let (d, r, c) = pop()
            if r == r2 && c == c2 { return d }
            if d > dist[r][c] { continue }
            for (dr, dc) in dirs {
                let nr = r + dr
                let nc = c + dc
                if nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 0 { continue }
                let nd = d + grid[nr][nc]
                if nd < dist[nr][nc] {
                    dist[nr][nc] = nd
                    push((nd, nr, nc))
                }
            }
        }
        return -1
    }
}
'''

SOLUTIONS["1812_determine_color_of_a_chessboard_square"] = r'''// LeetCode 1812 - Determine Color of a Chessboard Square
// https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution {
    func squareIsWhite(_ coordinates: String) -> Bool {
        let chars = Array(coordinates)
        let col = Int(chars[0].asciiValue! - Character("a").asciiValue!) + 1
        let row = Int(String(chars[1]))!
        return (col + row) % 2 == 1
    }
}
'''

SOLUTIONS["1813_sentence_similarity_iii"] = r'''// LeetCode 1813 - Sentence Similarity III
// https://leetcode.com/problems/sentence-similarity-iii/

class Solution {
    func areSentencesSimilar(_ sentence1: String, _ sentence2: String) -> Bool {
        let words1 = sentence1.split(separator: " ").map(String.init)
        let words2 = sentence2.split(separator: " ").map(String.init)
        let n1 = words1.count
        let n2 = words2.count
        var i = 0
        while i < n1 && i < n2 && words1[i] == words2[i] {
            i += 1
        }
        if i == n1 || i == n2 { return true }
        var j1 = n1 - 1
        var j2 = n2 - 1
        while j1 >= i && j2 >= i && words1[j1] == words2[j2] {
            j1 -= 1
            j2 -= 1
        }
        return j1 < i || j2 < i
    }
}
'''

SOLUTIONS["1814_count_nice_pairs_in_an_array"] = r'''// LeetCode 1814 - Count Nice Pairs in an Array
// https://leetcode.com/problems/count-nice-pairs-in-an-array/

class Solution {
    func countNicePairs(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        var freq = [Int: Int]()
        var ans = 0
        for num in nums {
            let diff = num - rev(num)
            ans = (ans + (freq[diff] ?? 0)) % mod
            freq[diff, default: 0] += 1
        }
        return ans
    }

    private func rev(_ x: Int) -> Int {
        var n = x
        var r = 0
        while n > 0 {
            r = r * 10 + n % 10
            n /= 10
        }
        return r
    }
}
'''

SOLUTIONS["1815_maximum_number_of_groups_getting_fresh_donuts"] = r'''// LeetCode 1815 - Maximum Number of Groups Getting Fresh Donuts
// https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/

class Solution {
    func maxHappyGroups(_ batchSize: Int, _ groups: [Int]) -> Int {
        var count = Array(repeating: 0, count: batchSize)
        for size in groups {
            count[size % batchSize] += 1
        }
        var memo = [String: Int]()

        func dfs(_ remainder: Int, _ state: inout [Int]) -> Int {
            let key = "\(remainder)|\(state.map(String.init).joined(separator: ","))"
            if let cached = memo[key] { return cached }
            var best = 0
            for mod in 1..<batchSize where state[mod] > 0 {
                state[mod] -= 1
                best = max(best, dfs((remainder + mod) % batchSize, &state))
                state[mod] += 1
            }
            if remainder == 0 { best += 1 }
            memo[key] = best
            return best
        }

        var state = count
        var ans = dfs(0, &state)
        if count[0] > 0 {
            ans += count[0] - 1
        }
        return ans
    }
}
'''

SOLUTIONS["1816_truncate_sentence"] = r'''// LeetCode 1816 - Truncate Sentence
// https://leetcode.com/problems/truncate-sentence/

class Solution {
    func truncateSentence(_ s: String, _ k: Int) -> String {
        return s.split(separator: " ").prefix(k).joined(separator: " ")
    }
}
'''

SOLUTIONS["1817_finding_the_users_active_minutes"] = r'''// LeetCode 1817 - Finding the Users Active Minutes
// https://leetcode.com/problems/finding-the-users-active-minutes/

class Solution {
    func findingUsersActiveMinutes(_ logs: [[Int]], _ k: Int) -> [Int] {
        var userMinutes = [Int: Set<Int>]()
        for log in logs {
            userMinutes[log[0], default: []].insert(log[1])
        }
        var answer = Array(repeating: 0, count: k)
        for minutes in userMinutes.values {
            let uam = minutes.count
            if uam <= k {
                answer[uam - 1] += 1
            }
        }
        return answer
    }
}
'''

SOLUTIONS["1818_minimum_absolute_sum_difference"] = r'''// LeetCode 1818 - Minimum Absolute Sum Difference
// https://leetcode.com/problems/minimum-absolute-sum-difference/

class Solution {
    func minAbsoluteSumDiff(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let mod = 1_000_000_007
        let sortedNums1 = nums1.sorted()
        var total = 0
        for i in 0..<nums1.count {
            total += abs(nums1[i] - nums2[i])
        }
        var bestGain = 0
        for i in 0..<nums2.count {
            let target = nums2[i]
            let current = abs(nums1[i] - target)
            var lo = 0, hi = sortedNums1.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if sortedNums1[mid] < target { lo = mid + 1 } else { hi = mid }
            }
            for j in [lo - 1, lo] where j >= 0 && j < sortedNums1.count {
                bestGain = max(bestGain, current - abs(sortedNums1[j] - target))
            }
        }
        return (total - bestGain) % mod
    }
}
'''

SOLUTIONS["1819_number_of_different_subsequences_gcds"] = r'''// LeetCode 1819 - Number of Different Subsequences GCDs
// https://leetcode.com/problems/number-of-different-subsequences-gcds/

class Solution {
    func countDifferentSubsequenceGCDs(_ nums: [Int]) -> Int {
        let maxVal = nums.max()!
        var present = Array(repeating: false, count: maxVal + 1)
        for num in nums { present[num] = true }

        func gcd(_ a: Int, _ b: Int) -> Int {
            var x = a, y = b
            while y != 0 {
                let t = x % y
                x = y
                y = t
            }
            return x
        }

        var ans = 0
        for g in 1...maxVal {
            var has = false
            var gcdVal = 0
            var multiple = g
            while multiple <= maxVal {
                if present[multiple] {
                    has = true
                    gcdVal = gcd(gcdVal, multiple / g)
                    if gcdVal == 1 { break }
                }
                multiple += g
            }
            if has && gcdVal == 1 { ans += 1 }
        }
        return ans
    }
}
'''

SOLUTIONS["1820_maximum_number_of_accepted_invitations"] = r'''// LeetCode 1820 - Maximum Number of Accepted Invitations
// https://leetcode.com/problems/maximum-number-of-accepted-invitations/

class Solution {
    func maximumInvitations(_ grid: [[Int]]) -> Int {
        let boys = grid.count
        let girls = grid[0].count
        var matchGirl = Array(repeating: -1, count: girls)

        func dfs(_ boy: Int, _ seen: inout [Bool]) -> Bool {
            for girl in 0..<girls where grid[boy][girl] == 1 && !seen[girl] {
                seen[girl] = true
                if matchGirl[girl] == -1 || dfs(matchGirl[girl], &seen) {
                    matchGirl[girl] = boy
                    return true
                }
            }
            return false
        }

        var ans = 0
        for boy in 0..<boys {
            var seen = Array(repeating: false, count: girls)
            if dfs(boy, &seen) { ans += 1 }
        }
        return ans
    }
}
'''

SOLUTIONS["1822_sign_of_the_product_of_an_array"] = r'''// LeetCode 1822 - Sign of the Product of an Array
// https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution {
    func arraySign(_ nums: [Int]) -> Int {
        var sign = 1
        for num in nums {
            if num == 0 { return 0 }
            if num < 0 { sign = -sign }
        }
        return sign
    }
}
'''

SOLUTIONS["1823_find_the_winner_of_the_circular_game"] = r'''// LeetCode 1823 - Find the Winner of the Circular Game
// https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution {
    func findTheWinner(_ n: Int, _ k: Int) -> Int {
        var pos = 0
        if n >= 2 {
            for size in 2...n {
                pos = (pos + k) % size
            }
        }
        return pos + 1
    }
}
'''

SOLUTIONS["1824_minimum_sideway_jumps"] = r'''// LeetCode 1824 - Minimum Sideway Jumps
// https://leetcode.com/problems/minimum-sideway-jumps/

class Solution {
    func minSideJumps(_ obstacles: [Int]) -> Int {
        let inf = Int.max / 4
        var dp = [1, 0, 1]
        for obs in obstacles {
            let blocked = (0..<3).map { obs == $0 + 1 }
            var ndp = [inf, inf, inf]
            for lane in 0..<3 where !blocked[lane] {
                for other in 0..<3 where !blocked[other] && dp[other] != inf {
                    ndp[lane] = min(ndp[lane], dp[other] + (lane != other ? 1 : 0))
                }
            }
            dp = ndp
        }
        return dp.min()!
    }
}
'''

SOLUTIONS["1825_finding_mk_average"] = r'''// LeetCode 1825 - Finding MK Average
// https://leetcode.com/problems/finding-mk-average/

class MKAverage {
    private let m: Int
    private let k: Int
    private var stream = [Int]()

    init(_ m: Int, _ k: Int) {
        self.m = m
        self.k = k
    }

    func addElement(_ num: Int) {
        stream.append(num)
    }

    func calculateMKAverage() -> Int {
        if stream.count < m { return -1 }
        let window = Array(stream.suffix(m)).sorted()
        let middle = window[k..<(window.count - k)]
        return middle.reduce(0, +) / middle.count
    }
}
'''

SOLUTIONS["1826_faulty_sensor"] = r'''// LeetCode 1826 - Faulty Sensor
// https://leetcode.com/problems/faulty-sensor/

class Solution {
    func badSensor(_ sensor1: [Int], _ sensor2: [Int]) -> Int {
        if sensor1 == sensor2 { return -1 }

        func isDefective(_ correct: [Int], _ faulty: [Int]) -> Bool {
            let n = correct.count
            var i = 0
            while i < n && correct[i] == faulty[i] { i += 1 }
            if i == n { return false }
            var j = i
            while j < n - 1 && correct[j + 1] == faulty[j] { j += 1 }
            return j == n - 1
        }

        let sensor1Bad = isDefective(sensor2, sensor1)
        let sensor2Bad = isDefective(sensor1, sensor2)
        if sensor1Bad && sensor2Bad { return -1 }
        if sensor1Bad { return 1 }
        if sensor2Bad { return 2 }
        return -1
    }
}
'''

SOLUTIONS["1827_minimum_operations_to_make_the_array_increasing"] = r'''// LeetCode 1827 - Minimum Operations to Make the Array Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var ops = 0
        var prev = nums[0]
        for value in nums.dropFirst() {
            if value <= prev {
                let needed = prev + 1
                ops += needed - value
                prev = needed
            } else {
                prev = value
            }
        }
        return ops
    }
}
'''

SOLUTIONS["1828_queries_on_number_of_points_inside_a_circle"] = r'''// LeetCode 1828 - Queries on Number of Points Inside a Circle
// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

class Solution {
    func countPoints(_ points: [[Int]], _ queries: [[Int]]) -> [Int] {
        var result = [Int]()
        for q in queries {
            let xq = q[0], yq = q[1], r = q[2]
            let radiusSq = r * r
            var count = 0
            for p in points {
                let dx = p[0] - xq
                let dy = p[1] - yq
                if dx * dx + dy * dy <= radiusSq { count += 1 }
            }
            result.append(count)
        }
        return result
    }
}
'''

SOLUTIONS["1829_maximum_xor_for_each_query"] = r'''// LeetCode 1829 - Maximum XOR for Each Query
// https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution {
    func getMaximumXor(_ nums: [Int], _ maximumBit: Int) -> [Int] {
        let limit = (1 << maximumBit) - 1
        var current = 0
        for num in nums { current ^= num }
        var result = [Int]()
        for i in stride(from: nums.count - 1, through: 0, by: -1) {
            result.append(current ^ limit)
            current ^= nums[i]
        }
        return result
    }
}
'''

SOLUTIONS["1830_minimum_number_of_operations_to_make_string_sorted"] = r'''// LeetCode 1830 - Minimum Number of Operations to Make String Sorted
// https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/

class Solution {
    func makeStringSorted(_ s: String) -> Int {
        let mod = 1_000_000_007
        let chars = Array(s)
        let n = chars.count
        var fact = Array(repeating: 1, count: n + 1)
        if n >= 2 {
            for i in 2...n {
                fact[i] = Int((Int64(fact[i - 1]) * Int64(i)) % Int64(mod))
            }
        }
        var invFact = Array(repeating: 1, count: n + 1)
        invFact[n] = modPow(fact[n], mod - 2, mod)
        for i in stride(from: n - 1, through: 0, by: -1) {
            invFact[i] = Int((Int64(invFact[i + 1]) * Int64(i + 1)) % Int64(mod))
        }

        var freq = Array(repeating: 0, count: 26)
        for ch in chars {
            freq[Int(ch.asciiValue! - Character("a").asciiValue!)] += 1
        }

        var ans = 0
        for i in 0..<n {
            let c = Int(chars[i].asciiValue! - Character("a").asciiValue!)
            for smaller in 0..<c where freq[smaller] > 0 {
                freq[smaller] -= 1
                var ways = fact[n - i - 1]
                for count in freq {
                    ways = Int((Int64(ways) * Int64(invFact[count])) % Int64(mod))
                }
                ans = (ans + ways) % mod
                freq[smaller] += 1
            }
            freq[c] -= 1
        }
        return ans
    }

    private func modPow(_ base: Int, _ exp: Int, _ mod: Int) -> Int {
        var b = Int64(base % mod)
        var e = exp
        var res: Int64 = 1
        let m = Int64(mod)
        while e > 0 {
            if e & 1 == 1 { res = res * b % m }
            b = b * b % m
            e >>= 1
        }
        return Int(res)
    }
}
'''

SOLUTIONS["1832_check_if_the_sentence_is_pangram"] = r'''// LeetCode 1832 - Check if the Sentence Is Pangram
// https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution {
    func checkIfPangram(_ sentence: String) -> Bool {
        return Set(sentence).count == 26
    }
}
'''

SOLUTIONS["1833_maximum_ice_cream_bars"] = r'''// LeetCode 1833 - Maximum Ice Cream Bars
// https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution {
    func maxIceCream(_ costs: [Int], _ coins: Int) -> Int {
        var remaining = coins
        var count = 0
        for cost in costs.sorted() {
            if remaining < cost { break }
            remaining -= cost
            count += 1
        }
        return count
    }
}
'''

SOLUTIONS["1834_single_threaded_cpu"] = r'''// LeetCode 1834 - Single-Threaded CPU
// https://leetcode.com/problems/single-threaded-cpu/

class Solution {
    func getOrder(_ tasks: [[Int]]) -> [Int] {
        let n = tasks.count
        var indexed = (0..<n).map { ($0, tasks[$0][0], tasks[$0][1]) }
        indexed.sort { a, b in
            if a.1 != b.1 { return a.1 < b.1 }
            return a.0 < b.0
        }
        var heap: [(Int, Int)] = []
        func push(_ duration: Int, _ idx: Int) {
            heap.append((duration, idx))
            var i = heap.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                let better = heap[i].0 < heap[p].0 || (heap[i].0 == heap[p].0 && heap[i].1 < heap[p].1)
                if !better { break }
                heap.swapAt(p, i)
                i = p
            }
        }
        func pop() -> (Int, Int) {
            let top = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                var i = 0
                while true {
                    var best = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < heap.count {
                        let better = heap[l].0 < heap[best].0 || (heap[l].0 == heap[best].0 && heap[l].1 < heap[best].1)
                        if better { best = l }
                    }
                    if r < heap.count {
                        let better = heap[r].0 < heap[best].0 || (heap[r].0 == heap[best].0 && heap[r].1 < heap[best].1)
                        if better { best = r }
                    }
                    if best == i { break }
                    heap.swapAt(i, best)
                    i = best
                }
            }
            return top
        }

        var i = 0
        var time = 0
        var order = [Int]()
        while i < n || !heap.isEmpty {
            if i < n && heap.isEmpty {
                time = max(time, indexed[i].1)
            }
            while i < n && indexed[i].1 <= time {
                push(indexed[i].2, indexed[i].0)
                i += 1
            }
            let (duration, idx) = pop()
            time += duration
            order.append(idx)
        }
        return order
    }
}
'''

SOLUTIONS["1835_find_xor_sum_of_all_pairs_bitwise_and"] = r'''// LeetCode 1835 - Find XOR Sum of All Pairs Bitwise AND
// https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

class Solution {
    func getXORSum(_ arr1: [Int], _ arr2: [Int]) -> Int {
        let xor1 = arr1.reduce(0, ^)
        let xor2 = arr2.reduce(0, ^)
        return xor1 & xor2
    }
}
'''

SOLUTIONS["1836_remove_duplicates_from_an_unsorted_linked_list"] = r'''// LeetCode 1836 - Remove Duplicates From an Unsorted Linked List
// https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func deleteDuplicatesUnsorted(_ head: ListNode?) -> ListNode? {
        var counts = [Int: Int]()
        var node = head
        while let cur = node {
            counts[cur.val, default: 0] += 1
            node = cur.next
        }
        let dummy = ListNode(0, head)
        var prev: ListNode? = dummy
        node = head
        while let cur = node {
            if counts[cur.val, default: 0] > 1 {
                prev?.next = cur.next
                node = cur.next
            } else {
                prev = cur
                node = cur.next
            }
        }
        return dummy.next
    }
}
'''

SOLUTIONS["1837_sum_of_digits_in_base_k"] = r'''// LeetCode 1837 - Sum of Digits in Base K
// https://leetcode.com/problems/sum-of-digits-in-base-k/

class Solution {
    func sumBase(_ n: Int, _ k: Int) -> Int {
        var value = n
        var total = 0
        while value > 0 {
            total += value % k
            value /= k
        }
        return total
    }
}
'''

SOLUTIONS["1838_frequency_of_the_most_frequent_element"] = r'''// LeetCode 1838 - Frequency of the Most Frequent Element
// https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution {
    func maxFrequency(_ nums: [Int], _ k: Int) -> Int {
        let sorted = nums.sorted()
        var left = 0
        var windowSum = 0
        var best = 0
        for right in 0..<sorted.count {
            let value = sorted[right]
            windowSum += value
            while value * (right - left + 1) - windowSum > k {
                windowSum -= sorted[left]
                left += 1
            }
            best = max(best, right - left + 1)
        }
        return best
    }
}
'''

SOLUTIONS["1839_longest_substring_of_all_vowels_in_order"] = r'''// LeetCode 1839 - Longest Substring Of All Vowels in Order
// https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

class Solution {
    func longestBeautifulSubstring(_ word: String) -> Int {
        let chars = Array(word)
        let vowels = Array("aeiou")
        var best = 0
        for start in 0..<chars.count where chars[start] == "a" {
            var counts = Array(repeating: 0, count: 5)
            for end in start..<chars.count {
                let current = chars[end]
                if end > start && current < chars[end - 1] { break }
                guard let idx = vowels.firstIndex(of: current) else { break }
                counts[idx] += 1
                if idx > 0 && counts[idx - 1] == 0 { break }
                if counts.allSatisfy({ $0 > 0 }) {
                    best = max(best, end - start + 1)
                }
            }
        }
        return best
    }
}
'''

SOLUTIONS["1840_maximum_building_height"] = r'''// LeetCode 1840 - Maximum Building Height
// https://leetcode.com/problems/maximum-building-height/

class Solution {
    func maxBuilding(_ n: Int, _ restrictions: [[Int]]) -> Int {
        var points = [[1, 0]] + restrictions.sorted { $0[0] < $1[0] }
        if points.last![0] != n {
            points.append([n, n - 1])
        }
        for i in 1..<points.count {
            let prevId = points[i - 1][0]
            let prevHeight = points[i - 1][1]
            let currId = points[i][0]
            points[i][1] = min(points[i][1], prevHeight + currId - prevId)
        }
        for i in stride(from: points.count - 2, through: 0, by: -1) {
            let nextId = points[i + 1][0]
            let nextHeight = points[i + 1][1]
            let currId = points[i][0]
            points[i][1] = min(points[i][1], nextHeight + nextId - currId)
        }
        var best = points.map { $0[1] }.max()!
        for i in 0..<(points.count - 1) {
            let id1 = points[i][0], h1 = points[i][1]
            let id2 = points[i + 1][0], h2 = points[i + 1][1]
            best = max(best, (h1 + h2 + id2 - id1) / 2)
        }
        return best
    }
}
'''

SOLUTIONS["1842_next_palindrome_using_same_digits"] = r'''// LeetCode 1842 - Next Palindrome Using Same Digits
// https://leetcode.com/problems/next-palindrome-using-same-digits/

class Solution {
    func nextPalindrome(_ num: String) -> String {
        var nums = Array(num)
        if !nextPermutation(&nums) { return "" }
        let n = nums.count
        for i in 0..<(n / 2) {
            nums[n - i - 1] = nums[i]
        }
        return String(nums)
    }

    private func nextPermutation(_ nums: inout [Character]) -> Bool {
        let n = nums.count / 2
        var i = n - 2
        while i >= 0 && nums[i] >= nums[i + 1] { i -= 1 }
        if i < 0 { return false }
        var j = n - 1
        while nums[j] <= nums[i] { j -= 1 }
        nums.swapAt(i, j)
        nums[(i + 1)..<n].reverse()
        return true
    }
}
'''

SOLUTIONS["1844_replace_all_digits_with_characters"] = r'''// LeetCode 1844 - Replace All Digits with Characters
// https://leetcode.com/problems/replace-all-digits-with-characters/

class Solution {
    func replaceDigits(_ s: String) -> String {
        var chars = Array(s)
        var i = 1
        while i < chars.count {
            let shift = Int(String(chars[i]))!
            let base = chars[i - 1].asciiValue!
            chars[i] = Character(UnicodeScalar(base + UInt8(shift)))
            i += 2
        }
        return String(chars)
    }
}
'''

SOLUTIONS["1845_seat_reservation_manager"] = r'''// LeetCode 1845 - Seat Reservation Manager
// https://leetcode.com/problems/seat-reservation-manager/

class SeatManager {
    private var available: [Int]

    init(_ n: Int) {
        available = Array(1...n)
        for i in stride(from: available.count / 2 - 1, through: 0, by: -1) {
            siftDown(i)
        }
    }

    func reserve() -> Int {
        let top = available[0]
        let last = available.removeLast()
        if !available.isEmpty {
            available[0] = last
            siftDown(0)
        }
        return top
    }

    func unreserve(_ seatNumber: Int) {
        available.append(seatNumber)
        siftUp(available.count - 1)
    }

    private func siftUp(_ index: Int) {
        var i = index
        while i > 0 {
            let p = (i - 1) / 2
            if available[p] <= available[i] { break }
            available.swapAt(p, i)
            i = p
        }
    }

    private func siftDown(_ index: Int) {
        var i = index
        while true {
            var smallest = i
            let l = 2 * i + 1, r = 2 * i + 2
            if l < available.count && available[l] < available[smallest] { smallest = l }
            if r < available.count && available[r] < available[smallest] { smallest = r }
            if smallest == i { break }
            available.swapAt(i, smallest)
            i = smallest
        }
    }
}
'''

SOLUTIONS["1846_maximum_element_after_decreasing_and_rearranging"] = r'''// LeetCode 1846 - Maximum Element After Decreasing and Rearranging
// https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

class Solution {
    func maximumElementAfterDecrementingAndRearranging(_ arr: [Int]) -> Int {
        var nums = arr.sorted()
        nums[0] = 1
        for i in 1..<nums.count {
            nums[i] = min(nums[i], nums[i - 1] + 1)
        }
        return nums.max()!
    }
}
'''

SOLUTIONS["1847_closest_room"] = r'''// LeetCode 1847 - Closest Room
// https://leetcode.com/problems/closest-room/

class Solution {
    func closestRoom(_ rooms: [[Int]], _ queries: [[Int]]) -> [Int] {
        let sortedRooms = rooms.sorted { $0[1] < $1[1] }
        var indexed = queries.enumerated().map { ($0.offset, $0.element[0], $0.element[1]) }
        indexed.sort { $0.2 > $1.2 }
        var availableIds = [Int]()
        var roomIndex = sortedRooms.count - 1
        var answer = Array(repeating: -1, count: queries.count)

        for (queryIndex, preferred, minSize) in indexed {
            while roomIndex >= 0 && sortedRooms[roomIndex][1] >= minSize {
                let roomId = sortedRooms[roomIndex][0]
                var lo = 0, hi = availableIds.count
                while lo < hi {
                    let mid = (lo + hi) / 2
                    if availableIds[mid] < roomId { lo = mid + 1 } else { hi = mid }
                }
                availableIds.insert(roomId, at: lo)
                roomIndex -= 1
            }
            if availableIds.isEmpty { continue }

            var lo = 0, hi = availableIds.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if availableIds[mid] < preferred { lo = mid + 1 } else { hi = mid }
            }
            var bestId = -1
            var bestDist = Int.max
            if lo < availableIds.count {
                let roomId = availableIds[lo]
                let dist = abs(roomId - preferred)
                if dist < bestDist || (dist == bestDist && roomId < bestId) {
                    bestId = roomId
                    bestDist = dist
                }
            }
            if lo > 0 {
                let roomId = availableIds[lo - 1]
                let dist = abs(roomId - preferred)
                if dist < bestDist || (dist == bestDist && roomId < bestId) {
                    bestId = roomId
                }
            }
            answer[queryIndex] = bestId
        }
        return answer
    }
}
'''

SOLUTIONS["1848_minimum_distance_to_the_target_element"] = r'''// LeetCode 1848 - Minimum Distance to the Target Element
// https://leetcode.com/problems/minimum-distance-to-the-target-element/

class Solution {
    func getMinDistance(_ nums: [Int], _ target: Int, _ start: Int) -> Int {
        var best = nums.count
        for (i, value) in nums.enumerated() where value == target {
            best = min(best, abs(i - start))
        }
        return best
    }
}
'''

SOLUTIONS["1849_splitting_a_string_into_descending_consecutive_values"] = r'''// LeetCode 1849 - Splitting a String Into Descending Consecutive Values
// https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution {
    func splitString(_ s: String) -> Bool {
        let chars = Array(s)
        let n = chars.count

        func normalize(_ digits: [Character]) -> String {
            var i = 0
            while i + 1 < digits.count && digits[i] == "0" { i += 1 }
            return String(digits[i...])
        }

        func compare(_ a: String, _ b: String) -> Int {
            if a.count != b.count { return a.count < b.count ? -1 : 1 }
            if a == b { return 0 }
            return a < b ? -1 : 1
        }

        func subtractOne(_ num: String) -> String {
            var digits = Array(num)
            var i = digits.count - 1
            while i >= 0 {
                if digits[i] != "0" {
                    digits[i] = Character(UnicodeScalar(digits[i].asciiValue! - 1))
                    break
                }
                digits[i] = "9"
                i -= 1
            }
            return normalize(digits)
        }

        func dfs(_ index: Int, _ previous: String?, _ parts: Int) -> Bool {
            if index == n { return parts >= 2 }
            var digits = [Character]()
            for end in index..<n {
                digits.append(chars[end])
                let value = normalize(digits)
                if let previous = previous {
                    let target = subtractOne(previous)
                    let cmp = compare(value, target)
                    if cmp == 0 {
                        if dfs(end + 1, value, parts + 1) { return true }
                    } else if cmp > 0 {
                        break
                    }
                } else {
                    if dfs(end + 1, value, parts + 1) { return true }
                }
            }
            return false
        }

        return dfs(0, nil, 0)
    }
}
'''

SOLUTIONS["1850_minimum_adjacent_swaps_to_reach_the_kth_smallest_number"] = r'''// LeetCode 1850 - Minimum Adjacent Swaps to Reach the Kth Smallest Number
// https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

class Solution {
    func getMinSwaps(_ num: String, _ k: Int) -> Int {
        var target = Array(num)
        for _ in 0..<k {
            nextPermutation(&target)
        }
        var source = Array(num)
        var swaps = 0
        for i in 0..<source.count {
            if source[i] == target[i] { continue }
            var j = i
            while source[j] != target[i] { j += 1 }
            while j > i {
                source.swapAt(j, j - 1)
                swaps += 1
                j -= 1
            }
        }
        return swaps
    }

    private func nextPermutation(_ arr: inout [Character]) {
        var i = arr.count - 2
        while i >= 0 && arr[i] >= arr[i + 1] { i -= 1 }
        if i < 0 {
            arr.reverse()
            return
        }
        var j = arr.count - 1
        while arr[j] <= arr[i] { j -= 1 }
        arr.swapAt(i, j)
        arr[(i + 1)...].reverse()
    }
}
'''


def main() -> None:
    written = []
    for folder, content in sorted(SOLUTIONS.items()):
        path = ROOT / folder / "Solution.swift"
        if not path.parent.exists():
            raise SystemExit(f"Missing folder: {folder}")
        path.write_text(content.rstrip() + "\n", encoding="utf-8")
        written.append(folder)
    print(f"Wrote {len(written)} Solution.swift files")
    for f in written:
        print(f"  {f}")


if __name__ == "__main__":
    main()
