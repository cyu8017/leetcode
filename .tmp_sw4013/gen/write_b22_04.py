#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")


def write(folder, content):
    p = ROOT / folder / "Solution.swift"
    if "func solve()" not in p.read_text():
        print("SKIP", folder)
        return
    p.write_text(content)
    print("WROTE", folder)


write("3903_smallest_stable_index_i", """// LeetCode 3903 - Smallest Stable Index I
// https://leetcode.com/problems/smallest-stable-index-i/

class Solution {
    func firstStableIndex(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var right = [Int](repeating: 0, count: n)
        right[n - 1] = nums[n - 1]
        if n >= 2 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                right[i] = min(right[i + 1], nums[i])
            }
        }
        var left = 0
        for i in 0..<n {
            left = max(left, nums[i])
            if left - right[i] <= k { return i }
        }
        return -1
    }
}
""")

write("3904_smallest_stable_index_ii", """// LeetCode 3904 - Smallest Stable Index II
// https://leetcode.com/problems/smallest-stable-index-ii/

class Solution {
    func firstStableIndex(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var right = [Int](repeating: 0, count: n)
        right[n - 1] = nums[n - 1]
        if n >= 2 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                right[i] = min(right[i + 1], nums[i])
            }
        }
        var left = 0
        for i in 0..<n {
            left = max(left, nums[i])
            if left - right[i] <= k { return i }
        }
        return -1
    }
}
""")

write("3905_multi_source_flood_fill", """// LeetCode 3905 - Multi Source Flood Fill
// https://leetcode.com/problems/multi-source-flood-fill/

class Solution {
    func colorGrid(_ n: Int, _ m: Int, _ sources: [[Int]]) -> [[Int]] {
        var ans = Array(repeating: [Int](repeating: 0, count: m), count: n)
        var q = sources
        let dirs = [-1, 0, 1, 0, -1]
        for s in q { ans[s[0]][s[1]] = s[2] }
        while !q.isEmpty {
            var vis = [Int: Int]()
            for curr in q {
                let r = curr[0], c = curr[1], color = curr[2]
                for i in 0..<4 {
                    let x = r + dirs[i], y = c + dirs[i + 1]
                    if x >= 0 && x < n && y >= 0 && y < m && ans[x][y] == 0 {
                        let key = (x << 32) | (y & 0xffffffff)
                        if vis[key] == nil || color > vis[key]! { vis[key] = color }
                    }
                }
            }
            q = []
            for (key, color) in vis {
                let x = key >> 32
                let y = key & 0xffffffff
                ans[x][y] = color
                q.append([x, y, color])
            }
        }
        return ans
    }
}
""")

write("3906_count_good_integers_on_a_grid_path", """// LeetCode 3906 - Count Good Integers On A Grid Path
// https://leetcode.com/problems/count-good-integers-on-a-grid-path/

class Solution {
    private var key = [Bool](repeating: false, count: 16)
    private var s = [Character]()
    private var f = Array(repeating: [Int](repeating: -1, count: 10), count: 16)

    func countGoodIntegersOnPath(_ l: Int, _ r: Int, _ directions: String) -> Int {
        key = [Bool](repeating: false, count: 16)
        var row = 0, col = 0
        key[0] = true
        for c in directions {
            if c == "D" { row += 1 } else { col += 1 }
            key[row * 4 + col] = true
        }
        return calc(r) - calc(l - 1)
    }

    private func dfs(_ pos: Int, _ last: Int, _ lim: Bool) -> Int {
        if pos == 16 { return 1 }
        if !lim && f[pos][last] != -1 { return f[pos][last] }
        var res = 0
        let start = key[pos] ? last : 0
        let end = lim ? Int(s[pos].asciiValue! - 48) : 9
        if start <= end {
            for i in start...end {
                let nextLast = key[pos] ? i : last
                res += dfs(pos + 1, nextLast, lim && (i == end))
            }
        }
        if !lim { f[pos][last] = res }
        return res
    }

    private func calc(_ x: Int) -> Int {
        if x < 0 { return 0 }
        let t = String(x)
        s = Array(String(repeating: "0", count: 16 - t.count) + t)
        f = Array(repeating: [Int](repeating: -1, count: 10), count: 16)
        return dfs(0, 0, true)
    }
}
""")

write("3907_count_smaller_elements_with_opposite_parity", """// LeetCode 3907 - Count Smaller Elements With Opposite Parity
// https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

class Solution {
    private class BIT {
        var n: Int
        var c: [Int]
        init(_ n_: Int) { n = n_; c = [Int](repeating: 0, count: n_ + 1) }
        func update(_ x: Int, _ delta: Int) {
            var x = x
            while x <= n { c[x] += delta; x += x & -x }
        }
        func query(_ x: Int) -> Int {
            var x = x, s = 0
            while x > 0 { s += c[x]; x -= x & -x }
            return s
        }
    }

    func countSmallerOppositeParity(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var sorted = nums.sorted()
        var m = 0
        for i in 0..<sorted.count {
            if i == 0 || sorted[i] != sorted[i - 1] {
                sorted[m] = sorted[i]
                m += 1
            }
        }
        sorted = Array(sorted.prefix(m))
        let bits = [BIT(m), BIT(m)]
        var ans = [Int](repeating: 0, count: n)
        for i in stride(from: n - 1, through: 0, by: -1) {
            var lo = 0, hi = sorted.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if sorted[mid] < nums[i] { lo = mid + 1 }
                else { hi = mid }
            }
            var x = lo + 1
            ans[i] = bits[(nums[i] & 1) ^ 1].query(x - 1)
            bits[nums[i] & 1].update(x, 1)
        }
        return ans
    }
}
""")

write("3908_valid_digit_number", """// LeetCode 3908 - Valid Digit Number
// https://leetcode.com/problems/valid-digit-number/

class Solution {
    func validDigit(_ n: Int, _ x: Int) -> Bool {
        var n = n
        var hasX = false
        while n > 9 {
            hasX = hasX || (n % 10 == x)
            n /= 10
        }
        return hasX && (n != x)
    }
}
""")

write("3909_compare_sums_of_bitonic_parts", """// LeetCode 3909 - Compare Sums Of Bitonic Parts
// https://leetcode.com/problems/compare-sums-of-bitonic-parts/

class Solution {
    func compareBitonicSums(_ nums: [Int]) -> Int {
        var l = nums[0], r = 0
        for x in nums { r += x }
        if nums.count > 1 {
            for i in 1..<nums.count {
                if nums[i - 1] > nums[i] { break }
                l += nums[i]
                r -= nums[i - 1]
            }
        }
        if l == r { return -1 }
        if l > r { return 0 }
        return 1
    }
}
""")

write("3910_count_connected_subgraphs_with_even_node_sum", """// LeetCode 3910 - Count Connected Subgraphs With Even Node Sum
// https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

class Solution {
    private var g = [[Int]]()
    private var vis = 0, m = 0

    func evenSumSubgraphs(_ nums: [Int], _ edges: [[Int]]) -> Int {
        let n = nums.count
        g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        m = (1 << n) - 1
        var ans = 0
        if m >= 1 {
            for sub in 1...m {
                var s = 0
                for i in 0..<n {
                    if ((sub >> i) & 1) != 0 { s += nums[i] }
                }
                if s % 2 != 0 { continue }
                vis = m ^ sub
                var start = 0, tmp = sub
                while tmp > 1 { tmp >>= 1; start += 1 }
                dfs(start)
                if vis == m { ans += 1 }
            }
        }
        return ans
    }

    private func dfs(_ u: Int) {
        vis |= 1 << u
        for v in g[u] {
            if ((vis >> v) & 1) == 0 { dfs(v) }
        }
    }
}
""")

write("3911_k_th_smallest_remaining_even_integer_in_subarray_queries", """// LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
// https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

class Solution {
    func kthSmallestEven(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        var evenPrefix = [Int](repeating: 0, count: n + 1)
        for i in 0..<n {
            evenPrefix[i + 1] = evenPrefix[i] + (nums[i] % 2 == 0 ? 1 : 0)
        }
        var ans = [Int](repeating: 0, count: queries.count)
        for qi in 0..<queries.count {
            let l = queries[qi][0], r = queries[qi][1]
            let k = queries[qi][2]
            var lo = 1, hi = k + (r - l + 1)
            while lo < hi {
                let mid = (lo + hi) / 2
                var pos = upperBound(nums, 2 * mid)
                if pos > r + 1 { pos = r + 1 }
                var removed = 0
                if pos > l { removed = evenPrefix[pos] - evenPrefix[l] }
                if mid - removed >= k { hi = mid }
                else { lo = mid + 1 }
            }
            ans[qi] = 2 * lo
        }
        return ans
    }

    private func upperBound(_ a: [Int], _ x: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] <= x { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }
}
""")

write("3912_valid_elements_in_an_array", """// LeetCode 3912 - Valid Elements In An Array
// https://leetcode.com/problems/valid-elements-in-an-array/

class Solution {
    func findValidElements(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var right = [Int](repeating: 0, count: n)
        right[n - 1] = nums[n - 1]
        if n >= 2 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                right[i] = max(right[i + 1], nums[i])
            }
        }
        var left = 0
        var ans = [Int]()
        for i in 0..<n {
            let x = nums[i]
            if x > left || i == n - 1 || x > right[i + 1] { ans.append(x) }
            left = max(left, x)
        }
        return ans
    }
}
""")

write("3913_sort_vowels_by_frequency", """// LeetCode 3913 - Sort Vowels By Frequency
// https://leetcode.com/problems/sort-vowels-by-frequency/

class Solution {
    func sortVowels(_ s: String) -> String {
        let vowelsSet: Set<Character> = ["a", "e", "i", "o", "u"]
        var vowels = [Character]()
        var cnt = [Character: Int]()
        for c in s {
            if !vowelsSet.contains(c) { continue }
            if cnt[c] == nil { vowels.append(c) }
            cnt[c, default: 0] += 1
        }
        vowels.sort { cnt[$0]! > cnt[$1]! }
        var ans = Array(s)
        var i = 0
        for k in 0..<ans.count {
            if !vowelsSet.contains(ans[k]) { continue }
            let ch = vowels[i]
            ans[k] = ch
            cnt[ch]! -= 1
            if cnt[ch] == 0 { i += 1 }
        }
        return String(ans)
    }
}
""")

write("3914_minimum_operations_to_make_array_non_decreasing", """// LeetCode 3914 - Minimum Operations To Make Array Non Decreasing
// https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var ans = 0
        if nums.count > 1 {
            for i in 1..<nums.count {
                ans += max(0, nums[i - 1] - nums[i])
            }
        }
        return ans
    }
}
""")

write("3915_maximum_sum_of_alternating_subsequence_with_distance_at_least_k", """// LeetCode 3915 - Maximum Sum Of Alternating Subsequence With Distance At Least K
// https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

class Solution {
    private class Fenwick {
        var f: [Int]
        init(_ n: Int) { f = [Int](repeating: 0, count: n) }
        func update(_ i: Int, _ val: Int) {
            var i = i
            while i < f.count {
                f[i] = max(f[i], val)
                i += i & -i
            }
        }
        func preMax(_ i: Int) -> Int {
            var i = i, res = 0
            while i > 0 {
                res = max(res, f[i])
                i &= i - 1
            }
            return res
        }
    }

    func maxAlternatingSum(_ nums: [Int], _ k: Int) -> Int {
        var sorted = nums.sorted()
        var m = 0
        for i in 0..<sorted.count {
            if i == 0 || sorted[i] != sorted[i - 1] {
                sorted[m] = sorted[i]
                m += 1
            }
        }
        sorted = Array(sorted.prefix(m))
        let n = nums.count
        var fInc = [Int](repeating: 0, count: n)
        var fDec = [Int](repeating: 0, count: n)
        let inc = Fenwick(m + 1)
        let dec = Fenwick(m + 1)
        var ans = 0
        var ranks = [Int](repeating: 0, count: n)
        for i in 0..<n {
            let x = nums[i]
            if i >= k {
                let j = ranks[i - k]
                inc.update(m - j, fInc[i - k])
                dec.update(j + 1, fDec[i - k])
            }
            var lo = 0, hi = sorted.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if sorted[mid] < x { lo = mid + 1 }
                else { hi = mid }
            }
            ranks[i] = lo
            fInc[i] = dec.preMax(lo) + x
            fDec[i] = inc.preMax(m - 1 - lo) + x
            ans = max(ans, max(fInc[i], fDec[i]))
        }
        return ans
    }
}
""")

write("3916_number_of_zigzag_arrays_iii", """// LeetCode 3916 - Number of ZigZag Arrays III
// https://leetcode.com/problems/number-of-zigzag-arrays-iii/

class Solution {
    func zigZagArrays(_ n: Int, _ l: Int, _ r: Int) -> Int {
        let mod = 1_000_000_007
        let points = n + 1
        var values = [Int](repeating: 0, count: points + 1)
        for m in 1...points {
            var up = [Int](repeating: 0, count: m)
            var down = [Int](repeating: 0, count: m)
            for value in 0..<m {
                up[value] = value
                down[value] = m - 1 - value
            }
            if n >= 3 {
                for _ in 3...n {
                    var nextUp = [Int](repeating: 0, count: m)
                    var nextDown = [Int](repeating: 0, count: m)
                    var prefix = 0
                    for value in 0..<m {
                        nextUp[value] = prefix
                        prefix = (prefix + down[value]) % mod
                    }
                    var suffix = 0
                    for value in stride(from: m - 1, through: 0, by: -1) {
                        nextDown[value] = suffix
                        suffix = (suffix + up[value]) % mod
                    }
                    up = nextUp
                    down = nextDown
                }
            }
            for value in 0..<m {
                values[m] = (values[m] + up[value] + down[value]) % mod
            }
        }
        let x = (r - l + 1) % mod
        if r - l + 1 <= points { return values[r - l + 1] }
        var prefixA = [Int](repeating: 0, count: points + 2)
        var suffixA = [Int](repeating: 0, count: points + 2)
        prefixA[0] = 1
        for i in 1...points {
            prefixA[i] = prefixA[i - 1] * ((x - i + mod) % mod) % mod
        }
        suffixA[points + 1] = 1
        for i in stride(from: points, through: 1, by: -1) {
            suffixA[i] = suffixA[i + 1] * ((x - i + mod) % mod) % mod
        }
        var factorial = [Int](repeating: 0, count: points + 1)
        factorial[0] = 1
        for i in 1...points { factorial[i] = factorial[i - 1] * i % mod }
        var answer = 0
        for i in 1...points {
            let numerator = prefixA[i - 1] * suffixA[i + 1] % mod
            let denominator = factorial[i - 1] * factorial[points - i] % mod
            let term = values[i] * numerator % mod * powm(denominator, mod - 2, mod) % mod
            if (points - i) % 2 == 1 { answer -= term }
            else { answer += term }
            answer %= mod
        }
        if answer < 0 { answer += mod }
        return answer
    }

    private func powm(_ a: Int, _ e: Int, _ mod: Int) -> Int {
        var a = a, e = e, res = 1
        while e > 0 {
            if (e & 1) != 0 { res = res * a % mod }
            a = a * a % mod
            e >>= 1
        }
        return res
    }
}
""")

write("3917_count_indices_with_opposite_parity", """// LeetCode 3917 - Count Indices With Opposite Parity
// https://leetcode.com/problems/count-indices-with-opposite-parity/

class Solution {
    func countOppositeParity(_ nums: [Int]) -> [Int] {
        var cnt = [0, 0]
        for x in nums { cnt[x & 1] += 1 }
        let n = nums.count
        var ans = [Int](repeating: 0, count: n)
        for i in 0..<n {
            let x = nums[i]
            cnt[x & 1] -= 1
            ans[i] = cnt[(x & 1) ^ 1]
        }
        return ans
    }
}
""")

write("3918_sum_of_primes_between_number_and_its_reverse", """// LeetCode 3918 - Sum Of Primes Between Number And Its Reverse
// https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

class Solution {
    private static let isPrime: [Bool] = {
        var ip = [Bool](repeating: true, count: 1001)
        ip[0] = false
        ip[1] = false
        var i = 2
        while i * i <= 1000 {
            if ip[i] {
                var j = i * i
                while j <= 1000 {
                    ip[j] = false
                    j += i
                }
            }
            i += 1
        }
        return ip
    }()

    func sumOfPrimesInRange(_ n: Int) -> Int {
        var r = 0, x = n
        while x > 0 {
            r = r * 10 + x % 10
            x /= 10
        }
        let low = min(n, r), high = max(n, r)
        var ans = 0
        for x in low...high {
            if Solution.isPrime[x] { ans += x }
        }
        return ans
    }
}
""")

write("3919_minimum_cost_to_move_between_indices", """// LeetCode 3919 - Minimum Cost To Move Between Indices
// https://leetcode.com/problems/minimum-cost-to-move-between-indices/

class Solution {
    func minCost(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        var s1 = [Int](repeating: 0, count: n)
        var s2 = [Int](repeating: 0, count: n)
        if n > 1 {
            for i in 1..<n {
                var c1 = 1
                if i > 1 && nums[i - 1] - nums[i - 2] <= nums[i] - nums[i - 1] { c1 = nums[i] - nums[i - 1] }
                var c2 = 1
                if i < n - 1 && nums[i] - nums[i - 1] > nums[i + 1] - nums[i] { c2 = nums[i] - nums[i - 1] }
                s1[i] = s1[i - 1] + c1
                s2[i] = s2[i - 1] + c2
            }
        }
        var ans = [Int](repeating: 0, count: queries.count)
        for i in 0..<queries.count {
            let l = queries[i][0], r = queries[i][1]
            ans[i] = (l < r) ? (s1[r] - s1[l]) : (s2[l] - s2[r])
        }
        return ans
    }
}
""")

write("3920_maximize_fixed_points_after_deletions", """// LeetCode 3920 - Maximize Fixed Points After Deletions
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/

class Solution {
    func maxFixedPoints(_ nums: [Int]) -> Int {
        var tails = [Int]()
        for i in 0..<nums.count {
            if i < nums[i] { continue }
            let d = i - nums[i]
            var lo = 0, hi = tails.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if tails[mid] < d { lo = mid + 1 }
                else { hi = mid }
            }
            if lo == tails.count { tails.append(d) }
            else { tails[lo] = d }
        }
        return tails.count
    }
}
""")

write("3921_score_validator", """// LeetCode 3921 - Score Validator
// https://leetcode.com/problems/score-validator/

class Solution {
    func scoreValidator(_ events: [String]) -> [Int] {
        var score = 0, counter = 0
        for eventStr in events {
            var isNum = !eventStr.isEmpty
            var num = 0
            var start = 0
            let chars = Array(eventStr)
            if isNum && chars[0] == "-" { start = 1 }
            if start < chars.count {
                for i in start..<chars.count {
                    if chars[i] < "0" || chars[i] > "9" {
                        isNum = false
                        break
                    }
                    num = num * 10 + Int(chars[i].asciiValue! - 48)
                }
            }
            if isNum && !(start == 1 && chars.count == 1) {
                if start == 1 { num = -num }
                score += num
            } else if eventStr == "W" {
                counter += 1
                if counter == 10 { break }
            } else {
                score += 1
            }
        }
        return [score, counter]
    }
}
""")

write("3922_minimum_flips_to_make_binary_string_coherent", """// LeetCode 3922 - Minimum Flips to Make Binary String Coherent
// https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

class Solution {
    func minFlips(_ s: String) -> Int {
        let chars = Array(s)
        var ones = 0
        for c in chars where c == "1" { ones += 1 }
        var answer = ones
        if ones > 0 { answer = ones - 1 }
        let zeros = chars.count - ones
        answer = min(answer, zeros)
        if chars.count >= 2 {
            var cost = 0
            for i in 0..<chars.count {
                let want: Character = (i == 0 || i == chars.count - 1) ? "1" : "0"
                if chars[i] != want { cost += 1 }
            }
            answer = min(answer, cost)
        }
        return answer
    }
}
""")
