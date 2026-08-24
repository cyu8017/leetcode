#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def hdr(num, title, slug):
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n"

MINHEAP3 = '''
private struct MinHeap3 {
    private var a: [(Int, Int, Int)] = []
    var isEmpty: Bool { a.isEmpty }
    mutating func push(_ x: (Int, Int, Int)) {
        a.append(x)
        var i = a.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if a[p].0 <= a[i].0 { break }
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
                if l < a.count && a[l].0 < a[s].0 { s = l }
                if rg < a.count && a[rg].0 < a[s].0 { s = rg }
                if s == i { break }
                a.swapAt(i, s)
                i = s
            }
        }
        return r
    }
}
'''

MINHEAP4 = '''
private struct MinHeap4 {
    private var a: [(Int, Int, Int, Int)] = []
    var isEmpty: Bool { a.isEmpty }
    mutating func push(_ x: (Int, Int, Int, Int)) {
        a.append(x)
        var i = a.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if a[p].0 <= a[i].0 { break }
            a.swapAt(p, i)
            i = p
        }
    }
    mutating func pop() -> (Int, Int, Int, Int) {
        let r = a[0]
        let last = a.removeLast()
        if !a.isEmpty {
            a[0] = last
            var i = 0
            while true {
                var s = i
                let l = 2 * i + 1, rg = 2 * i + 2
                if l < a.count && a[l].0 < a[s].0 { s = l }
                if rg < a.count && a[rg].0 < a[s].0 { s = rg }
                if s == i { break }
                a.swapAt(i, s)
                i = s
            }
        }
        return r
    }
}
'''

MAXHEAP = '''
private struct MaxHeap {
    private var a: [Int] = []
    var isEmpty: Bool { a.isEmpty }
    var peek: Int { a[0] }
    mutating func push(_ x: Int) {
        a.append(x)
        var i = a.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if a[p] >= a[i] { break }
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
                if l < a.count && a[l] > a[s] { s = l }
                if rg < a.count && a[rg] > a[s] { s = rg }
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

FILES["3340_check_balanced_string"] = hdr("3340", "Check Balanced String", "check-balanced-string") + '''
class Solution {
    func isBalanced(_ num: String) -> Bool {
        var even = 0, odd = 0
        for (i, c) in num.enumerated() {
            let d = Int(c.asciiValue! - 48)
            if i % 2 == 0 { even += d } else { odd += d }
        }
        return even == odd
    }
}
'''

FILES["3341_find_minimum_time_to_reach_last_room_i"] = hdr("3341", "Find Minimum Time to Reach Last Room I", "find-minimum-time-to-reach-last-room-i") + MINHEAP3 + '''
class Solution {
    func minTimeToReach(_ moveTime: [[Int]]) -> Int {
        let m = moveTime.count, n = moveTime[0].count
        var dist = Array(repeating: Array(repeating: 1 << 30, count: n), count: m)
        var h = MinHeap3()
        h.push((0, 0, 0))
        dist[0][0] = 0
        let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while !h.isEmpty {
            let (t, r, c) = h.pop()
            if t != dist[r][c] { continue }
            if r == m - 1 && c == n - 1 { return t }
            for (dr, dc) in dirs {
                let nr = r + dr, nc = c + dc
                if nr < 0 || nc < 0 || nr >= m || nc >= n { continue }
                let start = max(t, moveTime[nr][nc])
                let nt = start + 1
                if nt < dist[nr][nc] {
                    dist[nr][nc] = nt
                    h.push((nt, nr, nc))
                }
            }
        }
        return -1
    }
}
'''

FILES["3342_find_minimum_time_to_reach_last_room_ii"] = hdr("3342", "Find Minimum Time to Reach Last Room II", "find-minimum-time-to-reach-last-room-ii") + MINHEAP4 + '''
class Solution {
    func minTimeToReach(_ moveTime: [[Int]]) -> Int {
        let m = moveTime.count, n = moveTime[0].count
        let INF = 1 << 30
        var dist = Array(repeating: Array(repeating: Array(repeating: INF, count: 2), count: n), count: m)
        var pq = MinHeap4()
        dist[0][0][0] = 0
        pq.push((0, 0, 0, 0))
        let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while !pq.isEmpty {
            let (t, r, c, parity) = pq.pop()
            if t != dist[r][c][parity] { continue }
            if r == m - 1 && c == n - 1 { return t }
            let cost = parity == 1 ? 2 : 1
            for (dr, dc) in dirs {
                let nr = r + dr, nc = c + dc
                if nr < 0 || nc < 0 || nr >= m || nc >= n { continue }
                let start = max(t, moveTime[nr][nc])
                let nt = start + cost
                let np = 1 - parity
                if nt < dist[nr][nc][np] {
                    dist[nr][nc][np] = nt
                    pq.push((nt, nr, nc, np))
                }
            }
        }
        return -1
    }
}
'''

FILES["3343_count_number_of_balanced_permutations"] = hdr("3343", "Count Number of Balanced Permutations", "count-number-of-balanced-permutations") + '''
class Solution {
    func countBalancedPermutations(_ num: String) -> Int {
        let mod = 1_000_000_007
        var cnt = Array(repeating: 0, count: 10)
        var sum = 0
        for c in num {
            let d = Int(c.asciiValue! - 48)
            cnt[d] += 1
            sum += d
        }
        if sum % 2 == 1 { return 0 }
        let n = num.count
        let halfN = n / 2, halfS = sum / 2
        var fact = Array(repeating: 1, count: n + 1)
        var invF = Array(repeating: 1, count: n + 1)
        if n >= 1 {
            for i in 1...n { fact[i] = fact[i - 1] * i % mod }
        }
        invF[n] = modPow(fact[n], mod - 2, mod)
        if n >= 1 {
            for i in stride(from: n, through: 1, by: -1) { invF[i - 1] = invF[i] * i % mod }
        }
        var dp = [Int: Int]()
        dp[0] = 1
        for d in 0...9 {
            var ndp = [Int: Int]()
            for (st, ways) in dp {
                let used = st >> 32
                let s = st & ((1 << 32) - 1)
                for take in 0...cnt[d] {
                    let nu = used + take, ns = s + take * d
                    if nu > halfN || ns > halfS { continue }
                    let w = ways * invF[take] % mod * invF[cnt[d] - take] % mod
                    let nk = (nu << 32) | ns
                    ndp[nk, default: 0] = (ndp[nk, default: 0] + w) % mod
                }
            }
            dp = ndp
        }
        var ans = dp[(halfN << 32) | halfS, default: 0]
        ans = ans * fact[halfN] % mod * fact[n - halfN] % mod
        for d in 0...9 { ans = ans * fact[cnt[d]] % mod }
        return ans
    }

    private func modPow(_ a: Int, _ e: Int, _ mod: Int) -> Int {
        var r = 1, a = a % mod, e = e
        while e > 0 {
            if e & 1 != 0 { r = r * a % mod }
            a = a * a % mod
            e >>= 1
        }
        return r
    }
}
'''

FILES["3344_maximum_sized_array"] = hdr("3344", "Maximum Sized Array", "maximum-sized-array") + '''
class Solution {
    func maxSizedArray(_ s: Int) -> Int {
        var lo = 1, hi = 2000
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if ok(mid, s) { lo = mid } else { hi = mid - 1 }
        }
        return lo
    }

    private func ok(_ n: Int, _ s: Int) -> Bool {
        var sum = 0
        for i in 0..<n {
            for j in 0..<n {
                let ij = i | j
                sum += ij * (n - 1) * n / 2
                if sum > s { return false }
            }
        }
        return sum <= s
    }
}
'''

FILES["3345_smallest_divisible_digit_product_i"] = hdr("3345", "Smallest Divisible Digit Product I", "smallest-divisible-digit-product-i") + '''
class Solution {
    func smallestNumber(_ n: Int, _ t: Int) -> Int {
        var x = n
        while true {
            var p = 1, y = x
            while y > 0 { p *= y % 10; y /= 10 }
            if p % t == 0 { return x }
            x += 1
        }
    }
}
'''

LBUB = '''
    private func lowerBound(_ a: [Int], _ x: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] < x { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }
    private func upperBound(_ a: [Int], _ x: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] <= x { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }
'''

FILES["3346_maximum_frequency_of_an_element_after_performing_operations_i"] = hdr("3346", "Maximum Frequency of an Element After Performing Operations I", "maximum-frequency-of-an-element-after-performing-operations-i") + '''
class Solution {
    func maxFrequency(_ nums: [Int], _ k: Int, _ numOperations: Int) -> Int {
        let nums = nums.sorted()
        let n = nums.count
        var freq = [Int: Int]()
        for x in nums { freq[x, default: 0] += 1 }
        var ans = 1
        for (t, f) in freq {
            let lo = lowerBound(nums, t - k)
            let hi = upperBound(nums, t + k)
            let can = hi - lo
            let use = min(can, f + numOperations)
            if use > ans { ans = use }
        }
        var l = 0
        for r in 0..<n {
            while nums[r] - nums[l] > 2 * k { l += 1 }
            let window = min(r - l + 1, numOperations)
            if window > ans { ans = window }
        }
        return ans
    }
''' + LBUB + '''
}
'''

FILES["3347_maximum_frequency_of_an_element_after_performing_operations_ii"] = hdr("3347", "Maximum Frequency of an Element After Performing Operations II", "maximum-frequency-of-an-element-after-performing-operations-ii") + '''
class Solution {
    func maxFrequency(_ nums: [Int], _ k: Int, _ numOperations: Int) -> Int {
        let nums = nums.sorted()
        var freq = [Int: Int]()
        for x in nums { freq[x, default: 0] += 1 }
        var ans = 1
        var seen = Set<Int>()
        var candidates = [Int]()
        for x in nums {
            for t in [x - k, x, x + k] {
                if seen.insert(t).inserted { candidates.append(t) }
            }
        }
        for t in candidates {
            let lo = lowerBound(nums, t - k)
            let hi = upperBound(nums, t + k)
            let can = hi - lo
            let f = freq[t, default: 0]
            ans = max(ans, min(can, f + numOperations))
        }
        return ans
    }
''' + LBUB + '''
}
'''

FILES["3348_smallest_divisible_digit_product_ii"] = hdr("3348", "Smallest Divisible Digit Product II", "smallest-divisible-digit-product-ii") + '''
class Solution {
    func smallestNumber(_ num: String, _ t: Int) -> String {
        var tt = t
        for d in stride(from: 9, through: 2, by: -1) {
            while tt % d == 0 { tt /= d }
        }
        if tt > 1 { return "-1" }
        let numArr = Array(num)
        for extra in 0...60 {
            let L = numArr.count + extra
            var res = Array(repeating: Character("0"), count: L)
            if dfs(&res, 0, true, extra == 0, numArr, t) { return String(res) }
        }
        return "-1"
    }

    private func dfs(_ res: inout [Character], _ i: Int, _ tight: Bool, _ sameLen: Bool, _ num: [Character], _ t: Int) -> Bool {
        if i == res.count {
            var prod = 1
            for c in res {
                prod *= Int(c.asciiValue! - 48)
                if prod == 0 { break }
            }
            return prod % t == 0 && prod > 0
        }
        var start: UInt8 = i == 0 ? 49 : 48
        if tight && sameLen && i < num.count { start = num[i].asciiValue! }
        var c = start
        while c <= 57 {
            res[i] = Character(UnicodeScalar(c))
            let nt = tight && sameLen && i < num.count && c == num[i].asciiValue!
            if dfs(&res, i + 1, nt, sameLen, num, t) { return true }
            c += 1
        }
        return false
    }
}
'''

FILES["3349_adjacent_increasing_subarrays_detection_i"] = hdr("3349", "Adjacent Increasing Subarrays Detection I", "adjacent-increasing-subarrays-detection-i") + '''
class Solution {
    func hasIncreasingSubarrays(_ nums: [Int], _ k: Int) -> Bool {
        let n = nums.count
        if n < 2 * k { return false }
        for i in 0...(n - 2 * k) {
            if inc(nums, i, k) && inc(nums, i + k, k) { return true }
        }
        return false
    }

    private func inc(_ nums: [Int], _ start: Int, _ k: Int) -> Bool {
        if k <= 1 { return true }
        for i in start..<(start + k - 1) {
            if nums[i] >= nums[i + 1] { return false }
        }
        return true
    }
}
'''

FILES["3350_adjacent_increasing_subarrays_detection_ii"] = hdr("3350", "Adjacent Increasing Subarrays Detection II", "adjacent-increasing-subarrays-detection-ii") + '''
class Solution {
    func maxIncreasingSubarrays(_ nums: [Int]) -> Int {
        let n = nums.count
        var up = Array(repeating: 1, count: n)
        for i in stride(from: n - 2, through: 0, by: -1) {
            up[i] = nums[i] < nums[i + 1] ? up[i + 1] + 1 : 1
        }
        var lo = 1, hi = n / 2
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if ok(up, n, mid) { lo = mid } else { hi = mid - 1 }
        }
        return lo
    }

    private func ok(_ up: [Int], _ n: Int, _ k: Int) -> Bool {
        if n < 2 * k { return false }
        for i in 0...(n - 2 * k) {
            if up[i] >= k && up[i + k] >= k { return true }
        }
        return false
    }
}
'''

FILES["3351_sum_of_good_subsequences"] = hdr("3351", "Sum of Good Subsequences", "sum-of-good-subsequences") + '''
class Solution {
    func sumOfGoodSubsequences(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        var cnt = [Int: Int]()
        var sum = [Int: Int]()
        var ans = 0
        for x in nums {
            var c = 1
            var s = x
            if cnt[x - 1, default: 0] > 0 {
                c = (c + cnt[x - 1]!) % mod
                s = (s + sum[x - 1]! + cnt[x - 1]! * x % mod) % mod
            }
            if cnt[x + 1, default: 0] > 0 {
                c = (c + cnt[x + 1]!) % mod
                s = (s + sum[x + 1]! + cnt[x + 1]! * x % mod) % mod
            }
            cnt[x, default: 0] = (cnt[x, default: 0] + c) % mod
            sum[x, default: 0] = (sum[x, default: 0] + s) % mod
            ans = (ans + s) % mod
        }
        return ans
    }
}
'''

FILES["3352_count_k_reducible_numbers_less_than_n"] = hdr("3352", "Count K-Reducible Numbers Less Than N", "count-k-reducible-numbers-less-than-n") + '''
class Solution {
    func countKReducibleNumbers(_ s: String, _ k: Int) -> Int {
        let mod = 1_000_000_007
        let chars = Array(s)
        var red = Array(repeating: 0, count: 801)
        func bitsPop(_ x: Int) -> Int {
            var x = x, c = 0
            while x > 0 { c += x & 1; x >>= 1 }
            return c
        }
        if 2 <= 800 {
            for i in 2...800 { red[i] = 1 + red[bitsPop(i)] }
        }
        var memo = [Int: Int]()
        func key(_ pos: Int, _ tight: Int, _ ones: Int) -> Int {
            return (pos << 32) | (tight << 16) | ones
        }
        func dfs(_ pos: Int, _ tight: Bool, _ ones: Int) -> Int {
            if pos == chars.count {
                if ones == 0 { return 0 }
                return red[ones] <= k - 1 ? 1 : 0
            }
            let ky = key(pos, tight ? 1 : 0, ones)
            if let v = memo[ky] { return v }
            let up = tight ? Int(chars[pos].asciiValue! - 48) : 1
            var ans = 0
            for d in 0...up {
                let nt = tight && d == up
                ans = (ans + dfs(pos + 1, nt, ones + d)) % mod
            }
            memo[ky] = ans
            return ans
        }
        return dfs(0, true, 0)
    }
}
'''

FILES["3353_minimum_total_operations"] = hdr("3353", "Minimum Total Operations", "minimum-total-operations") + '''
class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        var ops = 0
        for i in stride(from: nums.count - 2, through: 0, by: -1) {
            if nums[i] != nums[i + 1] { ops += 1 }
        }
        return ops
    }
}
'''

FILES["3354_make_array_elements_equal_to_zero"] = hdr("3354", "Make Array Elements Equal to Zero", "make-array-elements-equal-to-zero") + '''
class Solution {
    func countValidSelections(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n where nums[i] == 0 {
            for dir in [-1, 1] {
                var a = nums
                var cur = i, d = dir
                while cur >= 0 && cur < n {
                    if a[cur] == 0 { cur += d }
                    else {
                        a[cur] -= 1
                        d = -d
                        cur += d
                    }
                }
                if a.allSatisfy({ $0 == 0 }) { ans += 1 }
            }
        }
        return ans
    }
}
'''

FILES["3355_zero_array_transformation_i"] = hdr("3355", "Zero Array Transformation I", "zero-array-transformation-i") + '''
class Solution {
    func isZeroArray(_ nums: [Int], _ queries: [[Int]]) -> Bool {
        let n = nums.count
        var diff = Array(repeating: 0, count: n + 1)
        for q in queries {
            diff[q[0]] += 1
            diff[q[1] + 1] -= 1
        }
        var cur = 0
        for i in 0..<n {
            cur += diff[i]
            if cur < nums[i] { return false }
        }
        return true
    }
}
'''

FILES["3356_zero_array_transformation_ii"] = hdr("3356", "Zero Array Transformation II", "zero-array-transformation-ii") + '''
class Solution {
    func minZeroArray(_ nums: [Int], _ queries: [[Int]]) -> Int {
        let n = nums.count
        if ok(0, nums, queries, n) { return 0 }
        var lo = 1, hi = queries.count + 1
        while lo < hi {
            let mid = (lo + hi) / 2
            if mid <= queries.count && ok(mid, nums, queries, n) { hi = mid }
            else { lo = mid + 1 }
        }
        if lo > queries.count { return -1 }
        return lo
    }

    private func ok(_ k: Int, _ nums: [Int], _ queries: [[Int]], _ n: Int) -> Bool {
        var diff = Array(repeating: 0, count: n + 1)
        for i in 0..<k {
            let q = queries[i]
            diff[q[0]] += q[2]
            diff[q[1] + 1] -= q[2]
        }
        var cur = 0
        for i in 0..<n {
            cur += diff[i]
            if cur < nums[i] { return false }
        }
        return true
    }
}
'''

FILES["3357_minimize_the_maximum_adjacent_element_difference"] = hdr("3357", "Minimize the Maximum Adjacent Element Difference", "minimize-the-maximum-adjacent-element-difference") + '''
class Solution {
    func minDifference(_ nums: [Int]) -> Int {
        let n = nums.count
        var lo = 0, hi = 1_000_000_000
        while lo < hi {
            let mid = (lo + hi) / 2
            if ok(mid, nums, n) { hi = mid } else { lo = mid + 1 }
        }
        return lo
    }

    private func ok(_ d: Int, _ nums: [Int], _ n: Int) -> Bool {
        var prev = -1
        var i = 0
        while i < n {
            if nums[i] != -1 {
                if prev != -1 && abs(nums[i] - prev) > d { return false }
                prev = nums[i]
                i += 1
                continue
            }
            var j = i
            while j < n && nums[j] == -1 { j += 1 }
            let left = prev
            let right = j < n ? nums[j] : -1
            let gap = j - i
            if left == -1 && right == -1 { return true }
            if left == -1 || right == -1 {
                prev = -1
                i = j
                continue
            }
            if abs(left - right) > d * (gap + 1) { return false }
            prev = -1
            i = j
        }
        return true
    }
}
'''

FILES["3359_find_sorted_submatrices_with_maximum_element_at_most_k"] = hdr("3359", "Find Sorted Submatrices With Maximum Element at Most K", "find-sorted-submatrices-with-maximum-element-at-most-k") + '''
class Solution {
    func countSortedMatrices(_ grid: [[Int]], _ k: Int) -> Int {
        let m = grid.count, n = grid[0].count
        var ans = 0
        for r1 in 0..<m {
            for r2 in r1..<m {
                for c1 in 0..<n {
                    for c2 in c1..<n {
                        var ok = true
                        var i = r1
                        while i <= r2 && ok {
                            for j in c1...c2 {
                                if grid[i][j] > k { ok = false; break }
                                if j > c1 && grid[i][j] < grid[i][j - 1] { ok = false; break }
                                if i > r1 && grid[i][j] < grid[i - 1][j] { ok = false; break }
                            }
                            i += 1
                        }
                        if ok { ans += 1 }
                    }
                }
            }
        }
        return ans
    }
}
'''

FILES["3360_stone_removal_game"] = hdr("3360", "Stone Removal Game", "stone-removal-game") + '''
class Solution {
    func canAliceWin(_ n: Int) -> Bool {
        var n = n, take = 10, alice = true
        while n >= take && take > 0 {
            n -= take
            take -= 1
            alice = !alice
        }
        return !alice
    }
}
'''

FILES["3361_shift_distance_between_two_strings"] = hdr("3361", "Shift Distance Between Two Strings", "shift-distance-between-two-strings") + '''
class Solution {
    func shiftDistance(_ s: String, _ t: String, _ nextCost: [Int], _ previousCost: [Int]) -> Int {
        let sa = Array(s), ta = Array(t)
        var ans = 0
        for i in 0..<sa.count {
            var a = Int(sa[i].asciiValue! - 97)
            let b = Int(ta[i].asciiValue! - 97)
            if a == b { continue }
            var fwd = 0
            var x = a
            while x != b {
                fwd += nextCost[x]
                x = (x + 1) % 26
            }
            var bwd = 0
            x = a
            while x != b {
                bwd += previousCost[x]
                x = (x + 25) % 26
            }
            ans += min(fwd, bwd)
        }
        return ans
    }
}
'''

FILES["3362_zero_array_transformation_iii"] = hdr("3362", "Zero Array Transformation III", "zero-array-transformation-iii") + MAXHEAP + '''
class Solution {
    func maxRemoval(_ nums: [Int], _ queries: [[Int]]) -> Int {
        let queries = queries.sorted { $0[0] < $1[0] }
        var h = MaxHeap()
        let n = nums.count
        var diff = Array(repeating: 0, count: n + 1)
        var j = 0, used = 0, cur = 0
        for i in 0..<n {
            cur += diff[i]
            while j < queries.count && queries[j][0] == i {
                h.push(queries[j][1])
                j += 1
            }
            while cur < nums[i] {
                if h.isEmpty || h.peek < i { return -1 }
                let r = h.pop()
                cur += 1
                diff[r + 1] -= 1
                used += 1
            }
        }
        return queries.count - used
    }
}
'''

FILES["3363_find_the_maximum_number_of_fruits_collected"] = hdr("3363", "Find the Maximum Number of Fruits Collected", "find-the-maximum-number-of-fruits-collected") + '''
class Solution {
    func maxCollectedFruits(_ fruits: [[Int]]) -> Int {
        var fruits = fruits
        let n = fruits.count
        var ans = 0
        for i in 0..<n {
            ans += fruits[i][i]
            fruits[i][i] = 0
        }
        let neg = -(1 << 30)
        var dp2 = Array(repeating: Array(repeating: neg, count: n), count: n)
        var dp3 = Array(repeating: Array(repeating: neg, count: n), count: n)
        dp2[0][n - 1] = fruits[0][n - 1]
        for i in 0..<n {
            for j in 0..<n {
                if dp2[i][j] == neg { continue }
                for dj in [-1, 0, 1] {
                    let ni = i + 1, nj = j + dj
                    if ni < n && nj >= 0 && nj < n && nj > ni {
                        let v = dp2[i][j] + fruits[ni][nj]
                        if v > dp2[ni][nj] { dp2[ni][nj] = v }
                    }
                }
            }
        }
        dp3[n - 1][0] = fruits[n - 1][0]
        for j in 0..<n {
            for i in 0..<n {
                if dp3[i][j] == neg { continue }
                for di in [-1, 0, 1] {
                    let ni = i + di, nj = j + 1
                    if ni >= 0 && ni < n && nj < n && ni > nj {
                        let v = dp3[i][j] + fruits[ni][nj]
                        if v > dp3[ni][nj] { dp3[ni][nj] = v }
                    }
                }
            }
        }
        ans += dp2[n - 1][n - 1] + dp3[n - 1][n - 1]
        return ans
    }
}
'''

FILES["3364_minimum_positive_sum_subarray"] = hdr("3364", "Minimum Positive Sum Subarray", "minimum-positive-sum-subarray") + '''
class Solution {
    func minimumSumSubarray(_ nums: [Int], _ l: Int, _ r: Int) -> Int {
        let n = nums.count
        var pref = Array(repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] + nums[i] }
        var ans = Int.max
        var found = false
        for i in 0..<n {
            var length = l
            while length <= r && i + length <= n {
                let s = pref[i + length] - pref[i]
                if s > 0 && s < ans {
                    ans = s
                    found = true
                }
                length += 1
            }
        }
        return found ? ans : -1
    }
}
'''

FILES["3365_rearrange_k_substrings_to_form_target_string"] = hdr("3365", "Rearrange K Substrings to Form Target String", "rearrange-k-substrings-to-form-target-string") + '''
class Solution {
    func isPossibleToRearrange(_ s: String, _ t: String, _ k: Int) -> Bool {
        let sa = Array(s), ta = Array(t)
        let n = sa.count
        let sz = n / k
        var cnt = [String: Int]()
        var i = 0
        while i < n {
            let a = String(sa[i..<(i + sz)])
            let b = String(ta[i..<(i + sz)])
            cnt[a, default: 0] += 1
            cnt[b, default: 0] -= 1
            i += sz
        }
        return cnt.values.allSatisfy { $0 == 0 }
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
