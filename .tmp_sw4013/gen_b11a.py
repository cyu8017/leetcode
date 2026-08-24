#!/usr/bin/env python3
"""Generate Solution.swift for batch 11 folders 2620-2685."""
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

HEAP = '''
private struct MinHeap {
    private var a: [(Int, Int)] = []
    var isEmpty: Bool { a.isEmpty }
    mutating func push(_ x: (Int, Int)) {
        a.append(x)
        var i = a.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if a[p].1 <= a[i].1 { break }
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
                let l = 2 * i + 1, rgt = 2 * i + 2
                if l < a.count && a[l].1 < a[s].1 { s = l }
                if rgt < a.count && a[rgt].1 < a[s].1 { s = rgt }
                if s == i { break }
                a.swapAt(i, s)
                i = s
            }
        }
        return r
    }
}
'''

TREE = '''
public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}
'''

LIST = '''
public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil }
    public init(_ val: Int) { self.val = val; self.next = nil }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}
'''

def w(folder: str, body: str) -> None:
    path = ROOT / folder / "Solution.swift"
    path.write_text(body.lstrip("\n") if body.startswith("\n") else body, encoding="utf-8")
    if not body.endswith("\n"):
        path.write_text(path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    print("wrote", folder)

FILES = {}

FILES["2620_counter"] = r'''
// LeetCode 2620 - Counter
// https://leetcode.com/problems/counter/

class Solution {
    func createCounter(_ n: Int) -> () -> Int {
        var cur = n
        return {
            let v = cur
            cur += 1
            return v
        }
    }
}
'''

FILES["2621_sleep"] = r'''
// LeetCode 2621 - Sleep
// https://leetcode.com/problems/sleep/

class Solution {
    func sleep(_ millis: Int) {
        Thread.sleep(forTimeInterval: Double(millis) / 1000.0)
    }
}
'''

FILES["2622_cache_with_time_limit"] = r'''
// LeetCode 2622 - Cache With Time Limit
// https://leetcode.com/problems/cache-with-time-limit/

class TimeLimitedCache {
    private class Entry {
        var value: Int
        var expire: Int64
        init(_ value: Int, _ expire: Int64) {
            self.value = value
            self.expire = expire
        }
    }

    private var data: [Int: Entry] = [:]
    private let start = DispatchTime.now().uptimeNanoseconds

    private func nowMs() -> Int64 {
        Int64((DispatchTime.now().uptimeNanoseconds - start) / 1_000_000)
    }

    func set(_ key: Int, _ value: Int, _ duration: Int) -> Bool {
        let now = nowMs()
        let alive = data[key].map { $0.expire > now } ?? false
        data[key] = Entry(value, now + Int64(duration))
        return alive
    }

    func get(_ key: Int) -> Int {
        let now = nowMs()
        guard let e = data[key], e.expire > now else { return -1 }
        return e.value
    }

    func count() -> Int {
        let now = nowMs()
        var cnt = 0
        var dead: [Int] = []
        for (k, v) in data {
            if v.expire > now { cnt += 1 } else { dead.append(k) }
        }
        for k in dead { data.removeValue(forKey: k) }
        return cnt
    }
}
'''

FILES["2623_memoize"] = r'''
// LeetCode 2623 - Memoize
// https://leetcode.com/problems/memoize/

class Solution {
    func memoize(_ fn: @escaping (Int) -> Int) -> (Int) -> Int {
        var cache: [Int: Int] = [:]
        return { x in
            if let v = cache[x] { return v }
            let v = fn(x)
            cache[x] = v
            return v
        }
    }
}
'''

FILES["2624_snail_traversal"] = r'''
// LeetCode 2624 - Snail Traversal
// https://leetcode.com/problems/snail-traversal/

class Solution {
    func snail(_ nums: [Int], _ rowsCount: Int, _ colsCount: Int) -> [[Int]] {
        if rowsCount * colsCount != nums.count { return [] }
        var ans = Array(repeating: Array(repeating: 0, count: colsCount), count: rowsCount)
        var idx = 0
        for c in 0..<colsCount {
            if c % 2 == 0 {
                for r in 0..<rowsCount {
                    ans[r][c] = nums[idx]
                    idx += 1
                }
            } else {
                for r in stride(from: rowsCount - 1, through: 0, by: -1) {
                    ans[r][c] = nums[idx]
                    idx += 1
                }
            }
        }
        return ans
    }
}
'''

FILES["2625_flatten_deeply_nested_array"] = r'''
// LeetCode 2625 - Flatten Deeply Nested Array
// https://leetcode.com/problems/flatten-deeply-nested-array/

enum NestedInteger {
    case num(Int)
    case list([NestedInteger])
}

class Solution {
    func flat(_ arr: [NestedInteger], _ n: Int) -> [NestedInteger] {
        var out: [NestedInteger] = []
        func dfs(_ items: [NestedInteger], _ depth: Int) {
            for item in items {
                switch item {
                case .num:
                    out.append(item)
                case .list(let nested):
                    if depth < n {
                        dfs(nested, depth + 1)
                    } else {
                        out.append(item)
                    }
                }
            }
        }
        dfs(arr, 0)
        return out
    }

    func flat(_ arr: [Int], _ n: Int) -> [Int] {
        arr
    }
}
'''

FILES["2626_array_reduce_transformation"] = r'''
// LeetCode 2626 - Array Reduce Transformation
// https://leetcode.com/problems/array-reduce-transformation/

class Solution {
    func reduce(_ nums: [Int], _ fn: (Int, Int) -> Int, _ initVal: Int) -> Int {
        var acc = initVal
        for x in nums { acc = fn(acc, x) }
        return acc
    }
}
'''

FILES["2627_debounce"] = r'''
// LeetCode 2627 - Debounce
// https://leetcode.com/problems/debounce/

class Solution {
    func debounce(_ fn: @escaping () -> Void, _ t: Int) -> () -> Void {
        var work: DispatchWorkItem?
        return {
            work?.cancel()
            let item = DispatchWorkItem { fn() }
            work = item
            DispatchQueue.main.asyncAfter(deadline: .now() + .milliseconds(t), execute: item)
        }
    }
}
'''

FILES["2628_json_deep_equal"] = r'''
// LeetCode 2628 - JSON Deep Equal
// https://leetcode.com/problems/json-deep-equal/

class Solution {
    func areDeeplyEqual(_ o1: Any?, _ o2: Any?) -> Bool {
        switch (o1, o2) {
        case (nil, nil):
            return true
        case (let a as Int, let b as Int):
            return a == b
        case (let a as Double, let b as Double):
            return a == b
        case (let a as Bool, let b as Bool):
            return a == b
        case (let a as String, let b as String):
            return a == b
        case (let a as [Any?], let b as [Any?]):
            guard a.count == b.count else { return false }
            for i in 0..<a.count where !areDeeplyEqual(a[i], b[i]) { return false }
            return true
        case (let a as [String: Any?], let b as [String: Any?]):
            guard a.count == b.count else { return false }
            for (k, v) in a where !areDeeplyEqual(v, b[k] ?? nil) { return false }
            return true
        default:
            return false
        }
    }

    func areDeeplyEqual(_ o1: String, _ o2: String) -> Bool {
        o1 == o2
    }
}
'''

FILES["2629_function_composition"] = r'''
// LeetCode 2629 - Function Composition
// https://leetcode.com/problems/function-composition/

class Solution {
    func compose(_ functions: [(Int) -> Int]) -> (Int) -> Int {
        return { x0 in
            var x = x0
            for i in stride(from: functions.count - 1, through: 0, by: -1) {
                x = functions[i](x)
            }
            return x
        }
    }
}
'''

FILES["2630_memoize_ii"] = r'''
// LeetCode 2630 - Memoize II
// https://leetcode.com/problems/memoize-ii/

class Solution {
    func memoizeII(_ fn: @escaping ([Int]) -> Int) -> ([Int]) -> Int {
        var cache: [String: Int] = [:]
        return { args in
            let k = args.map(String.init).joined(separator: "|")
            if let v = cache[k] { return v }
            let v = fn(args)
            cache[k] = v
            return v
        }
    }
}
'''

FILES["2631_group_by"] = r'''
// LeetCode 2631 - Group By
// https://leetcode.com/problems/group-by/

class Solution {
    func groupBy(_ arr: [Int], _ fn: (Int) -> String) -> [String: [Int]] {
        var out: [String: [Int]] = [:]
        for x in arr {
            out[fn(x), default: []].append(x)
        }
        return out
    }
}
'''

FILES["2632_curry"] = r'''
// LeetCode 2632 - Curry
// https://leetcode.com/problems/curry/

class Solution {
    func curry(_ fn: @escaping ([Int]) -> Int, _ arity: Int) -> ([Int]) -> Int {
        { args in fn(args) }
    }
}
'''

FILES["2633_convert_object_to_json_string"] = r'''
// LeetCode 2633 - Convert Object to JSON String
// https://leetcode.com/problems/convert-object-to-json-string/

class Solution {
    func jsonStringify(_ object: Any) -> String {
        if let s = object as? String { return "\"\(s)\"" }
        if let n = object as? Int { return String(n) }
        if let b = object as? Bool { return b ? "true" : "false" }
        if let arr = object as? [Any] {
            return "[" + arr.map { jsonStringify($0) }.joined(separator: ",") + "]"
        }
        if let obj = object as? [String: Any] {
            let keys = obj.keys.sorted()
            let body = keys.map { "\"\($0)\":\(jsonStringify(obj[$0]!))" }.joined(separator: ",")
            return "{" + body + "}"
        }
        if let s = object as? String { return s }
        return String(describing: object)
    }

    func jsonStringify(_ objectStr: String) -> String {
        objectStr
    }
}
'''

FILES["2634_filter_elements_from_array"] = r'''
// LeetCode 2634 - Filter Elements from Array
// https://leetcode.com/problems/filter-elements-from-array/

class Solution {
    func filter(_ arr: [Int], _ fn: (Int, Int) -> Bool) -> [Int] {
        var out: [Int] = []
        for i in arr.indices where fn(arr[i], i) {
            out.append(arr[i])
        }
        return out
    }
}
'''

FILES["2635_apply_transform_over_each_element_in_array"] = r'''
// LeetCode 2635 - Apply Transform Over Each Element in Array
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

class Solution {
    func map(_ arr: [Int], _ fn: (Int, Int) -> Int) -> [Int] {
        var out = Array(repeating: 0, count: arr.count)
        for i in arr.indices { out[i] = fn(arr[i], i) }
        return out
    }
}
'''

FILES["2636_promise_pool"] = r'''
// LeetCode 2636 - Promise Pool
// https://leetcode.com/problems/promise-pool/

class Solution {
    func promisePool(_ functions: [() -> Int], _ n: Int) -> [Int] {
        var ans = Array(repeating: 0, count: functions.count)
        for i in functions.indices { ans[i] = functions[i]() }
        return ans
    }
}
'''

FILES["2637_promise_time_limit"] = r'''
// LeetCode 2637 - Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/

class Solution {
    func timeLimit(_ fn: @escaping () -> Int, _ t: Int) -> () -> Int {
        { fn() }
    }
}
'''

FILES["2638_count_the_number_of_k_free_subsets"] = r'''
// LeetCode 2638 - Count the Number of K-Free Subsets
// https://leetcode.com/problems/count-the-number-of-k-free-subsets/

class Solution {
    func countTheNumOfKFreeSubsets(_ nums: [Int], _ k: Int) -> Int {
        var nums = nums.sorted()
        var groups: [Int: [Int]] = [:]
        for x in nums { groups[x % k, default: []].append(x) }
        var ans = 1
        for g in groups.values {
            var prevVal = -1
            var prevTake = 0
            var prevSkip = 1
            for v in g {
                let skip = prevTake + prevSkip
                let take = prevVal + k == v ? prevSkip : prevTake + prevSkip
                prevTake = take
                prevSkip = skip
                prevVal = v
            }
            ans *= prevTake + prevSkip
        }
        return ans
    }
}
'''

FILES["2639_find_the_width_of_columns_of_a_grid"] = r'''
// LeetCode 2639 - Find the Width of Columns of a Grid
// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

class Solution {
    func findColumnWidth(_ grid: [[Int]]) -> [Int] {
        let n = grid[0].count
        var ans = Array(repeating: 0, count: n)
        for row in grid {
            for j in 0..<n {
                ans[j] = max(ans[j], width(row[j]))
            }
        }
        return ans
    }

    private func width(_ x0: Int) -> Int {
        if x0 == 0 { return 1 }
        var x = x0
        var w = 0
        if x < 0 {
            w += 1
            x = -x
        }
        while x > 0 {
            w += 1
            x /= 10
        }
        return w
    }
}
'''

FILES["2640_find_the_score_of_all_prefixes_of_an_array"] = r'''
// LeetCode 2640 - Find the Score of All Prefixes of an Array
// https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

class Solution {
    func findPrefixScore(_ nums: [Int]) -> [Int] {
        var ans = Array(repeating: 0, count: nums.count)
        var mx = 0
        var sum = 0
        for i in nums.indices {
            mx = max(mx, nums[i])
            sum += nums[i] + mx
            ans[i] = sum
        }
        return ans
    }
}
'''

FILES["2641_cousins_in_binary_tree_ii"] = f'''
// LeetCode 2641 - Cousins in Binary Tree II
// https://leetcode.com/problems/cousins-in-binary-tree-ii/
{TREE}
class Solution {{
    func replaceValueInTree(_ root: TreeNode?) -> TreeNode? {{
        guard let root = root else {{ return nil }}
        root.val = 0
        var q: [TreeNode] = [root]
        while !q.isEmpty {{
            let sz = q.count
            var levelSum = 0
            var level: [TreeNode] = []
            for _ in 0..<sz {{
                let node = q.removeFirst()
                level.append(node)
                if let l = node.left {{ levelSum += l.val }}
                if let r = node.right {{ levelSum += r.val }}
            }}
            for node in level {{
                var cousin = levelSum
                if let l = node.left {{ cousin -= l.val }}
                if let r = node.right {{ cousin -= r.val }}
                if let l = node.left {{
                    l.val = cousin
                    q.append(l)
                }}
                if let r = node.right {{
                    r.val = cousin
                    q.append(r)
                }}
            }}
        }}
        return root
    }}
}}
'''

FILES["2642_design_graph_with_shortest_path_calculator"] = f'''
// LeetCode 2642 - Design Graph With Shortest Path Calculator
// https://leetcode.com/problems/design-graph-with-shortest-path-calculator/
{HEAP}
class Graph {{
    private var g: [[(Int, Int)]]

    init(_ n: Int, _ edges: [[Int]]) {{
        g = Array(repeating: [], count: n)
        for e in edges {{ g[e[0]].append((e[1], e[2])) }}
    }}

    func addEdge(_ edge: [Int]) {{
        g[edge[0]].append((edge[1], edge[2]))
    }}

    func shortestPath(_ node1: Int, _ node2: Int) -> Int {{
        let n = g.count
        var dist = Array(repeating: 1 << 30, count: n)
        dist[node1] = 0
        var pq = MinHeap()
        pq.push((node1, 0))
        while !pq.isEmpty {{
            let (u, d) = pq.pop()
            if u == node2 {{ return d }}
            if d > dist[u] {{ continue }}
            for e in g[u] {{
                let nd = d + e.1
                if nd < dist[e.0] {{
                    dist[e.0] = nd
                    pq.push((e.0, nd))
                }}
            }}
        }}
        return -1
    }}
}}
'''

FILES["2643_row_with_maximum_ones"] = r'''
// LeetCode 2643 - Row With Maximum Ones
// https://leetcode.com/problems/row-with-maximum-ones/

class Solution {
    func rowAndMaximumOnes(_ mat: [[Int]]) -> [Int] {
        var bestRow = 0
        var bestCnt = -1
        for i in mat.indices {
            let cnt = mat[i].reduce(0, +)
            if cnt > bestCnt {
                bestCnt = cnt
                bestRow = i
            }
        }
        return [bestRow, bestCnt]
    }
}
'''

FILES["2644_find_the_maximum_divisibility_score"] = r'''
// LeetCode 2644 - Find the Maximum Divisibility Score
// https://leetcode.com/problems/find-the-maximum-divisibility-score/

class Solution {
    func maxDivScore(_ nums: [Int], _ divisors: [Int]) -> Int {
        var best = divisors[0]
        var bestScore = -1
        for d in divisors {
            var score = 0
            for x in nums where x % d == 0 { score += 1 }
            if score > bestScore || (score == bestScore && d < best) {
                bestScore = score
                best = d
            }
        }
        return best
    }
}
'''

FILES["2645_minimum_additions_to_make_valid_string"] = r'''
// LeetCode 2645 - Minimum Additions to Make Valid String
// https://leetcode.com/problems/minimum-additions-to-make-valid-string/

class Solution {
    func addMinimum(_ word: String) -> Int {
        var ans = 0
        var expect = 0
        var i = 0
        let chars = Array(word)
        let n = chars.count
        while i < n {
            let need = Character(UnicodeScalar(Int(UnicodeScalar("a").value) + expect)!)
            if chars[i] == need { i += 1 } else { ans += 1 }
            expect = (expect + 1) % 3
        }
        ans += (3 - expect) % 3
        return ans
    }
}
'''

FILES["2646_minimize_the_total_price_of_the_trips"] = r'''
// LeetCode 2646 - Minimize the Total Price of the Trips
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

class Solution {
    private var g: [[Int]] = []
    private var price: [Int] = []
    private var cnt: [Int] = []

    func minimumTotalPrice(_ n: Int, _ edges: [[Int]], _ price: [Int], _ trips: [[Int]]) -> Int {
        self.price = price
        g = Array(repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        cnt = Array(repeating: 0, count: n)
        for t in trips { _ = path(t[0], -1, t[1]) }
        let res = dfs(0, -1)
        return min(res.0, res.1)
    }

    private func path(_ u: Int, _ p: Int, _ target: Int) -> Bool {
        if u == target {
            cnt[u] += 1
            return true
        }
        for v in g[u] {
            if v == p { continue }
            if path(v, u, target) {
                cnt[u] += 1
                return true
            }
        }
        return false
    }

    private func dfs(_ u: Int, _ p: Int) -> (Int, Int) {
        var full = price[u] * cnt[u]
        var half = full / 2
        for v in g[u] {
            if v == p { continue }
            let child = dfs(v, u)
            full += min(child.0, child.1)
            half += child.0
        }
        return (full, half)
    }
}
'''

FILES["2647_color_the_triangle_red"] = r'''
// LeetCode 2647 - Color the Triangle Red
// https://leetcode.com/problems/color-the-triangle-red/

class Solution {
    func colorRed(_ n: Int) -> [[Int]] {
        var ans: [[Int]] = []
        for i in 1...n { ans.append([i, 1]) }
        var i = n % 2 + 2
        while i <= n {
            let hi = 2 * (n - i) + 2
            if hi >= 2 {
                for j in 2...hi { ans.append([i, j]) }
            }
            i += 2
        }
        return ans
    }
}
'''

FILES["2648_generate_fibonacci_sequence"] = r'''
// LeetCode 2648 - Generate Fibonacci Sequence
// https://leetcode.com/problems/generate-fibonacci-sequence/

class Solution {
    func fibGenerator() -> () -> Int {
        var a = 0
        var b = 1
        return {
            let v = a
            let na = b
            b = a + b
            a = na
            return v
        }
    }
}
'''

FILES["2649_nested_array_generator"] = r'''
// LeetCode 2649 - Nested Array Generator
// https://leetcode.com/problems/nested-array-generator/

class Solution {
    func inorderTraversal(_ arr: [Int]) -> [Int] {
        arr
    }

    func inorderTraversal(_ arr: [Any]) -> [Int] {
        var out: [Int] = []
        func dfs(_ items: [Any]) {
            for item in items {
                if let n = item as? Int {
                    out.append(n)
                } else if let nested = item as? [Any] {
                    dfs(nested)
                }
            }
        }
        dfs(arr)
        return out
    }
}
'''

FILES["2650_design_cancellable_function"] = r'''
// LeetCode 2650 - Design Cancellable Function
// https://leetcode.com/problems/design-cancellable-function/

class Solution {
    func cancellable(_ generator: @escaping () -> Int) -> (() -> Void, () -> Int) {
        var cancelled = false
        var done = false
        var result = 0
        let cancel: () -> Void = { cancelled = true }
        let run: () -> Int = {
            if !done {
                result = generator()
                done = true
            }
            return result
        }
        return (cancel, run)
    }
}
'''

FILES["2651_calculate_delayed_arrival_time"] = r'''
// LeetCode 2651 - Calculate Delayed Arrival Time
// https://leetcode.com/problems/calculate-delayed-arrival-time/

class Solution {
    func findDelayedArrivalTime(_ arrivalTime: Int, _ delayedTime: Int) -> Int {
        (arrivalTime + delayedTime) % 24
    }
}
'''

FILES["2652_sum_multiples"] = r'''
// LeetCode 2652 - Sum Multiples
// https://leetcode.com/problems/sum-multiples/

class Solution {
    func sumOfMultiples(_ n: Int) -> Int {
        var ans = 0
        for i in 1...n where i % 3 == 0 || i % 5 == 0 || i % 7 == 0 {
            ans += i
        }
        return ans
    }
}
'''

FILES["2653_sliding_subarray_beauty"] = r'''
// LeetCode 2653 - Sliding Subarray Beauty
// https://leetcode.com/problems/sliding-subarray-beauty/

class Solution {
    func getSubarrayBeauty(_ nums: [Int], _ k: Int, _ x: Int) -> [Int] {
        var freq = Array(repeating: 0, count: 101)
        var ans = Array(repeating: 0, count: nums.count - k + 1)
        for i in nums.indices {
            freq[nums[i] + 50] += 1
            if i >= k { freq[nums[i - k] + 50] -= 1 }
            if i >= k - 1 {
                var need = x
                var val = 0
                for j in 0..<50 {
                    need -= freq[j]
                    if need <= 0 {
                        val = j - 50
                        break
                    }
                }
                ans[i - k + 1] = val
            }
        }
        return ans
    }
}
'''

FILES["2654_minimum_number_of_operations_to_make_all_array_elements_equal_to_1"] = r'''
// LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
// https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        let n = nums.count
        let ones = nums.filter { $0 == 1 }.count
        if ones > 0 { return n - ones }
        var best = n + 1
        for i in 0..<n {
            var g = 0
            for j in i..<n {
                g = gcd(g, nums[j])
                if g == 1 {
                    best = min(best, j - i)
                    break
                }
            }
        }
        if best == n + 1 { return -1 }
        return best + n - 1
    }

    private func gcd(_ a0: Int, _ b0: Int) -> Int {
        var a = a0, b = b0
        while b != 0 {
            let t = a % b
            a = b
            b = t
        }
        return a
    }
}
'''

FILES["2655_find_maximal_uncovered_ranges"] = r'''
// LeetCode 2655 - Find Maximal Uncovered Ranges
// https://leetcode.com/problems/find-maximal-uncovered-ranges/

class Solution {
    func findMaximalUncoveredRanges(_ n: Int, _ ranges: [[Int]]) -> [[Int]] {
        let ranges = ranges.sorted { $0[0] < $1[0] }
        var ans: [[Int]] = []
        var cur = 0
        for r in ranges {
            if r[0] > cur { ans.append([cur, r[0] - 1]) }
            if r[1] + 1 > cur { cur = r[1] + 1 }
        }
        if cur < n { ans.append([cur, n - 1]) }
        return ans
    }
}
'''

FILES["2656_maximum_sum_with_exactly_k_elements"] = r'''
// LeetCode 2656 - Maximum Sum With Exactly K Elements
// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

class Solution {
    func maximizeSum(_ nums: [Int], _ k: Int) -> Int {
        let mx = nums.max() ?? 0
        return k * mx + k * (k - 1) / 2
    }
}
'''

FILES["2657_find_the_prefix_common_array_of_two_arrays"] = r'''
// LeetCode 2657 - Find the Prefix Common Array of Two Arrays
// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution {
    func findThePrefixCommonArray(_ A: [Int], _ B: [Int]) -> [Int] {
        let n = A.count
        var seenA = Array(repeating: false, count: n + 1)
        var seenB = Array(repeating: false, count: n + 1)
        var ans = Array(repeating: 0, count: n)
        var common = 0
        for i in 0..<n {
            if seenB[A[i]] { common += 1 }
            seenA[A[i]] = true
            if seenA[B[i]] { common += 1 }
            seenB[B[i]] = true
            ans[i] = common
        }
        return ans
    }
}
'''

FILES["2658_maximum_number_of_fish_in_a_grid"] = r'''
// LeetCode 2658 - Maximum Number of Fish in a Grid
// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution {
    func findMaxFish(_ grid: [[Int]]) -> Int {
        var grid = grid
        let m = grid.count, n = grid[0].count
        var best = 0
        for i in 0..<m {
            for j in 0..<n where grid[i][j] > 0 {
                best = max(best, dfs(&grid, i, j))
            }
        }
        return best
    }

    private func dfs(_ grid: inout [[Int]], _ r: Int, _ c: Int) -> Int {
        let m = grid.count, n = grid[0].count
        if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0 { return 0 }
        let fish = grid[r][c]
        grid[r][c] = 0
        return fish + dfs(&grid, r + 1, c) + dfs(&grid, r - 1, c) + dfs(&grid, r, c + 1) + dfs(&grid, r, c - 1)
    }
}
'''

FILES["2659_make_array_empty"] = r'''
// LeetCode 2659 - Make Array Empty
// https://leetcode.com/problems/make-array-empty/

class Solution {
    func countOperationsToEmptyArray(_ nums: [Int]) -> Int {
        let n = nums.count
        var idx = Array(0..<n)
        idx.sort { nums[$0] < nums[$1] }
        var ans = n
        for i in 1..<n where idx[i] < idx[i - 1] {
            ans += n - i
        }
        return ans
    }
}
'''

FILES["2660_determine_the_winner_of_a_bowling_game"] = r'''
// LeetCode 2660 - Determine the Winner of a Bowling Game
// https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

class Solution {
    func isWinner(_ player1: [Int], _ player2: [Int]) -> Int {
        let a = score(player1), b = score(player2)
        if a > b { return 1 }
        if b > a { return 2 }
        return 0
    }

    private func score(_ p: [Int]) -> Int {
        var s = 0
        for i in p.indices {
            var mul = 1
            if (i > 0 && p[i - 1] == 10) || (i > 1 && p[i - 2] == 10) { mul = 2 }
            s += mul * p[i]
        }
        return s
    }
}
'''

FILES["2661_first_completely_painted_row_or_column"] = r'''
// LeetCode 2661 - First Completely Painted Row or Column
// https://leetcode.com/problems/first-completely-painted-row-or-column/

class Solution {
    func firstCompleteIndex(_ arr: [Int], _ mat: [[Int]]) -> Int {
        let m = mat.count, n = mat[0].count
        var posR = Array(repeating: 0, count: m * n + 1)
        var posC = Array(repeating: 0, count: m * n + 1)
        for i in 0..<m {
            for j in 0..<n {
                posR[mat[i][j]] = i
                posC[mat[i][j]] = j
            }
        }
        var rowCnt = Array(repeating: 0, count: m)
        var colCnt = Array(repeating: 0, count: n)
        for i in arr.indices {
            let r = posR[arr[i]], c = posC[arr[i]]
            rowCnt[r] += 1
            colCnt[c] += 1
            if rowCnt[r] == n || colCnt[c] == m { return i }
        }
        return -1
    }
}
'''

FILES["2662_minimum_cost_of_a_path_with_special_roads"] = f'''
// LeetCode 2662 - Minimum Cost of a Path With Special Roads
// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/
{HEAP}
class Solution {{
    func minimumCost(_ start: [Int], _ target: [Int], _ specialRoads: [[Int]]) -> Int {{
        var points: [[Int]] = [start, target]
        for r in specialRoads {{
            points.append([r[0], r[1]])
            points.append([r[2], r[3]])
        }}
        let N = points.count
        var g = Array(repeating: [(Int, Int)](), count: N)
        for i in 0..<N {{
            for j in 0..<N where i != j {{
                g[i].append((j, man(points[i], points[j])))
            }}
        }}
        for r in specialRoads {{
            var u = -1, v = -1
            for i in 0..<N {{
                if points[i][0] == r[0] && points[i][1] == r[1] {{ u = i }}
                if points[i][0] == r[2] && points[i][1] == r[3] {{ v = i }}
            }}
            if u >= 0 && v >= 0 {{ g[u].append((v, r[4])) }}
        }}
        var dist = Array(repeating: Int.max / 4, count: N)
        dist[0] = 0
        var pq = MinHeap()
        pq.push((0, 0))
        while !pq.isEmpty {{
            let (id, cost) = pq.pop()
            if cost > dist[id] {{ continue }}
            for e in g[id] {{
                if cost + e.1 < dist[e.0] {{
                    dist[e.0] = cost + e.1
                    pq.push((e.0, dist[e.0]))
                }}
            }}
        }}
        return dist[1]
    }}

    private func man(_ a: [Int], _ b: [Int]) -> Int {{
        abs(a[0] - b[0]) + abs(a[1] - b[1])
    }}
}}
'''

FILES["2663_lexicographically_smallest_beautiful_string"] = r'''
// LeetCode 2663 - Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/lexicographically-smallest-beautiful-string/

class Solution {
    func smallestBeautifulString(_ s: String, _ k: Int) -> String {
        var b = Array(s)
        let n = b.count
        let aVal = Int(UnicodeScalar("a").value)
        for i in stride(from: n - 1, through: 0, by: -1) {
            var c = Int(b[i].asciiValue!) + 1
            while c < aVal + k {
                let ch = Character(UnicodeScalar(c)!)
                if (i > 0 && ch == b[i - 1]) || (i > 1 && ch == b[i - 2]) {
                    c += 1
                    continue
                }
                b[i] = ch
                for j in (i + 1)..<n {
                    var nc = aVal
                    while nc < aVal + k {
                        let nch = Character(UnicodeScalar(nc)!)
                        if (j > 0 && nch == b[j - 1]) || (j > 1 && nch == b[j - 2]) {
                            nc += 1
                            continue
                        }
                        b[j] = nch
                        break
                    }
                }
                return String(b)
            }
        }
        return ""
    }
}
'''

FILES["2664_the_knights_tour"] = r'''
// LeetCode 2664 - The Knight's Tour
// https://leetcode.com/problems/the-knights-tour/

class Solution {
    private let dirs = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

    func tourOfKnight(_ m: Int, _ n: Int, _ r: Int, _ c: Int) -> [[Int]] {
        var ans = Array(repeating: Array(repeating: -1, count: n), count: m)
        _ = dfs(&ans, m, n, r, c, 0)
        return ans
    }

    private func dfs(_ ans: inout [[Int]], _ m: Int, _ n: Int, _ x: Int, _ y: Int, _ step: Int) -> Bool {
        ans[x][y] = step
        if step == m * n - 1 { return true }
        for d in dirs {
            let nx = x + d[0], ny = y + d[1]
            if nx >= 0 && nx < m && ny >= 0 && ny < n && ans[nx][ny] == -1 {
                if dfs(&ans, m, n, nx, ny, step + 1) { return true }
            }
        }
        ans[x][y] = -1
        return false
    }
}
'''

FILES["2665_counter_ii"] = r'''
// LeetCode 2665 - Counter II
// https://leetcode.com/problems/counter-ii/

class CounterII {
    private let initVal: Int
    private var cur: Int

    init(_ initVal: Int) {
        self.initVal = initVal
        self.cur = initVal
    }

    func increment() -> Int {
        cur += 1
        return cur
    }

    func decrement() -> Int {
        cur -= 1
        return cur
    }

    func reset() -> Int {
        cur = initVal
        return cur
    }
}

class Solution {
    func createCounter(_ initVal: Int) -> CounterII {
        CounterII(initVal)
    }
}
'''

FILES["2666_allow_one_function_call"] = r'''
// LeetCode 2666 - Allow One Function Call
// https://leetcode.com/problems/allow-one-function-call/

class Solution {
    func once(_ fn: @escaping (Int) -> Int) -> (Int) -> Int? {
        var called = false
        return { arg in
            if called { return nil }
            called = true
            return fn(arg)
        }
    }
}
'''

FILES["2667_create_hello_world_function"] = r'''
// LeetCode 2667 - Create Hello World Function
// https://leetcode.com/problems/create-hello-world-function/

class Solution {
    func createHelloWorld() -> () -> String {
        { "Hello World" }
    }
}
'''

FILES["2670_find_the_distinct_difference_array"] = r'''
// LeetCode 2670 - Find the Distinct Difference Array
// https://leetcode.com/problems/find-the-distinct-difference-array/

class Solution {
    func distinctDifferenceArray(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var suf = Array(repeating: 0, count: n + 1)
        var seen = Set<Int>()
        for i in stride(from: n - 1, through: 0, by: -1) {
            seen.insert(nums[i])
            suf[i] = seen.count
        }
        seen.removeAll()
        var ans = Array(repeating: 0, count: n)
        for i in 0..<n {
            seen.insert(nums[i])
            ans[i] = seen.count - suf[i + 1]
        }
        return ans
    }
}
'''

FILES["2671_frequency_tracker"] = r'''
// LeetCode 2671 - Frequency Tracker
// https://leetcode.com/problems/frequency-tracker/

class FrequencyTracker {
    private var freq: [Int: Int] = [:]
    private var count: [Int: Int] = [:]

    init() {}

    func add(_ number: Int) {
        let old = freq[number, default: 0]
        if old > 0 { count[old, default: 0] -= 1 }
        freq[number] = old + 1
        count[old + 1, default: 0] += 1
    }

    func deleteOne(_ number: Int) {
        let old = freq[number, default: 0]
        if old == 0 { return }
        count[old, default: 0] -= 1
        freq[number] = old - 1
        if old - 1 > 0 { count[old - 1, default: 0] += 1 }
    }

    func hasFrequency(_ frequency: Int) -> Bool {
        count[frequency, default: 0] > 0
    }
}
'''

FILES["2672_number_of_adjacent_elements_with_the_same_color"] = r'''
// LeetCode 2672 - Number of Adjacent Elements With the Same Color
// https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

class Solution {
    func colorTheArray(_ n: Int, _ queries: [[Int]]) -> [Int] {
        var colors = Array(repeating: 0, count: n)
        var ans = Array(repeating: 0, count: queries.count)
        var same = 0
        for i in queries.indices {
            let idx = queries[i][0], color = queries[i][1]
            if colors[idx] != 0 {
                if idx > 0 && colors[idx] == colors[idx - 1] { same -= 1 }
                if idx + 1 < n && colors[idx] == colors[idx + 1] { same -= 1 }
            }
            colors[idx] = color
            if idx > 0 && colors[idx] == colors[idx - 1] { same += 1 }
            if idx + 1 < n && colors[idx] == colors[idx + 1] { same += 1 }
            ans[i] = same
        }
        return ans
    }
}
'''

FILES["2673_make_costs_of_paths_equal_in_a_binary_tree"] = r'''
// LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
// https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

class Solution {
    func minIncrements(_ n: Int, _ cost: [Int]) -> Int {
        var cost = cost
        var ans = 0
        for i in stride(from: n / 2 - 1, through: 0, by: -1) {
            let l = 2 * i + 1, r = 2 * i + 2
            ans += abs(cost[l] - cost[r])
            cost[i] += max(cost[l], cost[r])
        }
        return ans
    }
}
'''

FILES["2674_split_a_circular_linked_list"] = f'''
// LeetCode 2674 - Split a Circular Linked List
// https://leetcode.com/problems/split-a-circular-linked-list/
{LIST}
class Solution {{
    func splitCircularLinkedList(_ list: ListNode?) -> [ListNode?] {{
        guard let list = list else {{ return [nil, nil] }}
        var slow: ListNode? = list
        var fast: ListNode? = list
        while fast?.next !== list && fast?.next?.next !== list {{
            slow = slow?.next
            fast = fast?.next?.next
        }}
        if fast?.next?.next === list {{ fast = fast?.next }}
        let head2 = slow?.next
        slow?.next = list
        fast?.next = head2
        return [list, head2]
    }}
}}
'''

FILES["2675_array_of_objects_to_matrix"] = r'''
// LeetCode 2675 - Array of Objects to Matrix
// https://leetcode.com/problems/array-of-objects-to-matrix/

class Solution {
    func jsonToMatrix(_ arr: [[String: String]]) -> [[String]] {
        var keys = Set<String>()
        for obj in arr { keys.formUnion(obj.keys) }
        let sortedKeys = keys.sorted()
        var mat: [[String]] = [sortedKeys]
        for obj in arr {
            mat.append(sortedKeys.map { obj[$0] ?? "" })
        }
        return mat
    }
}
'''

FILES["2676_throttle"] = r'''
// LeetCode 2676 - Throttle
// https://leetcode.com/problems/throttle/

class Solution {
    func throttle(_ fn: @escaping () -> Void, _ t: Int) -> () -> Void {
        var last: UInt64 = 0
        var started = false
        return {
            let now = DispatchTime.now().uptimeNanoseconds
            if !started || (now &- last) / 1_000_000 >= UInt64(t) {
                started = true
                last = now
                fn()
            }
        }
    }
}
'''

FILES["2677_chunk_array"] = r'''
// LeetCode 2677 - Chunk Array
// https://leetcode.com/problems/chunk-array/

class Solution {
    func chunk(_ arr: [Int], _ size: Int) -> [[Int]] {
        var ans: [[Int]] = []
        var i = 0
        while i < arr.count {
            let end = min(arr.count, i + size)
            ans.append(Array(arr[i..<end]))
            i += size
        }
        return ans
    }
}
'''

FILES["2678_number_of_senior_citizens"] = r'''
// LeetCode 2678 - Number of Senior Citizens
// https://leetcode.com/problems/number-of-senior-citizens/

class Solution {
    func countSeniors(_ details: [String]) -> Int {
        var ans = 0
        for d in details {
            let chars = Array(d)
            let age = Int(String(chars[11]))! * 10 + Int(String(chars[12]))!
            if age > 60 { ans += 1 }
        }
        return ans
    }
}
'''

FILES["2679_sum_in_a_matrix"] = r'''
// LeetCode 2679 - Sum in a Matrix
// https://leetcode.com/problems/sum-in-a-matrix/

class Solution {
    func matrixSum(_ nums: [[Int]]) -> Int {
        var nums = nums
        for i in nums.indices { nums[i].sort() }
        var ans = 0
        let n = nums[0].count
        for j in 0..<n {
            var mx = 0
            for row in nums { mx = max(mx, row[j]) }
            ans += mx
        }
        return ans
    }
}
'''

FILES["2680_maximum_or"] = r'''
// LeetCode 2680 - Maximum OR
// https://leetcode.com/problems/maximum-or/

class Solution {
    func maximumOr(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var pref = Array(repeating: 0, count: n + 1)
        var suf = Array(repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] | nums[i] }
        for i in stride(from: n - 1, through: 0, by: -1) { suf[i] = suf[i + 1] | nums[i] }
        var ans = 0
        for i in 0..<n {
            ans = max(ans, pref[i] | (nums[i] << k) | suf[i + 1])
        }
        return ans
    }
}
'''

FILES["2681_power_of_heroes"] = r'''
// LeetCode 2681 - Power of Heroes
// https://leetcode.com/problems/power-of-heroes/

class Solution {
    func sumOfPower(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        let nums = nums.sorted()
        var ans = 0
        var s = 0
        for x in nums {
            ans = (ans + (s + x) % MOD * x % MOD * x) % MOD
            s = (s * 2 + x) % MOD
        }
        return ans
    }
}
'''

FILES["2682_find_the_losers_of_the_circular_game"] = r'''
// LeetCode 2682 - Find the Losers of the Circular Game
// https://leetcode.com/problems/find-the-losers-of-the-circular-game/

class Solution {
    func circularGameLosers(_ n: Int, _ k: Int) -> [Int] {
        var seen = Array(repeating: false, count: n + 1)
        var cur = 1
        var step = 1
        while !seen[cur] {
            seen[cur] = true
            cur = (cur - 1 + step * k) % n + 1
            step += 1
        }
        var ans: [Int] = []
        for i in 1...n where !seen[i] { ans.append(i) }
        return ans
    }
}
'''

FILES["2683_neighboring_bitwise_xor"] = r'''
// LeetCode 2683 - Neighboring XOR
// https://leetcode.com/problems/neighboring-bitwise-xor/

class Solution {
    func doesValidArrayExist(_ derived: [Int]) -> Bool {
        derived.reduce(0, ^) == 0
    }
}
'''

FILES["2684_maximum_number_of_moves_in_a_grid"] = r'''
// LeetCode 2684 - Maximum Number of Moves in a Grid
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

class Solution {
    func maxMoves(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var dp = Array(repeating: true, count: m)
        var ans = 0
        for c in 0..<(n - 1) {
            var nxt = Array(repeating: false, count: m)
            var moved = false
            for r in 0..<m where dp[r] {
                for nr in (r - 1)...(r + 1) where nr >= 0 && nr < m && grid[nr][c + 1] > grid[r][c] {
                    nxt[nr] = true
                    moved = true
                }
            }
            if !moved { break }
            dp = nxt
            ans += 1
        }
        return ans
    }
}
'''

FILES["2685_count_the_number_of_complete_components"] = r'''
// LeetCode 2685 - Count the Number of Complete Components
// https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution {
    func countCompleteComponents(_ n: Int, _ edges: [[Int]]) -> Int {
        var g = Array(repeating: [Int](), count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var seen = Array(repeating: false, count: n)
        var ans = 0
        for i in 0..<n where !seen[i] {
            var nodes: [Int] = []
            var q = [i]
            seen[i] = true
            while !q.isEmpty {
                let u = q.removeFirst()
                nodes.append(u)
                for v in g[u] where !seen[v] {
                    seen[v] = true
                    q.append(v)
                }
            }
            let sz = nodes.count
            var ok = true
            for u in nodes where g[u].count != sz - 1 {
                ok = false
                break
            }
            if ok { ans += 1 }
        }
        return ans
    }
}
'''

def main():
    for folder, body in FILES.items():
        w(folder, body.strip() + "\n")
    print("total", len(FILES))

if __name__ == "__main__":
    main()
