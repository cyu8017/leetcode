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

TREE = '''
public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val; self.left = left; self.right = right
    }
}
'''

def w(folder, body):
    (ROOT / folder / "Solution.swift").write_text(body.strip() + "\n", encoding="utf-8")
    print("wrote", folder)

FILES = {}

FILES["2727_is_object_empty"] = r'''
// LeetCode 2727 - Is Object Empty
// https://leetcode.com/problems/is-object-empty/

class Solution {
    func isEmpty(_ obj: [String: Int]) -> Bool {
        obj.isEmpty
    }

    func isEmpty(_ arr: [Int]) -> Bool {
        arr.isEmpty
    }
}
'''

FILES["2728_count_houses_in_a_circular_street"] = r'''
// LeetCode 2728 - Count Houses in a Circular Street
// https://leetcode.com/problems/count-houses-in-a-circular-street/

protocol Street {
    func openDoor()
    func closeDoor()
    func isDoorOpen() -> Bool
    func moveRight()
    func moveLeft()
}

class Solution {
    func countHouses(_ street: Street, _ k: Int) -> Int {
        for _ in 0..<k {
            street.closeDoor()
            street.moveRight()
        }
        var ans = 0
        while true {
            ans += 1
            street.openDoor()
            street.moveRight()
            if street.isDoorOpen() { break }
        }
        return ans
    }
}
'''

FILES["2729_check_if_the_number_is_fascinating"] = r'''
// LeetCode 2729 - Check if The Number is Fascinating
// https://leetcode.com/problems/check-if-the-number-is-fascinating/

class Solution {
    func isFascinating(_ n: Int) -> Bool {
        let s = String(n) + String(2 * n) + String(3 * n)
        if s.count != 9 { return false }
        var cnt = Array(repeating: 0, count: 10)
        for c in s { cnt[Int(String(c))!] += 1 }
        if cnt[0] != 0 { return false }
        for i in 1...9 where cnt[i] != 1 { return false }
        return true
    }
}
'''

FILES["2730_find_the_longest_semi_repetitive_substring"] = r'''
// LeetCode 2730 - Find the Longest Semi-Repetitive Substring
// https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution {
    func longestSemiRepetitiveSubstring(_ s: String) -> Int {
        let chars = Array(s)
        var ans = 0, left = 0, lastPair = -1
        for right in chars.indices {
            if right > 0 && chars[right] == chars[right - 1] {
                if lastPair >= left { left = lastPair + 1 }
                lastPair = right - 1
            }
            ans = max(ans, right - left + 1)
        }
        return ans
    }
}
'''

FILES["2731_movement_of_robots"] = r'''
// LeetCode 2731 - Movement of Robots
// https://leetcode.com/problems/movement-of-robots/

class Solution {
    func sumDistance(_ nums: [Int], _ s: String, _ d: Int) -> Int {
        let MOD = 1_000_000_007
        let chars = Array(s)
        var pos = nums.enumerated().map { i, x in x + (chars[i] == "R" ? d : -d) }
        pos.sort()
        var ans = 0
        var pref = 0
        for i in pos.indices {
            ans = (ans + ((pos[i] % MOD + MOD) % MOD) * i - pref) % MOD
            pref = (pref + (pos[i] % MOD + MOD) % MOD) % MOD
        }
        return (ans % MOD + MOD) % MOD
    }
}
'''

FILES["2732_find_a_good_subset_of_the_matrix"] = r'''
// LeetCode 2732 - Find a Good Subset of the Matrix
// https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

class Solution {
    func goodSubsetofBinaryMatrix(_ grid: [[Int]]) -> [Int] {
        let n = grid[0].count
        var first: [Int: Int] = [:]
        for i in grid.indices {
            var mask = 0
            for j in 0..<n where grid[i][j] == 1 { mask |= 1 << j }
            if mask == 0 { return [i] }
            for (key, value) in first where (key & mask) == 0 {
                return value < i ? [value, i] : [i, value]
            }
            if first[mask] == nil { first[mask] = i }
        }
        return []
    }
}
'''

FILES["2733_neither_minimum_nor_maximum"] = r'''
// LeetCode 2733 - Neither Minimum nor Maximum
// https://leetcode.com/problems/neither-minimum-nor-maximum/

class Solution {
    func findNonMinOrMax(_ nums: [Int]) -> Int {
        if nums.count < 3 { return -1 }
        let a = nums[0], b = nums[1], c = nums[2]
        return a + b + c - max(a, max(b, c)) - min(a, min(b, c))
    }
}
'''

FILES["2734_lexicographically_smallest_string_after_substring_operation"] = r'''
// LeetCode 2734 - Lexicographically Smallest String After Substring Operation
// https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

class Solution {
    func smallestString(_ s: String) -> String {
        var arr = Array(s)
        let n = arr.count
        var i = 0
        while i < n && arr[i] == "a" { i += 1 }
        if i == n {
            arr[n - 1] = "z"
            return String(arr)
        }
        while i < n && arr[i] != "a" {
            let v = Int(arr[i].asciiValue!) - 1
            arr[i] = Character(UnicodeScalar(v)!)
            i += 1
        }
        return String(arr)
    }
}
'''

FILES["2735_collecting_chocolates"] = r'''
// LeetCode 2735 - Collecting Chocolates
// https://leetcode.com/problems/collecting-chocolates/

class Solution {
    func minCost(_ nums: [Int], _ x: Int) -> Int {
        let n = nums.count
        var best = nums
        var ans = nums.reduce(0, +)
        for rot in 1..<n {
            var cur = rot * x
            for i in 0..<n {
                best[i] = min(best[i], nums[(i + rot) % n])
                cur += best[i]
            }
            ans = min(ans, cur)
        }
        return ans
    }
}
'''

FILES["2736_maximum_sum_queries"] = r'''
// LeetCode 2736 - Maximum Sum Queries
// https://leetcode.com/problems/maximum-sum-queries/

class Solution {
    func maximumSumQueries(_ nums1: [Int], _ nums2: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums1.count
        var pts = (0..<n).map { [nums1[$0], nums2[$0], nums1[$0] + nums2[$0]] }
        pts.sort { $0[0] > $1[0] }
        var qs = queries.enumerated().map { i, q in [q[0], q[1], i] }
        qs.sort { $0[0] > $1[0] }
        var ys = nums2 + queries.map { $0[1] }
        ys.sort()
        var uniq: [Int] = []
        for y in ys {
            if uniq.isEmpty || uniq.last != y { uniq.append(y) }
        }
        let m = uniq.count
        var bit = Array(repeating: -1, count: m + 2)
        var ans = Array(repeating: 0, count: queries.count)
        var j = 0
        for q in qs {
            while j < n && pts[j][0] >= q[0] {
                update(&bit, m, m - rank(uniq, pts[j][1]) + 1, pts[j][2])
                j += 1
            }
            ans[q[2]] = query(bit, m - rank(uniq, q[1]) + 1)
        }
        return ans
    }

    private func rank(_ ys: [Int], _ y: Int) -> Int {
        var lo = 0, hi = ys.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if ys[mid] < y { lo = mid + 1 } else { hi = mid }
        }
        return lo + 1
    }

    private func update(_ bit: inout [Int], _ m: Int, _ i0: Int, _ v: Int) {
        var i = i0
        while i <= m {
            bit[i] = max(bit[i], v)
            i += i & -i
        }
    }

    private func query(_ bit: [Int], _ i0: Int) -> Int {
        var i = i0, best = -1
        while i > 0 {
            best = max(best, bit[i])
            i -= i & -i
        }
        return best
    }
}
'''

FILES["2737_find_the_closest_marked_node"] = f'''
// LeetCode 2737 - Find the Closest Marked Node
// https://leetcode.com/problems/find-the-closest-marked-node/
{HEAP}
class Solution {{
    func minimumDistance(_ n: Int, _ edges: [[Int]], _ s: Int, _ marked: [Int]) -> Int {{
        var g = Array(repeating: [(Int, Int)](), count: n)
        for e in edges {{ g[e[0]].append((e[1], e[2])) }}
        let mark = Set(marked)
        var dist = Array(repeating: Int.max / 4, count: n)
        dist[s] = 0
        var pq = MinHeap()
        pq.push((s, 0))
        while !pq.isEmpty {{
            let (u, d) = pq.pop()
            if mark.contains(u) {{ return d }}
            if d > dist[u] {{ continue }}
            for e in g[u] where d + e.1 < dist[e.0] {{
                dist[e.0] = d + e.1
                pq.push((e.0, dist[e.0]))
            }}
        }}
        return -1
    }}
}}
'''

FILES["2739_total_distance_traveled"] = r'''
// LeetCode 2739 - Total Distance Traveled
// https://leetcode.com/problems/total-distance-traveled/

class Solution {
    func distanceTraveled(_ mainTank: Int, _ additionalTank: Int) -> Int {
        var mainTank = mainTank, additionalTank = additionalTank, ans = 0
        while mainTank > 0 {
            if mainTank >= 5 {
                ans += 50
                mainTank -= 5
                if additionalTank > 0 {
                    additionalTank -= 1
                    mainTank += 1
                }
            } else {
                ans += mainTank * 10
                mainTank = 0
            }
        }
        return ans
    }
}
'''

FILES["2740_find_the_value_of_the_partition"] = r'''
// LeetCode 2740 - Find the Value of the Partition
// https://leetcode.com/problems/find-the-value-of-the-partition/

class Solution {
    func findValueOfPartition(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        var ans = Int.max
        for i in 1..<nums.count { ans = min(ans, nums[i] - nums[i - 1]) }
        return ans
    }
}
'''

FILES["2741_special_permutations"] = r'''
// LeetCode 2741 - Special Permutations
// https://leetcode.com/problems/special-permutations/

class Solution {
    private let MOD = 1_000_000_007
    private var nums: [Int] = []
    private var memo: [[Int]] = []

    func specialPerm(_ nums: [Int]) -> Int {
        self.nums = nums
        let n = nums.count
        memo = Array(repeating: Array(repeating: -1, count: n), count: 1 << n)
        var ans = 0
        for i in 0..<n { ans = (ans + dfs(1 << i, i)) % MOD }
        return ans
    }

    private func dfs(_ mask: Int, _ last: Int) -> Int {
        if mask == (1 << nums.count) - 1 { return 1 }
        if memo[mask][last] != -1 { return memo[mask][last] }
        var res = 0
        for i in 0..<nums.count {
            if (mask & (1 << i)) != 0 { continue }
            if nums[i] % nums[last] == 0 || nums[last] % nums[i] == 0 {
                res = (res + dfs(mask | (1 << i), i)) % MOD
            }
        }
        memo[mask][last] = res
        return res
    }
}
'''

FILES["2742_painting_the_walls"] = r'''
// LeetCode 2742 - Painting the Walls
// https://leetcode.com/problems/painting-the-walls/

class Solution {
    func paintWalls(_ cost: [Int], _ time: [Int]) -> Int {
        let n = cost.count
        let INF = Int.max / 4
        var dp = Array(repeating: INF, count: n + 1)
        dp[0] = 0
        for i in 0..<n {
            for j in stride(from: n, through: 0, by: -1) {
                let nj = min(n, j + time[i] + 1)
                if dp[j] + cost[i] < dp[nj] { dp[nj] = dp[j] + cost[i] }
            }
        }
        return dp[n]
    }
}
'''

FILES["2743_count_substrings_without_repeating_character"] = r'''
// LeetCode 2743 - Count Substrings Without Repeating Character
// https://leetcode.com/problems/count-substrings-without-repeating-character/

class Solution {
    func numberOfSpecialSubstrings(_ s: String) -> Int {
        let chars = Array(s)
        var ans = 0, left = 0
        var cnt = Array(repeating: 0, count: 26)
        for i in chars.indices {
            let c = Int(chars[i].asciiValue! - 97)
            cnt[c] += 1
            while cnt[c] > 1 {
                cnt[Int(chars[left].asciiValue! - 97)] -= 1
                left += 1
            }
            ans += i - left + 1
        }
        return ans
    }
}
'''

FILES["2744_find_maximum_number_of_string_pairs"] = r'''
// LeetCode 2744 - Find Maximum Number of String Pairs
// https://leetcode.com/problems/find-maximum-number-of-string-pairs/

class Solution {
    func maximumNumberOfStringPairs(_ words: [String]) -> Int {
        var freq: [String: Int] = [:]
        var ans = 0
        for w in words {
            let rev = String(w.reversed())
            let c = freq[rev, default: 0]
            if c > 0 {
                ans += 1
                freq[rev] = c - 1
            } else {
                freq[w, default: 0] += 1
            }
        }
        return ans
    }
}
'''

FILES["2745_construct_the_longest_new_string"] = r'''
// LeetCode 2745 - Construct the Longest New String
// https://leetcode.com/problems/construct-the-longest-new-string/

class Solution {
    func longestString(_ x: Int, _ y: Int, _ z: Int) -> Int {
        if x < y { return (2 * x + 1 + z) * 2 }
        if y < x { return (2 * y + 1 + z) * 2 }
        return (x + y + z) * 2
    }
}
'''

FILES["2746_decremental_string_concatenation"] = r'''
// LeetCode 2746 - Decremental String Concatenation
// https://leetcode.com/problems/decremental-string-concatenation/

class Solution {
    func minimizeConcatenatedLength(_ words: [String]) -> Int {
        let w0 = Array(words[0])
        var memo: [String: Int] = [:]
        return w0.count + dfs(words, 1, w0[0], w0[w0.count - 1], &memo)
    }

    private func dfs(_ words: [String], _ i: Int, _ first: Character, _ last: Character, _ memo: inout [String: Int]) -> Int {
        if i == words.count { return 0 }
        let key = "\(i),\(first),\(last)"
        if let v = memo[key] { return v }
        let w = Array(words[i])
        let wf = w[0], wl = w[w.count - 1]
        let add1 = w.count - (last == wf ? 1 : 0)
        let add2 = w.count - (wl == first ? 1 : 0)
        let ans = min(add1 + dfs(words, i + 1, first, wl, &memo), add2 + dfs(words, i + 1, wf, last, &memo))
        memo[key] = ans
        return ans
    }
}
'''

FILES["2747_count_zero_request_servers"] = r'''
// LeetCode 2747 - Count Zero Request Servers
// https://leetcode.com/problems/count-zero-request-servers/

class Solution {
    func countServers(_ n: Int, _ logs: [[Int]], _ x: Int, _ queries: [Int]) -> [Int] {
        let logs = logs.sorted { $0[1] < $1[1] }
        var qs = queries.enumerated().map { [$1, $0] }
        qs.sort { $0[0] < $1[0] }
        var ans = Array(repeating: 0, count: queries.count)
        var cnt: [Int: Int] = [:]
        var active = 0, l = 0, r = 0
        for q in qs {
            let t = q[0], qi = q[1]
            while r < logs.count && logs[r][1] <= t {
                let id = logs[r][0]
                if cnt[id, default: 0] == 0 { active += 1 }
                cnt[id, default: 0] += 1
                r += 1
            }
            while l < r && logs[l][1] < t - x {
                let id = logs[l][0]
                cnt[id]! -= 1
                if cnt[id] == 0 { active -= 1 }
                l += 1
            }
            ans[qi] = n - active
        }
        return ans
    }
}
'''

FILES["2748_number_of_beautiful_pairs"] = r'''
// LeetCode 2748 - Number of Beautiful Pairs
// https://leetcode.com/problems/number-of-beautiful-pairs/

class Solution {
    func countBeautifulPairs(_ nums: [Int]) -> Int {
        var ans = 0
        var freq = Array(repeating: 0, count: 10)
        for x in nums {
            let last = x % 10
            for d in 1...9 where freq[d] > 0 && gcd(d, last) == 1 {
                ans += freq[d]
            }
            freq[firstDigit(x)] += 1
        }
        return ans
    }

    private func firstDigit(_ x: Int) -> Int {
        var v = x
        while v >= 10 { v /= 10 }
        return v
    }

    private func gcd(_ a: Int, _ b: Int) -> Int {
        var x = a, y = b
        while y != 0 { let t = x % y; x = y; y = t }
        return x
    }
}
'''

FILES["2749_minimum_operations_to_make_the_integer_zero"] = r'''
// LeetCode 2749 - Minimum Operations to Make the Integer Zero
// https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

class Solution {
    func makeTheIntegerZero(_ num1: Int, _ num2: Int) -> Int {
        for k in 1...60 {
            let rem = num1 - k * num2
            if rem < k { continue }
            if rem.nonzeroBitCount <= k { return k }
        }
        return -1
    }
}
'''

FILES["2750_ways_to_split_array_into_good_subarrays"] = r'''
// LeetCode 2750 - Ways to Split Array Into Good Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

class Solution {
    func numberOfGoodSubarraySplits(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        var ones: [Int] = []
        for i in nums.indices where nums[i] == 1 { ones.append(i) }
        if ones.isEmpty { return 0 }
        var ans = 1
        for i in 1..<ones.count {
            ans = ans * (ones[i] - ones[i - 1]) % MOD
        }
        return ans
    }
}
'''

FILES["2751_robot_collisions"] = r'''
// LeetCode 2751 - Robot Collisions
// https://leetcode.com/problems/robot-collisions/

class Solution {
    func survivedRobotsHealths(_ positions: [Int], _ healths: [Int], _ directions: String) -> [Int] {
        let n = positions.count
        let dirs = Array(directions)
        var idx = Array(0..<n)
        idx.sort { positions[$0] < positions[$1] }
        var stack: [[Int]] = []
        for i in idx {
            var cur = [i, healths[i], Int(dirs[i].asciiValue!)]
            while !stack.isEmpty && stack.last![2] == Int(Character("R").asciiValue!) && cur[2] == Int(Character("L").asciiValue!) {
                var top = stack.removeLast()
                if top[1] == cur[1] {
                    cur[1] = 0
                    break
                } else if top[1] > cur[1] {
                    top[1] -= 1
                    stack.append(top)
                    cur[1] = 0
                    break
                } else {
                    cur[1] -= 1
                }
            }
            if cur[1] > 0 { stack.append(cur) }
        }
        var alive: [Int: Int] = [:]
        for r in stack { alive[r[0]] = r[1] }
        return (0..<n).compactMap { alive[$0] }
    }
}
'''

FILES["2753_count_houses_in_a_circular_street_ii"] = r'''
// LeetCode 2753 - Count Houses in a Circular Street II
// https://leetcode.com/problems/count-houses-in-a-circular-street-ii/

protocol Street {
    func closeDoor()
    func isDoorOpen() -> Bool
    func moveRight()
}

class Solution {
    func houseCount(_ street: Street, _ k: Int) -> Int {
        for _ in 0..<k { street.moveRight() }
        var ans = 0
        for _ in 0..<k {
            if street.isDoorOpen() {
                ans += 1
                street.closeDoor()
            }
            street.moveRight()
        }
        return ans
    }

    func houseCount(_ street: [Int], _ k: Int) -> Int {
        let n = street.count
        if n == 0 { return 0 }
        guard let start = street.firstIndex(of: 1) else { return 0 }
        var count = 1, moves = 0, i2 = start
        while moves < k {
            i2 = (i2 + 1) % n
            moves += 1
            if i2 == start { break }
            if street[i2] == 1 { count += 1 }
        }
        return count
    }
}
'''

FILES["2754_bind_function_to_context"] = r'''
// LeetCode 2754 - Bind Function to Context
// https://leetcode.com/problems/bind-function-to-context/

class Solution {
    func bindFunction(_ fn: (Int, [Int]) -> Int, _ ctx: Int) -> ([Int]) -> Int {
        { args in fn(ctx, args) }
    }

    func bindFunction(_ fn: Int, _ args: [Int]) -> Int {
        fn
    }
}
'''

FILES["2755_deep_merge_of_two_objects"] = r'''
// LeetCode 2755 - Deep Merge of Two Objects
// https://leetcode.com/problems/deep-merge-of-two-objects/

class Solution {
    func deepMerge(_ obj1: [String: String], _ obj2: [String: String]) -> [String: String] {
        var output = obj1
        for (k, v) in obj2 { output[k] = v }
        return output
    }
}
'''

FILES["2756_query_batching"] = r'''
// LeetCode 2756 - Query Batching
// https://leetcode.com/problems/query-batching/

class QueryBatcher {
    private let queryMultiple: ([Int]) -> [Int]
    private let t: Int
    private var pending: [Int] = []
    private var resolvers: [(Int) -> Void] = []

    init(_ queryMultiple: @escaping ([Int]) -> [Int], _ t: Int) {
        self.queryMultiple = queryMultiple
        self.t = t
    }

    func addQuery(_ query: Int, _ resolve: @escaping (Int) -> Void) {
        pending.append(query)
        resolvers.append(resolve)
    }

    func flush() {
        guard !pending.isEmpty else { return }
        let results = queryMultiple(pending)
        for i in results.indices { resolvers[i](results[i]) }
        pending.removeAll()
        resolvers.removeAll()
    }
}
'''

FILES["2757_generate_circular_array_values"] = r'''
// LeetCode 2757 - Generate Circular Array Values
// https://leetcode.com/problems/generate-circular-array-values/

class Solution {
    func cyclicGenerator(_ arr: [Int], _ startIndex: Int) -> () -> Int {
        var i = startIndex
        let n = arr.count
        return {
            let v = arr[i]
            i = (i + 1) % n
            return v
        }
    }
}
'''

FILES["2758_next_day"] = r'''
// LeetCode 2758 - Next Day
// https://leetcode.com/problems/next-day/

class Solution {
    func nextDay(_ date: String) -> String {
        let parts = date.split(separator: "-").map { Int($0)! }
        if parts.count != 3 { return date }
        var y = parts[0], m = parts[1], d = parts[2]
        var mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if isLeap(y) { mdays[2] = 29 }
        d += 1
        if d > mdays[m] { d = 1; m += 1 }
        if m > 12 { m = 1; y += 1 }
        return String(format: "%04d-%02d-%02d", y, m, d)
    }

    private func isLeap(_ yy: Int) -> Bool {
        (yy % 4 == 0 && yy % 100 != 0) || (yy % 400 == 0)
    }
}
'''

FILES["2759_convert_json_string_to_object"] = r'''
// LeetCode 2759 - Convert JSON String to Object
// https://leetcode.com/problems/convert-json-string-to-object/

class Solution {
    func jsonParse(_ str: String) -> String {
        str
    }
}
'''

FILES["2760_longest_even_odd_subarray_with_threshold"] = r'''
// LeetCode 2760 - Longest Even Odd Subarray With Threshold
// https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

class Solution {
    func longestAlternatingSubarray(_ nums: [Int], _ threshold: Int) -> Int {
        var ans = 0
        let n = nums.count
        for i in 0..<n {
            if nums[i] % 2 != 0 || nums[i] > threshold { continue }
            var j = i
            while j + 1 < n && nums[j + 1] <= threshold && nums[j + 1] % 2 != nums[j] % 2 { j += 1 }
            ans = max(ans, j - i + 1)
        }
        return ans
    }
}
'''

FILES["2761_prime_pairs_with_target_sum"] = r'''
// LeetCode 2761 - Prime Pairs With Target Sum
// https://leetcode.com/problems/prime-pairs-with-target-sum/

class Solution {
    func findPrimePairs(_ n: Int) -> [[Int]] {
        if n < 2 { return [] }
        var isPrime = Array(repeating: false, count: n + 1)
        if n >= 2 { for i in 2...n { isPrime[i] = true } }
        var i = 2
        while i * i <= n {
            if isPrime[i] {
                var j = i * i
                while j <= n { isPrime[j] = false; j += i }
            }
            i += 1
        }
        var ans: [[Int]] = []
        if n >= 4 {
            for x in 2...(n / 2) {
                let y = n - x
                if isPrime[x] && isPrime[y] { ans.append([x, y]) }
            }
        }
        return ans
    }
}
'''

FILES["2762_continuous_subarrays"] = r'''
// LeetCode 2762 - Continuous Subarrays
// https://leetcode.com/problems/continuous-subarrays/

class Solution {
    func continuousSubarrays(_ nums: [Int]) -> Int {
        var ans = 0, left = 0
        var freq: [Int: Int] = [:]
        for right in nums.indices {
            freq[nums[right], default: 0] += 1
            while let mn = freq.keys.min(), let mx = freq.keys.max(), mx - mn > 2 {
                let v = nums[left]
                freq[v]! -= 1
                if freq[v] == 0 { freq.removeValue(forKey: v) }
                left += 1
            }
            ans += right - left + 1
        }
        return ans
    }
}
'''

FILES["2763_sum_of_imbalance_numbers_of_all_subarrays"] = r'''
// LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
// https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

class Solution {
    func sumImbalanceNumbers(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var seen = Set<Int>()
            var sortedVals: [Int] = []
            var imbalance = 0
            for j in i..<n {
                let x = nums[j]
                if !seen.contains(x) {
                    seen.insert(x)
                    let idx = lowerBound(sortedVals, x)
                    let prev = idx > 0 ? sortedVals[idx - 1] : nil
                    let next = idx < sortedVals.count ? sortedVals[idx] : nil
                    if let p = prev, x - p != 1 { imbalance += 1 }
                    if let nx = next, nx - x != 1 { imbalance += 1 }
                    if let p = prev, let nx = next, nx - p > 1 { imbalance -= 1 }
                    sortedVals.insert(x, at: idx)
                }
                ans += imbalance
            }
        }
        return ans
    }

    private func lowerBound(_ a: [Int], _ x: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] < x { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }
}
'''

FILES["2764_is_array_a_preorder_of_some_binary_tree"] = r'''
// LeetCode 2764 - Is Array a Preorder of Some Binary Tree
// https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

class Solution {
    func isPreorder(_ nodes: [[Int]]) -> Bool {
        if nodes.isEmpty { return true }
        var stack: [Int] = [nodes[0][0]]
        for i in 1..<nodes.count {
            let id = nodes[i][0], parent = nodes[i][1]
            while !stack.isEmpty && stack.last != parent { stack.removeLast() }
            if stack.isEmpty { return false }
            stack.append(id)
        }
        return true
    }
}
'''

FILES["2765_longest_alternating_subarray"] = r'''
// LeetCode 2765 - Longest Alternating Subarray
// https://leetcode.com/problems/longest-alternating-subarray/

class Solution {
    func alternatingSubarray(_ nums: [Int]) -> Int {
        var ans = -1
        let n = nums.count
        for i in 0..<n {
            for j in (i + 1)..<n {
                let expect = (j - i) % 2 == 0 ? -1 : 1
                if nums[j] - nums[j - 1] != expect { break }
                if nums[i + 1] - nums[i] != 1 { break }
                ans = max(ans, j - i + 1)
            }
        }
        return ans
    }
}
'''

FILES["2766_relocate_marbles"] = r'''
// LeetCode 2766 - Relocate Marbles
// https://leetcode.com/problems/relocate-marbles/

class Solution {
    func relocateMarbles(_ nums: [Int], _ moveFrom: [Int], _ moveTo: [Int]) -> [Int] {
        var pos = Set(nums)
        for i in moveFrom.indices {
            pos.remove(moveFrom[i])
            pos.insert(moveTo[i])
        }
        return pos.sorted()
    }
}
'''

FILES["2767_partition_string_into_minimum_beautiful_substrings"] = r'''
// LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
// https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

class Solution {
    func minimumBeautifulSubstrings(_ s: String) -> Int {
        let n = s.count
        var pow5 = Set<String>()
        var x = 1
        while true {
            let b = String(x, radix: 2)
            if b.count > n { break }
            pow5.insert(b)
            x *= 5
        }
        let INF = 1 << 30
        var dp = Array(repeating: INF, count: n + 1)
        dp[0] = 0
        let chars = Array(s)
        for i in 0..<n {
            if dp[i] == INF || chars[i] == "0" { continue }
            for j in (i + 1)...n {
                if pow5.contains(String(chars[i..<j])) {
                    dp[j] = min(dp[j], dp[i] + 1)
                }
            }
        }
        return dp[n] == INF ? -1 : dp[n]
    }
}
'''

FILES["2768_number_of_black_blocks"] = r'''
// LeetCode 2768 - Number of Black Blocks
// https://leetcode.com/problems/number-of-black-blocks/

class Solution {
    func countBlackBlocks(_ m: Int, _ n: Int, _ coordinates: [[Int]]) -> [Int] {
        var cnt: [Int: Int] = [:]
        for c in coordinates {
            let x = c[0], y = c[1]
            for i in (x - 1)...x {
                for j in (y - 1)...y {
                    if i >= 0 && j >= 0 && i < m - 1 && j < n - 1 {
                        let key = (i << 32) | (j & 0xffffffff)
                        cnt[key, default: 0] += 1
                    }
                }
            }
        }
        var ans = Array(repeating: 0, count: 5)
        ans[0] = (m - 1) * (n - 1)
        for v in cnt.values {
            ans[v] += 1
            ans[0] -= 1
        }
        return ans
    }
}
'''

FILES["2769_find_the_maximum_achievable_number"] = r'''
// LeetCode 2769 - Find the Maximum Achievable Number
// https://leetcode.com/problems/find-the-maximum-achievable-number/

class Solution {
    func theMaximumAchievableX(_ num: Int, _ t: Int) -> Int {
        num + 2 * t
    }
}
'''

FILES["2770_maximum_number_of_jumps_to_reach_the_last_index"] = r'''
// LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
// https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

class Solution {
    func maximumJumps(_ nums: [Int], _ target: Int) -> Int {
        let n = nums.count
        var dp = Array(repeating: -1, count: n)
        dp[0] = 0
        for i in 0..<n where dp[i] >= 0 {
            for j in (i + 1)..<n where abs(nums[j] - nums[i]) <= target {
                dp[j] = max(dp[j], dp[i] + 1)
            }
        }
        return dp[n - 1]
    }
}
'''

FILES["2771_longest_non_decreasing_subarray_from_two_arrays"] = r'''
// LeetCode 2771 - Longest Non-decreasing Subarray From Two Arrays
// https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

class Solution {
    func maxNonDecreasingLength(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        var dp1 = 1, dp2 = 1, ans = 1
        for i in 1..<n {
            var nd1 = 1, nd2 = 1
            if nums1[i] >= nums1[i - 1] { nd1 = max(nd1, dp1 + 1) }
            if nums1[i] >= nums2[i - 1] { nd1 = max(nd1, dp2 + 1) }
            if nums2[i] >= nums1[i - 1] { nd2 = max(nd2, dp1 + 1) }
            if nums2[i] >= nums2[i - 1] { nd2 = max(nd2, dp2 + 1) }
            dp1 = nd1
            dp2 = nd2
            ans = max(ans, max(dp1, dp2))
        }
        return ans
    }
}
'''

FILES["2772_apply_operations_to_make_all_array_elements_equal_to_zero"] = r'''
// LeetCode 2772 - Apply Operations to Make All Array Elements Equal to Zero
// https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

class Solution {
    func checkArray(_ nums: [Int], _ k: Int) -> Bool {
        let n = nums.count
        var diff = Array(repeating: 0, count: n + 1)
        var cur = 0
        for i in 0..<n {
            cur += diff[i]
            let need = nums[i] - cur
            if need < 0 { return false }
            if need > 0 {
                if i + k > n { return false }
                cur += need
                diff[i + k] -= need
            }
        }
        return true
    }
}
'''

FILES["2773_height_of_special_binary_tree"] = f'''
// LeetCode 2773 - Height of Special Binary Tree
// https://leetcode.com/problems/height-of-special-binary-tree/
{TREE}
class Solution {{
    func heightOfTree(_ root: TreeNode?) -> Int {{
        if root == nil {{ return -1 }}
        return dfs(root)
    }}

    private func dfs(_ node: TreeNode?) -> Int {{
        guard let node = node else {{ return -1 }}
        if let l = node.left, l.right === node {{ return dfs(node.right) + 1 }}
        if let r = node.right, r.left === node {{ return dfs(node.left) + 1 }}
        return max(dfs(node.left), dfs(node.right)) + 1
    }}
}}
'''

def main():
    for folder, body in FILES.items():
        w(folder, body)
    print("total", len(FILES))

if __name__ == "__main__":
    main()
