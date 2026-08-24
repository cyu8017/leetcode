from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def hdr(num, title, slug):
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n\n"

def write(folder, content):
    (ROOT / folder / "Solution.swift").write_text(content)
    print("W", folder)

FILES = {}

FILES["3961_maximize_sum_of_device_ratings"] = hdr("3961", "Maximize Sum of Device Ratings", "maximize-sum-of-device-ratings") + r'''
class Solution {
    func maxRatings(_ units: [[Int]]) -> Int {
        let n = units[0].count
        if n == 1 {
            var ans = 0
            for x in units { ans += x[0] }
            return ans
        }
        var answer = 0
        var mn = Int.max, mn2 = Int.max
        for x in units {
            var x = x.sorted()
            answer += x[1]
            mn2 = min(mn2, x[1])
            mn = min(mn, x[0])
        }
        return answer - (mn2 - mn)
    }
}
'''

FILES["3962_maximum_subarray_sum_after_at_most_k_swaps"] = hdr("3962", "Maximum Subarray Sum After at Most K Swaps", "maximum-subarray-sum-after-at-most-k-swaps") + r'''
class Solution {
    private var unique: [Int] = []

    func maxSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        unique = nums.sorted()
        var u = 0
        for i in 0..<unique.count {
            if u == 0 || unique[i] != unique[u - 1] {
                unique[u] = unique[i]
                u += 1
            }
        }
        unique = Array(unique.prefix(u))
        var rank = Array(repeating: 0, count: n)
        var globalCount = Array(repeating: 0, count: unique.count + 1)
        var globalSum = Array(repeating: 0, count: unique.count + 1)
        for i in 0..<n {
            rank[i] = lowerBound(unique, nums[i]) + 1
            add(&globalCount, &globalSum, rank[i], 1)
        }
        var answer = -(Int.max / 4)
        for left in 0..<n {
            var insideCount = Array(repeating: 0, count: unique.count + 1)
            var insideSum = Array(repeating: 0, count: unique.count + 1)
            var outsideCount = globalCount
            var outsideSum = globalSum
            var subarraySum = 0
            for right in left..<n {
                add(&outsideCount, &outsideSum, rank[right], -1)
                add(&insideCount, &insideSum, rank[right], 1)
                subarraySum += nums[right]
                let insideSize = right - left + 1
                let outsideSize = n - insideSize
                let limit = min(k, min(insideSize, outsideSize))
                var low = 0, high = limit
                while low < high {
                    let mid = (low + high + 1) / 2
                    let insideValue = unique[kth(insideCount, mid) - 1]
                    let outsideOrder = outsideSize - mid + 1
                    let outsideValue = unique[kth(outsideCount, outsideOrder) - 1]
                    if outsideValue > insideValue { low = mid }
                    else { high = mid - 1 }
                }
                let swaps = low
                var gain = 0
                if swaps > 0 {
                    let smallInside = sumSmallest(insideCount, insideSum, swaps)
                    let totalOutside = querySum(outsideSum, unique.count)
                    let largeOutside = totalOutside - sumSmallest(outsideCount, outsideSum, outsideSize - swaps)
                    gain = largeOutside - smallInside
                }
                answer = max(answer, subarraySum + gain)
            }
        }
        return answer
    }

    private func add(_ count: inout [Int], _ sum: inout [Int], _ index0: Int, _ delta: Int) {
        var index = index0
        let value = unique[index - 1]
        while index < count.count {
            count[index] += delta
            sum[index] += delta * value
            index += index & -index
        }
    }

    private func queryCount(_ bit: [Int], _ index0: Int) -> Int {
        var index = index0, result = 0
        while index > 0 {
            result += bit[index]
            index -= index & -index
        }
        return result
    }

    private func querySum(_ bit: [Int], _ index0: Int) -> Int {
        var index = index0, result = 0
        while index > 0 {
            result += bit[index]
            index -= index & -index
        }
        return result
    }

    private func kth(_ bit: [Int], _ order0: Int) -> Int {
        var order = order0, index = 0, step = 1
        while (step << 1) < bit.count { step <<= 1 }
        while step > 0 {
            let next = index + step
            if next < bit.count && bit[next] < order {
                index = next
                order -= bit[next]
            }
            step >>= 1
        }
        return index + 1
    }

    private func sumSmallest(_ count: [Int], _ sum: [Int], _ amount: Int) -> Int {
        if amount <= 0 { return 0 }
        let index = kth(count, amount)
        let countBefore = queryCount(count, index - 1)
        let sumBefore = querySum(sum, index - 1)
        return sumBefore + (amount - countBefore) * unique[index - 1]
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
'''

FILES["3963_create_grid_with_exactly_one_path"] = hdr("3963", "Create Grid With Exactly One Path", "create-grid-with-exactly-one-path") + r'''
class Solution {
    func createGrid(_ m: Int, _ n: Int) -> [String] {
        var g = [String]()
        for i in 0..<m {
            var row = Array(repeating: Character("#"), count: n)
            if i == 0 {
                for j in 0..<n { row[j] = "." }
            }
            row[n - 1] = "."
            g.append(String(row))
        }
        return g
    }
}
'''

FILES["3964_minimum_lights_to_illuminate_a_road"] = hdr("3964", "Minimum Lights to Illuminate a Road", "minimum-lights-to-illuminate-a-road") + r'''
class Solution {
    func minLights(_ lights: [Int]) -> Int {
        let n = lights.count
        var d = Array(repeating: 0, count: n)
        for i in 0..<n {
            let v = lights[i]
            if v > 0 {
                let l = max(0, i - v)
                let r = min(n - 1, i + v)
                d[l] += 1
                if r + 1 < n { d[r + 1] -= 1 }
            }
        }
        var s = 0, cnt = 0, ans = 0
        for x in d {
            s += x
            if s == 0 { cnt += 1 }
            else {
                ans += (cnt + 2) / 3
                cnt = 0
            }
        }
        ans += (cnt + 2) / 3
        return ans
    }
}
'''

FILES["3965_finish_time_of_tasks_i"] = hdr("3965", "Finish Time of Tasks I", "finish-time-of-tasks-i") + r'''
class Solution {
    func finishTime(_ n: Int, _ edges: [[Int]], _ baseTime: [Int]) -> Int {
        var g = Array(repeating: [Int](), count: n)
        for e in edges { g[e[0]].append(e[1]) }
        func dfs(_ i: Int) -> Int {
            if g[i].isEmpty { return baseTime[i] }
            let INF = Int.max / 4
            var earliest = INF, latest = -INF
            for j in g[i] {
                let a = dfs(j)
                earliest = min(earliest, a)
                latest = max(latest, a)
            }
            let ownDuration = (latest - earliest) + baseTime[i]
            return latest + ownDuration
        }
        return dfs(0)
    }
}
'''

FILES["3966_count_good_integers_in_a_range"] = hdr("3966", "Count Good Integers in a Range", "count-good-integers-in-a-range") + r'''
class Solution {
    func countGoodIntegers(_ l: Int, _ r: Int, _ k: Int) -> Int {
        return count(r, k) - count(l - 1, k)
    }

    private func count(_ bound: Int, _ k: Int) -> Int {
        if bound <= 0 { return 0 }
        let digits = Array(String(bound))
        var memo = [String: Int]()
        func dfs(_ position: Int, _ previous: Int, _ started: Bool, _ tight: Bool) -> Int {
            if position == digits.count { return started ? 1 : 0 }
            let key = "\(position),\(previous),\(started)"
            if !tight, let v = memo[key] { return v }
            let limit = tight ? Int(String(digits[position]))! : 9
            var result = 0
            for digit in 0...limit {
                let nextStarted = started || digit != 0
                if started && abs(previous - digit) > k { continue }
                let nextPrevious = nextStarted ? digit : previous
                result += dfs(position + 1, nextPrevious, nextStarted, tight && digit == limit)
            }
            if !tight { memo[key] = result }
            return result
        }
        return dfs(0, 0, false, true)
    }
}
'''

FILES["3967_finish_time_of_tasks_ii"] = hdr("3967", "Finish Time of Tasks II", "finish-time-of-tasks-ii") + r'''
class Solution {
    private struct Edge {
        var to: Int
        var reverse: Int
    }

    private func combine(_ minimum: Int, _ maximum: Int, _ count: Int, _ base: Int) -> Int {
        if count == 0 { return base }
        return 2 * maximum - minimum + base
    }

    func minFinishTime(_ n: Int, _ edges: [[Int]], _ baseTime: [Int]) -> Int {
        var graph = Array(repeating: [Edge](), count: n)
        for edge in edges {
            let u = edge[0], v = edge[1]
            let iu = graph[u].count, iv = graph[v].count
            graph[u].append(Edge(to: v, reverse: iv))
            graph[v].append(Edge(to: u, reverse: iu))
        }
        var parent = Array(repeating: -2, count: n)
        var parentEdge = Array(repeating: 0, count: n)
        parent[0] = -1
        var order = [0]
        var oi = 0
        while oi < order.count {
            let u = order[oi]
            for edge in graph[u] {
                if parent[edge.to] == -2 {
                    parent[edge.to] = u
                    parentEdge[edge.to] = edge.reverse
                    order.append(edge.to)
                }
            }
            oi += 1
        }
        var incoming = Array(repeating: [Int](), count: n)
        for i in 0..<n { incoming[i] = Array(repeating: 0, count: graph[i].count) }
        for oii in stride(from: n - 1, through: 1, by: -1) {
            let u = order[oii]
            var minimum = Int.max / 4, maximum = -1, count = 0
            for edgeIndex in 0..<incoming[u].count {
                if edgeIndex == parentEdge[u] { continue }
                let value = incoming[u][edgeIndex]
                minimum = min(minimum, value)
                maximum = max(maximum, value)
                count += 1
            }
            let value = combine(minimum, maximum, count, baseTime[u])
            let parentNode = parent[u]
            let reverseIndex = graph[u][parentEdge[u]].reverse
            incoming[parentNode][reverseIndex] = value
        }
        var answer = Int.max / 4
        for u in order {
            var min1 = Int.max / 4, min2 = Int.max / 4, minIndex = -1
            var max1 = -1, max2 = -1, maxIndex = -1
            for i in 0..<incoming[u].count {
                let value = incoming[u][i]
                if value < min1 {
                    min2 = min1
                    min1 = value
                    minIndex = i
                } else if value < min2 {
                    min2 = value
                }
                if value > max1 {
                    max2 = max1
                    max1 = value
                    maxIndex = i
                } else if value > max2 {
                    max2 = value
                }
            }
            let rootValue = combine(min1, max1, graph[u].count, baseTime[u])
            answer = min(answer, rootValue)
            for i in 0..<graph[u].count {
                let edge = graph[u][i]
                if edge.to == parent[u] { continue }
                if graph[u].count == 1 {
                    incoming[edge.to][edge.reverse] = baseTime[u]
                    continue
                }
                var minimum = min1, maximum = max1
                if i == minIndex { minimum = min2 }
                if i == maxIndex { maximum = max2 }
                incoming[edge.to][edge.reverse] = combine(minimum, maximum, graph[u].count - 1, baseTime[u])
            }
        }
        return answer
    }
}
'''

FILES["3968_maximum_manhattan_distance_after_all_moves"] = hdr("3968", "Maximum Manhattan Distance After All Moves", "maximum-manhattan-distance-after-all-moves") + r'''
class Solution {
    func maxDistance(_ moves: String) -> Int {
        var x = 0, y = 0, z = 0
        for c in moves {
            if c == "U" { x -= 1 }
            else if c == "D" { x += 1 }
            else if c == "L" { y -= 1 }
            else if c == "R" { y += 1 }
            else { z += 1 }
        }
        return abs(x) + abs(y) + z
    }
}
'''

FILES["3969_valid_subarrays_with_matching_sum_digits_i"] = hdr("3969", "Valid Subarrays With Matching Sum Digits I", "valid-subarrays-with-matching-sum-digits-i") + r'''
class Solution {
    func countValidSubarrays(_ nums: [Int], _ x: Int) -> Int {
        let n = nums.count
        var ans = 0
        for l in 0..<n {
            var s = 0
            for r in l..<n {
                s += nums[r]
                if s % 10 == x {
                    let t = String(s)
                    if Int(String(t.first!))! == x { ans += 1 }
                }
            }
        }
        return ans
    }
}
'''

FILES["3970_shortest_path_with_at_most_k_consecutive_identical_characters"] = hdr("3970", "Shortest Path With At Most K Consecutive Identical Characters", "shortest-path-with-at-most-k-consecutive-identical-characters") + r'''
class Solution {
    func shortestPath(_ n: Int, _ edges: [[Int]], _ labels: String, _ k: Int) -> Int {
        let labs = Array(labels)
        var graph = Array(repeating: [(Int, Int)](), count: n)
        for edge in edges { graph[edge[0]].append((edge[1], edge[2])) }
        let infinity = Int.max / 4
        var distances = Array(repeating: Array(repeating: infinity, count: k + 1), count: n)
        distances[0][1] = 0
        var pq = [(0, 0, 1)]
        while !pq.isEmpty {
            pq.sort { $0.0 < $1.0 }
            let cur = pq.removeFirst()
            let distance = cur.0, node = cur.1, run = cur.2
            if distance != distances[node][run] { continue }
            if node == n - 1 { return distance }
            for (to, weight) in graph[node] {
                var nextRun = 1
                if labs[node] == labs[to] { nextRun = run + 1 }
                if nextRun > k { continue }
                let nextDistance = distance + weight
                if nextDistance < distances[to][nextRun] {
                    distances[to][nextRun] = nextDistance
                    pq.append((nextDistance, to, nextRun))
                }
            }
        }
        return -1
    }
}
'''

FILES["3971_maximum_total_value"] = hdr("3971", "Maximum Total Value", "maximum-total-value") + r'''
class Solution {
    func maximumTotalValue(_ value: [Int], _ decay: [Int], _ m: Int) -> Int {
        let mod = 1_000_000_007
        func countAtLeast(_ threshold: Int) -> Int {
            var count = 0
            for i in 0..<value.count {
                if value[i] >= threshold {
                    count += (value[i] - threshold) / decay[i] + 1
                }
            }
            return count
        }
        if countAtLeast(1) <= m {
            var sum = 0
            for i in 0..<value.count {
                let terms = (value[i] - 1) / decay[i] + 1
                sum = (sum + terms * value[i] - decay[i] * terms * (terms - 1) / 2) % mod
            }
            return sum
        }
        var high = 0
        for v in value { if v > high { high = v } }
        var low = 1
        while low < high {
            let mid = (low + high + 1) / 2
            if countAtLeast(mid) >= m { low = mid }
            else { high = mid - 1 }
        }
        let threshold = low
        var count = 0, sum = 0
        for i in 0..<value.count {
            if value[i] < threshold { continue }
            let terms = (value[i] - threshold) / decay[i] + 1
            count += terms
            sum = (sum + (terms * value[i] - decay[i] * terms * (terms - 1) / 2) % mod) % mod
        }
        sum = (sum - ((count - m) % mod) * (threshold % mod)) % mod
        if sum < 0 { sum += mod }
        return sum
    }
}
'''

FILES["3972_valid_subarrays_with_matching_sum_digits_ii"] = hdr("3972", "Valid Subarrays With Matching Sum Digits II", "valid-subarrays-with-matching-sum-digits-ii") + r'''
class Solution {
    func countValidSubarrays(_ nums: [Int], _ x: Int) -> Int {
        var byRemainder = Array(repeating: [Int](), count: 10)
        byRemainder[0].append(0)
        var prefix = 0, answer = 0
        func lowerBound(_ a: [Int], _ x: Int) -> Int {
            var lo = 0, hi = a.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if a[mid] < x { lo = mid + 1 }
                else { hi = mid }
            }
            return lo
        }
        func upperBound(_ a: [Int], _ x: Int) -> Int {
            var lo = 0, hi = a.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if a[mid] <= x { lo = mid + 1 }
                else { hi = mid }
            }
            return lo
        }
        for value in nums {
            prefix += value
            let required = ((prefix - x) % 10 + 10) % 10
            let values = byRemainder[required]
            var power = 1
            while x * power <= prefix {
                let low = x * power
                let high = (x + 1) * power - 1
                let minPrefix = prefix - high, maxPrefix = prefix - low
                let left = lowerBound(values, minPrefix)
                let right = upperBound(values, maxPrefix)
                answer += right - left
                if power > prefix / 10 { break }
                power *= 10
            }
            byRemainder[prefix % 10].append(prefix)
        }
        return answer
    }
}
'''

FILES["3973_distinct_gate_paths_to_lca"] = hdr("3973", "Distinct Gate Paths to LCA", "distinct-gate-paths-to-lca") + r'''
class Solution {
    private let MOD = 1_000_000_007

    private func multiply(_ a: [[Int]], _ b: [[Int]]) -> [[Int]] {
        var c = [[0, 0], [0, 0]]
        for i in 0..<2 {
            for j in 0..<2 {
                for k in 0..<2 {
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD
                }
            }
        }
        return c
    }

    func gatePathXor(_ n: Int, _ parent: [Int], _ gates: [[Int]], _ queries: [[Int]]) -> Int {
        var logn = 1
        while (1 << logn) <= n { logn += 1 }
        var up = Array(repeating: Array(repeating: 0, count: n), count: logn)
        var product = Array(repeating: Array(repeating: [[0, 0], [0, 0]], count: n), count: logn)
        var children = Array(repeating: [Int](), count: n)
        for node in 1..<n { children[parent[node]].append(node) }
        var depth = Array(repeating: 0, count: n)
        var order = [0]
        var oi = 0
        while oi < order.count {
            let u = order[oi]
            for v in children[u] {
                depth[v] = depth[u] + 1
                order.append(v)
            }
            oi += 1
        }
        for u in 0..<n {
            up[0][u] = (u == 0) ? 0 : parent[u]
            product[0][u] = [
                [gates[u][1], gates[u][2]],
                [gates[u][2], gates[u][0]]
            ]
        }
        for level in 1..<logn {
            for u in 0..<n {
                let mid = up[level - 1][u]
                up[level][u] = up[level - 1][mid]
                product[level][u] = multiply(product[level - 1][u], product[level - 1][mid])
            }
        }
        func liftNode(_ node0: Int, _ distance0: Int) -> Int {
            var node = node0, distance = distance0, level = 0
            while distance > 0 {
                if (distance & 1) != 0 { node = up[level][node] }
                distance >>= 1
                level += 1
            }
            return node
        }
        func lca(_ a0: Int, _ b0: Int) -> Int {
            var a = a0, b = b0
            if depth[a] > depth[b] { a = liftNode(a, depth[a] - depth[b]) }
            else if depth[b] > depth[a] { b = liftNode(b, depth[b] - depth[a]) }
            if a == b { return a }
            for level in stride(from: logn - 1, through: 0, by: -1) {
                if up[level][a] != up[level][b] {
                    a = up[level][a]
                    b = up[level][b]
                }
            }
            return up[0][a]
        }
        func ways(_ node0: Int, _ card: Int, _ distance0: Int) -> Int {
            var node = node0, distance = distance0
            var vector = [0, 0]
            vector[card] = 1
            var level = 0
            while distance > 0 {
                if (distance & 1) != 0 {
                    let matrix = product[level][node]
                    vector = [
                        (vector[0] * matrix[0][0] + vector[1] * matrix[1][0]) % MOD,
                        (vector[0] * matrix[0][1] + vector[1] * matrix[1][1]) % MOD
                    ]
                    node = up[level][node]
                }
                distance >>= 1
                level += 1
            }
            return (vector[0] + vector[1]) % MOD
        }
        var answer = 0
        for query in queries {
            let ancestor = lca(query[0], query[2])
            let alice = ways(query[0], query[1], depth[query[0]] - depth[ancestor])
            let bob = ways(query[2], query[3], depth[query[2]] - depth[ancestor])
            let total = alice * bob % MOD
            answer ^= total
        }
        return answer
    }
}
'''

FILES["3974_maximum_total_sum_of_k_selected_elements"] = hdr("3974", "Maximum Total Sum of K Selected Elements", "maximum-total-sum-of-k-selected-elements") + r'''
class Solution {
    func maxSum(_ nums: [Int], _ k: Int, _ mul: Int) -> Int {
        let nums = nums.sorted()
        let n = nums.count
        var ans = 0
        var mul = mul
        for i in stride(from: n - 1, through: n - k, by: -1) {
            let m = max(1, mul)
            ans += nums[i] * m
            mul -= 1
        }
        return ans
    }
}
'''

FILES["3975_filter_occupied_intervals"] = hdr("3975", "Filter Occupied Intervals", "filter-occupied-intervals") + r'''
class Solution {
    func filterOccupiedIntervals(_ occupiedIntervals: [[Int]], _ freeStart: Int, _ freeEnd: Int) -> [[Int]] {
        var occupied = occupiedIntervals.sorted { $0[0] < $1[0] }
        var busy = [[occupied[0][0], occupied[0][1]]]
        for i in 1..<occupied.count {
            let cur = occupied[i]
            if busy[busy.count - 1][1] + 1 < cur[0] {
                busy.append([cur[0], cur[1]])
            } else if cur[1] > busy[busy.count - 1][1] {
                busy[busy.count - 1][1] = cur[1]
            }
        }
        var ans = [[Int]]()
        for it in busy {
            let s = it[0], e = it[1]
            if e < freeStart || s > freeEnd {
                ans.append([s, e])
            } else {
                if s < freeStart { ans.append([s, freeStart - 1]) }
                if e > freeEnd { ans.append([freeEnd + 1, e]) }
            }
        }
        return ans
    }
}
'''

FILES["3976_maximum_subarray_sum_after_multiplier"] = hdr("3976", "Maximum Subarray Sum After Multiplier", "maximum-subarray-sum-after-multiplier") + r'''
class Solution {
    func maxSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        let inf = Int.min / 4
        var f = Array(repeating: Array(repeating: inf, count: 4), count: n + 1)
        f[0][0] = 0
        var ans = inf
        for i in 1...n {
            let x = nums[i - 1]
            f[i][0] = max(f[i - 1][0], 0) + x
            f[i][1] = max(max(f[i - 1][0], f[i - 1][1]), 0) + x * k
            f[i][2] = max(max(f[i - 1][0], f[i - 1][2]), 0) + x / k
            f[i][3] = max(max(f[i - 1][1], f[i - 1][2]), f[i - 1][3]) + x
            ans = max(ans, max(max(f[i][0], f[i][1]), max(f[i][2], f[i][3])))
        }
        return ans
    }
}
'''

FILES["3977_minimum_time_to_reach_target_with_limited_power"] = hdr("3977", "Minimum Time to Reach Target With Limited Power", "minimum-time-to-reach-target-with-limited-power") + r'''
class Solution {
    func minTimeMaxPower(_ n: Int, _ edges: [[Int]], _ power: Int, _ cost: [Int], _ source: Int, _ target: Int) -> [Int] {
        let INF = Int.max / 4
        var g = Array(repeating: [(Int, Int)](), count: n)
        for e in edges { g[e[0]].append((e[1], e[2])) }
        var dist = Array(repeating: Array(repeating: INF, count: power + 1), count: n)
        var pq = [(0, -power, source)]
        dist[source][power] = 0
        while !pq.isEmpty {
            pq.sort {
                if $0.0 != $1.0 { return $0.0 < $1.0 }
                return $0.1 < $1.1
            }
            let cur = pq.removeFirst()
            let d = cur.0
            var p = -cur.1
            let u = cur.2
            if u == target { return [d, p] }
            if d > dist[u][p] || p < cost[u] { continue }
            p -= cost[u]
            for (v, t) in g[u] {
                let nd = d + t
                if nd < dist[v][p] {
                    dist[v][p] = nd
                    pq.append((nd, -p, v))
                }
            }
        }
        return [-1, -1]
    }
}
'''

FILES["3978_unique_middle_element"] = hdr("3978", "Unique Middle Element", "unique-middle-element") + r'''
class Solution {
    func isMiddleElementUnique(_ nums: [Int]) -> Bool {
        let mid = nums[nums.count / 2]
        var cnt = 0
        for x in nums { if x == mid { cnt += 1 } }
        return cnt == 1
    }
}
'''

FILES["3979_maximum_valid_pair_sum"] = hdr("3979", "Maximum Valid Pair Sum", "maximum-valid-pair-sum") + r'''
class Solution {
    func maxValidPairSum(_ nums: [Int], _ k: Int) -> Int {
        var ans = 0, x = 0
        if k < nums.count {
            for j in k..<nums.count {
                let y = nums[j]
                x = max(x, nums[j - k])
                ans = max(ans, x + y)
            }
        }
        return ans
    }
}
'''

FILES["3980_minimum_operations_to_transform_binary_string"] = hdr("3980", "Minimum Operations to Transform Binary String", "minimum-operations-to-transform-binary-string") + r'''
class Solution {
    func minOperations(_ s1: String, _ s2: String) -> Int {
        let a = Array(s1), b = Array(s2)
        let infinity = 1_000_000_000
        var dp = [0, infinity]
        let n = a.count
        for i in 0..<n {
            var next = [infinity, infinity]
            for forcedZero in 0...1 {
                if dp[forcedZero] == infinity { continue }
                var current = a[i]
                if forcedZero == 1 { current = "0" }
                var direct = dp[forcedZero]
                if current == "0" && b[i] == "1" { direct += 1 }
                else if current == "1" && b[i] == "0" { direct = infinity }
                next[0] = min(next[0], direct)
                if i + 1 < n {
                    var cost = dp[forcedZero] + 1
                    if current == "0" { cost += 1 }
                    if a[i + 1] == "0" { cost += 1 }
                    if b[i] == "1" { cost += 1 }
                    next[1] = min(next[1], cost)
                }
            }
            dp = next
        }
        return dp[0] == infinity ? -1 : dp[0]
    }
}
'''

FILES["3981_count_distinct_ways_to_form_target_from_two_strings"] = hdr("3981", "Count Distinct Ways to Form Target from Two Strings", "count-distinct-ways-to-form-target-from-two-strings") + r'''
class Solution {
    func countWays(_ word1: String, _ word2: String, _ target: String) -> Int {
        let mod = 1_000_000_007
        let w1 = Array(word1), w2 = Array(word2), t = Array(target)
        let n1 = w1.count, n2 = w2.count
        func idx(_ i: Int, _ j: Int, _ mask: Int) -> Int {
            ((i * (n2 + 1) + j) * 4) + mask
        }
        let size = (n1 + 1) * (n2 + 1) * 4
        var dp = Array(repeating: 0, count: size)
        var next = Array(repeating: 0, count: size)
        dp[idx(0, 0, 0)] = 1
        for ti in 0..<t.count {
            let ch = t[ti]
            next = Array(repeating: 0, count: size)
            for j in 0...n2 {
                var prefix = Array(repeating: 0, count: 4)
                for a in 0..<n1 {
                    for mask in 0..<4 {
                        prefix[mask] += dp[idx(a, j, mask)]
                        if prefix[mask] >= mod { prefix[mask] -= mod }
                    }
                    if w1[a] == ch {
                        for mask in 0..<4 {
                            let at = idx(a + 1, j, mask | 1)
                            next[at] += prefix[mask]
                            if next[at] >= mod { next[at] -= mod }
                        }
                    }
                }
            }
            for i in 0...n1 {
                var prefix = Array(repeating: 0, count: 4)
                for b in 0..<n2 {
                    for mask in 0..<4 {
                        prefix[mask] += dp[idx(i, b, mask)]
                        if prefix[mask] >= mod { prefix[mask] -= mod }
                    }
                    if w2[b] == ch {
                        for mask in 0..<4 {
                            let at = idx(i, b + 1, mask | 2)
                            next[at] += prefix[mask]
                            if next[at] >= mod { next[at] -= mod }
                        }
                    }
                }
            }
            swap(&dp, &next)
        }
        var answer = 0
        for i in 0...n1 {
            for j in 0...n2 {
                answer += dp[idx(i, j, 3)]
                if answer >= mod { answer -= mod }
            }
        }
        return answer
    }
}
'''

FILES["3982_sum_of_integers_with_maximum_digit_range"] = hdr("3982", "Sum of Integers with Maximum Digit Range", "sum-of-integers-with-maximum-digit-range") + r'''
class Solution {
    func maxDigitRange(_ nums: [Int]) -> Int {
        var mx = 0, ans = 0
        for x in nums {
            var a = 10, b = 0, y = x
            while y > 0 {
                let v = y % 10
                a = min(a, v)
                b = max(b, v)
                y /= 10
            }
            let r = b - a
            if mx < r {
                mx = r
                ans = x
            } else if mx == r {
                ans += x
            }
        }
        return ans
    }
}
'''

FILES["3983_subsequence_after_one_replacement"] = hdr("3983", "Subsequence After One Replacement", "subsequence-after-one-replacement") + r'''
class Solution {
    func canMakeSubsequence(_ s: String, _ t: String) -> Bool {
        let s = Array(s), t = Array(t)
        let m = s.count, n = t.count
        var i0 = 0, i1 = 0, j = 0
        while i1 < m && j < n {
            if s[i1] == t[j] { i1 += 1 }
            if i1 < i0 + 1 { i1 = i0 + 1 }
            if s[i0] == t[j] { i0 += 1 }
            j += 1
        }
        return i1 == m
    }
}
'''

FILES["3984_divisible_game"] = hdr("3984", "Divisible Game", "divisible-game") + r'''
class Solution {
    func divisibleGame(_ nums: [Int]) -> Int {
        var candidates = Set<Int>()
        candidates.insert(2)
        for value in nums {
            var divisor = 2
            while divisor * divisor <= value {
                if value % divisor == 0 {
                    candidates.insert(divisor)
                    candidates.insert(value / divisor)
                }
                divisor += 1
            }
            if value > 1 { candidates.insert(value) }
        }
        var bestScore = -(Int.max / 4)
        var bestK = 0
        for k in candidates {
            var ending = 0, score = 0
            for i in 0..<nums.count {
                let value = nums[i]
                var contribution = -value
                if value % k == 0 { contribution = value }
                if i == 0 || ending + contribution < contribution { ending = contribution }
                else { ending += contribution }
                if i == 0 || ending > score { score = ending }
            }
            if score > bestScore || (score == bestScore && k < bestK) {
                bestScore = score
                bestK = k
            }
        }
        let mod = 1_000_000_007
        var answer = (bestScore % mod) * bestK % mod
        if answer < 0 { answer += mod }
        return answer
    }
}
'''

FILES["3985_palindromic_subarray_sum"] = hdr("3985", "Palindromic Subarray Sum", "palindromic-subarray-sum") + r'''
class Solution {
    func maxPalindromicSubarraySum(_ nums: [Int]) -> Int {
        let n = nums.count
        var prefix = Array(repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + nums[i] }
        var odd = Array(repeating: 0, count: n)
        var left = 0, right = -1
        for i in 0..<n {
            var radius = 1
            if i <= right {
                let mirror = left + right - i
                radius = odd[mirror]
                if right - i + 1 < radius { radius = right - i + 1 }
            }
            while i - radius >= 0 && i + radius < n && nums[i - radius] == nums[i + radius] {
                radius += 1
            }
            odd[i] = radius
            if i + radius - 1 > right {
                left = i - radius + 1
                right = i + radius - 1
            }
        }
        var even = Array(repeating: 0, count: n)
        left = 0; right = -1
        for i in 0..<n {
            var radius = 0
            if i <= right {
                let mirror = left + right - i + 1
                radius = even[mirror]
                if right - i + 1 < radius { radius = right - i + 1 }
            }
            while i - radius - 1 >= 0 && i + radius < n && nums[i - radius - 1] == nums[i + radius] {
                radius += 1
            }
            even[i] = radius
            if i + radius - 1 > right {
                left = i - radius
                right = i + radius - 1
            }
        }
        var answer = 0
        for i in 0..<n {
            var sum = prefix[i + odd[i]] - prefix[i - odd[i] + 1]
            if sum > answer { answer = sum }
            if even[i] > 0 {
                sum = prefix[i + even[i]] - prefix[i - even[i]]
                if sum > answer { answer = sum }
            }
        }
        return answer
    }
}
'''

FILES["3986_number_of_elapsed_seconds_between_two_times"] = hdr("3986", "Number of Elapsed Seconds Between Two Times", "number-of-elapsed-seconds-between-two-times") + r'''
class Solution {
    func secondsBetweenTimes(_ startTime: String, _ endTime: String) -> Int {
        func toSeconds(_ s: String) -> Int {
            let c = Array(s)
            let h = (Int(String(c[0]))! * 10) + Int(String(c[1]))!
            let m = (Int(String(c[3]))! * 10) + Int(String(c[4]))!
            let sec = (Int(String(c[6]))! * 10) + Int(String(c[7]))!
            return h * 3600 + m * 60 + sec
        }
        return toSeconds(endTime) - toSeconds(startTime)
    }
}
'''

FILES["3987_minimum_total_cost_to_process_all_elements"] = hdr("3987", "Minimum Total Cost to Process All Elements", "minimum-total-cost-to-process-all-elements") + r'''
class Solution {
    func minimumCost(_ nums: [Int], _ k: Int) -> Int {
        let mod = 1_000_000_007
        var cnt = 0
        var cur = k
        for x0 in nums {
            let x = x0
            let diff = x - cur
            if diff > 0 {
                let m = (diff + k - 1) / k
                cur += m * k
                cnt += m
            }
            cur -= x
        }
        cnt %= mod
        return ((cnt + 1) * cnt / 2) % mod
    }
}
'''

FILES["3988_create_grid_with_exactly_k_paths_i"] = hdr("3988", "Create Grid With Exactly K Paths I", "create-grid-with-exactly-k-paths-i") + r'''
class Solution {
    func createGrid(_ m: Int, _ n: Int, _ k: Int) -> [String] {
        var cands = [[String]]()
        if k == 1 { cands.append(["."]) }
        else if k == 2 { cands.append(["..", ".."]) }
        else if k == 3 {
            cands.append(["..", "..", ".."])
            cands.append(["...", "..."])
        } else if k == 4 {
            cands.append(["..", "..", "..", ".."])
            cands.append(["....", "...."])
            cands.append(["..#", "...", "#.."])
        }
        for pat in cands {
            let pr = pat.count, pc = pat[0].count
            if pr > m || pc > n { continue }
            var result = [String]()
            for _ in 0..<m {
                result.append(String(repeating: "#", count: n))
            }
            for i in 0..<pr {
                var row = Array(result[i])
                let p = Array(pat[i])
                for j in 0..<pc { row[j] = p[j] }
                result[i] = String(row)
            }
            if pr < m {
                for i in pr..<m {
                    var row = Array(result[i])
                    row[pc - 1] = "."
                    result[i] = String(row)
                }
            }
            if pc < n {
                var row = Array(result[m - 1])
                for j in pc..<n { row[j] = "." }
                result[m - 1] = String(row)
            }
            return result
        }
        return []
    }
}
'''

FILES["3989_maximum_consistent_columns_in_a_grid"] = hdr("3989", "Maximum Consistent Columns in a Grid", "maximum-consistent-columns-in-a-grid") + r'''
class Solution {
    func maxConsistentColumns(_ grid: [[Int]], _ limit: Int) -> Int {
        let m = grid.count, n = grid[0].count
        var dp = Array(repeating: 0, count: n)
        var ans = 1
        for j in 0..<n {
            dp[j] = 1
            for i in 0..<j {
                if dp[i] + 1 <= dp[j] { continue }
                var ok = true
                for r in 0..<m {
                    if abs(grid[r][j] - grid[r][i]) > limit { ok = false; break }
                }
                if ok { dp[j] = dp[i] + 1 }
            }
            if dp[j] > ans { ans = dp[j] }
        }
        return ans
    }
}
'''

for folder, content in FILES.items():
    write(folder, content)
print("done", len(FILES))
