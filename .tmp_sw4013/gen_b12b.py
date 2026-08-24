#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

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

LIST = '''
public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil }
    public init(_ val: Int) { self.val = val; self.next = nil }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}
'''

def w(folder, body):
    (ROOT / folder / "Solution.swift").write_text(body.strip() + "\n", encoding="utf-8")
    print("wrote", folder)

FILES = {}

FILES["2774_array_upper_bound"] = r'''
// LeetCode 2774 - Array Upper Bound
// https://leetcode.com/problems/array-upper-bound/

class Solution {
    func upperBound(_ nums: [Int], _ target: Int) -> Int {
        var lo = 0, hi = nums.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if nums[mid] <= target { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }
}
'''

FILES["2775_undefined_to_null"] = r'''
// LeetCode 2775 - Undefined to Null
// https://leetcode.com/problems/undefined-to-null/

class Solution {
    func undefinedToNull(_ obj: Int?) -> Int? {
        obj
    }
}
'''

FILES["2776_convert_callback_based_function_to_promise_based_function"] = r'''
// LeetCode 2776 - Convert Callback Based Function to Promise Based Function
// https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/

class Solution {
    func promisify(_ fn: @escaping ([Int], (Int) -> Void) -> Void) -> ([Int]) -> Int {
        { args in
            var result = 0
            fn(args) { result = $0 }
            return result
        }
    }
}
'''

FILES["2777_date_range_generator"] = r'''
// LeetCode 2777 - Date Range Generator
// https://leetcode.com/problems/date-range-generator/

class Solution {
    func dateRangeGenerator(_ start: String, _ end: String, _ step: Int) -> [String] {
        let sp = start.split(separator: "-").compactMap { Int($0) }
        let ep = end.split(separator: "-").compactMap { Int($0) }
        if sp.count != 3 || ep.count != 3 { return [] }
        var y = sp[0], m = sp[1], d = sp[2]
        let ey = ep[0], em = ep[1], ed = ep[2]
        var ans: [String] = []
        while cmp(y, m, d, ey, em, ed) {
            ans.append(String(format: "%04d-%02d-%02d", y, m, d))
            let ymd = addDays(y, m, d, step)
            y = ymd.0; m = ymd.1; d = ymd.2
        }
        return ans
    }

    private func isLeap(_ yy: Int) -> Bool {
        (yy % 4 == 0 && yy % 100 != 0) || (yy % 400 == 0)
    }

    private func addDays(_ yy0: Int, _ mm0: Int, _ dd0: Int, _ days0: Int) -> (Int, Int, Int) {
        var yy = yy0, mm = mm0, dd = dd0, days = days0
        while days > 0 {
            var mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            mdays[2] = isLeap(yy) ? 29 : 28
            dd += 1
            if dd > mdays[mm] { dd = 1; mm += 1 }
            if mm > 12 { mm = 1; yy += 1 }
            days -= 1
        }
        return (yy, mm, dd)
    }

    private func cmp(_ y: Int, _ m: Int, _ d: Int, _ ey: Int, _ em: Int, _ ed: Int) -> Bool {
        if y != ey { return y < ey }
        if m != em { return m < em }
        return d <= ed
    }
}
'''

FILES["2778_sum_of_squares_of_special_elements"] = r'''
// LeetCode 2778 - Sum of Squares of Special Elements
// https://leetcode.com/problems/sum-of-squares-of-special-elements/

class Solution {
    func sumOfSquares(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n where n % (i + 1) == 0 { ans += nums[i] * nums[i] }
        return ans
    }
}
'''

FILES["2779_maximum_beauty_of_an_array_after_applying_operation"] = r'''
// LeetCode 2779 - Maximum Beauty of an Array After Applying Operation
// https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

class Solution {
    func maximumBeauty(_ nums: [Int], _ k: Int) -> Int {
        let nums = nums.sorted()
        var ans = 0, left = 0
        for right in nums.indices {
            while nums[right] - nums[left] > 2 * k { left += 1 }
            ans = max(ans, right - left + 1)
        }
        return ans
    }
}
'''

FILES["2780_minimum_index_of_a_valid_split"] = r'''
// LeetCode 2780 - Minimum Index of a Valid Split
// https://leetcode.com/problems/minimum-index-of-a-valid-split/

class Solution {
    func minimumIndex(_ nums: [Int]) -> Int {
        var freq: [Int: Int] = [:]
        var dom = 0, best = 0
        for v in nums {
            freq[v, default: 0] += 1
            if freq[v]! > best {
                best = freq[v]!
                dom = v
            }
        }
        var left = 0
        let n = nums.count
        for i in 0..<(n - 1) {
            if nums[i] == dom { left += 1 }
            let right = best - left
            if left * 2 > i + 1 && right * 2 > n - i - 1 { return i }
        }
        return -1
    }
}
'''

FILES["2781_length_of_the_longest_valid_substring"] = r'''
// LeetCode 2781 - Length of the Longest Valid Substring
// https://leetcode.com/problems/length-of-the-longest-valid-substring/

class Solution {
    func longestValidSubstring(_ word: String, _ forbidden: [String]) -> Int {
        let forbid = Set(forbidden)
        let maxLen = forbidden.map(\.count).max() ?? 0
        let chars = Array(word)
        var ans = 0
        var right = chars.count - 1
        for left in stride(from: chars.count - 1, through: 0, by: -1) {
            var k = left
            while k <= right && k - left + 1 <= maxLen {
                if forbid.contains(String(chars[left...k])) {
                    right = k - 1
                    break
                }
                k += 1
            }
            ans = max(ans, right - left + 1)
        }
        return ans
    }
}
'''

FILES["2782_number_of_unique_categories"] = r'''
// LeetCode 2782 - Number of Unique Categories
// https://leetcode.com/problems/number-of-unique-categories/

protocol CategoryHandler {
    func haveSameCategory(_ a: Int, _ b: Int) -> Bool
}

class Solution {
    func numberOfCategories(_ n: Int, _ categoryHandler: CategoryHandler) -> Int {
        var parent = Array(0..<n)
        func find(_ x0: Int) -> Int {
            var x = x0
            while parent[x] != x {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        for i in 0..<n {
            for j in (i + 1)..<n where categoryHandler.haveSameCategory(i, j) {
                let a = find(i), b = find(j)
                if a != b { parent[a] = b }
            }
        }
        var ans = 0
        for i in 0..<n where find(i) == i { ans += 1 }
        return ans
    }
}
'''

FILES["2784_check_if_array_is_good"] = r'''
// LeetCode 2784 - Check if Array is Good
// https://leetcode.com/problems/check-if-array-is-good/

class Solution {
    func isGood(_ nums: [Int]) -> Bool {
        let n = nums.count - 1
        if n < 1 { return false }
        var freq = Array(repeating: 0, count: n + 1)
        for v in nums {
            if v < 1 || v > n { return false }
            freq[v] += 1
        }
        for i in 1..<n where freq[i] != 1 { return false }
        return freq[n] == 2
    }
}
'''

FILES["2785_sort_vowels_in_a_string"] = r'''
// LeetCode 2785 - Sort Vowels in a String
// https://leetcode.com/problems/sort-vowels-in-a-string/

class Solution {
    func sortVowels(_ s: String) -> String {
        var vowels = Array(s).filter { isVowel($0) }.sorted()
        var arr = Array(s)
        var vi = 0
        for i in arr.indices where isVowel(arr[i]) {
            arr[i] = vowels[vi]
            vi += 1
        }
        return String(arr)
    }

    private func isVowel(_ c: Character) -> Bool {
        "aeiouAEIOU".contains(c)
    }
}
'''

FILES["2786_visit_array_positions_to_maximize_score"] = r'''
// LeetCode 2786 - Visit Array Positions to Maximize Score
// https://leetcode.com/problems/visit-array-positions-to-maximize-score/

class Solution {
    func maxScore(_ nums: [Int], _ x: Int) -> Int {
        let NEG = -(1 << 60)
        var even = nums[0], odd = nums[0]
        if nums[0] % 2 == 0 { odd = NEG } else { even = NEG }
        for i in 1..<nums.count {
            let v = nums[i]
            if v % 2 == 0 {
                even = max(even + v, odd + v - x)
            } else {
                odd = max(odd + v, even + v - x)
            }
        }
        return max(even, odd)
    }
}
'''

FILES["2787_ways_to_express_an_integer_as_sum_of_powers"] = r'''
// LeetCode 2787 - Ways to Express an Integer as Sum of Powers
// https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

class Solution {
    func numberOfWays(_ n: Int, _ x: Int) -> Int {
        let MOD = 1_000_000_007
        var powers: [Int] = []
        var i = 1
        while true {
            var p = 1
            var overflow = false
            for _ in 0..<x {
                if p > n / i { overflow = true; break }
                p *= i
            }
            if overflow || p > n { break }
            powers.append(p)
            i += 1
        }
        var dp = Array(repeating: 0, count: n + 1)
        dp[0] = 1
        for p in powers {
            for s in stride(from: n, through: p, by: -1) {
                dp[s] = (dp[s] + dp[s - p]) % MOD
            }
        }
        return dp[n]
    }
}
'''

FILES["2788_split_strings_by_separator"] = r'''
// LeetCode 2788 - Split Strings by Separator
// https://leetcode.com/problems/split-strings-by-separator/

class Solution {
    func splitWordsBySeparator(_ words: [String], _ separator: Character) -> [String] {
        var ans: [String] = []
        for w in words {
            let chars = Array(w)
            var start = 0
            for i in 0...chars.count {
                if i == chars.count || chars[i] == separator {
                    if i > start { ans.append(String(chars[start..<i])) }
                    start = i + 1
                }
            }
        }
        return ans
    }
}
'''

FILES["2789_largest_element_in_an_array_after_merge_operations"] = r'''
// LeetCode 2789 - Largest Element in an Array after Merge Operations
// https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

class Solution {
    func maxArrayValue(_ nums: [Int]) -> Int {
        var cur = nums[nums.count - 1]
        var ans = cur
        for i in stride(from: nums.count - 2, through: 0, by: -1) {
            if nums[i] <= cur { cur += nums[i] } else { cur = nums[i] }
            ans = max(ans, cur)
        }
        return ans
    }
}
'''

FILES["2790_maximum_number_of_groups_with_increasing_length"] = r'''
// LeetCode 2790 - Maximum Number of Groups With Increasing Length
// https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

class Solution {
    func maxIncreasingGroups(_ usageLimits: [Int]) -> Int {
        let arr = usageLimits.sorted()
        var ans = 0, sum = 0
        for v in arr {
            sum += v
            let need = (ans + 1) * (ans + 2) / 2
            if sum >= need { ans += 1 }
        }
        return ans
    }
}
'''

FILES["2791_count_paths_that_can_form_a_palindrome_in_a_tree"] = r'''
// LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
// https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

class Solution {
    private var ans = 0
    private var freq: [Int: Int] = [:]
    private var g: [[Int]] = []
    private var s: [Character] = []

    func countPalindromePaths(_ parent: [Int], _ s: String) -> Int {
        let n = parent.count
        self.s = Array(s)
        g = Array(repeating: [], count: n)
        for i in 1..<n { g[parent[i]].append(i) }
        freq = [0: 1]
        ans = 0
        dfs(0, 0)
        return ans
    }

    private func dfs(_ u: Int, _ mask: Int) {
        for v in g[u] {
            let nm = mask ^ (1 << Int(s[v].asciiValue! - 97))
            ans += freq[nm, default: 0]
            for b in 0..<26 { ans += freq[nm ^ (1 << b), default: 0] }
            freq[nm, default: 0] += 1
            dfs(v, nm)
        }
    }
}
'''

FILES["2792_count_nodes_that_are_great_enough"] = f'''
// LeetCode 2792 - Count Nodes That Are Great Enough
// https://leetcode.com/problems/count-nodes-that-are-great-enough/
{TREE}
class Solution {{
    private var ans = 0
    private var k = 0

    func countGreatEnoughNodes(_ root: TreeNode?, _ k: Int) -> Int {{
        self.k = k
        self.ans = 0
        _ = dfs(root)
        return ans
    }}

    private func dfs(_ node: TreeNode?) -> [Int] {{
        guard let node = node else {{ return [] }}
        var vals = merge(dfs(node.left), dfs(node.right))
        var smaller = 0
        for v in vals where v < node.val {{ smaller += 1 }}
        if smaller >= k {{ ans += 1 }}
        vals.append(node.val)
        vals.sort()
        if vals.count > k {{ vals = Array(vals.prefix(k)) }}
        return vals
    }}

    private func merge(_ a: [Int], _ b: [Int]) -> [Int] {{
        var i = 0, j = 0, out: [Int] = []
        while i < a.count && j < b.count && out.count < k {{
            if a[i] < b[j] {{ out.append(a[i]); i += 1 }} else {{ out.append(b[j]); j += 1 }}
        }}
        while i < a.count && out.count < k {{ out.append(a[i]); i += 1 }}
        while j < b.count && out.count < k {{ out.append(b[j]); j += 1 }}
        return out
    }}
}}
'''

FILES["2794_create_object_from_two_arrays"] = r'''
// LeetCode 2794 - Create Object from Two Arrays
// https://leetcode.com/problems/create-object-from-two-arrays/

class Solution {
    func createObject(_ keysArr: [String], _ valuesArr: [Int]) -> [String: Int] {
        var output: [String: Int] = [:]
        let n = min(keysArr.count, valuesArr.count)
        for i in 0..<n where output[keysArr[i]] == nil {
            output[keysArr[i]] = valuesArr[i]
        }
        return output
    }
}
'''

FILES["2795_parallel_execution_of_promises_for_individual_results_retrieval"] = r'''
// LeetCode 2795 - Parallel Execution of Promises for Individual Results Retrieval
// https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/

class Solution {
    func promiseAllSettled(_ functions: [() -> Int]) -> [(String, Int)] {
        functions.map { ("fulfilled", $0()) }
    }
}
'''

FILES["2796_repeat_string"] = r'''
// LeetCode 2796 - Repeat String
// https://leetcode.com/problems/repeat-string/

class Solution {
    func replicate(_ str: String, _ times: Int) -> String {
        if times <= 0 { return "" }
        return String(repeating: str, count: times)
    }
}
'''

FILES["2797_partial_function_with_placeholders"] = r'''
// LeetCode 2797 - Partial Function with Placeholders
// https://leetcode.com/problems/partial-function-with-placeholders/

class Solution {
    func partial(_ fn: @escaping ([Int]) -> Int, _ args: [Int]) -> ([Int]) -> Int {
        { rest in
            var full: [Int] = []
            var ri = 0
            for a in args {
                if a == Int.min, ri < rest.count {
                    full.append(rest[ri])
                    ri += 1
                } else {
                    full.append(a)
                }
            }
            while ri < rest.count {
                full.append(rest[ri])
                ri += 1
            }
            return fn(full)
        }
    }
}
'''

FILES["2798_number_of_employees_who_met_the_target"] = r'''
// LeetCode 2798 - Number of Employees Who Met the Target
// https://leetcode.com/problems/number-of-employees-who-met-the-target/

class Solution {
    func numberOfEmployeesWhoMetTarget(_ hours: [Int], _ target: Int) -> Int {
        hours.filter { $0 >= target }.count
    }
}
'''

FILES["2799_count_complete_subarrays_in_an_array"] = r'''
// LeetCode 2799 - Count Complete Subarrays in an Array
// https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution {
    func countCompleteSubarrays(_ nums: [Int]) -> Int {
        let need = Set(nums).count
        var ans = 0
        let n = nums.count
        for i in 0..<n {
            var seen = Set<Int>()
            for j in i..<n {
                seen.insert(nums[j])
                if seen.count == need {
                    ans += n - j
                    break
                }
            }
        }
        return ans
    }
}
'''

FILES["2800_shortest_string_that_contains_three_strings"] = r'''
// LeetCode 2800 - Shortest String That Contains Three Strings
// https://leetcode.com/problems/shortest-string-that-contains-three-strings/

class Solution {
    func minimumString(_ a: String, _ b: String, _ c: String) -> String {
        let perms = [[a, b, c], [a, c, b], [b, a, c], [b, c, a], [c, a, b], [c, b, a]]
        var ans = ""
        for p in perms {
            let cur = merge(merge(p[0], p[1]), p[2])
            if ans.isEmpty || cur.count < ans.count || (cur.count == ans.count && cur < ans) {
                ans = cur
            }
        }
        return ans
    }

    private func merge(_ x: String, _ y: String) -> String {
        if x.contains(y) { return x }
        var best = x + y
        let n = min(x.count, y.count)
        for i in stride(from: n, through: 1, by: -1) {
            if x.suffix(i) == y.prefix(i) {
                let cand = x + String(y.dropFirst(i))
                if cand.count < best.count || (cand.count == best.count && cand < best) {
                    best = cand
                }
                break
            }
        }
        return best
    }
}
'''

FILES["2801_count_stepping_numbers_in_range"] = r'''
// LeetCode 2801 - Count Stepping Numbers in Range
// https://leetcode.com/problems/count-stepping-numbers-in-range/

class Solution {
    private let MOD = 1_000_000_007

    func countSteppingNumbers(_ low: String, _ high: String) -> Int {
        var ans = (countTo(high) - countTo(dec(low))) % MOD
        if ans < 0 { ans += MOD }
        return ans
    }

    private func countTo(_ s: String) -> Int {
        var memo = Array(repeating: Array(repeating: Array(repeating: Array(repeating: -1, count: 2), count: 11), count: 2), count: 85)
        return dfs(Array(s), 0, 1, -1, 0, &memo)
    }

    private func dfs(_ s: [Character], _ pos: Int, _ tight: Int, _ last: Int, _ started: Int, _ memo: inout [[[[Int]]]]) -> Int {
        if pos == s.count { return started }
        if memo[pos][tight][last + 1][started] != -1 { return memo[pos][tight][last + 1][started] }
        let up = tight == 1 ? Int(String(s[pos]))! : 9
        var ans = 0
        for d in 0...up {
            let nt = (tight == 1 && d == up) ? 1 : 0
            if started == 0 {
                ans += d == 0 ? dfs(s, pos + 1, nt, -1, 0, &memo) : dfs(s, pos + 1, nt, d, 1, &memo)
            } else if abs(d - last) == 1 {
                ans += dfs(s, pos + 1, nt, d, 1, &memo)
            }
            ans %= MOD
        }
        memo[pos][tight][last + 1][started] = ans
        return ans
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
}
'''

FILES["2802_find_the_k_th_lucky_number"] = r'''
// LeetCode 2802 - Find The K-th Lucky Number
// https://leetcode.com/problems/find-the-k-th-lucky-number/

class Solution {
    func kthLuckyNumber(_ k: Int) -> String {
        var k = k + 1
        var bits = ""
        while k > 1 {
            bits = (k % 2 == 0 ? "4" : "7") + bits
            k /= 2
        }
        return bits
    }
}
'''

FILES["2803_factorial_generator"] = r'''
// LeetCode 2803 - Factorial Generator
// https://leetcode.com/problems/factorial-generator/

class Solution {
    func factorialGenerator(_ n: Int) -> [Int] {
        var ans: [Int] = []
        var cur = 1
        if n >= 0 { ans.append(1) }
        for i in 1...max(n, 1) where i <= n {
            cur *= i
            ans.append(cur)
        }
        return n == 0 ? [1] : (n < 1 ? [] : ans)
    }

    func factorialGen(_ n: Int) -> () -> Int {
        var i = 0
        var cur = 1
        return {
            if i == 0 {
                i = 1
                return 1
            }
            cur *= i
            i += 1
            return cur
        }
    }
}
'''

FILES["2804_array_prototype_foreach"] = r'''
// LeetCode 2804 - Array Prototype ForEach
// https://leetcode.com/problems/array-prototype-foreach/

class Solution {
    func forEach(_ arr: [Int], _ callback: (Int, Int, [Int]) -> Void) {
        for i in arr.indices { callback(arr[i], i, arr) }
    }
}
'''

FILES["2805_custom_interval"] = r'''
// LeetCode 2805 - Custom Interval
// https://leetcode.com/problems/custom-interval/

class Solution {
    func customInterval(_ fn: @escaping () -> Void, _ delay: Int, _ period: Int) -> () -> Void {
        var cancelled = false
        return { cancelled = true }
    }
}
'''

FILES["2806_account_balance_after_rounded_purchase"] = r'''
// LeetCode 2806 - Account Balance After Rounded Purchase
// https://leetcode.com/problems/account-balance-after-rounded-purchase/

class Solution {
    func accountBalanceAfterPurchase(_ purchaseAmount: Int) -> Int {
        100 - ((purchaseAmount + 5) / 10) * 10
    }
}
'''

FILES["2807_insert_greatest_common_divisors_in_linked_list"] = f'''
// LeetCode 2807 - Insert Greatest Common Divisors in Linked List
// https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
{LIST}
class Solution {{
    func insertGreatestCommonDivisors(_ head: ListNode?) -> ListNode? {{
        var cur = head
        while let node = cur, let nxt = node.next {{
            let g = gcd(node.val, nxt.val)
            node.next = ListNode(g, nxt)
            cur = node.next?.next
        }}
        return head
    }}

    private func gcd(_ a0: Int, _ b0: Int) -> Int {{
        var a = a0, b = b0
        while b != 0 {{
            let t = a % b
            a = b
            b = t
        }}
        return a
    }}
}}
'''

FILES["2808_minimum_seconds_to_equalize_a_circular_array"] = r'''
// LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
// https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

class Solution {
    func minimumSeconds(_ nums: [Int]) -> Int {
        let n = nums.count
        var pos: [Int: [Int]] = [:]
        for i in 0..<n { pos[nums[i], default: []].append(i) }
        var ans = n
        for p in pos.values {
            var maxGap = 0
            for i in p.indices {
                let gap = i + 1 < p.count ? p[i + 1] - p[i] : p[0] + n - p[i]
                maxGap = max(maxGap, gap / 2)
            }
            ans = min(ans, maxGap)
        }
        return ans
    }
}
'''

FILES["2809_minimum_time_to_make_array_sum_at_most_x"] = r'''
// LeetCode 2809 - Minimum Time to Make Array Sum At Most x
// https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

class Solution {
    func minimumTime(_ nums1: [Int], _ nums2: [Int], _ x: Int) -> Int {
        let n = nums1.count
        var arr = (0..<n).map { (nums1[$0], nums2[$0]) }
        arr.sort { $0.1 < $1.1 }
        let sum1 = nums1.reduce(0, +)
        let sum2 = nums2.reduce(0, +)
        var dp = Array(repeating: 0, count: n + 1)
        for i in 0..<n {
            for j in stride(from: i + 1, through: 1, by: -1) {
                dp[j] = max(dp[j], dp[j - 1] + arr[i].0 + j * arr[i].1)
            }
        }
        for t in 0...n where sum1 + sum2 * t - dp[t] <= x { return t }
        return -1
    }
}
'''

FILES["2810_faulty_keyboard"] = r'''
// LeetCode 2810 - Faulty Keyboard
// https://leetcode.com/problems/faulty-keyboard/

class Solution {
    func finalString(_ s: String) -> String {
        var b: [Character] = []
        for c in s {
            if c == "i" { b.reverse() } else { b.append(c) }
        }
        return String(b)
    }
}
'''

FILES["2811_check_if_it_is_possible_to_split_array"] = r'''
// LeetCode 2811 - Check if it is Possible to Split Array
// https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

class Solution {
    func canSplitArray(_ nums: [Int], _ m: Int) -> Bool {
        let n = nums.count
        if n <= 2 { return true }
        for i in 0..<(n - 1) where nums[i] + nums[i + 1] >= m { return true }
        return false
    }
}
'''

FILES["2812_find_the_safest_path_in_a_grid"] = r'''
// LeetCode 2812 - Find the Safest Path in a Grid
// https://leetcode.com/problems/find-the-safest-path-in-a-grid/

class Solution {
    func maximumSafenessFactor(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var dist = Array(repeating: Array(repeating: -1, count: n), count: n)
        var q: [(Int, Int)] = []
        for i in 0..<n {
            for j in 0..<n where grid[i][j] == 1 {
                dist[i][j] = 0
                q.append((i, j))
            }
        }
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        var head = 0
        while head < q.count {
            let (x, y) = q[head]; head += 1
            for d in dirs {
                let ni = x + d.0, nj = y + d.1
                if ni >= 0 && ni < n && nj >= 0 && nj < n && dist[ni][nj] == -1 {
                    dist[ni][nj] = dist[x][y] + 1
                    q.append((ni, nj))
                }
            }
        }
        var lo = 0, hi = n * n, ans = 0
        while lo <= hi {
            let mid = (lo + hi) / 2
            if ok(dist, dirs, mid) {
                ans = mid
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return ans
    }

    private func ok(_ dist: [[Int]], _ dirs: [(Int, Int)], _ sf: Int) -> Bool {
        let n = dist.count
        if dist[0][0] < sf { return false }
        var seen = Array(repeating: Array(repeating: false, count: n), count: n)
        var st = [(0, 0)]
        seen[0][0] = true
        while !st.isEmpty {
            let (x, y) = st.removeLast()
            if x == n - 1 && y == n - 1 { return true }
            for d in dirs {
                let ni = x + d.0, nj = y + d.1
                if ni >= 0 && ni < n && nj >= 0 && nj < n && !seen[ni][nj] && dist[ni][nj] >= sf {
                    seen[ni][nj] = true
                    st.append((ni, nj))
                }
            }
        }
        return false
    }
}
'''

FILES["2813_maximum_elegance_of_a_k_length_subsequence"] = r'''
// LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
// https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

class Solution {
    func findMaximumElegance(_ items: [[Int]], _ k: Int) -> Int {
        let items = items.sorted { $0[0] > $1[0] }
        var seen = Set<Int>()
        var total = 0
        var dup: [Int] = []
        for i in 0..<k {
            total += items[i][0]
            let c = items[i][1]
            if seen.contains(c) { dup.append(items[i][0]) } else { seen.insert(c) }
        }
        var ans = total + seen.count * seen.count
        for i in k..<items.count {
            let c = items[i][1]
            if seen.contains(c) || dup.isEmpty { continue }
            total += items[i][0] - dup.removeLast()
            seen.insert(c)
            ans = max(ans, total + seen.count * seen.count)
        }
        return ans
    }
}
'''

FILES["2814_minimum_time_takes_to_reach_destination_without_drowning"] = r'''
// LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
// https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

class Solution {
    func minimumSeconds(_ land: [[String]]) -> Int {
        let m = land.count, n = land[0].count
        let INF = 1 << 30
        var water = Array(repeating: Array(repeating: INF, count: n), count: m)
        var wq: [(Int, Int)] = []
        var sx = 0, sy = 0, dx = 0, dy = 0
        for i in 0..<m {
            for j in 0..<n {
                switch land[i][j] {
                case "*":
                    water[i][j] = 0
                    wq.append((i, j))
                case "S":
                    sx = i; sy = j
                case "D":
                    dx = i; dy = j
                default:
                    break
                }
            }
        }
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        var head = 0
        while head < wq.count {
            let (x, y) = wq[head]; head += 1
            for d in dirs {
                let ni = x + d.0, nj = y + d.1
                if ni < 0 || ni >= m || nj < 0 || nj >= n { continue }
                let cell = land[ni][nj]
                if cell == "X" || cell == "D" { continue }
                if water[ni][nj] > water[x][y] + 1 {
                    water[ni][nj] = water[x][y] + 1
                    wq.append((ni, nj))
                }
            }
        }
        var dist = Array(repeating: Array(repeating: -1, count: n), count: m)
        var q = [(sx, sy)]
        dist[sx][sy] = 0
        head = 0
        while head < q.count {
            let (x, y) = q[head]; head += 1
            if x == dx && y == dy { return dist[x][y] }
            for d in dirs {
                let ni = x + d.0, nj = y + d.1
                if ni < 0 || ni >= m || nj < 0 || nj >= n || dist[ni][nj] != -1 { continue }
                if land[ni][nj] == "X" { continue }
                let nd = dist[x][y] + 1
                if land[ni][nj] != "D" && nd >= water[ni][nj] { continue }
                dist[ni][nj] = nd
                q.append((ni, nj))
            }
        }
        return -1
    }
}
'''

FILES["2815_max_pair_sum_in_an_array"] = r'''
// LeetCode 2815 - Max Pair Sum in an Array
// https://leetcode.com/problems/max-pair-sum-in-an-array/

class Solution {
    func maxSum(_ nums: [Int]) -> Int {
        var best: [Int: Int] = [:]
        var ans = -1
        for v in nums {
            var x = v, md = 0
            while x > 0 { md = max(md, x % 10); x /= 10 }
            if let prev = best[md] {
                ans = max(ans, prev + v)
                best[md] = max(prev, v)
            } else {
                best[md] = v
            }
        }
        return ans
    }
}
'''

FILES["2816_double_a_number_represented_as_a_linked_list"] = f'''
// LeetCode 2816 - Double a Number Represented as a Linked List
// https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
{LIST}
class Solution {{
    func doubleIt(_ head: ListNode?) -> ListNode? {{
        var head = rev(head)
        var carry = 0
        var cur = head
        var prev: ListNode? = nil
        while let node = cur {{
            let val = node.val * 2 + carry
            node.val = val % 10
            carry = val / 10
            prev = node
            cur = node.next
        }}
        if carry > 0 {{ prev?.next = ListNode(carry) }}
        return rev(head)
    }}

    private func rev(_ node0: ListNode?) -> ListNode? {{
        var node = node0
        var prev: ListNode? = nil
        while let cur = node {{
            let nxt = cur.next
            cur.next = prev
            prev = cur
            node = nxt
        }}
        return prev
    }}
}}
'''

FILES["2817_minimum_absolute_difference_between_elements_with_constraint"] = r'''
// LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
// https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

class Solution {
    func minAbsoluteDifference(_ nums: [Int], _ x: Int) -> Int {
        if x == 0 {
            var ans0 = Int.max
            for i in 1..<nums.count { ans0 = min(ans0, abs(nums[i] - nums[i - 1])) }
            return ans0
        }
        var ans = Int.max
        var arr: [Int] = []
        for i in x..<nums.count {
            insert(&arr, nums[i - x])
            let cur = nums[i]
            let idx = lowerBound(arr, cur)
            if idx < arr.count { ans = min(ans, arr[idx] - cur) }
            if idx > 0 { ans = min(ans, cur - arr[idx - 1]) }
        }
        return ans
    }

    private func insert(_ a: inout [Int], _ x: Int) {
        let i = lowerBound(a, x)
        a.insert(x, at: i)
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

FILES["2818_apply_operations_to_maximize_score"] = r'''
// LeetCode 2818 - Apply Operations to Maximize Score
// https://leetcode.com/problems/apply-operations-to-maximize-score/

class Solution {
    private let MOD = 1_000_000_007

    func maximumScore(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        let maxV = nums.max() ?? 0
        var spf = Array(repeating: 0, count: maxV + 1)
        if maxV >= 2 {
            for i in 2...maxV where spf[i] == 0 {
                var j = i
                while j <= maxV {
                    if spf[j] == 0 { spf[j] = i }
                    j += i
                }
            }
        }
        let score = nums.map { primeScore($0, spf) }
        var left = Array(repeating: 0, count: n)
        var right = Array(repeating: 0, count: n)
        var st: [Int] = []
        for i in 0..<n {
            while !st.isEmpty && score[st.last!] < score[i] { st.removeLast() }
            left[i] = st.isEmpty ? -1 : st.last!
            st.append(i)
        }
        st.removeAll()
        for i in stride(from: n - 1, through: 0, by: -1) {
            while !st.isEmpty && score[st.last!] <= score[i] { st.removeLast() }
            right[i] = st.isEmpty ? n : st.last!
            st.append(i)
        }
        var arr = (0..<n).map { (nums[$0], (i: $0 - left[$0]) * (right[$0] - $0)) }
        arr.sort { $0.0 > $1.0 }
        var ans = 1
        var remain = k
        for pair in arr {
            if remain <= 0 { break }
            let use = min(pair.1, remain)
            ans = ans * modPow(pair.0, use) % MOD
            remain -= use
        }
        return ans
    }

    private func primeScore(_ x0: Int, _ spf: [Int]) -> Int {
        var x = x0
        var seen = Set<Int>()
        while x > 1 {
            let p = spf[x]
            seen.insert(p)
            while x % p == 0 { x /= p }
        }
        return seen.count
    }

    private func modPow(_ a0: Int, _ b0: Int) -> Int {
        var a = a0 % MOD, b = b0, res = 1
        while b > 0 {
            if b & 1 != 0 { res = res * a % MOD }
            a = a * a % MOD
            b >>= 1
        }
        return res
    }
}
'''

FILES["2819_minimum_relative_loss_after_buying_chocolates"] = r'''
// LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
// https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

class Solution {
    func minimumRelativeLosses(_ prices: [Int], _ queries: [[Int]]) -> [Int] {
        let prices = prices.sorted()
        let n = prices.count
        return queries.map { q in
            let kk = q[0], m = q[1]
            var losses = prices.map { $0 <= kk ? $0 : 2 * kk - $0 }
            losses.sort()
            return losses.prefix(m).reduce(0, +)
        }
    }
}
'''

FILES["2821_delay_the_resolution_of_each_promise"] = r'''
// LeetCode 2821 - Delay the Resolution of Each Promise
// https://leetcode.com/problems/delay-the-resolution-of-each-promise/

class Solution {
    func delayAll(_ functions: [() -> Int], _ ms: Int) -> [() -> Int] {
        functions
    }
}
'''

FILES["2822_inversion_of_object"] = r'''
// LeetCode 2822 - Inversion of Object
// https://leetcode.com/problems/inversion-of-object/

class Solution {
    func invertObject(_ obj: [String: String]) -> [String: [String]] {
        var output: [String: [String]] = [:]
        for (k, v) in obj { output[v, default: []].append(k) }
        return output
    }
}
'''

FILES["2823_deep_object_filter"] = r'''
// LeetCode 2823 - Deep Object Filter
// https://leetcode.com/problems/deep-object-filter/

class Solution {
    func deepFilter(_ obj: [Int], _ fn: (Int) -> Bool) -> [Int] {
        obj.filter(fn)
    }
}
'''

FILES["2824_count_pairs_whose_sum_is_less_than_target"] = r'''
// LeetCode 2824 - Count Pairs Whose Sum is Less than Target
// https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution {
    func countPairs(_ nums: [Int], _ target: Int) -> Int {
        var ans = 0
        for i in nums.indices {
            for j in (i + 1)..<nums.count where nums[i] + nums[j] < target { ans += 1 }
        }
        return ans
    }
}
'''

FILES["2825_make_string_a_subsequence_using_cyclic_increments"] = r'''
// LeetCode 2825 - Make String a Subsequence Using Cyclic Increments
// https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

class Solution {
    func canMakeSubsequence(_ str1: String, _ str2: String) -> Bool {
        let a = Array(str1), b = Array(str2)
        var j = 0
        for ch in a where j < b.count {
            let av = Int(ch.asciiValue! - 97)
            let bv = Int(b[j].asciiValue! - 97)
            if av == bv || (av + 1) % 26 == bv { j += 1 }
        }
        return j == b.count
    }
}
'''

FILES["2826_sorting_three_groups"] = r'''
// LeetCode 2826 - Sorting Three Groups
// https://leetcode.com/problems/sorting-three-groups/

class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        let n = nums.count
        let INF = 1 << 30
        var dp = Array(repeating: Array(repeating: INF, count: 4), count: n + 1)
        dp[0][1] = 0; dp[0][2] = 0; dp[0][3] = 0
        for i in 1...n {
            let v = nums[i - 1]
            for g in 1...3 {
                let cost = v != g ? 1 : 0
                for prev in 1...g {
                    dp[i][g] = min(dp[i][g], dp[i - 1][prev] + cost)
                }
            }
        }
        return min(dp[n][1], dp[n][2], dp[n][3])
    }
}
'''

FILES["2827_number_of_beautiful_integers_in_the_range"] = r'''
// LeetCode 2827 - Number of Beautiful Integers in the Range
// https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

class Solution {
    func numberOfBeautifulIntegers(_ low: Int, _ high: Int, _ k: Int) -> Int {
        count(high, k) - count(low - 1, k)
    }

    private func count(_ n: Int, _ k: Int) -> Int {
        if n < 0 { return 0 }
        let s = Array(String(n))
        var memo = Array(repeating: Array(repeating: Array(repeating: Array(repeating: Array(repeating: -1, count: 2), count: 2), count: 22), count: 45), count: 12)
        return dfs(s, k, 0, 0, 0, 1, 0, &memo)
    }

    private func dfs(_ s: [Character], _ k: Int, _ pos: Int, _ diff: Int, _ mod: Int, _ tight: Int, _ started: Int, _ memo: inout [[[[[Int]]]]]) -> Int {
        if pos == s.count { return started == 1 && diff == 0 && mod == 0 ? 1 : 0 }
        if memo[pos][diff + 20][mod][tight][started] != -1 {
            return memo[pos][diff + 20][mod][tight][started]
        }
        let up = tight == 1 ? Int(String(s[pos]))! : 9
        var ans = 0
        for digit in 0...up {
            let nt = (tight == 1 && digit == up) ? 1 : 0
            if started == 0 {
                if digit == 0 {
                    ans += dfs(s, k, pos + 1, diff, mod, nt, 0, &memo)
                } else {
                    let nd = diff + (digit % 2 == 0 ? 1 : -1)
                    ans += dfs(s, k, pos + 1, nd, digit % k, nt, 1, &memo)
                }
            } else {
                let nd = diff + (digit % 2 == 0 ? 1 : -1)
                ans += dfs(s, k, pos + 1, nd, (mod * 10 + digit) % k, nt, 1, &memo)
            }
        }
        memo[pos][diff + 20][mod][tight][started] = ans
        return ans
    }
}
'''

FILES["2828_check_if_a_string_is_an_acronym_of_words"] = r'''
// LeetCode 2828 - Check if a String Is an Acronym of Words
// https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

class Solution {
    func isAcronym(_ words: [String], _ s: String) -> Bool {
        let chars = Array(s)
        if words.count != chars.count { return false }
        for i in words.indices {
            guard let first = words[i].first, first == chars[i] else { return false }
        }
        return true
    }
}
'''

FILES["2829_determine_the_minimum_sum_of_a_k_avoiding_array"] = r'''
// LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
// https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

class Solution {
    func minimumSum(_ n: Int, _ k: Int) -> Int {
        var used = Set<Int>()
        var sum = 0, x = 1
        while used.count < n {
            if !used.contains(k - x) {
                used.insert(x)
                sum += x
            }
            x += 1
        }
        return sum
    }
}
'''

FILES["2830_maximize_the_profit_as_the_salesman"] = r'''
// LeetCode 2830 - Maximize the Profit as the Salesman
// https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

class Solution {
    func maximizeTheProfit(_ n: Int, _ offers: [[Int]]) -> Int {
        var byEnd = Array(repeating: [[Int]](), count: n)
        for o in offers { byEnd[o[1]].append(o) }
        var dp = Array(repeating: 0, count: n + 1)
        for end in 0..<n {
            dp[end + 1] = dp[end]
            for o in byEnd[end] {
                dp[end + 1] = max(dp[end + 1], dp[o[0]] + o[2])
            }
        }
        return dp[n]
    }
}
'''

FILES["2831_find_the_longest_equal_subarray"] = r'''
// LeetCode 2831 - Find the Longest Equal Subarray
// https://leetcode.com/problems/find-the-longest-equal-subarray/

class Solution {
    func longestEqualSubarray(_ nums: [Int], _ k: Int) -> Int {
        var pos: [Int: [Int]] = [:]
        for i in nums.indices { pos[nums[i], default: []].append(i) }
        var ans = 0
        for p in pos.values {
            var left = 0
            for right in p.indices {
                while p[right] - p[left] - (right - left) > k { left += 1 }
                ans = max(ans, right - left + 1)
            }
        }
        return ans
    }
}
'''

def main():
    for folder, body in FILES.items():
        w(folder, body)
    print("total", len(FILES))

if __name__ == "__main__":
    main()
