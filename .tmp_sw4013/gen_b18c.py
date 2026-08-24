#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def hdr(num, title, slug):
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n"

MINHEAP = '''
private struct MinHeap {
    private var a: [Int] = []
    var isEmpty: Bool { a.isEmpty }
    var count: Int { a.count }
    mutating func push(_ x: Int) {
        a.append(x)
        var i = a.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if a[p] <= a[i] { break }
            a.swapAt(p, i)
            i = p
        }
    }
    mutating func pop() -> Int {
        let r = a[0]
        let last = a.removeLast()
        if !a.isEmpty {
            a[0] = last
            var i = 0
            while true {
                var s = i
                let l = 2 * i + 1, rg = 2 * i + 2
                if l < a.count && a[l] < a[s] { s = l }
                if rg < a.count && a[rg] < a[s] { s = rg }
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

FILES["3449_maximize_the_minimum_game_score"] = hdr("3449", "Maximize the Minimum Game Score", "maximize-the-minimum-game-score") + '''
class Solution {
    func maxScore(_ points: [Int], _ m: Int) -> Int {
        var lo = 0, hi = Int(1e18)
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if ok(points, m, mid) { lo = mid }
            else { hi = mid - 1 }
        }
        return lo
    }

    private func ok(_ points: [Int], _ m: Int, _ mid: Int) -> Bool {
        var need = 0
        var extra = 0
        for p in points {
            let req = (mid + p - 1) / p
            if req > extra {
                let visits = req - extra
                need += 2 * visits - 1
                extra = visits - 1
            } else {
                need += 1
                extra = 0
            }
            if need > m { return false }
        }
        return need <= m
    }
}
'''

FILES["3450_maximum_students_on_a_single_bench"] = hdr("3450", "Maximum Students on a Single Bench", "maximum-students-on-a-single-bench") + '''
class Solution {
    func maxStudentsOnBench(_ students: [[Int]]) -> Int {
        var bench = [Int: Set<Int>]()
        for s in students { bench[s[1], default: []].insert(s[0]) }
        return bench.values.map { $0.count }.max() ?? 0
    }
}
'''

FILES["3452_sum_of_good_numbers"] = hdr("3452", "Sum of Good Numbers", "sum-of-good-numbers") + '''
class Solution {
    func sumOfGoodNumbers(_ nums: [Int], _ k: Int) -> Int {
        var ans = 0
        let n = nums.count
        for i in 0..<n {
            var good = true
            if i - k >= 0 && nums[i] <= nums[i - k] { good = false }
            if i + k < n && nums[i] <= nums[i + k] { good = false }
            if good { ans += nums[i] }
        }
        return ans
    }
}
'''

SEP = '''
class Solution {
    func separateSquares(_ squares: [[Int]]) -> Double {
        var total = 0.0
        for sq in squares {
            let l = Double(sq[2])
            total += l * l
        }
        var lo = 0.0, hi = 2e9
        for _ in 0..<60 {
            let mid = (lo + hi) / 2
            if areaBelow(squares, mid) * 2 < total { lo = mid }
            else { hi = mid }
        }
        return hi
    }

    private func areaBelow(_ squares: [[Int]], _ y: Double) -> Double {
        var below = 0.0
        for sq in squares {
            let yi = Double(sq[1]), l = Double(sq[2])
            let top = yi + l
            if y <= yi { continue }
            else if y >= top { below += l * l }
            else { below += l * (y - yi) }
        }
        return below
    }
}
'''
FILES["3453_separate_squares_i"] = hdr("3453", "Separate Squares I", "separate-squares-i") + SEP
FILES["3454_separate_squares_ii"] = hdr("3454", "Separate Squares II", "separate-squares-ii") + SEP

FILES["3455_shortest_matching_substring"] = hdr("3455", "Shortest Matching Substring", "shortest-matching-substring") + '''
class Solution {
    func shortestMatchingSubstring(_ s: String, _ p: String) -> Int {
        var parts = [String]()
        var cur = ""
        for c in p {
            if c == "*" {
                parts.append(cur)
                cur = ""
            } else { cur.append(c) }
        }
        parts.append(cur)
        while parts.count < 3 { parts.append("") }
        let a = parts[0], b = parts[1], c = parts[2]
        let n = s.count
        let posA = findAll(s, a), posB = findAll(s, b), posC = findAll(s, c)
        var ans = n + 1
        for ia in posA {
            let endA = ia + a.count
            var bi = lowerBound(posB, endA)
            if bi < posB.count {
                let endB = posB[bi] + b.count
                let ci = lowerBound(posC, endB)
                if ci < posC.count {
                    let length = posC[ci] + c.count - ia
                    if length < ans { ans = length }
                }
            }
        }
        return ans == n + 1 ? -1 : ans
    }

    private func findAll(_ s: String, _ sub: String) -> [Int] {
        let sa = Array(s), suba = Array(sub)
        var res = [Int]()
        if suba.isEmpty {
            for i in 0...sa.count { res.append(i) }
            return res
        }
        if sa.count >= suba.count {
            for i in 0...(sa.count - suba.count) {
                if Array(sa[i..<(i + suba.count)]) == suba { res.append(i) }
            }
        }
        return res
    }

    private func lowerBound(_ arr: [Int], _ x: Int) -> Int {
        var lo = 0, hi = arr.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if arr[mid] < x { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }
}
'''

FILES["3456_find_special_substring_of_length_k"] = hdr("3456", "Find Special Substring of Length K", "find-special-substring-of-length-k") + '''
class Solution {
    func hasSpecialSubstring(_ s: String, _ k: Int) -> Bool {
        let chars = Array(s)
        let n = chars.count
        if n < k { return false }
        for i in 0...(n - k) {
            var ok = true
            for j in (i + 1)..<(i + k) where chars[j] != chars[i] { ok = false; break }
            if !ok { continue }
            if i > 0 && chars[i - 1] == chars[i] { continue }
            if i + k < n && chars[i + k] == chars[i] { continue }
            return true
        }
        return false
    }
}
'''

FILES["3457_eat_pizzas"] = hdr("3457", "Eat Pizzas!", "eat-pizzas") + '''
class Solution {
    func maxWeight(_ pizzas: [Int]) -> Int {
        let pizzas = pizzas.sorted()
        let n = pizzas.count
        let days = n / 4
        var ans = 0
        let oddDays = (days + 1) / 2
        let evenDays = days / 2
        var idx = n - 1
        for _ in 0..<oddDays {
            ans += pizzas[idx]
            idx -= 1
        }
        for _ in 0..<evenDays {
            idx -= 1
            ans += pizzas[idx]
            idx -= 1
        }
        return ans
    }
}
'''

FILES["3458_select_k_disjoint_special_substrings"] = hdr("3458", "Select K Disjoint Special Substrings", "select-k-disjoint-special-substrings") + '''
class Solution {
    func maxSubstringLength(_ s: String, _ k: Int) -> Bool {
        let chars = Array(s)
        let n = chars.count
        var first = Array(repeating: n, count: 26)
        var last = Array(repeating: -1, count: 26)
        for i in 0..<n {
            let ci = Int(chars[i].asciiValue! - 97)
            if first[ci] == n { first[ci] = i }
            last[ci] = i
        }
        var segs = [[Int]]()
        for c in 0..<26 {
            if last[c] == -1 { continue }
            var l = first[c], r = last[c]
            var i = l
            while i <= r {
                let ci = Int(chars[i].asciiValue! - 97)
                if first[ci] < l {
                    l = first[ci]
                    i = l
                    continue
                }
                if last[ci] > r { r = last[ci] }
                i += 1
            }
            if !(l == 0 && r == n - 1) { segs.append([l, r]) }
        }
        var uniq = Set<Int>()
        var arr = [[Int]]()
        for sg in segs {
            let key = (sg[0] << 32) | (sg[1] & ((1 << 32) - 1))
            if uniq.insert(key).inserted { arr.append(sg) }
        }
        arr.sort { $0[1] < $1[1] }
        var cnt = 0, end = -1
        for sg in arr where sg[0] > end {
            cnt += 1
            end = sg[1]
        }
        return cnt >= k
    }
}
'''

FILES["3459_length_of_longest_v_shaped_diagonal_segment"] = hdr("3459", "Length of Longest V-Shaped Diagonal Segment", "length-of-longest-v-shaped-diagonal-segment") + '''
class Solution {
    func lenOfVDiagonal(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        let dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        let nextDir = [1, 2, 3, 0]
        var memo = [Int: Int]()
        func key(_ i: Int, _ j: Int, _ d: Int, _ turned: Int, _ expect: Int) -> Int {
            return ((((i * 101 + j) * 5 + d) * 3 + turned) * 5 + expect)
        }
        func dfs(_ i: Int, _ j: Int, _ d: Int, _ turned: Int, _ expect: Int) -> Int {
            if i < 0 || j < 0 || i >= m || j >= n || grid[i][j] != expect { return 0 }
            let k = key(i, j, d, turned, expect)
            if let c = memo[k] { return c }
            let ni = i + dirs[d].0, nj = j + dirs[d].1
            let nx = expect == 2 ? 0 : 2
            var best = 1 + dfs(ni, nj, d, turned, nx)
            if turned == 0 {
                let nd = nextDir[d]
                let ti = i + dirs[nd].0, tj = j + dirs[nd].1
                best = max(best, 1 + dfs(ti, tj, nd, 1, nx))
            }
            memo[k] = best
            return best
        }
        var ans = 0
        for i in 0..<m {
            for j in 0..<n where grid[i][j] == 1 {
                for d in 0..<4 {
                    let ni = i + dirs[d].0, nj = j + dirs[d].1
                    ans = max(ans, 1 + dfs(ni, nj, d, 0, 2))
                }
                if ans < 1 { ans = 1 }
            }
        }
        return ans
    }
}
'''

FILES["3460_longest_common_prefix_after_at_most_one_removal"] = hdr("3460", "Longest Common Prefix After at Most One Removal", "longest-common-prefix-after-at-most-one-removal") + '''
class Solution {
    func longestCommonPrefix(_ s: String, _ t: String) -> Int {
        let sa = Array(s), ta = Array(t)
        var i = 0, j = 0
        var removed = false
        while i < sa.count && j < ta.count {
            if sa[i] == ta[j] {
                i += 1; j += 1
                continue
            }
            if removed { break }
            removed = true
            i += 1
        }
        return j
    }
}
'''

FILES["3461_check_if_digits_are_equal_in_string_after_operations_i"] = hdr("3461", "Check If Digits Are Equal in String After Operations I", "check-if-digits-are-equal-in-string-after-operations-i") + '''
class Solution {
    func hasSameDigits(_ s: String) -> Bool {
        var b = Array(s).map { Int($0.asciiValue! - 48) }
        while b.count > 2 {
            var nb = [Int]()
            for i in 0..<(b.count - 1) { nb.append((b[i] + b[i + 1]) % 10) }
            b = nb
        }
        return b[0] == b[1]
    }
}
'''

FILES["3462_maximum_sum_with_at_most_k_elements"] = hdr("3462", "Maximum Sum With at Most K Elements", "maximum-sum-with-at-most-k-elements") + MINHEAP + '''
class Solution {
    func maxSum(_ grid: [[Int]], _ limits: [Int], _ k: Int) -> Int {
        var h = MinHeap()
        var sum = 0
        for i in 0..<grid.count {
            var r = grid[i].sorted()
            var lim = limits[i]
            if lim > r.count { lim = r.count }
            for j in 0..<lim {
                let val = r[r.count - 1 - j]
                h.push(val)
                sum += val
                if h.count > k { sum -= h.pop() }
            }
        }
        return sum
    }
}
'''

FILES["3463_check_if_digits_are_equal_in_string_after_operations_ii"] = hdr("3463", "Check If Digits Are Equal in String After Operations II", "check-if-digits-are-equal-in-string-after-operations-ii") + '''
class Solution {
    func hasSameDigits(_ s: String) -> Bool {
        let n = s.count
        return combineDigit(s, n, 0) == combineDigit(s, n, 1)
    }

    private func modPowP(_ a: Int, _ e: Int, _ p: Int) -> Int {
        var r = 1, a = a, e = e
        while e > 0 {
            if e & 1 != 0 { r = r * a % p }
            a = a * a % p
            e >>= 1
        }
        return r
    }

    private func binomMod(_ n: Int, _ k: Int, _ p: Int) -> Int {
        if k < 0 || k > n { return 0 }
        var num = 1, den = 1
        if k > 0 {
            for i in 0..<k {
                num = num * (n - i) % p
                den = den * (i + 1) % p
            }
        }
        return num * modPowP(den, p - 2, p) % p
    }

    private func crt(_ a1: Int, _ m1: Int, _ a2: Int, _ m2: Int) -> Int {
        for x in 0..<(m1 * m2) {
            if x % m1 == a1 && x % m2 == a2 { return x }
        }
        return 0
    }

    private func binomMod10(_ n: Int, _ k: Int) -> Int {
        return crt(binomMod(n, k, 2), 2, binomMod(n, k, 5), 5)
    }

    private func combineDigit(_ s: String, _ n: Int, _ offset: Int) -> Int {
        let chars = Array(s)
        var sum = 0
        if n >= 2 {
            for i in 0...(n - 2) {
                sum = (sum + binomMod10(n - 2, i) * Int(chars[i + offset].asciiValue! - 48)) % 10
            }
        }
        return sum
    }
}
'''

FILES["3464_maximize_the_distance_between_points_on_a_square"] = hdr("3464", "Maximize the Distance Between Points on a Square", "maximize-the-distance-between-points-on-a-square") + '''
class Solution {
    func maxDistance(_ side: Int, _ points: [[Int]], _ k: Int) -> Int {
        var arr = [Int]()
        for p in points {
            let x = p[0], y = p[1]
            var d = 0
            if y == 0 { d = x }
            else if x == side { d = side + y }
            else if y == side { d = 2 * side + (side - x) }
            else { d = 3 * side + (side - y) }
            arr.append(d)
        }
        arr.sort()
        let perim = 4 * side
        var lo = 0, hi = 2 * side
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if canPlace(arr, perim, k, mid) { lo = mid }
            else { hi = mid - 1 }
        }
        return lo
    }

    private func canPlace(_ arr: [Int], _ perim: Int, _ k: Int, _ mid: Int) -> Bool {
        let n = arr.count
        for s in 0..<n {
            var cnt = 1
            var last = arr[s]
            var idx = s
            while cnt < k {
                let target = last + mid
                var found = false
                for step in 1..<n {
                    let ni = (idx + step) % n
                    let val = arr[ni]
                    let add = ni <= idx ? perim : 0
                    if val + add >= target {
                        last = val + add
                        idx = ni
                        cnt += 1
                        found = true
                        break
                    }
                }
                if !found { break }
            }
            if cnt == k && last - arr[s] <= perim - mid { return true }
        }
        return false
    }
}
'''

FILES["3466_maximum_coin_collection"] = hdr("3466", "Maximum Coin Collection", "maximum-coin-collection") + '''
class Solution {
    func maxCoins(_ lane1: [Int], _ lane2: [Int]) -> Int {
        let n = lane1.count
        let neg = -(1 << 60)
        var dp = Array(repeating: Array(repeating: 0, count: 2), count: 2)
        dp[0][0] = lane1[0]
        dp[1][0] = lane2[0]
        dp[0][1] = neg
        dp[1][1] = neg
        var ans = max(dp[0][0], dp[1][0])
        if n >= 2 {
            for i in 1..<n {
                var ndp = Array(repeating: Array(repeating: 0, count: 2), count: 2)
                ndp[0][0] = max(dp[0][0], 0) + lane1[i]
                ndp[1][0] = max(dp[1][0], 0) + lane2[i]
                ndp[0][1] = max(dp[0][1], dp[1][0]) + lane1[i]
                ndp[1][1] = max(dp[1][1], dp[0][0]) + lane2[i]
                if lane1[i] > ndp[0][0] { ndp[0][0] = lane1[i] }
                if lane2[i] > ndp[1][0] { ndp[1][0] = lane2[i] }
                for a in 0..<2 {
                    for b in 0..<2 {
                        dp[a][b] = ndp[a][b]
                        if dp[a][b] > ans { ans = dp[a][b] }
                    }
                }
            }
        }
        return ans
    }
}
'''

FILES["3467_transform_array_by_parity"] = hdr("3467", "Transform Array by Parity", "transform-array-by-parity") + '''
class Solution {
    func transformArray(_ nums: [Int]) -> [Int] {
        var nums = nums.map { $0 % 2 }
        var j = 0
        for i in 0..<nums.count where nums[i] == 0 {
            nums.swapAt(i, j)
            j += 1
        }
        return nums
    }
}
'''

FILES["3468_find_the_number_of_copy_arrays"] = hdr("3468", "Find the Number of Copy Arrays", "find-the-number-of-copy-arrays") + '''
class Solution {
    func countArrays(_ original: [Int], _ bounds: [[Int]]) -> Int {
        let n = original.count
        var lo = bounds[0][0], hi = bounds[0][1]
        if n >= 2 {
            for i in 1..<n {
                let diff = original[i] - original[i - 1]
                let lo2 = bounds[i][0], hi2 = bounds[i][1]
                var nlo = lo + diff, nhi = hi + diff
                if nlo < lo2 { nlo = lo2 }
                if nhi > hi2 { nhi = hi2 }
                if nlo > nhi { return 0 }
                lo = nlo
                hi = nhi
            }
        }
        return hi - lo + 1
    }
}
'''

FILES["3469_find_minimum_cost_to_remove_array_elements"] = hdr("3469", "Find Minimum Cost to Remove Array Elements", "find-minimum-cost-to-remove-array-elements") + '''
class Solution {
    func minCost(_ nums: [Int]) -> Int {
        let n = nums.count
        var memo = [Int: Int]()
        func key(_ i: Int, _ prev: Int) -> Int { return (i << 32) | (prev & ((1 << 32) - 1)) }
        func max2(_ a: Int, _ b: Int) -> Int { a > b ? a : b }
        func min3(_ a: Int, _ b: Int, _ c: Int) -> Int { min(a, min(b, c)) }
        func dfs(_ i: Int, _ prev: Int) -> Int {
            if i >= n { return prev == -1 ? 0 : nums[prev] }
            let k = key(i, prev)
            if let c = memo[k] { return c }
            var res = 0
            if prev == -1 {
                if i + 1 >= n { res = nums[i] }
                else if i + 2 >= n { res = max2(nums[i], nums[i + 1]) }
                else {
                    let a = nums[i], b = nums[i + 1], c = nums[i + 2]
                    res = min3(max2(b, c) + dfs(i + 3, i), max2(a, c) + dfs(i + 3, i + 1), max2(a, b) + dfs(i + 3, i + 2))
                }
            } else {
                if i + 1 >= n { res = max2(nums[prev], nums[i]) }
                else {
                    let a = nums[prev], b = nums[i], c = nums[i + 1]
                    res = min3(max2(b, c) + dfs(i + 2, prev), max2(a, c) + dfs(i + 2, i), max2(a, b) + dfs(i + 2, i + 1))
                }
            }
            memo[k] = res
            return res
        }
        return dfs(0, -1)
    }
}
'''

FILES["3470_permutations_iv"] = hdr("3470", "Permutations IV", "permutations-iv") + '''
class Solution {
    func permute(_ n: Int, _ k: Int) -> [Int] {
        var fact = Array(repeating: 1, count: n + 1)
        if n >= 1 {
            for i in 1...n {
                fact[i] = fact[i - 1] * i
                if fact[i] > Int(1e18) { fact[i] = Int(1e18) + 1 }
            }
        }
        var used = Array(repeating: false, count: n + 1)
        var ans = [Int]()
        var k = k
        func dfs(_ pos: Int) -> Bool {
            if pos == n { return true }
            for x in 1...n {
                if used[x] { continue }
                if pos > 0 && (ans[pos - 1] % 2 == x % 2) { continue }
                let rem = n - pos - 1
                let cnt = fact[rem]
                if cnt >= k {
                    used[x] = true
                    ans.append(x)
                    if dfs(pos + 1) { return true }
                    ans.removeLast()
                    used[x] = false
                } else {
                    k -= cnt
                }
            }
            return false
        }
        if !dfs(0) { return [] }
        return ans
    }
}
'''

FILES["3471_find_the_largest_almost_missing_integer"] = hdr("3471", "Find the Largest Almost Missing Integer", "find-the-largest-almost-missing-integer") + '''
class Solution {
    func largestInteger(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var cnt = [Int: Int]()
        if n >= k {
            for i in 0...(n - k) {
                var seen = Set<Int>()
                for j in i..<(i + k) { seen.insert(nums[j]) }
                for x in seen { cnt[x, default: 0] += 1 }
            }
        }
        var ans = -1
        for (x, c) in cnt where c == 1 && x > ans { ans = x }
        return ans
    }
}
'''

FILES["3472_longest_palindromic_subsequence_after_at_most_k_operations"] = hdr("3472", "Longest Palindromic Subsequence After at Most K Operations", "longest-palindromic-subsequence-after-at-most-k-operations") + '''
class Solution {
    func longestPalindromicSubsequence(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var dp = Array(repeating: Array(repeating: Array(repeating: -1, count: k + 1), count: n), count: n)
        func distCirc(_ a: Character, _ b: Character) -> Int {
            let d = abs(Int(a.asciiValue!) - Int(b.asciiValue!))
            return min(d, 26 - d)
        }
        func dfs(_ i: Int, _ j: Int, _ ops: Int) -> Int {
            if i > j { return 0 }
            if i == j { return 1 }
            if dp[i][j][ops] != -1 { return dp[i][j][ops] }
            var best = max(dfs(i + 1, j, ops), dfs(i, j - 1, ops))
            let cost = distCirc(chars[i], chars[j])
            if cost <= ops { best = max(best, 2 + dfs(i + 1, j - 1, ops - cost)) }
            dp[i][j][ops] = best
            return best
        }
        return dfs(0, n - 1, k)
    }
}
'''

FILES["3473_sum_of_k_subarrays_with_length_at_least_m"] = hdr("3473", "Sum of K Subarrays With Length at Least M", "sum-of-k-subarrays-with-length-at-least-m") + '''
class Solution {
    func maxSum(_ nums: [Int], _ k: Int, _ m: Int) -> Int {
        let n = nums.count
        var pref = Array(repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] + nums[i] }
        let neg = -(1 << 60)
        var dp = Array(repeating: Array(repeating: neg, count: n + 1), count: k + 1)
        for i in 0...n { dp[0][i] = 0 }
        if k >= 1 {
            for t in 1...k {
                var best = neg
                if t * m <= n {
                    for i in (t * m)...n {
                        let j = i - m
                        best = max(best, dp[t - 1][j] - pref[j])
                        dp[t][i] = best + pref[i]
                    }
                }
                for i in 1...n { dp[t][i] = max(dp[t][i], dp[t][i - 1]) }
            }
        }
        return dp[k][n]
    }
}
'''

FILES["3474_lexicographically_smallest_generated_string"] = hdr("3474", "Lexicographically Smallest Generated String", "lexicographically-smallest-generated-string") + '''
class Solution {
    func generateString(_ str1: String, _ str2: String) -> String {
        let s1 = Array(str1), s2 = Array(str2)
        let n = s1.count, m = s2.count
        let L = n + m - 1
        var ans = Array(repeating: Character("?"), count: L)
        for i in 0..<n where s1[i] == "T" {
            for j in 0..<m {
                if ans[i + j] != "?" && ans[i + j] != s2[j] { return "" }
                ans[i + j] = s2[j]
            }
        }
        for i in 0..<L where ans[i] == "?" { ans[i] = "a" }
        for i in 0..<n where s1[i] == "F" {
            var match = true
            for j in 0..<m where ans[i + j] != s2[j] { match = false; break }
            if match {
                var changed = false
                for j in stride(from: m - 1, through: 0, by: -1) {
                    let pos = i + j
                    var forced = false
                    for t in 0..<n {
                        if s1[t] == "T" && pos >= t && pos < t + m { forced = true; break }
                    }
                    if !forced {
                        ans[pos] = "b"
                        changed = true
                        break
                    }
                }
                if !changed { return "" }
            }
        }
        for i in 0..<n {
            var match = true
            for j in 0..<m where ans[i + j] != s2[j] { match = false; break }
            if s1[i] == "T" && !match { return "" }
            if s1[i] == "F" && match { return "" }
        }
        return String(ans)
    }
}
'''

FILES["3476_maximize_profit_from_task_assignment"] = hdr("3476", "Maximize Profit from Task Assignment", "maximize-profit-from-task-assignment") + '''
class Solution {
    func maxProfit(_ workers: [Int], _ tasks: [[Int]]) -> Int {
        let workers = workers.sorted()
        let tasks = tasks.sorted { $0[0] < $1[0] }
        var ans = 0
        var used = Array(repeating: false, count: tasks.count)
        for w in workers {
            var best = -1, bi = -1
            for i in 0..<tasks.count {
                if used[i] { continue }
                if tasks[i][0] > w { break }
                if tasks[i][1] > best {
                    best = tasks[i][1]
                    bi = i
                }
            }
            if bi >= 0 {
                used[bi] = true
                ans += best
            }
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
