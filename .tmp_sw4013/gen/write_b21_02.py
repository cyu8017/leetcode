#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")


def write(folder, content):
    p = ROOT / folder / "Solution.swift"
    text = p.read_text()
    if "func solve()" not in text:
        print("SKIP", folder)
        return
    p.write_text(content)
    print("WROTE", folder)


write("3759_count_elements_with_at_least_k_greater_values", """// LeetCode 3759 - Count Elements With At Least K Greater Values
// https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

class Solution {
    func countElements(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        if k == 0 { return n }
        let a = nums.sorted()
        var ans = 0
        for i in 0..<(n - k) {
            if a[n - k] > a[i] { ans += 1 }
        }
        return ans
    }
}
""")

write("3760_maximum_substrings_with_distinct_start", """// LeetCode 3760 - Maximum Substrings With Distinct Start
// https://leetcode.com/problems/maximum-substrings-with-distinct-start/

class Solution {
    func maxDistinct(_ s: String) -> Int {
        var cnt = [Int](repeating: 0, count: 26)
        var ans = 0
        for c in s {
            let i = Int(c.asciiValue! - 97)
            cnt[i] += 1
            if cnt[i] == 1 { ans += 1 }
        }
        return ans
    }
}
""")

write("3761_minimum_absolute_distance_between_mirror_pairs", """// LeetCode 3761 - Minimum Absolute Distance Between Mirror Pairs
// https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

class Solution {
    func minMirrorPairDistance(_ nums: [Int]) -> Int {
        let n = nums.count
        var pos = [Int: Int]()
        var ans = n + 1
        for i in 0..<n {
            if let p = pos[nums[i]] { ans = min(ans, i - p) }
            pos[reverse(nums[i])] = i
        }
        return ans > n ? -1 : ans
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

write("3762_minimum_operations_to_equalize_subarrays", """// LeetCode 3762 - Minimum Operations To Equalize Subarrays
// https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/

class Solution {
    private class Node {
        var left = 0, right = 0, count = 0
        var sum = 0
        init() {}
        init(_ o: Node) {
            left = o.left; right = o.right; count = o.count; sum = o.sum
        }
    }

    private var nodes = [Node]()

    func minOperations(_ nums: [Int], _ k: Int, _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        var quotient = [Int](repeating: 0, count: n)
        var remainder = [Int](repeating: 0, count: n)
        var values = [Int](repeating: 0, count: n)
        for i in 0..<n {
            quotient[i] = nums[i] / k
            remainder[i] = nums[i] % k
            values[i] = quotient[i]
        }
        values.sort()
        var vu = 1
        if n > 1 {
            for i in 1..<n {
                if values[i] != values[vu - 1] {
                    values[vu] = values[i]
                    vu += 1
                }
            }
        }
        values = Array(values.prefix(vu))

        nodes = [Node()]
        var roots = [Int](repeating: 0, count: n + 1)
        let umax = values.count - 1
        for i in 0..<n {
            let position = lowerBound(values, quotient[i])
            roots[i + 1] = update(roots[i], 0, umax, position, quotient[i])
        }

        var logv = [Int](repeating: 0, count: n + 1)
        if n >= 2 {
            for i in 2...n { logv[i] = logv[i / 2] + 1 }
        }
        let levels = logv[n] + 1
        var minTable = [[Int]](repeating: [], count: levels)
        var maxTable = [[Int]](repeating: [], count: levels)
        minTable[0] = remainder
        maxTable[0] = remainder
        if levels > 1 {
            for level in 1..<levels {
                let length = n - (1 << level) + 1
                minTable[level] = [Int](repeating: 0, count: length)
                maxTable[level] = [Int](repeating: 0, count: length)
                let half = 1 << (level - 1)
                if length > 0 {
                    for i in 0..<length {
                        minTable[level][i] = min(minTable[level - 1][i], minTable[level - 1][i + half])
                        maxTable[level][i] = max(maxTable[level - 1][i], maxTable[level - 1][i + half])
                    }
                }
            }
        }

        var answer = [Int](repeating: 0, count: queries.count)
        for qi in 0..<queries.count {
            let left = queries[qi][0], right = queries[qi][1]
            let length = right - left + 1
            let level = logv[length]
            let offset = right - (1 << level) + 1
            let minR = min(minTable[level][left], minTable[level][offset])
            let maxR = max(maxTable[level][left], maxTable[level][offset])
            if minR != maxR {
                answer[qi] = -1
                continue
            }
            let medianIndex = kth(roots[right + 1], roots[left], 0, umax, (length + 1) / 2)
            let median = values[medianIndex]
            let stats = prefixStats(roots[right + 1], roots[left], 0, umax, medianIndex)
            let leftCount = stats.0
            let leftSum = stats.1
            let totalSum = nodes[roots[right + 1]].sum - nodes[roots[left]].sum
            answer[qi] = median * leftCount - leftSum + (totalSum - leftSum) - median * (length - leftCount)
        }
        return answer
    }

    private func update(_ previous: Int, _ lo: Int, _ hi: Int, _ position: Int, _ value: Int) -> Int {
        let current = nodes.count
        nodes.append(Node(nodes[previous]))
        nodes[current].count += 1
        nodes[current].sum += value
        if lo < hi {
            let mid = (lo + hi) / 2
            if position <= mid {
                nodes[current].left = update(nodes[previous].left, lo, mid, position, value)
            } else {
                nodes[current].right = update(nodes[previous].right, mid + 1, hi, position, value)
            }
        }
        return current
    }

    private func kth(_ rightRoot: Int, _ leftRoot: Int, _ lo: Int, _ hi: Int, _ rank: Int) -> Int {
        if lo == hi { return lo }
        let leftCount = nodes[nodes[rightRoot].left].count - nodes[nodes[leftRoot].left].count
        let mid = (lo + hi) / 2
        if rank <= leftCount { return kth(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, rank) }
        return kth(nodes[rightRoot].right, nodes[leftRoot].right, mid + 1, hi, rank - leftCount)
    }

    private func prefixStats(_ rightRoot: Int, _ leftRoot: Int, _ lo: Int, _ hi: Int, _ end: Int) -> (Int, Int) {
        if end < lo { return (0, 0) }
        if hi <= end {
            return (nodes[rightRoot].count - nodes[leftRoot].count,
                    nodes[rightRoot].sum - nodes[leftRoot].sum)
        }
        let mid = (lo + hi) / 2
        var left = prefixStats(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, end)
        if end > mid {
            let right = prefixStats(nodes[rightRoot].right, nodes[leftRoot].right, mid + 1, hi, end)
            left.0 += right.0
            left.1 += right.1
        }
        return left
    }

    private func lowerBound(_ a: [Int], _ x: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] < x { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }
}
""")

write("3763_maximum_total_sum_with_threshold_constraints", """// LeetCode 3763 - Maximum Total Sum With Threshold Constraints
// https://leetcode.com/problems/maximum-total-sum-with-threshold-constraints/

class Solution {
    func maxSum(_ nums: [Int], _ threshold: [Int]) -> Int {
        let n = nums.count
        var idx = Array(0..<n)
        idx.sort { threshold[$0] < threshold[$1] }
        var tree = [Int]()
        var ans = 0
        var i = 0
        var step = 1
        while true {
            while i < n && threshold[idx[i]] <= step {
                tree.append(nums[idx[i]])
                i += 1
            }
            tree.sort(by: >)
            if tree.isEmpty { break }
            ans += tree.removeFirst()
            step += 1
        }
        return ans
    }
}
""")

write("3765_complete_prime_number", """// LeetCode 3765 - Complete Prime Number
// https://leetcode.com/problems/complete-prime-number/

class Solution {
    private func isPrime(_ x: Int) -> Bool {
        if x < 2 { return false }
        var i = 2
        while i * i <= x {
            if x % i == 0 { return false }
            i += 1
        }
        return true
    }

    func completePrime(_ num: Int) -> Bool {
        let s = Array(String(num))
        var x = 0
        for c in s {
            x = x * 10 + Int(c.asciiValue! - 48)
            if !isPrime(x) { return false }
        }
        x = 0
        var p = 1
        for i in stride(from: s.count - 1, through: 0, by: -1) {
            x = p * Int(s[i].asciiValue! - 48) + x
            p *= 10
            if !isPrime(x) { return false }
        }
        return true
    }
}
""")

write("3766_minimum_operations_to_make_binary_palindrome", """// LeetCode 3766 - Minimum Operations To Make Binary Palindrome
// https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/

class Solution {
    private static let PALS: [Int] = {
        let N = 1 << 14
        var pals = [Int]()
        for i in 0..<N {
            var sb = [Character]()
            var x = i
            if x == 0 {
                sb.append("0")
            } else {
                while x > 0 {
                    sb.append(Character(UnicodeScalar(48 + (x & 1))!))
                    x >>= 1
                }
                sb.reverse()
            }
            if isPalindrome(sb) { pals.append(i) }
        }
        return pals
    }()

    private static func isPalindrome(_ s: [Character]) -> Bool {
        let m = s.count
        for i in 0..<(m / 2) where s[i] != s[m - 1 - i] { return false }
        return true
    }

    func minOperations(_ nums: [Int]) -> [Int] {
        var ans = [Int](repeating: 0, count: nums.count)
        for k in 0..<nums.count {
            let x = nums[k]
            let it = lowerBound(x)
            var t = Int.max
            if it < Solution.PALS.count { t = Solution.PALS[it] - x }
            if it > 0 { t = min(t, x - Solution.PALS[it - 1]) }
            ans[k] = t
        }
        return ans
    }

    private func lowerBound(_ x: Int) -> Int {
        var lo = 0, hi = Solution.PALS.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if Solution.PALS[mid] < x { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }
}
""")

write("3767_maximize_points_after_choosing_k_tasks", """// LeetCode 3767 - Maximize Points After Choosing K Tasks
// https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/

class Solution {
    func maxPoints(_ technique1: [Int], _ technique2: [Int], _ k: Int) -> Int {
        let n = technique1.count
        var idx = Array(0..<n)
        idx.sort { technique1[$0] - technique2[$0] > technique1[$1] - technique2[$1] }
        var ans = 0
        for x in technique2 { ans += x }
        if k > 0 {
            for i in 0..<k {
                let index = idx[i]
                ans -= technique2[index]
                ans += technique1[index]
            }
        }
        if k < n {
            for i in k..<n {
                let index = idx[i]
                if technique1[index] >= technique2[index] {
                    ans -= technique2[index]
                    ans += technique1[index]
                }
            }
        }
        return ans
    }
}
""")

write("3768_minimum_inversion_count_in_subarrays_of_fixed_length", """// LeetCode 3768 - Minimum Inversion Count In Subarrays Of Fixed Length
// https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/

class Solution {
    private var bit = [Int]()

    func minInversionCount(_ nums: [Int], _ k: Int) -> Int {
        var vals = nums.sorted()
        let u = unique(&vals)
        vals = Array(vals.prefix(u))
        bit = [Int](repeating: 0, count: vals.count + 1)
        var rank = [Int](repeating: 0, count: nums.count)
        var inv = 0
        for i in 0..<nums.count {
            rank[i] = lowerBound(vals, nums[i]) + 1
            if i < k {
                inv += i - sum(rank[i])
                add(rank[i], 1)
            }
        }
        var best = inv
        if nums.count > k {
            for r in k..<nums.count {
                let left = rank[r - k]
                inv -= sum(left - 1)
                add(left, -1)
                inv += k - 1 - sum(rank[r])
                add(rank[r], 1)
                if inv < best { best = inv }
            }
        }
        return best
    }

    private func add(_ i: Int, _ delta: Int) {
        var i = i
        while i < bit.count {
            bit[i] += delta
            i += i & -i
        }
    }

    private func sum(_ i: Int) -> Int {
        var i = i, res = 0
        while i > 0 {
            res += bit[i]
            i -= i & -i
        }
        return res
    }

    private func unique(_ a: inout [Int]) -> Int {
        var n = 0
        for i in 0..<a.count {
            if n == 0 || a[i] != a[n - 1] {
                a[n] = a[i]
                n += 1
            }
        }
        return n
    }

    private func lowerBound(_ a: [Int], _ x: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] < x { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }
}
""")

write("3769_sort_integers_by_binary_reflection", """// LeetCode 3769 - Sort Integers By Binary Reflection
// https://leetcode.com/problems/sort-integers-by-binary-reflection/

class Solution {
    func sortByReflection(_ nums: [Int]) -> [Int] {
        return nums.sorted { a, b in
            let fa = f(a), fb = f(b)
            if fa != fb { return fa < fb }
            return a < b
        }
    }

    private func f(_ x: Int) -> Int {
        var x = x, y = 0
        while x != 0 {
            y = (y << 1) | (x & 1)
            x >>= 1
        }
        return y
    }
}
""")

write("3770_largest_prime_from_consecutive_prime_sum", """// LeetCode 3770 - Largest Prime From Consecutive Prime Sum
// https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/

class Solution {
    private static let MX = 500000
    private static let S: [Int] = {
        var isPrime = [Bool](repeating: true, count: MX + 1)
        isPrime[0] = false
        isPrime[1] = false
        var primes = [Int]()
        for i in 2...MX {
            if isPrime[i] {
                primes.append(i)
                if i * i <= MX {
                    var j = i * i
                    while j <= MX {
                        isPrime[j] = false
                        j += i
                    }
                }
            }
        }
        var s = [0]
        var t = 0
        for x in primes {
            t += x
            if t > MX { break }
            if isPrime[t] { s.append(t) }
        }
        return s
    }()

    func largestPrime(_ n: Int) -> Int {
        var lo = 0, hi = Solution.S.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if Solution.S[mid] <= n { lo = mid + 1 }
            else { hi = mid }
        }
        return Solution.S[lo - 1]
    }
}
""")

write("3771_total_score_of_dungeon_runs", """// LeetCode 3771 - Total Score of Dungeon Runs
// https://leetcode.com/problems/total-score-of-dungeon-runs/

class Solution {
    func totalScore(_ hp: Int, _ damage: [Int], _ requirement: [Int]) -> Int {
        let n = damage.count
        var prefix = [Int](repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + damage[i] }
        var answer = n * (n + 1) / 2
        for j in 1...n {
            let threshold = prefix[j] + (requirement[j - 1] - hp)
            var lo = 0, hi = j
            while lo < hi {
                let mid = (lo + hi) / 2
                if prefix[mid] < threshold { lo = mid + 1 }
                else { hi = mid }
            }
            answer -= lo
        }
        return answer
    }
}
""")

write("3772_maximum_subgraph_score_in_a_tree", """// LeetCode 3772 - Maximum Subgraph Score In A Tree
// https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/

class Solution {
    func maxSubgraphScore(_ n: Int, _ edges: [[Int]], _ good: [Int]) -> [Int] {
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
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
        var down = [Int](repeating: 0, count: n)
        for i in stride(from: n - 1, through: 0, by: -1) {
            let u = order[i]
            down[u] = 2 * good[u] - 1
            for v in g[u] {
                if parent[v] == u && down[v] > 0 { down[u] += down[v] }
            }
        }
        var ans = down
        for u in order {
            for v in g[u] {
                if parent[v] == u {
                    var outside = ans[u]
                    if down[v] > 0 { outside -= down[v] }
                    ans[v] = down[v]
                    if outside > 0 { ans[v] += outside }
                }
            }
        }
        return ans
    }
}
""")

write("3773_maximum_number_of_equal_length_runs", """// LeetCode 3773 - Maximum Number Of Equal Length Runs
// https://leetcode.com/problems/maximum-number-of-equal-length-runs/

class Solution {
    func maxSameLengthRuns(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var cnt = [Int: Int]()
        var ans = 0
        var i = 0
        while i < n {
            var j = i + 1
            while j < n && chars[j] == chars[i] { j += 1 }
            let m = j - i
            cnt[m, default: 0] += 1
            ans = max(ans, cnt[m]!)
            i = j
        }
        return ans
    }
}
""")

write("3774_absolute_difference_between_maximum_and_minimum_k_elements", """// LeetCode 3774 - Absolute Difference Between Maximum And Minimum K Elements
// https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

class Solution {
    func absDifference(_ nums: [Int], _ k: Int) -> Int {
        let a = nums.sorted()
        var ans = 0
        let n = a.count
        for i in 0..<k { ans += a[n - i - 1] - a[i] }
        return ans
    }
}
""")

write("3775_reverse_words_with_same_vowel_count", """// LeetCode 3775 - Reverse Words With Same Vowel Count
// https://leetcode.com/problems/reverse-words-with-same-vowel-count/

class Solution {
    private func calc(_ w: String) -> Int {
        var cnt = 0
        for c in w where "aeiou".contains(c) { cnt += 1 }
        return cnt
    }

    func reverseWords(_ s: String) -> String {
        let words = s.split { $0.isWhitespace }.map(String.init)
        let cnt = calc(words[0])
        var ans = words[0]
        if words.count > 1 {
            for i in 1..<words.count {
                var w = words[i]
                if calc(w) == cnt { w = String(w.reversed()) }
                ans += " " + w
            }
        }
        return ans
    }
}
""")

write("3776_minimum_moves_to_balance_circular_array", """// LeetCode 3776 - Minimum Moves To Balance Circular Array
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array/

class Solution {
    func minMoves(_ balance: [Int]) -> Int {
        var sum = 0
        for b in balance { sum += b }
        if sum < 0 { return -1 }

        let n = balance.count
        var mn = balance[0], idx = 0
        if n > 1 {
            for i in 1..<n {
                if balance[i] < mn {
                    mn = balance[i]
                    idx = i
                }
            }
        }
        if mn >= 0 { return 0 }

        var need = -mn
        var ans = 0
        if n > 1 {
            for j in 1..<n {
                let a = balance[(idx - j + n) % n]
                let b = balance[(idx + j) % n]
                let c1 = min(a, need)
                need -= c1
                ans += c1 * j
                let c2 = min(b, need)
                need -= c2
                ans += c2 * j
            }
        }
        return ans
    }
}
""")

write("3777_minimum_deletions_to_make_alternating_substring", """// LeetCode 3777 - Minimum Deletions To Make Alternating Substring
// https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

class Solution {
    private class BIT {
        var n: Int
        var c: [Int]
        init(_ n_: Int) { n = n_; c = [Int](repeating: 0, count: n_ + 1) }
        func update(_ x: Int, _ delta: Int) {
            var x = x
            while x <= n {
                c[x] += delta
                x += x & -x
            }
        }
        func query(_ x: Int) -> Int {
            var x = x, s = 0
            while x > 0 {
                s += c[x]
                x -= x & -x
            }
            return s
        }
    }

    func minDeletions(_ s: String, _ queries: [[Int]]) -> [Int] {
        let chars = Array(s)
        let n = chars.count
        var nums = [Int](repeating: 0, count: n)
        let bit = BIT(n)
        if n > 1 {
            for i in 1..<n {
                if chars[i] == chars[i - 1] {
                    nums[i] = 1
                    bit.update(i + 1, 1)
                }
            }
        }
        var ans = [Int]()
        for q in queries {
            if q[0] == 1 {
                let j = q[1]
                var delta = (nums[j] ^ 1) - nums[j]
                nums[j] ^= 1
                bit.update(j + 1, delta)
                if j + 1 < n {
                    delta = (nums[j + 1] ^ 1) - nums[j + 1]
                    nums[j + 1] ^= 1
                    bit.update(j + 2, delta)
                }
            } else {
                let l = q[1], r = q[2]
                ans.append(bit.query(r + 1) - bit.query(l + 1))
            }
        }
        return ans
    }
}
""")

write("3778_minimum_distance_excluding_one_maximum_weighted_edge", """// LeetCode 3778 - Minimum Distance Excluding One Maximum Weighted Edge
// https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/

class Solution {
    func minCostExcludingMax(_ n: Int, _ edges: [[Int]]) -> Int {
        var g = [[[Int]]](repeating: [], count: n)
        for e in edges {
            let u = e[0], v = e[1], w = e[2]
            g[u].append([v, w])
            g[v].append([u, w])
        }
        let INF = Int(4e18)
        var dist = Array(repeating: [INF, INF], count: n)
        dist[0][0] = 0
        var pq = [(0, 0, 0)]
        while !pq.isEmpty {
            pq.sort { $0.0 < $1.0 }
            let cur = pq.removeFirst()
            let c = cur.0, u = cur.1, used = cur.2
            if c > dist[u][used] { continue }
            if u == n - 1 && used == 1 { return c }
            for e in g[u] {
                let v = e[0], w = e[1]
                var nxt = c + w
                if nxt < dist[v][used] {
                    dist[v][used] = nxt
                    pq.append((nxt, v, used))
                }
                if used == 0 {
                    nxt = c
                    if nxt < dist[v][1] {
                        dist[v][1] = nxt
                        pq.append((nxt, v, 1))
                    }
                }
            }
        }
        return dist[n - 1][1]
    }
}
""")

write("3779_minimum_number_of_operations_to_have_distinct_elements", """// LeetCode 3779 - Minimum Number Of Operations To Have Distinct Elements
// https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var st = Set<Int>()
        for i in stride(from: nums.count - 1, through: 0, by: -1) {
            if st.contains(nums[i]) { return i / 3 + 1 }
            st.insert(nums[i])
        }
        return 0
    }
}
""")
