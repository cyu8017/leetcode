from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def hdr(num, title, slug):
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n\n"

def write(folder, content):
    (ROOT / folder / "Solution.swift").write_text(content)
    print("W", folder)

FILES = {}

FILES["3990_create_grid_with_exactly_k_paths_ii"] = hdr("3990", "Create Grid With Exactly K Paths II", "create-grid-with-exactly-k-paths-ii") + r'''
class Solution {
    func createGrid(_ k: Int) -> [String] {
        if k <= 0 { return [] }
        func bitWidth(_ k0: Int) -> Int {
            var w = 0, k = k0
            while k != 0 { w += 1; k >>= 1 }
            return w
        }
        let l = bitWidth(k)
        let m = 2 * l, n = l + 3
        var result = Array(repeating: String(repeating: "#", count: n), count: m)
        for i in 0..<l {
            let r = 2 * i
            var row0 = Array(result[r])
            var row1 = Array(result[r + 1])
            row0[i] = "."
            row0[i + 1] = "."
            row1[i] = "."
            row1[i + 1] = "."
            if (k & (1 << i)) != 0 {
                for c in (i + 2)..<n { row0[c] = "." }
            }
            result[r] = String(row0)
            result[r + 1] = String(row1)
        }
        for r in 0..<m {
            var row = Array(result[r])
            row[n - 1] = "."
            result[r] = String(row)
        }
        return result
    }
}
'''

FILES["3992_rearrange_string_to_avoid_character_pair"] = hdr("3992", "Rearrange String to Avoid Character Pair", "rearrange-string-to-avoid-character-pair") + r'''
class Solution {
    func rearrangeString(_ s: String, _ x: Character, _ y: Character) -> String {
        var arr = Array(s)
        var i = 0
        for j in 0..<arr.count {
            if arr[j] == y {
                arr.swapAt(i, j)
                i += 1
            }
        }
        return String(arr)
    }
}
'''

FILES["3993_maximum_value_of_an_alternating_sequence"] = hdr("3993", "Maximum Value of an Alternating Sequence", "maximum-value-of-an-alternating-sequence") + r'''
class Solution {
    func maximumValue(_ n: Int, _ s: Int, _ m: Int) -> Int {
        if n == 1 { return s }
        return s + (n / 2) * (m - 1) + 1
    }
}
'''

FILES["3994_minimum_adjacent_swaps_to_partition_array"] = hdr("3994", "Minimum Adjacent Swaps to Partition Array", "minimum-adjacent-swaps-to-partition-array") + r'''
class Solution {
    func minAdjacentSwaps(_ nums: [Int], _ a: Int, _ b: Int) -> Int {
        let MOD = 1_000_000_007
        var result = 0, cnt1 = 0, cnt2 = 0
        for x in nums {
            if x < a {
                result = (result + cnt1 + cnt2) % MOD
            } else if x <= b {
                cnt1 += 1
                result = (result + cnt2) % MOD
            } else {
                cnt2 += 1
            }
        }
        return result
    }
}
'''

FILES["3995_minimum_cost_to_convert_string_iii"] = hdr("3995", "Minimum Cost to Convert String III", "minimum-cost-to-convert-string-iii") + r'''
class Solution {
    func minCost(_ source: String, _ target: String, _ rules: [[String]], _ costs: [Int]) -> Int {
        let src = Array(source), tgt = Array(target)
        let n = src.count
        if tgt.count != n { return -1 }
        var dp = Array(repeating: Int.max, count: n + 1)
        dp[0] = 0
        for i in 0..<n {
            if dp[i] == Int.max { continue }
            if src[i] == tgt[i] && dp[i] < dp[i + 1] { dp[i + 1] = dp[i] }
            for j in 0..<rules.count {
                let p = Array(rules[j][0])
                let r = Array(rules[j][1])
                let plen = p.count
                if i + plen > n { continue }
                var c = costs[j]
                var ok = true
                for k in 0..<plen {
                    if r[k] != tgt[i + k] { ok = false; break }
                    if p[k] == "*" { c += 1 }
                    else if p[k] != src[i + k] { ok = false; break }
                }
                if ok && dp[i] <= Int.max - c && dp[i] + c < dp[i + plen] {
                    dp[i + plen] = dp[i] + c
                }
            }
        }
        return dp[n] == Int.max ? -1 : dp[n]
    }
}
'''

FILES["3996_even_number_of_knight_moves"] = hdr("3996", "Even Number of Knight Moves", "even-number-of-knight-moves") + r'''
class Solution {
    func canReach(_ start: [Int], _ target: [Int]) -> Bool {
        ((start[0] + start[1]) % 2) == ((target[0] + target[1]) % 2)
    }
}
'''

FILES["3997_count_dominant_nodes_in_a_binary_tree"] = hdr("3997", "Count Dominant Nodes in a Binary Tree", "count-dominant-nodes-in-a-binary-tree") + r'''
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

class Solution {
    private var ans = 0

    private func dfs(_ node: TreeNode?) -> Int {
        guard let node = node else { return Int.min }
        let l = dfs(node.left)
        let r = dfs(node.right)
        let mx = max(max(l, r), node.val)
        if mx == node.val { ans += 1 }
        return mx
    }

    func countDominantNodes(_ root: TreeNode?) -> Int {
        ans = 0
        _ = dfs(root)
        return ans
    }
}
'''

FILES["3998_transform_binary_string_using_subsequence_sort"] = hdr("3998", "Transform Binary String Using Subsequence Sort", "transform-binary-string-using-subsequence-sort") + r'''
class Solution {
    func transformStr(_ s: String, _ strs: [String]) -> [Bool] {
        let sArr = Array(s)
        let n = sArr.count
        var prefix = Array(repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + (sArr[i] == "1" ? 1 : 0) }
        var result = Array(repeating: false, count: strs.count)
        for i in 0..<strs.count {
            let t = Array(strs[i])
            var left = 0, right = 0
            var ok = true
            for j in 0..<n {
                left += (t[j] == "1" ? 1 : 0)
                let add = (t[j] != "0" ? 1 : 0)
                right = right + add
                if right > prefix[j + 1] { right = prefix[j + 1] }
                if left > right {
                    ok = false
                    break
                }
            }
            result[i] = ok && left <= prefix[n] && prefix[n] <= right
        }
        return result
    }
}
'''

FILES["3999_minimum_number_of_string_groups_through_transformations"] = hdr("3999", "Minimum Number of String Groups Through Transformations", "minimum-number-of-string-groups-through-transformations") + r'''
class Solution {
    func minimumGroups(_ words: [String]) -> Int {
        func leastRotation(_ s: [Character]) -> Int {
            let n = s.count
            var i = 0, j = 1, k = 0
            while i < n && j < n && k < n {
                let a = s[(i + k) % n]
                let b = s[(j + k) % n]
                if a == b { k += 1 }
                else {
                    if a > b { i += k + 1 }
                    else { j += k + 1 }
                    if i == j { j += 1 }
                    k = 0
                }
            }
            return i < j ? i : j
        }
        func canonicalRotate(_ s: String) -> String {
            let arr = Array(s)
            let n = arr.count
            if n <= 1 { return s }
            let r = leastRotation(arr)
            if r == 0 { return s }
            return String(arr[r...]) + String(arr[..<r])
        }
        var keys = [String]()
        for w in words {
            let arr = Array(w)
            var even = "", odd = ""
            for i in 0..<arr.count {
                if i % 2 == 0 { even.append(arr[i]) }
                else { odd.append(arr[i]) }
            }
            keys.append(canonicalRotate(even) + "#" + canonicalRotate(odd))
        }
        keys.sort()
        var groups = 0
        for i in 0..<keys.count {
            if i == 0 || keys[i] != keys[i - 1] { groups += 1 }
        }
        return groups
    }
}
'''

FILES["4000_largest_integer_with_given_digit_sum"] = hdr("4000", "Largest Integer With Given Digit Sum", "largest-integer-with-given-digit-sum") + r'''
class Solution {
    func largestInteger(_ n: Int, _ s: Int) -> Int {
        if n * 9 < s { return -1 }
        var s = s, ans = 0
        for _ in 0..<n {
            let x = s < 9 ? s : 9
            ans = ans * 10 + x
            s -= x
        }
        return ans
    }
}
'''

FILES["4001_aggregate_two_time_series"] = hdr("4001", "Aggregate Two Time Series", "aggregate-two-time-series") + r'''
class Solution {
    func aggregateTimeSeries(_ series1: [[Int]], _ series2: [[Int]]) -> [[Int]] {
        let m = series1.count, n = series2.count
        var i = 0, j = 0
        var ans = [[Int]]()
        while i < m && j < n {
            let t1 = series1[i][0], v1 = series1[i][1]
            let t2 = series2[j][0], v2 = series2[j][1]
            if t1 == t2 {
                ans.append([t1, v1 + v2])
                i += 1
                j += 1
            } else if t1 < t2 {
                ans.append([t1, v1 + v2])
                i += 1
            } else {
                ans.append([t2, v1 + v2])
                j += 1
            }
        }
        while i < m {
            ans.append([series1[i][0], series1[i][1]])
            i += 1
        }
        while j < n {
            ans.append([series2[j][0], series2[j][1]])
            j += 1
        }
        return ans
    }
}
'''

FILES["4002_count_valid_sequences"] = hdr("4002", "Count Valid Sequences", "count-valid-sequences") + r'''
class Solution {
    private static let MX = 500001
    private static let MOD = 1_000_000_007
    private static let tables: ([Int], [Int]) = {
        var f = Array(repeating: 0, count: MX)
        var g = Array(repeating: 0, count: MX)
        f[0] = 1
        g[0] = 1
        func modPow(_ a0: Int, _ b0: Int) -> Int {
            var a = a0 % MOD, b = b0, res = 1
            while b > 0 {
                if (b & 1) != 0 { res = res * a % MOD }
                a = a * a % MOD
                b >>= 1
            }
            return res
        }
        for i in 1..<MX {
            f[i] = f[i - 1] * i % MOD
            g[i] = modPow(f[i], MOD - 2)
        }
        return (f, g)
    }()

    func countValidSequences(_ n: Int, _ k: Int) -> Int {
        let MOD = Solution.MOD
        let (f, g) = Solution.tables
        func comb(_ n: Int, _ k: Int) -> Int {
            if k < 0 || k > n { return 0 }
            return f[n] * g[k] % MOD * g[n - k] % MOD
        }
        var ans = comb(n - 1, k - 1)
        if (n + k) % 2 == 0 {
            ans = (ans - comb((n + k) / 2 - 1, k - 1) + MOD) % MOD
        }
        return ans
    }
}
'''

FILES["4003_minimum_cost_path_with_alternating_directions_iii"] = hdr("4003", "Minimum Cost Path with Alternating Directions III", "minimum-cost-path-with-alternating-directions-iii") + r'''
class Solution {
    func minCost(_ m: Int, _ n: Int, _ penalty: [[Int]]) -> Int {
        let INF = Int.max / 4
        var dist = Array(repeating: Array(repeating: [INF, INF], count: n), count: m)
        dist[0][0][1] = 1
        var pq = [(1, 0, 0, 1)]
        let dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        while !pq.isEmpty {
            pq.sort { $0.0 < $1.0 }
            let cur = pq.removeFirst()
            let d = cur.0, i = cur.1, j = cur.2, k = cur.3
            if i == m - 1 && j == n - 1 { return d }
            if d > dist[i][j][k] { continue }
            let p = penalty[i][j]
            var nd = d + p
            if nd < dist[i][j][k ^ 1] {
                dist[i][j][k ^ 1] = nd
                pq.append((nd, i, j, k ^ 1))
            }
            for idx in 0..<4 {
                let x = i + dirs[idx][0], y = j + dirs[idx][1]
                if 0 <= x && x < m && 0 <= y && y < n {
                    nd = d + ((x + 1) * (y + 1) + (((idx & 1) ^ k) * p))
                    if nd < dist[x][y][k ^ 1] {
                        dist[x][y][k ^ 1] = nd
                        pq.append((nd, x, y, k ^ 1))
                    }
                }
            }
        }
        return -1
    }
}
'''

FILES["4004_minimum_moves_to_balance_circular_array_ii"] = hdr("4004", "Minimum Moves to Balance Circular Array II", "minimum-moves-to-balance-circular-array-ii") + r'''
class Solution {
    func minMoves(_ balance: [Int]) -> Int {
        class Edge {
            var to: Int
            var cap: Int
            var cost: Int
            var rev: Int
            init(_ to: Int, _ cap: Int, _ cost: Int, _ rev: Int) {
                self.to = to; self.cap = cap; self.cost = cost; self.rev = rev
            }
        }
        class MinCostMaxFlow {
            let n: Int
            var graph: [[Edge]]
            let INF = 1_000_000_000
            init(_ n: Int) {
                self.n = n
                graph = Array(repeating: [Edge](), count: n)
            }
            func addEdge(_ u: Int, _ v: Int, _ cap: Int, _ cost: Int) {
                graph[u].append(Edge(v, cap, cost, graph[v].count))
                graph[v].append(Edge(u, 0, -cost, graph[u].count - 1))
            }
            func minCostFlow(_ source: Int, _ sink: Int, _ maxFlow: Int) -> Int {
                var totalCost = 0
                var currentFlow = 0
                while currentFlow < maxFlow {
                    var dist = Array(repeating: INF, count: n)
                    var parentNode = Array(repeating: -1, count: n)
                    var parentEdge = Array(repeating: -1, count: n)
                    var inQueue = Array(repeating: false, count: n)
                    var q = [source]
                    var head = 0
                    dist[source] = 0
                    inQueue[source] = true
                    while head < q.count {
                        let u = q[head]; head += 1
                        inQueue[u] = false
                        for i in 0..<graph[u].count {
                            let e = graph[u][i]
                            if e.cap > 0 && dist[e.to] > dist[u] + e.cost {
                                dist[e.to] = dist[u] + e.cost
                                parentNode[e.to] = u
                                parentEdge[e.to] = i
                                if !inQueue[e.to] {
                                    inQueue[e.to] = true
                                    q.append(e.to)
                                }
                            }
                        }
                    }
                    if dist[sink] == INF { return -1 }
                    var pushFlow = maxFlow - currentFlow
                    var cur = sink
                    while cur != source {
                        let e = graph[parentNode[cur]][parentEdge[cur]]
                        if e.cap < pushFlow { pushFlow = e.cap }
                        cur = parentNode[cur]
                    }
                    cur = sink
                    while cur != source {
                        let p = parentNode[cur]
                        let idx = parentEdge[cur]
                        let rev = graph[p][idx].rev
                        graph[p][idx].cap -= pushFlow
                        graph[cur][rev].cap += pushFlow
                        cur = parentNode[cur]
                    }
                    currentFlow += pushFlow
                    totalCost += pushFlow * dist[sink]
                }
                return totalCost
            }
        }
        var totalBalance = 0, totalDeficit = 0
        for x in balance {
            totalBalance += x
            if x < 0 { totalDeficit += -x }
        }
        if totalBalance < 0 { return -1 }
        if totalDeficit == 0 { return 0 }
        let n = balance.count
        let source = n, sink = n + 1
        let mcmf = MinCostMaxFlow(n + 2)
        let INF = 1_000_000_000
        for i in 0..<n {
            let x = balance[i]
            if x > 0 { mcmf.addEdge(source, i, x, 0) }
            else if x < 0 { mcmf.addEdge(i, sink, -x, 0) }
            mcmf.addEdge(i, (i + 1) % n, INF, 1)
            mcmf.addEdge(i, (i - 1 + n) % n, INF, 1)
        }
        return mcmf.minCostFlow(source, sink, totalDeficit)
    }
}
'''

FILES["4005_minimum_operations_to_make_array_equal_iii"] = hdr("4005", "Minimum Operations to Make Array Equal III", "minimum-operations-to-make-array-equal-iii") + r'''
class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        func cost(_ x: Int, _ t: Int) -> Int {
            if x == t { return 0 }
            if x % t == 0 || t % x == 0 { return 1 }
            return 2
        }
        func gcd(_ a0: Int, _ b0: Int) -> Int {
            var a = a0, b = b0
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        let n = nums.count
        if n <= 1 { return 0 }
        var g = nums[0], mn = nums[0]
        for i in 1..<n {
            g = gcd(g, nums[i])
            mn = min(mn, nums[i])
        }
        var cands = Set<Int>()
        for x in nums { cands.insert(x) }
        var d = 1
        while d * d <= mn {
            if mn % d == 0 {
                cands.insert(d)
                cands.insert(mn / d)
            }
            d += 1
        }
        cands.insert(g)
        var ans = Int.max
        for t in cands {
            var sum = 0
            for x in nums {
                sum += cost(x, t)
                if sum >= ans { break }
            }
            ans = min(ans, sum)
        }
        return ans
    }
}
'''

FILES["4006_count_valid_prefixes"] = hdr("4006", "Count Valid Prefixes", "count-valid-prefixes") + r'''
class Solution {
    func countValidPrefixes(_ s: String) -> Int {
        var ans = 0, t = 0
        for ch in s {
            if ch == "1" { t += 1 }
            else { t -= 1 }
            if t >= -1 && t <= 1 { ans += 1 }
        }
        return ans
    }
}
'''

FILES["4007_widest_possible_fence"] = hdr("4007", "Widest Possible Fence", "widest-possible-fence") + r'''
class Solution {
    func maximumWidth(_ planks: [Int]) -> Int {
        var cnt = [Int: Int]()
        for x in planks { cnt[x, default: 0] += 1 }
        var t = [Int: Int]()
        var ans = 0
        for (x, v1) in cnt {
            t[x, default: 0] += v1
            ans = max(ans, t[x]!)
            t[x * 2, default: 0] += v1 / 2
            ans = max(ans, t[x * 2]!)
            for (y, v2) in cnt {
                if y > x {
                    let key = x + y
                    t[key, default: 0] += min(v1, v2)
                    ans = max(ans, t[key]!)
                }
            }
        }
        return ans
    }
}
'''

FILES["4008_minimum_initial_strength_to_defeat_all_monsters"] = hdr("4008", "Minimum Initial Strength to Defeat All Monsters", "minimum-initial-strength-to-defeat-all-monsters") + r'''
class Solution {
    func minInitialStrength(_ monsters: [Int], _ boosts: [[Int]]) -> Int {
        let n = monsters.count
        var d = Array(repeating: 0, count: n + 1)
        for b in boosts {
            d[b[0]] += b[2]
            d[b[1] + 1] -= b[2]
        }
        func check(_ v0: Int) -> Bool {
            var v = v0, bonus = 0
            for i in 0..<monsters.count {
                bonus += d[i]
                if v + bonus < monsters[i] { return false }
                v -= monsters[i]
                if v < 0 { v = 0 }
            }
            return true
        }
        var left = 0, right = 1_000_000_000_000_000
        while left < right {
            let mid = (left + right) / 2
            if check(mid) { right = mid }
            else { left = mid + 1 }
        }
        return left
    }
}
'''

FILES["4009_minimum_possible_maximum_waiting_time"] = hdr("4009", "Minimum Possible Maximum Waiting Time", "minimum-possible-maximum-waiting-time") + r'''
class Solution {
    func minMaxWaitingTime(_ demand: [Int], _ fuel: [Int]) -> Int {
        let dem = demand
        let n = demand.count
        let f0 = fuel[0], f1 = fuel[1]
        if f0 < demand[0] && f1 < demand[0] { return -1 }
        func packKey(_ i: Int, _ f0: Int, _ f1: Int, _ d0: Int, _ d1: Int) -> Int {
            ((((i * 51 + f0) * 51 + f1) * 21 + d0) * 21 + d1)
        }
        var memo = [Int: Int]()
        func maxServe(_ i: Int, _ f0: Int, _ f1: Int, _ d0: Int, _ d1: Int) -> Int {
            if i == n { return i }
            let key = packKey(i, f0, f1, d0, d1)
            if let v = memo[key] { return v }
            let need = dem[i]
            let can0 = f0 >= need
            let can1 = f1 >= need
            var best = i
            if !can0 && !can1 {
                memo[key] = best
                return best
            }
            if can0 {
                let nd1 = d1 > d0 ? d1 - d0 : 0
                best = max(best, maxServe(i + 1, f0 - need, f1, need, nd1))
            }
            if can1 {
                let nd0 = d0 > d1 ? d0 - d1 : 0
                best = max(best, maxServe(i + 1, f0, f1 - need, nd0, need))
            }
            memo[key] = best
            return best
        }
        memo.removeAll()
        let bestServe = maxServe(0, f0, f1, 0, 0)
        if bestServe == 0 { return -1 }
        var W = 0
        func canWithW(_ i: Int, _ f0: Int, _ f1: Int, _ d0: Int, _ d1: Int) -> Bool {
            if i >= bestServe { return true }
            if i == n { return true }
            let key = packKey(i, f0, f1, d0, d1)
            if let v = memo[key] { return v == 2 }
            let need = dem[i]
            let can0 = f0 >= need
            let can1 = f1 >= need
            var ok = false
            if !can0 && !can1 {
                memo[key] = 1
                return false
            }
            if can0 && d0 <= W {
                let nd1 = d1 > d0 ? d1 - d0 : 0
                if canWithW(i + 1, f0 - need, f1, need, nd1) { ok = true }
            }
            if !ok && can1 && d1 <= W {
                let nd0 = d0 > d1 ? d0 - d1 : 0
                if canWithW(i + 1, f0, f1 - need, nd0, need) { ok = true }
            }
            memo[key] = ok ? 2 : 1
            return ok
        }
        var lo = 0, hi = 0
        for x in demand { hi += x }
        var ans = hi
        while lo <= hi {
            let mid = (lo + hi) / 2
            W = mid
            memo.removeAll()
            if canWithW(0, f0, f1, 0, 0) {
                ans = mid
                hi = mid - 1
            } else {
                lo = mid + 1
            }
        }
        return ans
    }
}
'''

FILES["4010_maximize_pair_strength_using_gcd"] = hdr("4010", "Maximize Pair Strength Using GCD", "maximize-pair-strength-using-gcd") + r'''
class Solution {
    func maxPairStrength(_ nums: [Int]) -> Int {
        func gcd(_ a0: Int, _ b0: Int) -> Int {
            var a = a0, b = b0
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            for j in (i + 1)..<n {
                let g = gcd(nums[i], nums[j])
                let x = nums[i] * nums[j] / (g * g)
                ans = max(ans, x)
            }
        }
        return ans
    }
}
'''

FILES["4011_count_subarrays_with_even_odd_ratio_i"] = hdr("4011", "Count Subarrays With Even Odd Ratio I", "count-subarrays-with-even-odd-ratio-i") + r'''
class Solution {
    func countRatioSubarrays(_ nums: [Int], _ a: Int, _ b: Int) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var y = 0
            for j in i..<n {
                y += nums[j] % 2
                let x = j - i + 1 - y
                if y > 0 && x * b <= y * a { ans += 1 }
            }
        }
        return ans
    }
}
'''

FILES["4012_count_of_unfinished_tasks_after_each_shift"] = hdr("4012", "Count of Unfinished Tasks After Each Shift", "count-of-unfinished-tasks-after-each-shift") + r'''
class Solution {
    func countTasks(_ tasks: [Int], _ shifts: [Int]) -> [Int] {
        let m = tasks.count, n = shifts.count
        var s = Array(repeating: 0, count: m + 1)
        for i in 0..<m { s[i + 1] = s[i] + tasks[i] }
        var ans = Array(repeating: 0, count: n)
        var iIdx = 0
        var cur = 0
        for j in 0..<n {
            if shifts[j] < tasks[iIdx] - cur {
                cur += shifts[j]
                ans[j] = m - iIdx
            } else {
                let t = shifts[j] - (tasks[iIdx] - cur)
                if t >= s[m] - s[iIdx + 1] {
                    iIdx = 0
                    cur = 0
                } else {
                    var l = iIdx + 1, r = m
                    while l < r {
                        let mid = (l + r) >> 1
                        if t < s[mid + 1] - s[iIdx + 1] { r = mid }
                        else { l = mid + 1 }
                    }
                    cur = t - (s[l] - s[iIdx + 1])
                    iIdx = l
                    ans[j] = m - iIdx
                }
            }
        }
        return ans
    }
}
'''

FILES["4013_count_subarrays_with_even_odd_ratio_ii"] = hdr("4013", "Count Subarrays With Even Odd Ratio II", "count-subarrays-with-even-odd-ratio-ii") + r'''
class Solution {
    func countRatioSubarrays(_ nums: [Int], _ a: Int, _ b: Int) -> Int {
        let n = nums.count
        var s = Array(repeating: 0, count: n + 1)
        for i in 0..<n {
            if nums[i] % 2 == 1 { s[i + 1] = s[i] + a }
            else { s[i + 1] = s[i] - b }
        }
        var st = s
        st.sort()
        var uniq = 0
        for i in 0..<st.count {
            if uniq == 0 || st[i] != st[uniq - 1] {
                st[uniq] = st[i]
                uniq += 1
            }
        }
        st = Array(st.prefix(uniq))
        var bit = BIT(st.count + 1)
        var ans = 0
        for v in s {
            let x = lowerBound(st, v) + 1
            ans += bit.query(x)
            bit.update(x, 1)
        }
        return ans
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

    private class BIT {
        let n: Int
        var c: [Int]
        init(_ n: Int) {
            self.n = n
            c = Array(repeating: 0, count: n + 1)
        }
        func update(_ x0: Int, _ delta: Int) {
            var x = x0
            while x <= n {
                c[x] += delta
                x += x & -x
            }
        }
        func query(_ x0: Int) -> Int {
            var x = x0, sum = 0
            while x > 0 {
                sum += c[x]
                x -= x & -x
            }
            return sum
        }
    }
}
'''

for folder, content in FILES.items():
    write(folder, content)
print("done", len(FILES))
