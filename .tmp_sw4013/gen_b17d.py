#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def hdr(num, title, slug):
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n"

MINHEAP2 = '''
private struct MinHeap2 {
    private var a: [(Int, Int)] = []
    var isEmpty: Bool { a.isEmpty }
    mutating func push(_ x: (Int, Int)) {
        a.append(x)
        var i = a.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if a[p].0 <= a[i].0 { break }
            a.swapAt(p, i)
            i = p
        }
    }
    mutating func pop() -> (Int, Int) {
        let r = a[0]
        let last = a.removeLast()
        if !a.isEmpty {
            a[0] = last
            var i = 0
            while true {
                var s = i
                let l = 2 * i + 1, rg = 2 * i + 2
                if l < a.count && a[l].0 < a[s].0 { s = l }
                if rg < a.count && a[rg].0 < a[s].0 { s = rg }
                if s == i { break }
                a.swapAt(i, s)
                i = s
            }
        }
        return r
    }
}
'''

FILES = {}

FILES["3366_minimum_array_sum"] = hdr("3366", "Minimum Array Sum", "minimum-array-sum") + '''
class Solution {
    func minArraySum(_ nums: [Int], _ k: Int, _ op1: Int, _ op2: Int) -> Int {
        let inf = Int(1e18)
        var dp = Array(repeating: Array(repeating: inf, count: op2 + 1), count: op1 + 1)
        dp[0][0] = 0
        for x in nums {
            var ndp = Array(repeating: Array(repeating: inf, count: op2 + 1), count: op1 + 1)
            for a in 0...op1 {
                for b in 0...op2 {
                    if dp[a][b] == inf { continue }
                    tryCand(&ndp, dp[a][b], a, b, x)
                    if a < op1 { tryCand(&ndp, dp[a][b], a + 1, b, (x + 1) / 2) }
                    if b < op2 && x >= k { tryCand(&ndp, dp[a][b], a, b + 1, x - k) }
                    if a < op1 && b < op2 {
                        let v1 = (x + 1) / 2
                        if v1 >= k { tryCand(&ndp, dp[a][b], a + 1, b + 1, v1 - k) }
                        if x >= k { tryCand(&ndp, dp[a][b], a + 1, b + 1, (x - k + 1) / 2) }
                    }
                }
            }
            dp = ndp
        }
        var ans = inf
        for a in 0...op1 {
            for b in 0...op2 where dp[a][b] < ans { ans = dp[a][b] }
        }
        return ans
    }

    private func tryCand(_ ndp: inout [[Int]], _ base: Int, _ na: Int, _ nb: Int, _ v: Int) {
        if base + v < ndp[na][nb] { ndp[na][nb] = base + v }
    }
}
'''

FILES["3367_maximize_sum_of_weights_after_edge_removals"] = hdr("3367", "Maximize Sum of Weights after Edge Removals", "maximize-sum-of-weights-after-edge-removals") + '''
class Solution {
    func maximizeSumOfWeights(_ edges: [[Int]], _ k: Int) -> Int {
        let n = edges.count + 1
        var g = Array(repeating: [(Int, Int)](), count: n)
        for e in edges {
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        }
        func dfs(_ u: Int, _ p: Int) -> (Int, Int) {
            var base = 0
            var gains = [Int]()
            for (to, w) in g[u] where to != p {
                let child = dfs(to, u)
                base += child.1
                let gain = child.0 + w - child.1
                if gain > 0 { gains.append(gain) }
            }
            gains.sort(by: >)
            var with = base, without = base
            for i in 0..<gains.count where i < k - 1 { with += gains[i] }
            for i in 0..<gains.count where i < k { without += gains[i] }
            return (with, without)
        }
        return dfs(0, -1).1
    }
}
'''

FILES["3369_design_an_array_statistics_tracker"] = hdr("3369", "Design an Array Statistics Tracker", "design-an-array-statistics-tracker") + '''
class StatisticsTracker {
    private var arr = [Int]()
    private var sum = 0
    private var freq = [Int: Int]()
    private var modeFreq = 0
    private var modes = Set<Int>()

    init() {}

    func addNumber(_ num: Int) {
        arr.append(num)
        sum += num
        freq[num, default: 0] += 1
        let f = freq[num]!
        if f > modeFreq {
            modeFreq = f
            modes = [num]
        } else if f == modeFreq {
            modes.insert(num)
        }
    }

    func removeFirst() {
        if arr.isEmpty { return }
        let num = arr.removeFirst()
        sum -= num
        freq[num]! -= 1
        if freq[num] == 0 { freq.removeValue(forKey: num) }
        modeFreq = 0
        modes.removeAll()
        for (v, ff) in freq {
            if ff > modeFreq {
                modeFreq = ff
                modes = [v]
            } else if ff == modeFreq {
                modes.insert(v)
            }
        }
    }

    func getMean() -> Int {
        if arr.isEmpty { return 0 }
        return sum / arr.count
    }

    func getMedian() -> Int {
        let tmp = arr.sorted()
        let n = tmp.count
        if n % 2 == 1 { return tmp[n / 2] }
        return tmp[n / 2 - 1]
    }

    func getMode() -> Int {
        return modes.min() ?? 0
    }
}
'''

FILES["3370_smallest_number_with_all_set_bits"] = hdr("3370", "Smallest Number With All Set Bits", "smallest-number-with-all-set-bits") + '''
class Solution {
    func smallestNumber(_ n: Int) -> Int {
        var x = 1
        while x < n { x = x * 2 + 1 }
        return x
    }
}
'''

FILES["3371_identify_the_largest_outlier_in_an_array"] = hdr("3371", "Identify the Largest Outlier in an Array", "identify-the-largest-outlier-in-an-array") + '''
class Solution {
    func getLargestOutlier(_ nums: [Int]) -> Int {
        var sum = 0
        var freq = [Int: Int]()
        for x in nums {
            sum += x
            freq[x, default: 0] += 1
        }
        var ans = Int.min
        for x in nums {
            freq[x]! -= 1
            let rem = sum - x
            if rem % 2 == 0 {
                let cand = rem / 2
                if freq[cand, default: 0] > 0 && x > ans { ans = x }
            }
            freq[x]! += 1
        }
        return ans
    }
}
'''

FILES["3372_maximize_the_number_of_target_nodes_after_connecting_trees_i"] = hdr("3372", "Maximize the Number of Target Nodes After Connecting Trees I", "maximize-the-number-of-target-nodes-after-connecting-trees-i") + '''
class Solution {
    func maxTargetNodes(_ edges1: [[Int]], _ edges2: [[Int]], _ k: Int) -> [Int] {
        let n = edges1.count + 1, m = edges2.count + 1
        let g1 = buildTree(n, edges1)
        let g2 = buildTree(m, edges2)
        var cnt1 = Array(repeating: 0, count: n)
        for i in 0..<n { cnt1[i] = countWithin(g1, i, k) }
        var best2 = 0
        if k > 0 {
            for i in 0..<m {
                let c = countWithin(g2, i, k - 1)
                if c > best2 { best2 = c }
            }
        }
        return cnt1.map { $0 + best2 }
    }

    private func buildTree(_ n: Int, _ edges: [[Int]]) -> [[Int]] {
        var g = Array(repeating: [Int](), count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        return g
    }

    private func countWithin(_ g: [[Int]], _ start: Int, _ k: Int) -> Int {
        if k < 0 { return 0 }
        var vis = Array(repeating: false, count: g.count)
        var q = [(start, 0)]
        vis[start] = true
        var cnt = 0, qi = 0
        while qi < q.count {
            let (u, d) = q[qi]; qi += 1
            cnt += 1
            if d == k { continue }
            for v in g[u] where !vis[v] {
                vis[v] = true
                q.append((v, d + 1))
            }
        }
        return cnt
    }
}
'''

FILES["3373_maximize_the_number_of_target_nodes_after_connecting_trees_ii"] = hdr("3373", "Maximize the Number of Target Nodes After Connecting Trees II", "maximize-the-number-of-target-nodes-after-connecting-trees-ii") + '''
class Solution {
    func maxTargetNodes(_ edges1: [[Int]], _ edges2: [[Int]]) -> [Int] {
        let n = edges1.count + 1, m = edges2.count + 1
        let g1 = buildTree(n, edges1)
        let g2 = buildTree(m, edges2)
        var color1 = Array(repeating: -1, count: n)
        var color2 = Array(repeating: -1, count: m)
        let c1 = bipartiteCount(g1, &color1)
        let c2 = bipartiteCount(g2, &color2)
        let best2 = max(c2.0, c2.1)
        var ans = Array(repeating: 0, count: n)
        for i in 0..<n { ans[i] = (color1[i] == 0 ? c1.0 : c1.1) + best2 }
        return ans
    }

    private func buildTree(_ n: Int, _ edges: [[Int]]) -> [[Int]] {
        var g = Array(repeating: [Int](), count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        return g
    }

    private func bipartiteCount(_ g: [[Int]], _ color: inout [Int]) -> (Int, Int) {
        var q = [0]
        color[0] = 0
        var cnt = [1, 0]
        var qi = 0
        while qi < q.count {
            let u = q[qi]; qi += 1
            for v in g[u] where color[v] == -1 {
                color[v] = color[u] ^ 1
                cnt[color[v]] += 1
                q.append(v)
            }
        }
        return (cnt[0], cnt[1])
    }
}
'''

FILES["3375_minimum_operations_to_make_array_values_equal_to_k"] = hdr("3375", "Minimum Operations to Make Array Values Equal to K", "minimum-operations-to-make-array-values-equal-to-k") + '''
class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        var seen = Set<Int>()
        for x in nums {
            if x < k { return -1 }
            if x > k { seen.insert(x) }
        }
        return seen.count
    }
}
'''

FILES["3376_minimum_time_to_break_locks_i"] = hdr("3376", "Minimum Time to Break Locks I", "minimum-time-to-break-locks-i") + '''
class Solution {
    func findMinimumTime(_ strength: [Int], _ k: Int) -> Int {
        let n = strength.count
        let inf = 1_000_000_000
        let N = 1 << n
        var dp = Array(repeating: inf, count: N)
        dp[0] = 0
        for mask in 0..<N {
            if dp[mask] == inf { continue }
            var opened = 0, xmask = mask
            while xmask > 0 { opened += xmask & 1; xmask >>= 1 }
            let x = 1 + opened * k
            for i in 0..<n where (mask & (1 << i)) == 0 {
                let t = (strength[i] + x - 1) / x
                let nmask = mask | (1 << i)
                if dp[mask] + t < dp[nmask] { dp[nmask] = dp[mask] + t }
            }
        }
        return dp[N - 1]
    }
}
'''

FILES["3377_digit_operations_to_make_two_integers_equal"] = hdr("3377", "Digit Operations to Make Two Integers Equal", "digit-operations-to-make-two-integers-equal") + MINHEAP2 + '''
class Solution {
    func minOperations(_ n: Int, _ m: Int) -> Int {
        var isPrime = Array(repeating: false, count: 100000)
        if 2 < 100000 {
            for i in 2..<100000 { isPrime[i] = true }
        }
        var i = 2
        while i * i < 100000 {
            if isPrime[i] {
                var j = i * i
                while j < 100000 {
                    isPrime[j] = false
                    j += i
                }
            }
            i += 1
        }
        if isPrime[n] { return -1 }
        var dist = Array(repeating: -1, count: 100000)
        var pq = MinHeap2()
        pq.push((n, n))
        dist[n] = n
        while !pq.isEmpty {
            let (cost, val) = pq.pop()
            if cost != dist[val] { continue }
            if val == m { return cost }
            var s = Array(String(val))
            for i in 0..<s.count {
                let orig = s[i]
                for d in [-1, 1] {
                    let nd = Int(orig.asciiValue! - 48) + d
                    if nd < 0 || nd > 9 { continue }
                    if i == 0 && nd == 0 && s.count > 1 { continue }
                    s[i] = Character(UnicodeScalar(nd + 48)!)
                    let nv = Int(String(s))!
                    s[i] = orig
                    if isPrime[nv] { continue }
                    let nc = cost + nv
                    if dist[nv] == -1 || nc < dist[nv] {
                        dist[nv] = nc
                        pq.push((nc, nv))
                    }
                }
            }
        }
        return -1
    }
}
'''

FILES["3378_count_connected_components_in_lcm_graph"] = hdr("3378", "Count Connected Components in LCM Graph", "count-connected-components-in-lcm-graph") + '''
class Solution {
    func countComponents(_ nums: [Int], _ threshold: Int) -> Int {
        let n = nums.count
        var parent = Array(0..<n)
        func find(_ x: Int) -> Int {
            if parent[x] != x { parent[x] = find(parent[x]) }
            return parent[x]
        }
        func unite(_ a: Int, _ b: Int) {
            let ra = find(a), rb = find(b)
            if ra != rb { parent[ra] = rb }
        }
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        var idx = [Int: Int]()
        for i in 0..<n { idx[nums[i]] = i }
        if threshold >= 1 {
            for d in 1...threshold {
                var first = -1
                var m = d
                while m <= threshold {
                    if let i = idx[m] {
                        if first == -1 { first = i }
                        else if nums[first] / gcd(nums[first], nums[i]) * nums[i] <= threshold {
                            unite(first, i)
                        }
                    }
                    m += d
                }
            }
        }
        for i in 0..<n {
            for j in (i + 1)..<n {
                let a = nums[i], b = nums[j]
                let g = gcd(a, b)
                if a / g * b <= threshold { unite(i, j) }
            }
        }
        return Set((0..<n).map { find($0) }).count
    }
}
'''

FILES["3379_transformed_array"] = hdr("3379", "Transformed Array", "transformed-array") + '''
class Solution {
    func constructTransformedArray(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var ans = Array(repeating: 0, count: n)
        for i in 0..<n {
            let j = ((i + nums[i]) % n + n) % n
            ans[i] = nums[j]
        }
        return ans
    }
}
'''

PACK_RECT = '''
    private func pack(_ x: Int, _ y: Int) -> Int {
        return (x << 32) ^ (y & ((1 << 32) - 1))
    }
'''

FILES["3380_maximum_area_rectangle_with_point_constraints_i"] = hdr("3380", "Maximum Area Rectangle With Point Constraints I", "maximum-area-rectangle-with-point-constraints-i") + '''
class Solution {
    func maxRectangleArea(_ points: [[Int]]) -> Int {
        var set = Set<Int>()
        for p in points { set.insert(pack(p[0], p[1])) }
        var ans = -1
        let n = points.count
        for i in 0..<n {
            for j in (i + 1)..<n {
                let x1 = points[i][0], y1 = points[i][1]
                let x2 = points[j][0], y2 = points[j][1]
                if x1 == x2 || y1 == y2 { continue }
                if !set.contains(pack(x1, y2)) || !set.contains(pack(x2, y1)) { continue }
                let minX = min(x1, x2), maxX = max(x1, x2)
                let minY = min(y1, y2), maxY = max(y1, y2)
                var ok = true
                for p in points {
                    let x = p[0], y = p[1]
                    if x > minX && x < maxX && y > minY && y < maxY { ok = false; break }
                    let onBorder = ((x == minX || x == maxX) && y >= minY && y <= maxY) ||
                        ((y == minY || y == maxY) && x >= minX && x <= maxX)
                    if onBorder {
                        let isCorner = (x == minX || x == maxX) && (y == minY || y == maxY)
                        if !isCorner { ok = false; break }
                    }
                }
                if ok {
                    let area = (maxX - minX) * (maxY - minY)
                    if area > ans { ans = area }
                }
            }
        }
        return ans
    }
''' + PACK_RECT + '''
}
'''

FILES["3381_maximum_subarray_sum_with_length_divisible_by_k"] = hdr("3381", "Maximum Subarray Sum With Length Divisible by K", "maximum-subarray-sum-with-length-divisible-by-k") + '''
class Solution {
    func maxSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var pref = Array(repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] + nums[i] }
        let INF = 1 << 62
        var best = Array(repeating: INF, count: k)
        best[0] = 0
        var ans = -(1 << 62)
        for i in 1...n {
            let r = i % k
            if best[r] != INF {
                let cand = pref[i] - best[r]
                if cand > ans { ans = cand }
            }
            if pref[i] < best[r] { best[r] = pref[i] }
        }
        return ans
    }
}
'''

FILES["3382_maximum_area_rectangle_with_point_constraints_ii"] = hdr("3382", "Maximum Area Rectangle With Point Constraints II", "maximum-area-rectangle-with-point-constraints-ii") + '''
class Solution {
    func maxRectangleArea(_ xCoord: [Int], _ yCoord: [Int]) -> Int {
        let n = xCoord.count
        var points = [[Int]]()
        for i in 0..<n { points.append([xCoord[i], yCoord[i]]) }
        var set = Set<Int>()
        for p in points { set.insert(pack(p[0], p[1])) }
        var ans = -1
        for i in 0..<n {
            for j in (i + 1)..<n {
                let x1 = points[i][0], y1 = points[i][1]
                let x2 = points[j][0], y2 = points[j][1]
                if x1 == x2 || y1 == y2 { continue }
                if !set.contains(pack(x1, y2)) || !set.contains(pack(x2, y1)) { continue }
                let minX = min(x1, x2), maxX = max(x1, x2)
                let minY = min(y1, y2), maxY = max(y1, y2)
                var ok = true
                for p in points {
                    let x = p[0], y = p[1]
                    if x > minX && x < maxX && y > minY && y < maxY { ok = false; break }
                    let onBorder = ((x == minX || x == maxX) && y >= minY && y <= maxY) ||
                        ((y == minY || y == maxY) && x >= minX && x <= maxX)
                    if onBorder {
                        let isCorner = (x == minX || x == maxX) && (y == minY || y == maxY)
                        if !isCorner { ok = false; break }
                    }
                }
                if ok {
                    let area = (maxX - minX) * (maxY - minY)
                    if area > ans { ans = area }
                }
            }
        }
        return ans
    }
''' + PACK_RECT + '''
}
'''

FILES["3383_minimum_runes_to_add_to_cast_spell"] = hdr("3383", "Minimum Runes to Add to Cast Spell", "minimum-runes-to-add-to-cast-spell") + '''
class Solution {
    func minRunesToAdd(_ n: Int, _ crystals: [Int], _ flowFrom: [Int], _ flowTo: [Int]) -> Int {
        var g = Array(repeating: [Int](), count: n)
        var rg = Array(repeating: [Int](), count: n)
        for i in 0..<flowFrom.count {
            g[flowFrom[i]].append(flowTo[i])
            rg[flowTo[i]].append(flowFrom[i])
        }
        var vis = Array(repeating: false, count: n)
        var order = [Int]()
        func dfs1(_ u: Int) {
            vis[u] = true
            for v in g[u] where !vis[v] { dfs1(v) }
            order.append(u)
        }
        for i in 0..<n where !vis[i] { dfs1(i) }
        var comp = Array(repeating: -1, count: n)
        var cid = 0
        func dfs2(_ u: Int) {
            comp[u] = cid
            for v in rg[u] where comp[v] == -1 { dfs2(v) }
        }
        for u in order.reversed() where comp[u] == -1 {
            dfs2(u)
            cid += 1
        }
        var hasCrystal = Array(repeating: false, count: cid)
        for c in crystals { hasCrystal[comp[c]] = true }
        var indeg = Array(repeating: 0, count: cid)
        for u in 0..<n {
            for v in g[u] where comp[u] != comp[v] { indeg[comp[v]] += 1 }
        }
        var ans = 0
        for i in 0..<cid where indeg[i] == 0 && !hasCrystal[i] { ans += 1 }
        return ans
    }
}
'''

FILES["3385_minimum_time_to_break_locks_ii"] = hdr("3385", "Minimum Time to Break Locks II", "minimum-time-to-break-locks-ii") + '''
class Solution {
    func findMinimumTime(_ strength: [Int]) -> Int {
        let n = strength.count
        let N = 1 << n
        let inf = Int(1e18)
        var dp = Array(repeating: inf, count: N)
        dp[0] = 0
        let k = 1
        for mask in 0..<N {
            if dp[mask] == inf { continue }
            var opened = 0, xmask = mask
            while xmask > 0 { opened += xmask & 1; xmask >>= 1 }
            let x = 1 + opened * k
            for i in 0..<n where (mask & (1 << i)) == 0 {
                let t = (strength[i] + x - 1) / x
                let nmask = mask | (1 << i)
                if dp[mask] + t < dp[nmask] { dp[nmask] = dp[mask] + t }
            }
        }
        return dp[N - 1]
    }
}
'''

FILES["3386_button_with_longest_push_time"] = hdr("3386", "Button with Longest Push Time", "button-with-longest-push-time") + '''
class Solution {
    func buttonWithLongestTime(_ events: [[Int]]) -> Int {
        var bestT = events[0][1], bestI = events[0][0]
        for i in 1..<events.count {
            let t = events[i][1] - events[i - 1][1]
            if t > bestT || (t == bestT && events[i][0] < bestI) {
                bestT = t
                bestI = events[i][0]
            }
        }
        return bestI
    }
}
'''

FILES["3387_maximize_amount_after_two_days_of_conversions"] = hdr("3387", "Maximize Amount After Two Days of Conversions", "maximize-amount-after-two-days-of-conversions") + '''
class Solution {
    func maxAmount(_ initialCurrency: String, _ pairs1: [[String]], _ rates1: [Double],
                   _ pairs2: [[String]], _ rates2: [Double]) -> Double {
        let amt1 = bellman(initialCurrency, pairs1, rates1)
        var ans = 1.0
        let g2 = buildRateGraph(pairs2, rates2)
        for (c, a) in amt1 where a > 0 {
            var dist = [c: a]
            var updated = true
            var it = 0
            while it < 100 && updated {
                updated = false
                it += 1
                for (from, tos) in g2 {
                    guard let df = dist[from], df != 0 else { continue }
                    for (to, rate) in tos {
                        let nv = df * rate
                        if dist[to] == nil || nv > dist[to]! {
                            dist[to] = nv
                            updated = true
                        }
                    }
                }
            }
            if let v = dist[initialCurrency], v > ans { ans = v }
        }
        return ans
    }

    private func buildRateGraph(_ pairs: [[String]], _ rates: [Double]) -> [String: [String: Double]] {
        var g = [String: [String: Double]]()
        for i in 0..<pairs.count {
            let a = pairs[i][0], b = pairs[i][1]
            g[a, default: [:]][b] = rates[i]
            g[b, default: [:]][a] = 1.0 / rates[i]
        }
        return g
    }

    private func bellman(_ start: String, _ pairs: [[String]], _ rates: [Double]) -> [String: Double] {
        let g = buildRateGraph(pairs, rates)
        var dist = [start: 1.0]
        for _ in 0..<100 {
            var updated = false
            for (from, tos) in g {
                guard let df = dist[from], df != 0 else { continue }
                for (to, rate) in tos {
                    let nv = df * rate
                    if dist[to] == nil || nv > dist[to]! {
                        dist[to] = nv
                        updated = true
                    }
                }
            }
            if !updated { break }
        }
        return dist
    }
}
'''

FILES["3388_count_beautiful_splits_in_an_array"] = hdr("3388", "Count Beautiful Splits in an Array", "count-beautiful-splits-in-an-array") + '''
class Solution {
    func beautifulSplits(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        if n < 3 { return 0 }
        for i in 1..<(n - 1) {
            for j in (i + 1)..<n {
                var ok = false
                if i <= j - i && equal(nums, 0, i, i, i + i) { ok = true }
                if !ok && j - i <= n - j && equal(nums, i, j, j, j + (j - i)) { ok = true }
                if ok { ans += 1 }
            }
        }
        return ans
    }

    private func equal(_ a: [Int], _ as_: Int, _ ae: Int, _ bs: Int, _ be: Int) -> Bool {
        if ae - as_ != be - bs { return false }
        for i in 0..<(ae - as_) where a[as_ + i] != a[bs + i] { return false }
        return true
    }
}
'''

FILES["3389_minimum_operations_to_make_character_frequencies_equal"] = hdr("3389", "Minimum Operations to Make Character Frequencies Equal", "minimum-operations-to-make-character-frequencies-equal") + '''
class Solution {
    func makeStringGood(_ s: String) -> Int {
        var freq = Array(repeating: 0, count: 26)
        for c in s { freq[Int(c.asciiValue! - 97)] += 1 }
        var ans = s.count
        if s.count >= 1 {
            for t in 1...s.count {
                var pool = 0, deficit = 0
                for i in 0..<26 {
                    if freq[i] > t { pool += freq[i] - t }
                    if freq[i] < t { deficit += t - freq[i] }
                }
                ans = min(ans, max(pool, deficit))
            }
        }
        return min(ans, s.count)
    }
}
'''

FILES["3391_design_a_3d_binary_matrix_with_efficient_layer_tracking"] = hdr("3391", "Design a 3D Binary Matrix with Efficient Layer Tracking", "design-a-3d-binary-matrix-with-efficient-layer-tracking") + '''
class Matrix3D {
    private var m: [[[Int]]]
    private var ones: [Int]
    private let n: Int

    init(_ n: Int) {
        self.n = n
        m = Array(repeating: Array(repeating: Array(repeating: 0, count: n), count: n), count: n)
        ones = Array(repeating: 0, count: n)
    }

    func setCell(_ x: Int, _ y: Int, _ z: Int) {
        if m[x][y][z] == 0 {
            m[x][y][z] = 1
            ones[x] += 1
        }
    }

    func unsetCell(_ x: Int, _ y: Int, _ z: Int) {
        if m[x][y][z] == 1 {
            m[x][y][z] = 0
            ones[x] -= 1
        }
    }

    func largestMatrix() -> Int {
        var best = -1, idx = 0
        for i in 0..<n {
            if ones[i] >= best {
                best = ones[i]
                idx = i
            }
        }
        return idx
    }
}
'''

FILES["3392_count_subarrays_of_length_three_with_a_condition"] = hdr("3392", "Count Subarrays of Length Three With a Condition", "count-subarrays-of-length-three-with-a-condition") + '''
class Solution {
    func countSubarrays(_ nums: [Int]) -> Int {
        var ans = 0
        if nums.count >= 3 {
            for i in 0..<(nums.count - 2) {
                if nums[i] * 2 + nums[i + 2] * 2 == nums[i + 1] { ans += 1 }
            }
        }
        return ans
    }
}
'''

FILES["3393_count_paths_with_the_given_xor_value"] = hdr("3393", "Count Paths With the Given XOR Value", "count-paths-with-the-given-xor-value") + '''
class Solution {
    func countPathsWithXorValue(_ grid: [[Int]], _ k: Int) -> Int {
        let mod = 1_000_000_007
        let m = grid.count, n = grid[0].count
        let XOR = 16
        if k >= XOR { return 0 }
        var dp = Array(repeating: Array(repeating: Array(repeating: 0, count: XOR), count: n), count: m)
        dp[0][0][grid[0][0]] = 1
        for i in 0..<m {
            for j in 0..<n {
                for x in 0..<XOR {
                    if dp[i][j][x] == 0 { continue }
                    if i + 1 < m {
                        let nx = x ^ grid[i + 1][j]
                        dp[i + 1][j][nx] = (dp[i + 1][j][nx] + dp[i][j][x]) % mod
                    }
                    if j + 1 < n {
                        let nx = x ^ grid[i][j + 1]
                        dp[i][j + 1][nx] = (dp[i][j + 1][nx] + dp[i][j][x]) % mod
                    }
                }
            }
        }
        return dp[m - 1][n - 1][k]
    }
}
'''

FILES["3394_check_if_grid_can_be_cut_into_sections"] = hdr("3394", "Check if Grid can be Cut into Sections", "check-if-grid-can-be-cut-into-sections") + '''
class Solution {
    func checkValidCuts(_ n: Int, _ rectangles: [[Int]]) -> Bool {
        return checkCut(rectangles, 0) || checkCut(rectangles, 1)
    }

    private func checkCut(_ rects: [[Int]], _ axis: Int) -> Bool {
        var arr = [[Int]]()
        for r in rects {
            if axis == 0 { arr.append([r[0], r[2]]) }
            else { arr.append([r[1], r[3]]) }
        }
        arr.sort { a, b in
            if a[0] == b[0] { return a[1] < b[1] }
            return a[0] < b[0]
        }
        var cuts = 0
        var end = arr[0][1]
        for i in 1..<arr.count {
            if arr[i][0] >= end {
                cuts += 1
                end = arr[i][1]
                if cuts >= 2 { return true }
            } else if arr[i][1] > end {
                end = arr[i][1]
            }
        }
        return false
    }
}
'''

def main():
    for folder, content in FILES.items():
        (ROOT / folder / "Solution.swift").write_text(content.lstrip("\n"))
        print("wrote", folder)
    print("total", len(FILES))

if __name__ == "__main__":
    main()
