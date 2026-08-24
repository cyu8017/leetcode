from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def hdr(num, title, slug):
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n\n"

def write(folder, content):
    p = ROOT / folder / "Solution.swift"
    p.write_text(content)
    print("W", folder, p.stat().st_size)

FILES = {}

FILES["3924_minimum_threshold_path_with_limited_heavy_edges"] = hdr("3924", "Minimum Threshold Path With Limited Heavy Edges", "minimum-threshold-path-with-limited-heavy-edges") + r'''
class Solution {
    func minThreshold(_ n: Int, _ edges: [[Int]], _ source: Int, _ target: Int, _ k: Int) -> Int {
        if source == target { return 0 }
        var g = Array(repeating: [(Int, Int)](), count: n)
        var maxWeight = 0
        for e in edges {
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
            maxWeight = max(maxWeight, e[2])
        }
        func can(_ threshold: Int) -> Bool {
            let inf = 1_000_000_000
            var dist = Array(repeating: inf, count: n)
            dist[source] = 0
            var dq = [source]
            var head = 0
            while head < dq.count {
                let u = dq[head]; head += 1
                for (to, weight) in g[u] {
                    let cost = weight > threshold ? 1 : 0
                    if dist[u] + cost >= dist[to] || dist[u] + cost > k { continue }
                    dist[to] = dist[u] + cost
                    if cost == 0 {
                        dq.insert(to, at: head)
                    } else {
                        dq.append(to)
                    }
                }
            }
            return dist[target] <= k
        }
        if !can(maxWeight) { return -1 }
        var lo = 0, hi = maxWeight
        while lo < hi {
            let mid = lo + (hi - lo) / 2
            if can(mid) { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }
}
'''

FILES["3925_concatenate_array_with_reverse"] = hdr("3925", "Concatenate Array With Reverse", "concatenate-array-with-reverse") + r'''
class Solution {
    func concatWithReverse(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var ans = Array(repeating: 0, count: 2 * n)
        for i in 0..<n {
            ans[i] = nums[i]
            ans[i + n] = nums[n - i - 1]
        }
        return ans
    }
}
'''

FILES["3926_count_valid_word_occurrences"] = hdr("3926", "Count Valid Word Occurrences", "count-valid-word-occurrences") + r'''
class Solution {
    func countWordOccurrences(_ chunks: [String], _ queries: [String]) -> [Int] {
        let s = Array(chunks.joined())
        let n = s.count
        var cnt = [String: Int]()
        var i = 0
        while i < n {
            if s[i] == " " || s[i] == "-" {
                i += 1
                continue
            }
            var j = i
            while j < n && s[j] != " " && (s[j] != "-" || (j + 1 < n && s[j + 1] != " " && s[j + 1] != "-")) {
                j += 1
            }
            let word = String(s[i..<j])
            cnt[word, default: 0] += 1
            i = j
        }
        return queries.map { cnt[$0, default: 0] }
    }
}
'''

FILES["3927_minimize_array_sum_using_divisible_replacements"] = hdr("3927", "Minimize Array Sum Using Divisible Replacements", "minimize-array-sum-using-divisible-replacements") + r'''
class Solution {
    func minArraySum(_ nums: [Int]) -> Int {
        var maximum = 0
        var present = Array(repeating: false, count: 100001)
        for value in nums {
            present[value] = true
            if value > maximum { maximum = value }
        }
        var best = Array(repeating: 0, count: maximum + 1)
        for divisor in 1...max(1, maximum) {
            if divisor > maximum { break }
            if !present[divisor] { continue }
            var multiple = divisor
            while multiple <= maximum {
                if best[multiple] == 0 { best[multiple] = divisor }
                multiple += divisor
            }
        }
        var answer = 0
        for value in nums { answer += best[value] }
        return answer
    }
}
'''

FILES["3928_minimum_cost_to_buy_apples_ii"] = hdr("3928", "Minimum Cost to Buy Apples II", "minimum-cost-to-buy-apples-ii") + r'''
class Solution {
    func minCostToBuyApples(_ n: Int, _ prices: [Int], _ roads: [[Int]]) -> [Int] {
        var g = Array(repeating: [(to: Int, empty: Int, full: Int)](), count: n)
        for road in roads {
            let empty = road[2], full = road[2] * road[3]
            g[road[0]].append((road[1], empty, full))
            g[road[1]].append((road[0], empty, full))
        }
        let inf = Int.max / 4
        func dijkstra(_ source: Int, _ carrying: Bool) -> [Int] {
            var dist = Array(repeating: inf, count: n)
            dist[source] = 0
            var heap = [(0, source)]
            while !heap.isEmpty {
                heap.sort { $0.0 < $1.0 }
                let cur = heap.removeFirst()
                let d = cur.0, node = cur.1
                if d != dist[node] { continue }
                for e in g[node] {
                    let weight = carrying ? e.full : e.empty
                    let next = d + weight
                    if next < dist[e.to] {
                        dist[e.to] = next
                        heap.append((next, e.to))
                    }
                }
            }
            return dist
        }
        var answer = Array(repeating: 0, count: n)
        for source in 0..<n {
            let emptyDist = dijkstra(source, false)
            let fullDist = dijkstra(source, true)
            var best = prices[source]
            for shop in 0..<n {
                if emptyDist[shop] == inf || fullDist[shop] == inf { continue }
                let total = emptyDist[shop] + fullDist[shop] + prices[shop]
                if total < best { best = total }
            }
            answer[source] = best
        }
        return answer
    }
}
'''

FILES["3929_minimum_partition_score_ii"] = hdr("3929", "Minimum Partition Score II", "minimum-partition-score-ii") + r'''
class Solution {
    private struct Line {
        var slope: Int
        var intercept: Int
        var count: Int
        var valid: Bool
        init() { slope = 0; intercept = 0; count = 0; valid = false }
        init(_ slope: Int, _ intercept: Int, _ count: Int, _ valid: Bool) {
            self.slope = slope; self.intercept = intercept; self.count = count; self.valid = valid
        }
    }
    private struct State {
        var value: Int
        var count: Int
        var valid: Bool
        init() { value = 0; count = 0; valid = false }
        init(_ value: Int, _ count: Int, _ valid: Bool) {
            self.value = value; self.count = count; self.valid = valid
        }
    }

    private var prefix: [Int] = []
    private var n = 0

    private func better(_ a: State, _ b: State) -> State {
        if !a.valid { return b }
        if !b.valid { return a }
        if a.value != b.value { return a.value < b.value ? a : b }
        return a.count >= b.count ? a : b
    }

    private func evaluate(_ line: Line, _ x: Int) -> State {
        if !line.valid { return State() }
        return State(line.slope * x + line.intercept, line.count, true)
    }

    private func insert(_ tree: inout [Line], _ node: Int, _ left: Int, _ right: Int, _ lineIn: Line) {
        var line = lineIn
        if !tree[node].valid {
            tree[node] = line
            return
        }
        let mid = (left + right) / 2
        let xLeft = prefix[left]
        let leftBetter = better(evaluate(line, xLeft), evaluate(tree[node], xLeft))
        let midBetter = better(evaluate(line, prefix[mid]), evaluate(tree[node], prefix[mid]))
        let lineWinsLeft = leftBetter.value == evaluate(line, xLeft).value && leftBetter.count == line.count
        let lineWinsMid = midBetter.value == evaluate(line, prefix[mid]).value && midBetter.count == line.count
        if lineWinsMid {
            let tmp = tree[node]
            tree[node] = line
            line = tmp
        }
        if left == right { return }
        if lineWinsLeft != lineWinsMid {
            insert(&tree, node * 2, left, mid, line)
        } else {
            insert(&tree, node * 2 + 1, mid + 1, right, line)
        }
    }

    private func query(_ tree: [Line], _ node: Int, _ left: Int, _ right: Int, _ index: Int) -> State {
        let result = evaluate(tree[node], prefix[index])
        if left == right { return result }
        let mid = (left + right) / 2
        if index <= mid { return better(result, query(tree, node * 2, left, mid, index)) }
        return better(result, query(tree, node * 2 + 1, mid + 1, right, index))
    }

    private func run(_ penalty: Int) -> State {
        var tree = Array(repeating: Line(), count: 4 * (n + 1))
        insert(&tree, 1, 0, n, Line(0, 0, 0, true))
        var current = State()
        for i in 1...n {
            let best = query(tree, 1, 0, n, i)
            let x = prefix[i]
            current = State(best.value + x * x + x + penalty, best.count + 1, true)
            insert(&tree, 1, 0, n, Line(-2 * x, current.value + x * x - x, current.count, true))
        }
        return current
    }

    func minPartitionScore(_ nums: [Int], _ k: Int) -> Int {
        n = nums.count
        prefix = Array(repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + nums[i] }
        let bound = prefix[n] * prefix[n] + prefix[n] + 1
        var low = 0, high = bound
        while low < high {
            let mid = low + (high - low + 1) / 2
            if run(mid).count >= k { low = mid }
            else { high = mid - 1 }
        }
        let state = run(low)
        return (state.value - low * k) / 2
    }
}
'''

FILES["3930_power_update_after_k_th_largest_insertion_ii"] = hdr("3930", "Power Update After K-th Largest Insertion II", "power-update-after-k-th-largest-insertion-ii") + r'''
class Solution {
    func powerUpdate(_ nums: [Int], _ p: Int, _ queries: [[Int]]) -> [Int] {
        let mod = 1_000_000_007
        var vals = nums + queries.map { $0[0] }
        vals.sort()
        var uniq = 0
        for i in 0..<vals.count {
            if uniq == 0 || vals[i] != vals[uniq - 1] {
                vals[uniq] = vals[i]
                uniq += 1
            }
        }
        vals = Array(vals.prefix(uniq))
        var bit = Array(repeating: 0, count: vals.count + 1)
        func add(_ i0: Int) {
            var i = i0
            while i < bit.count {
                bit[i] += 1
                i += i & -i
            }
        }
        func lowerBound(_ x: Int) -> Int {
            var lo = 0, hi = vals.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if vals[mid] < x { lo = mid + 1 }
                else { hi = mid }
            }
            return lo
        }
        func kth(_ rank0: Int) -> Int {
            var rank = rank0
            var idx = 0
            var step = 1
            while (step << 1) < bit.count { step <<= 1 }
            while step > 0 {
                let next = idx + step
                if next < bit.count && bit[next] < rank {
                    idx = next
                    rank -= bit[next]
                }
                step >>= 1
            }
            return vals[idx]
        }
        func powm(_ a0: Int, _ e0: Int) -> Int {
            var a = a0 % mod, e = e0, res = 1
            while e > 0 {
                if e & 1 != 0 { res = res * a % mod }
                a = a * a % mod
                e >>= 1
            }
            return res
        }
        for x in nums { add(lowerBound(x) + 1) }
        var ans = Array(repeating: 0, count: queries.count)
        var size = nums.count
        var cur = p
        for i in 0..<queries.count {
            add(lowerBound(queries[i][0]) + 1)
            size += 1
            let x = kth(size - queries[i][1] + 1)
            cur = powm(cur, x)
            ans[i] = cur
        }
        return ans
    }
}
'''

FILES["3931_check_adjacent_digit_differences"] = hdr("3931", "Check Adjacent Digit Differences", "check-adjacent-digit-differences") + r'''
class Solution {
    func isAdjacentDiffAtMostTwo(_ s: String) -> Bool {
        let chars = Array(s)
        for i in 1..<chars.count {
            let a = Int(chars[i - 1].asciiValue!)
            let b = Int(chars[i].asciiValue!)
            if abs(a - b) > 2 { return false }
        }
        return true
    }
}
'''

FILES["3932_count_k_th_roots_in_a_range"] = hdr("3932", "Count K-th Roots in a Range", "count-k-th-roots-in-a-range") + r'''
class Solution {
    func countKthRoots(_ l: Int, _ r: Int, _ k: Int) -> Int {
        if k == 1 { return r - l + 1 }
        var ans = 0
        var x = 0
        while true {
            var y = 1
            var tooBig = false
            for _ in 0..<k {
                if x != 0 && y > r / x {
                    tooBig = true
                    break
                }
                y *= x
                if y > r { break }
            }
            if tooBig || y > r { break }
            if l <= y && y <= r { ans += 1 }
            x += 1
        }
        return ans
    }
}
'''

FILES["3933_largest_local_values_in_a_matrix_ii"] = hdr("3933", "Largest Local Values in a Matrix II", "largest-local-values-in-a-matrix-ii") + r'''
class Solution {
    func countLocalMaximums(_ matrix: [[Int]]) -> Int {
        let rows = matrix.count, cols = matrix[0].count
        var positions = Array(repeating: [(Int, Int)](), count: 201)
        for row in 0..<rows {
            for col in 0..<cols {
                let value = matrix[row][col]
                if value > 0 { positions[value].append((row, col)) }
            }
        }
        var answer = 0
        for value in 1...200 {
            if positions[value].isEmpty { continue }
            var prefix = Array(repeating: Array(repeating: 0, count: cols + 1), count: rows + 1)
            for row in 0..<rows {
                for col in 0..<cols {
                    let add = matrix[row][col] > value ? 1 : 0
                    prefix[row + 1][col + 1] = prefix[row][col + 1] + prefix[row + 1][col] - prefix[row][col] + add
                }
            }
            for (row, col) in positions[value] {
                let top = max(0, row - value), bottom = min(rows - 1, row + value)
                let left = max(0, col - value), right = min(cols - 1, col + value)
                var greater = prefix[bottom + 1][right + 1] - prefix[top][right + 1] - prefix[bottom + 1][left] + prefix[top][left]
                for dr in [-value, value] {
                    for dc in [-value, value] {
                        let rr = row + dr, cc = col + dc
                        if rr >= 0 && rr < rows && cc >= 0 && cc < cols && matrix[rr][cc] > value {
                            greater -= 1
                        }
                    }
                }
                if greater == 0 { answer += 1 }
            }
        }
        return answer
    }
}
'''

FILES["3934_smallest_unique_subarray"] = hdr("3934", "Smallest Unique Subarray", "smallest-unique-subarray") + r'''
class Solution {
    func smallestUniqueSubarray(_ nums: [Int]) -> Int {
        let n = nums.count
        var sa = Array(0..<n)
        var rank = nums
        var width = 1
        while width < n {
            let w = width
            let r = rank
            sa.sort { a, b in
                if r[a] != r[b] { return r[a] < r[b] }
                let ra = a + w < n ? r[a + w] : -1
                let rb = b + w < n ? r[b + w] : -1
                return ra < rb
            }
            var next = Array(repeating: 0, count: n)
            for i in 1..<n {
                let a = sa[i - 1], b = sa[i]
                let different = rank[a] != rank[b]
                let ra = a + width < n ? rank[a + width] : -1
                let rb = b + width < n ? rank[b + width] : -1
                next[b] = (different || ra != rb) ? next[a] + 1 : next[a]
            }
            rank = next
            if rank[sa[n - 1]] == n - 1 { break }
            width <<= 1
        }
        var pos = Array(repeating: 0, count: n)
        for i in 0..<n { pos[sa[i]] = i }
        var lcp = Array(repeating: 0, count: max(0, n - 1))
        var height = 0
        for i in 0..<n {
            let p = pos[i]
            if p == n - 1 {
                height = 0
                continue
            }
            let j = sa[p + 1]
            while i + height < n && j + height < n && nums[i + height] == nums[j + height] {
                height += 1
            }
            lcp[p] = height
            if height > 0 { height -= 1 }
        }
        var ans = n
        for p in 0..<n {
            let start = sa[p]
            var need = 1
            if p > 0 && lcp[p - 1] + 1 > need { need = lcp[p - 1] + 1 }
            if p + 1 < n && lcp[p] + 1 > need { need = lcp[p] + 1 }
            if need <= n - start && need < ans { ans = need }
        }
        return ans
    }
}
'''

FILES["3935_power_update_after_k_th_largest_insertion_i"] = hdr("3935", "Power Update After K-th Largest Insertion I", "power-update-after-k-th-largest-insertion-i") + r'''
class Solution {
    func powerUpdate(_ nums: [Int], _ p: Int, _ queries: [[Int]]) -> [Int] {
        var L = [Int: Int]()
        var R = [Int: Int]()
        func merge(_ st: inout [Int: Int], _ x: Int, _ v: Int) {
            let c = st[x, default: 0]
            if c + v == 0 { st.removeValue(forKey: x) }
            else { st[x] = c + v }
        }
        func firstKey(_ st: [Int: Int]) -> Int { st.keys.min()! }
        func lastKey(_ st: [Int: Int]) -> Int { st.keys.max()! }
        var sz1 = 0, sz2 = nums.count
        for x in nums { merge(&R, x, 1) }
        let mod = 1_000_000_007
        func qpow(_ a0: Int, _ b0: Int) -> Int {
            var a = a0 % mod, b = b0, ans = 1
            while b > 0 {
                if b & 1 != 0 { ans = ans * a % mod }
                a = a * a % mod
                b >>= 1
            }
            return ans
        }
        var ans = Array(repeating: 0, count: queries.count)
        var pCur = p
        for qi in 0..<queries.count {
            let val = queries[qi][0], k = queries[qi][1]
            merge(&R, val, 1)
            sz2 += 1
            var node = firstKey(R)
            merge(&R, node, -1)
            sz2 -= 1
            merge(&L, node, 1)
            sz1 += 1
            while sz2 < k {
                node = lastKey(L)
                merge(&L, node, -1)
                sz1 -= 1
                merge(&R, node, 1)
                sz2 += 1
            }
            while sz2 > k {
                node = firstKey(R)
                merge(&R, node, -1)
                sz2 -= 1
                merge(&L, node, 1)
                sz1 += 1
            }
            let x = firstKey(R)
            pCur = qpow(pCur, x)
            ans[qi] = pCur
        }
        return ans
    }
}
'''

FILES["3936_minimum_swaps_to_move_zeros_to_end"] = hdr("3936", "Minimum Swaps to Move Zeros to End", "minimum-swaps-to-move-zeros-to-end") + r'''
class Solution {
    func minimumSwaps(_ nums: [Int]) -> Int {
        var ans = 0
        let n = nums.count
        var i = 0, j = n - 1
        while i < j {
            while i < n && nums[i] != 0 { i += 1 }
            while j > 0 && nums[j] == 0 { j -= 1 }
            if i >= j { break }
            ans += 1
            i += 1
            j -= 1
        }
        return ans
    }
}
'''

FILES["3937_minimum_operations_to_make_array_modulo_alternating_i"] = hdr("3937", "Minimum Operations to Make Array Modulo Alternating I", "minimum-operations-to-make-array-modulo-alternating-i") + r'''
class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        let a = nums.map { $0 % k }
        var ans = Int.max
        for x in 0..<k {
            for y in 0..<k {
                if x == y { continue }
                var cnt = 0
                for i in 0..<a.count {
                    let target = (i & 1) != 0 ? y : x
                    let diff = abs(target - a[i])
                    cnt += min(diff, k - diff)
                }
                ans = min(ans, cnt)
            }
        }
        return ans
    }
}
'''

for folder, content in FILES.items():
    write(folder, content)
print("done", len(FILES))
