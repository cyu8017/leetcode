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


write("3739_count_subarrays_with_majority_element_ii", """// LeetCode 3739 - Count Subarrays With Majority Element II
// https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

class Solution {
    private class BIT {
        var n: Int
        var c: [Int]
        init(_ n_: Int) {
            n = n_
            c = [Int](repeating: 0, count: n_ + 1)
        }
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

    func countMajoritySubarrays(_ nums: [Int], _ target: Int) -> Int {
        let n = nums.count
        let tree = BIT(2 * n + 1)
        var s = n + 1
        tree.update(s, 1)
        var ans = 0
        for x in nums {
            if x == target { s += 1 } else { s -= 1 }
            ans += tree.query(s - 1)
            tree.update(s, 1)
        }
        return ans
    }
}
""")

write("3740_minimum_distance_between_three_equal_elements_i", """// LeetCode 3740 - Minimum Distance Between Three Equal Elements I
// https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/

class Solution {
    func minimumDistance(_ nums: [Int]) -> Int {
        var g = [Int: [Int]]()
        for i in 0..<nums.count {
            g[nums[i], default: []].append(i)
        }
        let inf = 1 << 30
        var ans = inf
        for ls in g.values {
            let m = ls.count
            if m >= 3 {
                for h in 0..<(m - 2) {
                    ans = min(ans, (ls[h + 2] - ls[h]) * 2)
                }
            }
        }
        return ans == inf ? -1 : ans
    }
}
""")

write("3741_minimum_distance_between_three_equal_elements_ii", """// LeetCode 3741 - Minimum Distance Between Three Equal Elements II
// https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

class Solution {
    func minimumDistance(_ nums: [Int]) -> Int {
        var g = [Int: [Int]]()
        for i in 0..<nums.count {
            g[nums[i], default: []].append(i)
        }
        let inf = 1 << 30
        var ans = inf
        for ls in g.values {
            let m = ls.count
            if m >= 3 {
                for h in 0..<(m - 2) {
                    ans = min(ans, (ls[h + 2] - ls[h]) * 2)
                }
            }
        }
        return ans == inf ? -1 : ans
    }
}
""")

write("3742_maximum_path_score_in_a_grid", """// LeetCode 3742 - Maximum Path Score In A Grid
// https://leetcode.com/problems/maximum-path-score-in-a-grid/

class Solution {
    private var grid = [[Int]]()
    private var f = [[[Int]]]()
    private var m = 0, n = 0
    private let INF = 1 << 30

    func maxPathScore(_ grid: [[Int]], _ k: Int) -> Int {
        self.grid = grid
        m = grid.count
        n = grid[0].count
        f = Array(repeating: Array(repeating: [Int](repeating: -1, count: k + 1), count: n), count: m)
        let ans = dfs(m - 1, n - 1, k)
        return ans < 0 ? -1 : ans
    }

    private func dfs(_ i: Int, _ j: Int, _ kk: Int) -> Int {
        if i < 0 || j < 0 || kk < 0 { return -INF }
        if i == 0 && j == 0 { return 0 }
        if f[i][j][kk] != -1 { return f[i][j][kk] }
        var res = grid[i][j]
        var nk = kk
        if grid[i][j] != 0 { nk -= 1 }
        let a = dfs(i - 1, j, nk)
        let b = dfs(i, j - 1, nk)
        res += max(a, b)
        f[i][j][kk] = res
        return res
    }
}
""")

write("3743_maximize_cyclic_partition_score", """// LeetCode 3743 - Maximize Cyclic Partition Score
// https://leetcode.com/problems/maximize-cyclic-partition-score/

class Solution {
    func maximumScore(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var a = nums + nums
        var kk = k
        if kk > n { kk = n }
        var best = 0
        let NEG = -(1 << 60)
        for start in 0..<n {
            let seg = Array(a[start..<(start + n)])
            var dp = Array(repeating: [Int](repeating: NEG, count: kk + 1), count: n + 1)
            dp[0][0] = 0
            for i in 1...n {
                let jmax = min(kk, i)
                if jmax >= 1 {
                    for j in 1...jmax {
                        var mx = NEG
                        for t in stride(from: i, through: j, by: -1) {
                            if seg[t - 1] > mx { mx = seg[t - 1] }
                            if dp[t - 1][j - 1] > NEG {
                                let cand = dp[t - 1][j - 1] + mx
                                if cand > dp[i][j] { dp[i][j] = cand }
                            }
                        }
                    }
                }
            }
            if dp[n][kk] > best { best = dp[n][kk] }
        }
        return best
    }
}
""")

write("3744_find_kth_character_in_expanded_string", """// LeetCode 3744 - Find Kth Character in Expanded String
// https://leetcode.com/problems/find-kth-character-in-expanded-string/

class Solution {
    func kthCharacter(_ s: String, _ k: Int) -> Character {
        var k = k
        let words = s.split { $0.isWhitespace }.map(String.init)
        for w in words {
            let chars = Array(w)
            let m = (1 + chars.count) * chars.count / 2
            if k == m { return " " }
            if k > m {
                k -= m + 1
            } else {
                var cur = 0
                var i = 0
                while true {
                    cur += i + 1
                    if k < cur { return chars[i] }
                    i += 1
                }
            }
        }
        return " "
    }
}
""")

write("3745_maximize_expression_of_three_elements", """// LeetCode 3745 - Maximize Expression of Three Elements
// https://leetcode.com/problems/maximize-expression-of-three-elements/

class Solution {
    func maximizeExpressionOfThree(_ nums: [Int]) -> Int {
        let inf = 1 << 30
        var a = -inf, b = -inf, c = inf
        for x in nums {
            if x < c { c = x }
            if x >= a { b = a; a = x }
            else if x > b { b = x }
        }
        return a + b - c
    }
}
""")

write("3746_minimum_string_length_after_balanced_removals", """// LeetCode 3746 - Minimum String Length After Balanced Removals
// https://leetcode.com/problems/minimum-string-length-after-balanced-removals/

class Solution {
    func minLengthAfterRemovals(_ s: String) -> Int {
        var a = 0
        for c in s where c == "a" { a += 1 }
        let b = s.count - a
        return abs(a - b)
    }
}
""")

write("3747_count_distinct_integers_after_removing_zeros", """// LeetCode 3747 - Count Distinct Integers After Removing Zeros
// https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/

class Solution {
    private var s = [Character]()
    private var m = 0
    private var f = [[[[Int]]]]()

    func countDistinct(_ n: Int) -> Int {
        s = Array(String(n))
        m = s.count
        f = Array(repeating: Array(repeating: Array(repeating: [Int](repeating: -1, count: 2), count: 2), count: 2), count: 20)
        return dfs(0, 0, 1, 1)
    }

    private func dfs(_ i: Int, _ zero: Int, _ lead: Int, _ limit: Int) -> Int {
        if i == m { return (zero == 0 && lead == 0) ? 1 : 0 }
        if limit == 0 && f[i][zero][lead][limit] != -1 { return f[i][zero][lead][limit] }
        let up = limit == 1 ? Int(s[i].asciiValue! - 48) : 9
        var ans = 0
        for d in 0...up {
            var nxtZero = zero
            if d == 0 && lead == 0 { nxtZero = 1 }
            let nxtLead = (lead == 1 && d == 0) ? 1 : 0
            let nxtLimit = (limit == 1 && d == up) ? 1 : 0
            ans += dfs(i + 1, nxtZero, nxtLead, nxtLimit)
        }
        if limit == 0 { f[i][zero][lead][limit] = ans }
        return ans
    }
}
""")

write("3748_count_stable_subarrays", """// LeetCode 3748 - Count Stable Subarrays
// https://leetcode.com/problems/count-stable-subarrays/

class Solution {
    func countStableSubarrays(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        var seg = [Int]()
        var s = [0]
        var l = 0
        for r in 0..<n {
            if r == n - 1 || nums[r] > nums[r + 1] {
                seg.append(l)
                let k = r - l + 1
                s.append(s[s.count - 1] + k * (k + 1) / 2)
                l = r + 1
            }
        }
        var ans = [Int](repeating: 0, count: queries.count)
        for idx in 0..<queries.count {
            let left = queries[idx][0], right = queries[idx][1]
            let i = lowerBound(seg, left + 1)
            let j = lowerBound(seg, right + 1) - 1
            if i > j {
                let k = right - left + 1
                ans[idx] = k * (k + 1) / 2
            } else {
                let a = seg[i] - left
                let b = right - seg[j] + 1
                ans[idx] = a * (a + 1) / 2 + s[j] - s[i] + b * (b + 1) / 2
            }
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
}
""")

write("3749_evaluate_valid_expressions", """// LeetCode 3749 - Evaluate Valid Expressions
// https://leetcode.com/problems/evaluate-valid-expressions/

class Solution {
    private var expression = [Character]()

    func evaluateExpression(_ expression: String) -> Int {
        self.expression = Array(expression)
        return parse(0).0
    }

    private func parse(_ i: Int) -> (Int, Int) {
        let ch = expression[i]
        if ch.isNumber || ch == "-" {
            var j = i
            if expression[j] == "-" { j += 1 }
            while j < expression.count && expression[j].isNumber { j += 1 }
            let val = Int(String(expression[i..<j]))!
            return (val, j)
        }
        var j = i
        while expression[j] != "(" { j += 1 }
        let op = String(expression[i..<j])
        j += 1
        let p1 = parse(j)
        j = p1.1 + 1
        let p2 = parse(j)
        j = p2.1 + 1
        var res = 0
        if op == "add" { res = p1.0 + p2.0 }
        else if op == "sub" { res = p1.0 - p2.0 }
        else if op == "mul" { res = p1.0 * p2.0 }
        else if op == "div" { res = p1.0 / p2.0 }
        return (res, j)
    }
}
""")

write("3750_minimum_number_of_flips_to_reverse_binary_string", """// LeetCode 3750 - Minimum Number Of Flips To Reverse Binary String
// https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

class Solution {
    func minimumFlips(_ n: Int) -> Int {
        var x = n
        var s: [Character]
        if x == 0 {
            s = ["0"]
        } else {
            var arr = [Character]()
            while x > 0 {
                arr.append(Character(UnicodeScalar(48 + (x & 1))!))
                x >>= 1
            }
            arr.reverse()
            s = arr
        }
        let m = s.count
        var cnt = 0
        for i in 0..<(m / 2) {
            if s[i] != s[m - i - 1] { cnt += 1 }
        }
        return cnt * 2
    }
}
""")

write("3751_total_waviness_of_numbers_in_range_i", """// LeetCode 3751 - Total Waviness Of Numbers In Range I
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

class Solution {
    private func F(_ x: Int) -> Int {
        var x = x
        var nums = [Int]()
        while x > 0 {
            nums.append(x % 10)
            x /= 10
        }
        let m = nums.count
        if m < 3 { return 0 }
        var s = 0
        for i in 1..<(m - 1) {
            if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) ||
               (nums[i] < nums[i - 1] && nums[i] < nums[i + 1]) {
                s += 1
            }
        }
        return s
    }

    func totalWaviness(_ num1: Int, _ num2: Int) -> Int {
        var ans = 0
        for x in num1...num2 { ans += F(x) }
        return ans
    }
}
""")

write("3752_lexicographically_smallest_negated_permutation_that_sums_to_target", """// LeetCode 3752 - Lexicographically Smallest Negated Permutation that Sums to Target
// https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

class Solution {
    func lexicographicallySmallest(_ n: Int, _ target: Int) -> [Int] {
        let total = n * (n + 1) / 2
        if target < -total || target > total || (total - target) % 2 != 0 { return [] }
        var remaining = (total - target) / 2
        var negative = [Bool](repeating: false, count: n + 1)
        for value in stride(from: n, through: 1, by: -1) {
            if value <= remaining {
                negative[value] = true
                remaining -= value
            }
        }
        var answer = [Int]()
        for value in stride(from: n, through: 1, by: -1) {
            if negative[value] { answer.append(-value) }
        }
        for value in 1...n {
            if !negative[value] { answer.append(value) }
        }
        return answer
    }
}
""")

write("3753_total_waviness_of_numbers_in_range_ii", """// LeetCode 3753 - Total Waviness Of Numbers In Range II
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

class Solution {
    private class Result {
        var count = 0
        var sum = 0
        init() {}
        init(_ c: Int, _ s: Int) { count = c; sum = s }
    }

    private func wavinessUpTo(_ limit: Int) -> Int {
        if limit < 0 { return 0 }
        var digits = [Int]()
        if limit == 0 {
            digits.append(0)
        } else {
            var value = limit
            while value > 0 {
                digits.append(value % 10)
                value /= 10
            }
            digits.reverse()
        }
        var memo = [String: Result]()
        return dfs(0, 10, 10, false, true, digits, &memo).sum
    }

    private func dfs(_ position: Int, _ secondLast: Int, _ last: Int, _ started: Bool, _ tight: Bool,
                     _ digits: [Int], _ memo: inout [String: Result]) -> Result {
        if position == digits.count { return Result(1, 0) }
        let key = "\\(position),\\(secondLast),\\(last),\\(started)"
        if !tight, let cached = memo[key] { return cached }
        let upper = tight ? digits[position] : 9
        let result = Result()
        for digit in 0...upper {
            let nextTight = tight && digit == upper
            var nextSecondLast = secondLast, nextLast = last
            let nextStarted = started || digit != 0
            var add = 0
            if !nextStarted {
                nextSecondLast = 10
                nextLast = 10
            } else if !started {
                nextSecondLast = 10
                nextLast = digit
            } else {
                if secondLast != 10 &&
                    ((last > secondLast && last > digit) || (last < secondLast && last < digit)) {
                    add = 1
                }
                nextSecondLast = last
                nextLast = digit
            }
            let child = dfs(position + 1, nextSecondLast, nextLast, nextStarted, nextTight, digits, &memo)
            result.count += child.count
            result.sum += child.sum + add * child.count
        }
        if !tight { memo[key] = result }
        return result
    }

    func totalWaviness(_ a: Int, _ b: Int) -> Int {
        return wavinessUpTo(b) - wavinessUpTo(a - 1)
    }
}
""")

write("3754_concatenate_non_zero_digits_and_multiply_by_sum_i", """// LeetCode 3754 - Concatenate Non Zero Digits And Multiply By Sum I
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

class Solution {
    func sumAndMultiply(_ n: Int) -> Int {
        var n = n
        var p = 1, x = 0, s = 0
        while n > 0 {
            let v = n % 10
            if v != 0 {
                s += v
                x += p * v
                p *= 10
            }
            n /= 10
        }
        return x * s
    }
}
""")

write("3755_find_maximum_balanced_xor_subarray_length", """// LeetCode 3755 - Find Maximum Balanced Xor Subarray Length
// https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/

class Solution {
    func maxBalancedSubarray(_ nums: [Int]) -> Int {
        var d = [Int: Int]()
        var a = 0, b = nums.count, ans = 0
        d[b] = -1
        for i in 0..<nums.count {
            a ^= nums[i]
            if nums[i] % 2 == 0 { b += 1 } else { b -= 1 }
            let key = (a << 32) | (b & 0xffffffff)
            if let prev = d[key] { ans = max(ans, i - prev) }
            else { d[key] = i }
        }
        return ans
    }
}
""")

write("3756_concatenate_non_zero_digits_and_multiply_by_sum_ii", """// LeetCode 3756 - Concatenate Non Zero Digits And Multiply By Sum II
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

class Solution {
    private static let MX = 100001
    private static let MOD = 1_000_000_007
    private static let PW: [Int] = {
        var pw = [Int](repeating: 0, count: 100001)
        pw[0] = 1
        for i in 1..<100001 { pw[i] = pw[i - 1] * 10 % 1_000_000_007 }
        return pw
    }()

    func sumAndMultiply(_ s: String, _ queries: [[Int]]) -> [Int] {
        let chars = Array(s)
        let n = chars.count
        var sumD = [Int](repeating: 0, count: n + 1)
        var cntN0 = [Int](repeating: 0, count: n + 1)
        var p = [Int](repeating: 0, count: n + 1)
        let MOD = 1_000_000_007
        for i in 1...n {
            let d = Int(chars[i - 1].asciiValue! - 48)
            sumD[i] = sumD[i - 1] + d
            cntN0[i] = cntN0[i - 1]
            if d > 0 {
                cntN0[i] += 1
                p[i] = (p[i - 1] * 10 + d) % MOD
            } else {
                p[i] = p[i - 1]
            }
        }
        var ans = [Int](repeating: 0, count: queries.count)
        for i in 0..<queries.count {
            let l = queries[i][0], r = queries[i][1]
            let n0 = cntN0[r + 1] - cntN0[l]
            let sd = sumD[r + 1] - sumD[l]
            let x = (p[r + 1] - p[l] * Solution.PW[n0] % MOD + MOD) % MOD
            ans[i] = x * sd % MOD
        }
        return ans
    }
}
""")

write("3757_number_of_effective_subsequences", """// LeetCode 3757 - Number of Effective Subsequences
// https://leetcode.com/problems/number-of-effective-subsequences/

class Solution {
    private func popCount(_ x: Int) -> Int {
        var x = x, c = 0
        while x != 0 { c += x & 1; x >>= 1 }
        return c
    }

    func countEffectiveSubsequences(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        var all = 0
        for x in nums { all |= x }
        var bits = [Int]()
        for b in 0..<20 where ((all >> b) & 1) != 0 { bits.append(b) }
        let m = bits.count
        var freq = [Int](repeating: 0, count: 1 << m)
        for x in nums {
            var mask = 0
            for i in 0..<m where ((x >> bits[i]) & 1) != 0 { mask |= 1 << i }
            freq[mask] += 1
        }
        var disjoint = freq
        for b in 0..<m {
            for mask in 0..<(1 << m) {
                if ((mask >> b) & 1) != 0 { disjoint[mask] += disjoint[mask ^ (1 << b)] }
            }
        }
        var pow2 = [Int](repeating: 0, count: nums.count + 1)
        pow2[0] = 1
        if nums.count >= 1 {
            for i in 1...nums.count { pow2[i] = pow2[i - 1] * 2 % mod }
        }
        var ans = 0
        let full = (1 << m) - 1
        if full >= 1 {
            for s in 1...full {
                let ways = pow2[disjoint[full ^ s]]
                let bc = popCount(s)
                if (bc & 1) != 0 {
                    ans += ways
                    if ans >= mod { ans -= mod }
                } else {
                    ans -= ways
                    if ans < 0 { ans += mod }
                }
            }
        }
        return ans
    }
}
""")

write("3758_convert_number_words_to_digits", """// LeetCode 3758 - Convert Number Words To Digits
// https://leetcode.com/problems/convert-number-words-to-digits/

class Solution {
    func convertNumber(_ s: String) -> String {
        let d = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        let chars = Array(s)
        let n = chars.count
        var ans = ""
        var i = 0
        while i < n {
            var matched = false
            for j in 0..<10 {
                let m = d[j].count
                if i + m <= n && String(chars[i..<(i + m)]) == d[j] {
                    ans.append(Character(UnicodeScalar(48 + j)!))
                    i += m - 1
                    matched = true
                    break
                }
            }
            i += 1
        }
        return ans
    }
}
""")
