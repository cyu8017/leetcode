#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def hdr(num, title, slug):
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n"

TASK_HEAP = '''
private struct TaskHeap {
    private var a: [(Int, Int, Int)] = [] // pri, taskId, userId
    var isEmpty: Bool { a.isEmpty }
    mutating func push(_ x: (Int, Int, Int)) {
        a.append(x)
        var i = a.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if better(a[p], a[i]) { break }
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
                let l = 2 * i + 1, rg = 2 * i + 2
                if l < a.count && better(a[l], a[s]) { s = l }
                if rg < a.count && better(a[rg], a[s]) { s = rg }
                if s == i { break }
                a.swapAt(i, s)
                i = s
            }
        }
        return r
    }
    private func better(_ a: (Int, Int, Int), _ b: (Int, Int, Int)) -> Bool {
        if a.0 != b.0 { return a.0 > b.0 }
        return a.1 > b.1
    }
}
'''

FILES = {}

MODE_SUB = '''
class Solution {
    func subsequencesWithMiddleMode(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        let n = nums.count
        var ans = 0
        if n < 5 { return 0 }
        for mid in 2..<(n - 2) {
            for a in 0..<mid {
                for b in (a + 1)..<mid {
                    for c in (mid + 1)..<n {
                        for d in (c + 1)..<n {
                            let seq = [nums[a], nums[b], nums[mid], nums[c], nums[d]]
                            if uniqueMode(seq) { ans = (ans + 1) % mod }
                        }
                    }
                }
            }
        }
        return ans
    }

    private func uniqueMode(_ a: [Int]) -> Bool {
        var freq = [Int: Int]()
        for x in a { freq[x, default: 0] += 1 }
        var best = 0, cnt = 0
        for f in freq.values {
            if f > best { best = f; cnt = 1 }
            else if f == best { cnt += 1 }
        }
        return cnt == 1
    }
}
'''

FILES["3395_subsequences_with_a_unique_middle_mode_i"] = hdr("3395", "Subsequences with a Unique Middle Mode I", "subsequences-with-a-unique-middle-mode-i") + MODE_SUB
FILES["3416_subsequences_with_a_unique_middle_mode_ii"] = hdr("3416", "Subsequences with a Unique Middle Mode II", "subsequences-with-a-unique-middle-mode-ii") + MODE_SUB

FILES["3396_minimum_number_of_operations_to_make_elements_in_array_distinct"] = hdr("3396", "Minimum Number of Operations to Make Elements in Array Distinct", "minimum-number-of-operations-to-make-elements-in-array-distinct") + '''
class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        var list = nums
        var ops = 0
        while true {
            var seen = Set<Int>()
            var dup = false
            for x in list {
                if !seen.insert(x).inserted { dup = true; break }
            }
            if !dup { return ops }
            if list.count <= 3 { return ops + 1 }
            list.removeFirst(3)
            ops += 1
        }
    }
}
'''

FILES["3397_maximum_number_of_distinct_elements_after_operations"] = hdr("3397", "Maximum Number of Distinct Elements After Operations", "maximum-number-of-distinct-elements-after-operations") + '''
class Solution {
    func maxDistinctElements(_ nums: [Int], _ k: Int) -> Int {
        let nums = nums.sorted()
        var ans = 0
        var prev = Int.min / 2
        for x in nums {
            var cur = x - k
            if cur <= prev { cur = prev + 1 }
            if cur > x + k { continue }
            ans += 1
            prev = cur
        }
        return ans
    }
}
'''

MINLEN = '''
class Solution {
    func minLength(_ s: String, _ numOps: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var lo = 1, hi = n
        while lo < hi {
            let mid = (lo + hi) / 2
            if ok(chars, n, numOps, mid) { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }

    private func ok(_ s: [Character], _ n: Int, _ numOps: Int, _ L: Int) -> Bool {
        if L == 0 { return false }
        var ops = 0
        var i = 0
        while i < n {
            var j = i
            while j < n && s[j] == s[i] { j += 1 }
            ops += (j - i) / (L + 1)
            i = j
        }
        return ops <= numOps
    }
}
'''
FILES["3398_smallest_substring_with_identical_characters_i"] = hdr("3398", "Smallest Substring With Identical Characters I", "smallest-substring-with-identical-characters-i") + MINLEN
FILES["3399_smallest_substring_with_identical_characters_ii"] = hdr("3399", "Smallest Substring With Identical Characters II", "smallest-substring-with-identical-characters-ii") + MINLEN

FILES["3400_maximum_number_of_matching_indices_after_right_shifts"] = hdr("3400", "Maximum Number of Matching Indices After Right Shifts", "maximum-number-of-matching-indices-after-right-shifts") + '''
class Solution {
    func maximumMatchingIndices(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        var ans = 0
        for shift in 0..<n {
            var cnt = 0
            for i in 0..<n {
                if nums1[(i - shift + n) % n] == nums2[i] { cnt += 1 }
            }
            if cnt > ans { ans = cnt }
        }
        return ans
    }
}
'''

FILES["3402_minimum_operations_to_make_columns_strictly_increasing"] = hdr("3402", "Minimum Operations to Make Columns Strictly Increasing", "minimum-operations-to-make-columns-strictly-increasing") + '''
class Solution {
    func minimumOperations(_ grid: [[Int]]) -> Int {
        var grid = grid
        let m = grid.count, n = grid[0].count
        var ans = 0
        for j in 0..<n {
            for i in 1..<m {
                if grid[i][j] <= grid[i - 1][j] {
                    let need = grid[i - 1][j] + 1
                    ans += need - grid[i][j]
                    grid[i][j] = need
                }
            }
        }
        return ans
    }
}
'''

BOX = '''
class Solution {
    func answerString(_ word: String, _ numFriends: Int) -> String {
        if numFriends == 1 { return word }
        let w = Array(word)
        let n = w.count
        let maxLen = n - (numFriends - 1)
        var ans = ""
        for i in 0..<n {
            var end = i + maxLen
            if end > n { end = n }
            let cand = String(w[i..<end])
            if cand > ans { ans = cand }
        }
        return ans
    }
}
'''
FILES["3403_find_the_lexicographically_largest_string_from_the_box_i"] = hdr("3403", "Find the Lexicographically Largest String From the Box I", "find-the-lexicographically-largest-string-from-the-box-i") + BOX
FILES["3406_find_the_lexicographically_largest_string_from_the_box_ii"] = hdr("3406", "Find the Lexicographically Largest String From the Box II", "find-the-lexicographically-largest-string-from-the-box-ii") + BOX

FILES["3404_count_special_subsequences"] = hdr("3404", "Count Special Subsequences", "count-special-subsequences") + '''
class Solution {
    func numberOfSubsequences(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            for j in (i + 2)..<n {
                for k in (j + 2)..<n {
                    for l in (k + 2)..<n {
                        if nums[i] * nums[k] == nums[j] * nums[l] { ans += 1 }
                    }
                }
            }
        }
        return ans
    }
}
'''

FILES["3405_count_the_number_of_arrays_with_k_matching_adjacent_elements"] = hdr("3405", "Count the Number of Arrays with K Matching Adjacent Elements", "count-the-number-of-arrays-with-k-matching-adjacent-elements") + '''
class Solution {
    func countGoodArrays(_ n: Int, _ m: Int, _ k: Int) -> Int {
        let mod = 1_000_000_007
        return comb(n - 1, k, mod) * m % mod * modPow(m - 1, n - 1 - k, mod) % mod
    }

    private func modPow(_ a: Int, _ e: Int, _ mod: Int) -> Int {
        var r = 1, a = ((a % mod) + mod) % mod, e = e
        if a < 0 { a = 0 }
        while e > 0 {
            if e & 1 != 0 { r = r * a % mod }
            a = a * a % mod
            e >>= 1
        }
        return r
    }

    private func comb(_ n: Int, _ k: Int, _ mod: Int) -> Int {
        if k < 0 || k > n { return 0 }
        var num = 1, den = 1
        if k > 0 {
            for i in 0..<k {
                num = num * (n - i) % mod
                den = den * (i + 1) % mod
            }
        }
        return num * modPow(den, mod - 2, mod) % mod
    }
}
'''

FILES["3407_substring_matching_pattern"] = hdr("3407", "Substring Matching Pattern", "substring-matching-pattern") + '''
class Solution {
    func hasMatch(_ s: String, _ p: String) -> Bool {
        let pa = Array(p)
        let star = pa.firstIndex(of: "*")!
        let left = String(pa[..<star])
        let right = String(pa[(star + 1)...])
        guard let li = s.range(of: left) else { return false }
        let rest = s[li.upperBound...]
        return rest.range(of: right) != nil
    }
}
'''

FILES["3408_design_task_manager"] = hdr("3408", "Design Task Manager", "design-task-manager") + TASK_HEAP + '''
class TaskManager {
    private var h = TaskHeap()
    private var pri = [Int: Int]()
    private var user = [Int: Int]()

    init(_ tasks: [[Int]]) {
        for t in tasks { add(t[0], t[1], t[2]) }
    }

    func add(_ userId: Int, _ taskId: Int, _ priority: Int) {
        pri[taskId] = priority
        user[taskId] = userId
        h.push((priority, taskId, userId))
    }

    func edit(_ taskId: Int, _ newPriority: Int) {
        pri[taskId] = newPriority
        h.push((newPriority, taskId, user[taskId]!))
    }

    func rmv(_ taskId: Int) {
        pri.removeValue(forKey: taskId)
        user.removeValue(forKey: taskId)
    }

    func execTop() -> Int {
        while !h.isEmpty {
            let top = h.pop()
            if let p = pri[top.1], p == top.0, user[top.1] == top.2 {
                pri.removeValue(forKey: top.1)
                let uid = user.removeValue(forKey: top.1)!
                return uid
            }
        }
        return -1
    }
}
'''

FILES["3409_longest_subsequence_with_decreasing_adjacent_difference"] = hdr("3409", "Longest Subsequence With Decreasing Adjacent Difference", "longest-subsequence-with-decreasing-adjacent-difference") + '''
class Solution {
    func longestSubsequence(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 1
        var dp = Array(repeating: Array(repeating: 0, count: 301), count: n)
        for i in 0..<n {
            for j in 0..<i {
                let d = abs(nums[i] - nums[j])
                var best = 1
                for pd in d...300 {
                    if dp[j][pd] > best { best = dp[j][pd] }
                }
                if best + 1 > dp[i][d] { dp[i][d] = best + 1 }
                if dp[i][d] > ans { ans = dp[i][d] }
            }
            if dp[i][0] < 1 { dp[i][0] = 1 }
        }
        return ans
    }
}
'''

FILES["3410_maximize_subarray_sum_after_removing_all_occurrences_of_one_element"] = hdr("3410", "Maximize Subarray Sum After Removing All Occurrences of One Element", "maximize-subarray-sum-after-removing-all-occurrences-of-one-element") + '''
class Solution {
    func maxSubarraySum(_ nums: [Int]) -> Int {
        var ans = kadane(nums)
        var uniq = Set<Int>()
        for x in nums where x < 0 { uniq.insert(x) }
        for v in uniq {
            let b = nums.filter { $0 != v }
            if b.isEmpty { continue }
            let cand = kadane(b)
            if cand > ans { ans = cand }
        }
        return ans
    }

    private func kadane(_ a: [Int]) -> Int {
        var best = -(1 << 62), cur = 0
        for x in a {
            cur += x
            if cur > best { best = cur }
            if cur < 0 { cur = 0 }
        }
        var allNeg = true
        var mx = a[0]
        for x in a {
            if x > mx { mx = x }
            if x >= 0 { allNeg = false }
        }
        if allNeg { return mx }
        return best
    }
}
'''

FILES["3411_maximum_subarray_with_equal_products"] = hdr("3411", "Maximum Subarray With Equal Products", "maximum-subarray-with-equal-products") + '''
class Solution {
    func maxLength(_ nums: [Int]) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        let n = nums.count
        var ans = 1
        for i in 0..<n {
            var prod = 1, g = 0, l = 1
            for j in i..<n {
                if prod > 1_000_000_000 / nums[j] { break }
                prod *= nums[j]
                if g == 0 { g = nums[j]; l = nums[j] }
                else {
                    g = gcd(g, nums[j])
                    l = l / gcd(l, nums[j]) * nums[j]
                }
                if prod == l * g && j - i + 1 > ans { ans = j - i + 1 }
            }
        }
        return ans
    }
}
'''

FILES["3412_find_mirror_score_of_a_string"] = hdr("3412", "Find Mirror Score of a String", "find-mirror-score-of-a-string") + '''
class Solution {
    func calculateScore(_ s: String) -> Int {
        var stacks = Array(repeating: [Int](), count: 26)
        var ans = 0
        for (i, ch) in s.enumerated() {
            let ci = Int(ch.asciiValue! - 97)
            let mir = 25 - ci
            if !stacks[mir].isEmpty {
                let j = stacks[mir].removeLast()
                ans += i - j
            } else {
                stacks[ci].append(i)
            }
        }
        return ans
    }
}
'''

FILES["3413_maximum_coins_from_k_consecutive_bags"] = hdr("3413", "Maximum Coins From K Consecutive Bags", "maximum-coins-from-k-consecutive-bags") + '''
class Solution {
    func maximumCoins(_ coins: [[Int]], _ k: Int) -> Int {
        let coins = coins.sorted { $0[0] < $1[0] }
        var ans = 0
        let n = coins.count
        for i in 0..<n {
            var sum = 0
            let start = coins[i][0]
            let end = start + k - 1
            var j = i
            while j < n && coins[j][0] <= end {
                var l = coins[j][0], r = coins[j][1]
                if r > end { r = end }
                if l < start { l = start }
                if l <= r { sum += (r - l + 1) * coins[j][2] }
                j += 1
            }
            if sum > ans { ans = sum }
        }
        for i in 0..<n {
            var sum = 0
            let end = coins[i][1]
            let start = end - k + 1
            for j in 0...i {
                var l = coins[j][0], r = coins[j][1]
                if l < start { l = start }
                if r > end { r = end }
                if l <= r { sum += (r - l + 1) * coins[j][2] }
            }
            if sum > ans { ans = sum }
        }
        return ans
    }
}
'''

FILES["3414_maximum_score_of_non_overlapping_intervals"] = hdr("3414", "Maximum Score of Non-overlapping Intervals", "maximum-score-of-non-overlapping-intervals") + '''
class Solution {
    func maximumWeight(_ intervals: [[Int]]) -> [Int] {
        let n = intervals.count
        var arr = [(l: Int, r: Int, w: Int, i: Int)]()
        for i in 0..<n { arr.append((intervals[i][0], intervals[i][1], intervals[i][2], i)) }
        arr.sort { $0.r < $1.r }
        struct State {
            var score: Int = 0
            var idx: [Int] = []
        }
        func better(_ a: State, _ b: State) -> State {
            if a.score != b.score { return a.score > b.score ? a : b }
            let m = min(a.idx.count, b.idx.count)
            for i in 0..<m {
                if a.idx[i] != b.idx[i] { return a.idx[i] < b.idx[i] ? a : b }
            }
            return a.idx.count <= b.idx.count ? a : b
        }
        var dp = Array(repeating: Array(repeating: State(), count: 5), count: n + 1)
        if n >= 1 {
            for i in 1...n {
                let cur = arr[i - 1]
                for t in 0...4 { dp[i][t] = dp[i - 1][t] }
                var lo = 0, hi = i - 1
                while lo < hi {
                    let mid = (lo + hi) / 2
                    if arr[mid].r < cur.l { lo = mid + 1 }
                    else { hi = mid }
                }
                let prev = lo
                for t in 1...4 {
                    var cand = dp[prev][t - 1]
                    cand.score += cur.w
                    cand.idx.append(cur.i)
                    cand.idx.sort()
                    dp[i][t] = better(dp[i][t], cand)
                }
            }
        }
        var best = dp[n][0]
        for t in 1...4 { best = better(best, dp[n][t]) }
        return best.idx
    }
}
'''

FILES["3417_zigzag_grid_traversal_with_skip"] = hdr("3417", "Zigzag Grid Traversal With Skip", "zigzag-grid-traversal-with-skip") + '''
class Solution {
    func zigzagTraversal(_ grid: [[Int]]) -> [Int] {
        var ans = [Int]()
        var skip = false
        for i in 0..<grid.count {
            let row = grid[i]
            if i % 2 == 0 {
                for v in row {
                    if !skip { ans.append(v) }
                    skip = !skip
                }
            } else {
                for j in stride(from: row.count - 1, through: 0, by: -1) {
                    if !skip { ans.append(row[j]) }
                    skip = !skip
                }
            }
        }
        return ans
    }
}
'''

FILES["3418_maximum_amount_of_money_robot_can_earn"] = hdr("3418", "Maximum Amount of Money Robot Can Earn", "maximum-amount-of-money-robot-can-earn") + '''
class Solution {
    func maximumAmount(_ coins: [[Int]]) -> Int {
        let m = coins.count, n = coins[0].count
        let neg = -(1 << 30)
        var dp = Array(repeating: Array(repeating: Array(repeating: neg, count: 3), count: n), count: m)
        if coins[0][0] < 0 {
            dp[0][0][0] = coins[0][0]
            dp[0][0][1] = 0
            dp[0][0][2] = 0
        } else {
            dp[0][0][0] = coins[0][0]
            dp[0][0][1] = coins[0][0]
            dp[0][0][2] = coins[0][0]
        }
        for i in 0..<m {
            for j in 0..<n {
                if i == 0 && j == 0 { continue }
                for k in 0..<3 {
                    var best = neg
                    if i > 0 { best = max(best, dp[i - 1][j][k]) }
                    if j > 0 { best = max(best, dp[i][j - 1][k]) }
                    if best == neg { continue }
                    if coins[i][j] >= 0 { dp[i][j][k] = best + coins[i][j] }
                    else { dp[i][j][k] = max(dp[i][j][k], best + coins[i][j]) }
                }
                for k in 1..<3 {
                    var best = neg
                    if i > 0 { best = max(best, dp[i - 1][j][k - 1]) }
                    if j > 0 { best = max(best, dp[i][j - 1][k - 1]) }
                    if best != neg && coins[i][j] < 0 { dp[i][j][k] = max(dp[i][j][k], best) }
                }
            }
        }
        return max(dp[m - 1][n - 1][0], max(dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]))
    }
}
'''

FILES["3419_minimize_the_maximum_edge_weight_of_graph"] = hdr("3419", "Minimize the Maximum Edge Weight of Graph", "minimize-the-maximum-edge-weight-of-graph") + '''
class Solution {
    func minMaxWeight(_ n: Int, _ edges: [[Int]], _ threshold: Int) -> Int {
        var lo = 1, hi = 1_000_001, ans = -1
        while lo < hi {
            let mid = (lo + hi) / 2
            if ok(n, edges, mid) {
                ans = mid
                hi = mid
            } else { lo = mid + 1 }
        }
        return ans
    }

    private func ok(_ n: Int, _ edges: [[Int]], _ mid: Int) -> Bool {
        var g = Array(repeating: [Int](), count: n)
        for e in edges where e[2] <= mid { g[e[1]].append(e[0]) }
        var vis = Array(repeating: false, count: n)
        var q = [0]
        vis[0] = true
        var cnt = 1, qi = 0
        while qi < q.count {
            let u = q[qi]; qi += 1
            for v in g[u] where !vis[v] {
                vis[v] = true
                cnt += 1
                q.append(v)
            }
        }
        return cnt == n
    }
}
'''

FILES["3420_count_non_decreasing_subarrays_after_k_operations"] = hdr("3420", "Count Non-Decreasing Subarrays After K Operations", "count-non-decreasing-subarrays-after-k-operations") + '''
class Solution {
    func countNonDecreasingSubarrays(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var cost = 0
            var maxV = nums[i]
            for j in i..<n {
                if nums[j] >= maxV { maxV = nums[j] }
                else { cost += maxV - nums[j] }
                if cost > k { break }
                ans += 1
            }
        }
        return ans
    }
}
'''

FILES["3422_minimum_operations_to_make_subarray_elements_equal"] = hdr("3422", "Minimum Operations to Make Subarray Elements Equal", "minimum-operations-to-make-subarray-elements-equal") + '''
class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var ans = 1 << 62
        if n < k { return 0 }
        for i in 0...(n - k) {
            var sub = Array(nums[i..<(i + k)])
            sub.sort()
            let med = sub[k / 2]
            var cost = 0
            for x in sub { cost += abs(x - med) }
            if cost < ans { ans = cost }
        }
        return ans
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
