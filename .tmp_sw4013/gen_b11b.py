#!/usr/bin/env python3
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

HEAP3 = '''
private struct MinHeap3 {
    private var a: [(Int, Int, Int)] = []
    var isEmpty: Bool { a.isEmpty }
    mutating func push(_ x: (Int, Int, Int)) {
        a.append(x)
        var i = a.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if a[p].2 <= a[i].2 { break }
            a.swapAt(p, i)
            i = p
        }
    }
    mutating func pop() -> (Int, Int, Int) {
        let r = a[0]
        let last = a.removeLast()
        if !a.isEmpty {
            a[0] = last
            var i = 0
            while true {
                var s = i
                let l = 2 * i + 1, rgt = 2 * i + 2
                if l < a.count && a[l].2 < a[s].2 { s = l }
                if rgt < a.count && a[rgt].2 < a[s].2 { s = rgt }
                if s == i { break }
                a.swapAt(i, s)
                i = s
            }
        }
        return r
    }
}
'''

def w(folder: str, body: str) -> None:
    path = ROOT / folder / "Solution.swift"
    text = body.strip() + "\n"
    path.write_text(text, encoding="utf-8")
    print("wrote", folder)

FILES = {}

FILES["2689_extract_kth_character_from_the_rope_tree"] = r'''
// LeetCode 2689 - Extract Kth Character From The Rope Tree
// https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

public class RopeTreeNode {
    public var len: Int
    public var val: Character
    public var left: RopeTreeNode?
    public var right: RopeTreeNode?
    public init() { self.len = 0; self.val = "\0"; self.left = nil; self.right = nil }
    public init(_ val: Character) { self.len = 0; self.val = val; self.left = nil; self.right = nil }
}

class Solution {
    func getKthCharacter(_ root: RopeTreeNode, _ k: Int) -> Character {
        dfs(root, k)
    }

    private func dfs(_ node: RopeTreeNode, _ kk: Int) -> Character {
        if node.left == nil && node.right == nil { return node.val }
        var leftLen = 0
        if let left = node.left {
            leftLen = left.len > 0 ? left.len : 1
        }
        if kk <= leftLen { return dfs(node.left!, kk) }
        return dfs(node.right!, kk - leftLen)
    }
}
'''

FILES["2690_infinite_method_object"] = r'''
// LeetCode 2690 - Infinite Method Object
// https://leetcode.com/problems/infinite-method-object/

class Solution {
    func createInfiniteObject() -> (String) -> String {
        { _ in "Hello World" }
    }
}
'''

FILES["2691_immutability_helper"] = r'''
// LeetCode 2691 - Immutability Helper
// https://leetcode.com/problems/immutability-helper/

class Solution {
    func immutableHelper(_ obj: [String: Int], _ mutators: [([String: Int]) -> [String: Int]]) -> [[String: Int]] {
        mutators.map { $0(obj) }
    }
}
'''

FILES["2692_make_object_immutable"] = r'''
// LeetCode 2692 - Make Object Immutable
// https://leetcode.com/problems/make-object-immutable/

class Solution {
    func makeImmutable(_ obj: [String: Int]) -> [String: Int] {
        obj
    }
}
'''

FILES["2693_call_function_with_custom_context"] = r'''
// LeetCode 2693 - Call Function with Custom Context
// https://leetcode.com/problems/call-function-with-custom-context/

class Solution {
    func call(_ fn: (Int, Int) -> Int, _ ctx: Int, _ arg: Int) -> Int {
        fn(ctx, arg)
    }
}
'''

FILES["2694_event_emitter"] = r'''
// LeetCode 2694 - Event Emitter
// https://leetcode.com/problems/event-emitter/

class EventEmitter {
    private var handlers: [String: [([Int]) -> Void]] = [:]

    func subscribe(_ eventName: String, _ callback: @escaping ([Int]) -> Void) -> () -> Void {
        handlers[eventName, default: []].append(callback)
        var idx = handlers[eventName]!.count - 1
        return {
            if var v = self.handlers[eventName], idx >= 0, idx < v.count {
                v.remove(at: idx)
                self.handlers[eventName] = v
                idx = -1
            }
        }
    }

    func emit(_ eventName: String, _ args: [Int]) -> [Int] {
        var res: [Int] = []
        if let list = handlers[eventName] {
            for cb in list {
                cb(args)
                res.append(0)
            }
        }
        return res
    }
}

class Solution {
    func createEmitter() -> EventEmitter {
        EventEmitter()
    }
}
'''

FILES["2695_array_wrapper"] = r'''
// LeetCode 2695 - Array Wrapper
// https://leetcode.com/problems/array-wrapper/

class ArrayWrapper {
    private let nums: [Int]

    init(_ nums: [Int]) {
        self.nums = nums
    }

    func valueOf() -> Int {
        nums.reduce(0, +)
    }

    var description: String {
        "[" + nums.map(String.init).joined(separator: ",") + "]"
    }
}

class Solution {
    func arrayWrapperCreate(_ nums: [Int]) -> ArrayWrapper {
        ArrayWrapper(nums)
    }
}
'''

FILES["2696_minimum_string_length_after_removing_substrings"] = r'''
// LeetCode 2696 - Minimum String Length After Removing Substrings
// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

class Solution {
    func minLength(_ s: String) -> Int {
        var st: [Character] = []
        for c in s {
            if let last = st.last, (last == "A" && c == "B") || (last == "C" && c == "D") {
                st.removeLast()
            } else {
                st.append(c)
            }
        }
        return st.count
    }
}
'''

FILES["2697_lexicographically_smallest_palindrome"] = r'''
// LeetCode 2697 - Lexicographically Smallest Palindrome
// https://leetcode.com/problems/lexicographically-smallest-palindrome/

class Solution {
    func makeSmallestPalindrome(_ s: String) -> String {
        var arr = Array(s)
        let n = arr.count
        for i in 0..<(n / 2) {
            let c = min(arr[i], arr[n - 1 - i])
            arr[i] = c
            arr[n - 1 - i] = c
        }
        return String(arr)
    }
}
'''

FILES["2698_find_the_punishment_number_of_an_integer"] = r'''
// LeetCode 2698 - Find the Punishment Number of an Integer
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

class Solution {
    func punishmentNumber(_ n: Int) -> Int {
        var ans = 0
        for i in 1...n {
            let sq = i * i
            if can(sq, i) { ans += sq }
        }
        return ans
    }

    private func can(_ sq: Int, _ target: Int) -> Bool {
        dfs(Array(String(sq)), 0, 0, target)
    }

    private func dfs(_ s: [Character], _ i: Int, _ sum: Int, _ target: Int) -> Bool {
        if i == s.count { return sum == target }
        var cur = 0
        for j in i..<s.count {
            cur = cur * 10 + Int(String(s[j]))!
            if sum + cur > target { break }
            if dfs(s, j + 1, sum + cur, target) { return true }
        }
        return false
    }
}
'''

FILES["2699_modify_graph_edge_weights"] = f'''
// LeetCode 2699 - Modify Graph Edge Weights
// https://leetcode.com/problems/modify-graph-edge-weights/
{HEAP}
class Solution {{
    private let INF = 2_000_000_000

    func modifiedGraphEdges(_ n: Int, _ edges: [[Int]], _ source: Int, _ destination: Int, _ target: Int) -> [[Int]] {{
        var edges = edges
        var d = dijkstra(n, edges, source, true)
        if d[destination] < target {{ return [] }}
        var matched = d[destination] == target
        for i in edges.indices {{
            if edges[i][2] != -1 {{ continue }}
            if matched {{
                edges[i][2] = INF
                continue
            }}
            edges[i][2] = 1
            d = dijkstra(n, edges, source, false)
            if d[destination] <= target {{
                edges[i][2] += target - d[destination]
                matched = true
            }}
        }}
        d = dijkstra(n, edges, source, false)
        if d[destination] != target {{ return [] }}
        return edges
    }}

    private func dijkstra(_ n: Int, _ edges: [[Int]], _ source: Int, _ ignoreNeg: Bool) -> [Int] {{
        var dist = Array(repeating: INF, count: n)
        dist[source] = 0
        var pq = MinHeap()
        pq.push((source, 0))
        while !pq.isEmpty {{
            let (u, d) = pq.pop()
            if d != dist[u] {{ continue }}
            for e in edges {{
                let a = e[0], b = e[1]
                var w = e[2]
                if a != u && b != u {{ continue }}
                let to = a == u ? b : a
                if w == -1 {{
                    if ignoreNeg {{ continue }}
                    w = 1
                }}
                if d + w < dist[to] {{
                    dist[to] = d + w
                    pq.push((to, dist[to]))
                }}
            }}
        }}
        return dist
    }}
}}
'''

FILES["2700_differences_between_two_objects"] = r'''
// LeetCode 2700 - Differences Between Two Objects
// https://leetcode.com/problems/differences-between-two-objects/

class Solution {
    func objDiff(_ obj1: [String: Int], _ obj2: [String: Int]) -> [String: [Int]] {
        var diff: [String: [Int]] = [:]
        for (k, v1) in obj1 {
            if let v2 = obj2[k], v2 != v1 {
                diff[k] = [v1, v2]
            }
        }
        return diff
    }
}
'''

FILES["2702_minimum_operations_to_make_numbers_non_positive"] = r'''
// LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
// https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

class Solution {
    func minOperations(_ nums: [Int], _ x: Int, _ y: Int) -> Int {
        var lo = 0
        var hi = 0
        for v in nums {
            hi = max(hi, (v + y - 1) / y)
            hi = max(hi, (v + x - 1) / x)
        }
        hi += nums.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if ok(nums, x, y, mid) { hi = mid } else { lo = mid + 1 }
        }
        return lo
    }

    private func ok(_ nums: [Int], _ x: Int, _ y: Int, _ ops: Int) -> Bool {
        var extra = 0
        for v in nums {
            let remain = v - ops * y
            if remain > 0 { extra += (remain + (x - y) - 1) / (x - y) }
        }
        return extra <= ops
    }
}
'''

FILES["2703_return_length_of_arguments_passed"] = r'''
// LeetCode 2703 - Return Length of Arguments Passed
// https://leetcode.com/problems/return-length-of-arguments-passed/

class Solution {
    func argumentsLength(_ args: [Int]) -> Int {
        args.count
    }
}
'''

FILES["2704_to_be_or_not_to_be"] = r'''
// LeetCode 2704 - To Be Or Not To Be
// https://leetcode.com/problems/to-be-or-not-to-be/

class Expect {
    private let val: Int

    init(_ val: Int) {
        self.val = val
    }

    func toBe(_ other: Int) -> Bool {
        if val == other { return true }
        fatalError("Not Equal")
    }

    func notToBe(_ other: Int) -> Bool {
        if val != other { return true }
        fatalError("Equal")
    }
}

class Solution {
    func expect(_ val: Int) -> Expect {
        Expect(val)
    }
}
'''

FILES["2705_compact_object"] = r'''
// LeetCode 2705 - Compact Object
// https://leetcode.com/problems/compact-object/

class Solution {
    func compactObject(_ obj: [Int]) -> [Int] {
        obj.filter { $0 != 0 }
    }
}
'''

FILES["2706_buy_two_chocolates"] = r'''
// LeetCode 2706 - Buy Two Chocolates
// https://leetcode.com/problems/buy-two-chocolates/

class Solution {
    func buyChoco(_ prices: [Int], _ money: Int) -> Int {
        let prices = prices.sorted()
        let cost = prices[0] + prices[1]
        return cost <= money ? money - cost : money
    }
}
'''

FILES["2707_extra_characters_in_a_string"] = r'''
// LeetCode 2707 - Extra Characters in a String
// https://leetcode.com/problems/extra-characters-in-a-string/

class Solution {
    func minExtraChar(_ s: String, _ dictionary: [String]) -> Int {
        let dict = Set(dictionary)
        let n = s.count
        let chars = Array(s)
        var dp = Array(repeating: n, count: n + 1)
        dp[0] = 0
        for i in 0..<n {
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)
            for j in (i + 1)...n {
                let sub = String(chars[i..<j])
                if dict.contains(sub) { dp[j] = min(dp[j], dp[i]) }
            }
        }
        return dp[n]
    }
}
'''

FILES["2708_maximum_strength_of_a_group"] = r'''
// LeetCode 2708 - Maximum Strength of a Group
// https://leetcode.com/problems/maximum-strength-of-a-group/

class Solution {
    func maxStrength(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        let n = nums.count
        if n == 1 { return nums[0] }
        var prod = 1
        var used = false
        var i = 0
        while i + 1 < n && nums[i] < 0 && nums[i + 1] < 0 {
            prod *= nums[i] * nums[i + 1]
            used = true
            i += 2
        }
        let negLeft = i < n && nums[i] < 0
        while i < n {
            if nums[i] > 0 {
                prod *= nums[i]
                used = true
            }
            i += 1
        }
        if !used {
            if negLeft {
                if nums.contains(0) { return 0 }
                return nums[n - 1]
            }
            return 0
        }
        return prod
    }
}
'''

FILES["2709_greatest_common_divisor_traversal"] = r'''
// LeetCode 2709 - Greatest Common Divisor Traversal
// https://leetcode.com/problems/greatest-common-divisor-traversal/

class Solution {
    private var parent: [Int] = []

    func canTraverseAllPairs(_ nums: [Int]) -> Bool {
        let n = nums.count
        if n == 1 { return true }
        let mx = nums.max() ?? 0
        parent = Array(0...mx)
        var has = Array(repeating: false, count: mx + 1)
        for x in nums {
            if x == 1 { return false }
            has[x] = true
        }
        var sieve = Array(repeating: 0, count: mx + 1)
        if mx >= 2 {
            for i in 2...mx {
                if sieve[i] == 0 {
                    var j = i
                    while j <= mx {
                        if sieve[j] == 0 { sieve[j] = i }
                        if has[j] { unite(i, j) }
                        j += i
                    }
                }
            }
        }
        let root = find(nums[0])
        for x in nums where find(x) != root { return false }
        return true
    }

    private func find(_ x: Int) -> Int {
        if parent[x] != x { parent[x] = find(parent[x]) }
        return parent[x]
    }

    private func unite(_ a: Int, _ b: Int) {
        let ra = find(a), rb = find(b)
        if ra != rb { parent[ra] = rb }
    }
}
'''

FILES["2710_remove_trailing_zeros_from_a_string"] = r'''
// LeetCode 2710 - Remove Trailing Zeros From a String
// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

class Solution {
    func removeTrailingZeros(_ num: String) -> String {
        var end = num.count
        let chars = Array(num)
        while end > 0 && chars[end - 1] == "0" { end -= 1 }
        return String(chars[0..<end])
    }
}
'''

FILES["2711_difference_of_number_of_distinct_values_on_diagonals"] = r'''
// LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

class Solution {
    func differenceOfDistinctValues(_ grid: [[Int]]) -> [[Int]] {
        let m = grid.count, n = grid[0].count
        var ans = Array(repeating: Array(repeating: 0, count: n), count: m)
        for i in 0..<m {
            for j in 0..<n {
                var top = Set<Int>()
                var bot = Set<Int>()
                var r = i - 1, c = j - 1
                while r >= 0 && c >= 0 {
                    top.insert(grid[r][c])
                    r -= 1; c -= 1
                }
                r = i + 1; c = j + 1
                while r < m && c < n {
                    bot.insert(grid[r][c])
                    r += 1; c += 1
                }
                ans[i][j] = abs(top.count - bot.count)
            }
        }
        return ans
    }
}
'''

FILES["2712_minimum_cost_to_make_all_characters_equal"] = r'''
// LeetCode 2712 - Minimum Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

class Solution {
    func minimumCost(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var ans = 0
        for i in 1..<n where chars[i] != chars[i - 1] {
            ans += min(i, n - i)
        }
        return ans
    }
}
'''

FILES["2713_maximum_strictly_increasing_cells_in_a_matrix"] = r'''
// LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

class Solution {
    func maxIncreasingCells(_ mat: [[Int]]) -> Int {
        let m = mat.count, n = mat[0].count
        var cells: [(Int, Int, Int)] = []
        for i in 0..<m {
            for j in 0..<n { cells.append((mat[i][j], i, j)) }
        }
        cells.sort { $0.0 < $1.0 }
        var rowMax = Array(repeating: 0, count: m)
        var colMax = Array(repeating: 0, count: n)
        var dp = Array(repeating: Array(repeating: 0, count: n), count: m)
        var ans = 0
        var i = 0
        while i < cells.count {
            var j = i
            while j < cells.count && cells[j].0 == cells[i].0 { j += 1 }
            var buf: [(Int, Int, Int)] = []
            for k in i..<j {
                let r = cells[k].1, c = cells[k].2
                let best = max(rowMax[r], colMax[c])
                dp[r][c] = best + 1
                ans = max(ans, dp[r][c])
                buf.append((r, c, dp[r][c]))
            }
            for b in buf {
                rowMax[b.0] = max(rowMax[b.0], b.2)
                colMax[b.1] = max(colMax[b.1], b.2)
            }
            i = j
        }
        return ans
    }
}
'''

FILES["2714_find_shortest_path_with_k_hops"] = f'''
// LeetCode 2714 - Find Shortest Path With K Hops
// https://leetcode.com/problems/find-shortest-path-with-k-hops/
{HEAP3}
class Solution {{
    func shortestPathWithHops(_ n: Int, _ edges: [[Int]], _ s: Int, _ d: Int, _ k: Int) -> Int {{
        var g = Array(repeating: [(Int, Int)](), count: n)
        for e in edges {{
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        }}
        var dist = Array(repeating: Array(repeating: Int.max / 4, count: k + 1), count: n)
        dist[s][0] = 0
        var pq = MinHeap3()
        pq.push((s, 0, 0))
        while !pq.isEmpty {{
            let (u, hops, cd) = pq.pop()
            if u == d {{ return cd }}
            if cd > dist[u][hops] {{ continue }}
            for e in g[u] {{
                let to = e.0, w = e.1
                if cd + w < dist[to][hops] {{
                    dist[to][hops] = cd + w
                    pq.push((to, hops, dist[to][hops]))
                }}
                if hops < k && cd < dist[to][hops + 1] {{
                    dist[to][hops + 1] = cd
                    pq.push((to, hops + 1, cd))
                }}
            }}
        }}
        return -1
    }}
}}
'''

FILES["2715_timeout_cancellation"] = r'''
// LeetCode 2715 - Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/

class Solution {
    func cancellable(_ fn: @escaping () -> Int, _ t: Int) -> (() -> Void, () -> Int?) {
        var cancelled = false
        let cancel: () -> Void = { cancelled = true }
        let result: () -> Int? = { cancelled ? nil : fn() }
        return (cancel, result)
    }
}
'''

FILES["2716_minimize_string_length"] = r'''
// LeetCode 2716 - Minimize String Length
// https://leetcode.com/problems/minimize-string-length/

class Solution {
    func minimizedStringLength(_ s: String) -> Int {
        Set(s).count
    }
}
'''

FILES["2717_semi_ordered_permutation"] = r'''
// LeetCode 2717 - Semi-Ordered Permutation
// https://leetcode.com/problems/semi-ordered-permutation/

class Solution {
    func semiOrderedPermutation(_ nums: [Int]) -> Int {
        let n = nums.count
        var p1 = 0, pn = 0
        for i in 0..<n {
            if nums[i] == 1 { p1 = i }
            if nums[i] == n { pn = i }
        }
        var ans = p1 + (n - 1 - pn)
        if p1 > pn { ans -= 1 }
        return ans
    }
}
'''

FILES["2718_sum_of_matrix_after_queries"] = r'''
// LeetCode 2718 - Sum of Matrix After Queries
// https://leetcode.com/problems/sum-of-matrix-after-queries/

class Solution {
    func matrixSumQueries(_ n: Int, _ queries: [[Int]]) -> Int {
        var rowDone = Array(repeating: false, count: n)
        var colDone = Array(repeating: false, count: n)
        var rowsLeft = n, colsLeft = n
        var ans = 0
        for i in stride(from: queries.count - 1, through: 0, by: -1) {
            let type = queries[i][0], idx = queries[i][1], val = queries[i][2]
            if type == 0 {
                if !rowDone[idx] {
                    ans += val * colsLeft
                    rowDone[idx] = true
                    rowsLeft -= 1
                }
            } else if !colDone[idx] {
                ans += val * rowsLeft
                colDone[idx] = true
                colsLeft -= 1
            }
        }
        return ans
    }
}
'''

FILES["2719_count_of_integers"] = r'''
// LeetCode 2719 - Count of Integers
// https://leetcode.com/problems/count-of-integers/

class Solution {
    private let MOD = 1_000_000_007
    private var minSum = 0
    private var maxSum = 0

    func count(_ num1: String, _ num2: String, _ min_sum: Int, _ max_sum: Int) -> Int {
        minSum = min_sum
        maxSum = max_sum
        return (dp(num2) - dp(dec(num1)) + MOD) % MOD
    }

    private func dec(_ s: String) -> String {
        var arr = Array(s)
        var i = arr.count - 1
        while i >= 0 && arr[i] == "0" {
            arr[i] = "9"
            i -= 1
        }
        if i >= 0 {
            let v = Int(arr[i].asciiValue!) - 1
            arr[i] = Character(UnicodeScalar(v)!)
        }
        var j = 0
        while j < arr.count - 1 && arr[j] == "0" { j += 1 }
        return String(arr[j...])
    }

    private func dp(_ s: String) -> Int {
        var memo: [String: Int] = [:]
        return dfs(Array(s), 0, 0, true, &memo)
    }

    private func dfs(_ s: [Character], _ pos: Int, _ sum: Int, _ tight: Bool, _ memo: inout [String: Int]) -> Int {
        if sum > maxSum { return 0 }
        if pos == s.count { return sum >= minSum ? 1 : 0 }
        let key = "\(pos),\(sum),\(tight ? 1 : 0)"
        if let v = memo[key] { return v }
        let up = tight ? Int(String(s[pos]))! : 9
        var res = 0
        for d in 0...up {
            res = (res + dfs(s, pos + 1, sum + d, tight && d == up, &memo)) % MOD
        }
        memo[key] = res
        return res
    }
}
'''

FILES["2721_execute_asynchronous_functions_in_parallel"] = r'''
// LeetCode 2721 - Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

class Solution {
    func promiseAll(_ functions: [() -> Int]) -> [Int] {
        functions.map { $0() }
    }
}
'''

FILES["2722_join_two_arrays_by_id"] = r'''
// LeetCode 2722 - Join Two Arrays by ID
// https://leetcode.com/problems/join-two-arrays-by-id/

class Solution {
    func join(_ arr1: [[String: Int]], _ arr2: [[String: Int]]) -> [[String: Int]] {
        var byId: [Int: [String: Int]] = [:]
        merge(&byId, arr1)
        merge(&byId, arr2)
        return byId.keys.sorted().compactMap { byId[$0] }
    }

    private func merge(_ byId: inout [Int: [String: Int]], _ arr: [[String: Int]]) {
        for obj in arr {
            guard let id = obj["id"] else { continue }
            var dest = byId[id] ?? [:]
            for (k, v) in obj { dest[k] = v }
            byId[id] = dest
        }
    }
}
'''

FILES["2723_add_two_promises"] = r'''
// LeetCode 2723 - Add Two Promises
// https://leetcode.com/problems/add-two-promises/

class Solution {
    func addTwoPromises(_ promise1: () -> Int, _ promise2: () -> Int) -> Int {
        promise1() + promise2()
    }
}
'''

FILES["2724_sort_by"] = r'''
// LeetCode 2724 - Sort By
// https://leetcode.com/problems/sort-by/

class Solution {
    func sortBy(_ arr: [Int], _ fn: (Int) -> Double) -> [Int] {
        arr.sorted { fn($0) < fn($1) }
    }
}
'''

FILES["2725_interval_cancellation"] = r'''
// LeetCode 2725 - Interval Cancellation
// https://leetcode.com/problems/interval-cancellation/

class Solution {
    func cancellable(_ fn: () -> Int, _ t: Int, _ times: Int) -> (() -> Void, [Int]) {
        var cancelled = false
        var results: [Int] = []
        var i = 0
        while i < times && !cancelled {
            results.append(fn())
            i += 1
        }
        let cancel: () -> Void = { cancelled = true }
        return (cancel, results)
    }
}
'''

FILES["2726_calculator_with_method_chaining"] = r'''
// LeetCode 2726 - Calculator with Method Chaining
// https://leetcode.com/problems/calculator-with-method-chaining/

class Calculator {
    private var val: Double

    init(_ val: Double) {
        self.val = val
    }

    func add(_ v: Double) -> Calculator {
        val += v
        return self
    }

    func subtract(_ v: Double) -> Calculator {
        val -= v
        return self
    }

    func multiply(_ v: Double) -> Calculator {
        val *= v
        return self
    }

    func divide(_ v: Double) -> Calculator {
        if v != 0 { val /= v }
        return self
    }

    func power(_ v: Double) -> Calculator {
        val = pow(val, v)
        return self
    }

    func getResult() -> Double {
        val
    }
}

class Solution {
    func calculatorCreate(_ val: Double) -> Calculator {
        Calculator(val)
    }
}
'''

def main():
    for folder, body in FILES.items():
        w(folder, body)
    print("total", len(FILES))

if __name__ == "__main__":
    main()
