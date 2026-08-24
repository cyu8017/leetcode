#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def hdr(num, title, slug):
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n"

FILES = {}

FILES["3423_maximum_difference_between_adjacent_elements_in_a_circular_array"] = hdr("3423", "Maximum Difference Between Adjacent Elements in a Circular Array", "maximum-difference-between-adjacent-elements-in-a-circular-array") + '''
class Solution {
    func maxAdjacentDistance(_ nums: [Int]) -> Int {
        var ans = 0
        let n = nums.count
        for i in 0..<n {
            let d = abs(nums[i] - nums[(i + 1) % n])
            if d > ans { ans = d }
        }
        return ans
    }
}
'''

FILES["3424_minimum_cost_to_make_arrays_identical"] = hdr("3424", "Minimum Cost to Make Arrays Identical", "minimum-cost-to-make-arrays-identical") + '''
class Solution {
    func minCost(_ arr: [Int], _ brr: [Int], _ k: Int) -> Int {
        var noSwap = 0
        for i in 0..<arr.count { noSwap += abs(arr[i] - brr[i]) }
        let a2 = arr.sorted(), b2 = brr.sorted()
        var withSwap = k
        for i in 0..<a2.count { withSwap += abs(a2[i] - b2[i]) }
        return min(noSwap, withSwap)
    }
}
'''

FILES["3425_longest_special_path"] = hdr("3425", "Longest Special Path", "longest-special-path") + '''
class Solution {
    func longestSpecialPath(_ edges: [[Int]], _ nums: [Int]) -> [Int] {
        let n = nums.count
        var g = Array(repeating: [(Int, Int)](), count: n)
        for e in edges {
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        }
        var bestLen = 0, bestNodes = 1
        var last = [Int: Int]()
        var path = [Int]()
        func dfs(_ u: Int, _ p: Int, _ dist: Int, _ left: Int) {
            let seen = last[nums[u]] != nil
            let prevPos = last[nums[u]] ?? -1
            last[nums[u]] = path.count
            var newLeft = left
            if seen && prevPos >= left { newLeft = prevPos + 1 }
            path.append(dist)
            let length = dist - path[newLeft]
            let nodes = path.count - newLeft
            if length > bestLen || (length == bestLen && nodes < bestNodes) {
                bestLen = length
                bestNodes = nodes
            }
            for (v, w) in g[u] where v != p {
                dfs(v, u, dist + w, newLeft)
            }
            path.removeLast()
            if seen { last[nums[u]] = prevPos }
            else { last.removeValue(forKey: nums[u]) }
        }
        dfs(0, -1, 0, 0)
        return [bestLen, bestNodes]
    }
}
'''

FILES["3426_manhattan_distances_of_all_arrangements_of_pieces"] = hdr("3426", "Manhattan Distances of All Arrangements of Pieces", "manhattan-distances-of-all-arrangements-of-pieces") + '''
class Solution {
    func distanceSum(_ m: Int, _ n: Int, _ k: Int) -> Int {
        let mod = 1_000_000_007
        if k < 2 { return 0 }
        let totalCells = m * n
        let pairChoose = comb(totalCells - 2, k - 2, mod)
        var sumDist = 0
        if m > 1 {
            for d in 1..<m { sumDist += d * (m - d) * n * n }
        }
        if n > 1 {
            for d in 1..<n { sumDist += d * (n - d) * m * m }
        }
        return sumDist % mod * pairChoose % mod
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

FILES["3427_sum_of_variable_length_subarrays"] = hdr("3427", "Sum of Variable Length Subarrays", "sum-of-variable-length-subarrays") + '''
class Solution {
    func subarraySum(_ nums: [Int]) -> Int {
        let n = nums.count
        var pref = Array(repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] + nums[i] }
        var ans = 0
        for i in 0..<n {
            var start = i - nums[i]
            if start < 0 { start = 0 }
            ans += pref[i + 1] - pref[start]
        }
        return ans
    }
}
'''

FILES["3428_maximum_and_minimum_sums_of_at_most_size_k_subsequences"] = hdr("3428", "Maximum and Minimum Sums of at Most Size K Subsequences", "maximum-and-minimum-sums-of-at-most-size-k-subsequences") + '''
class Solution {
    func minMaxSums(_ nums: [Int], _ k: Int) -> Int {
        let mod = 1_000_000_007
        let nums = nums.sorted()
        let n = nums.count
        var C = Array(repeating: Array(repeating: 0, count: k), count: n + 1)
        for i in 0...n {
            C[i][0] = 1
            var j = 1
            while j < k && j <= i {
                C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % mod
                j += 1
            }
        }
        var ans = 0
        for i in 0..<n {
            var waysMax = 0
            var j = 0
            while j < k && j <= i {
                waysMax = (waysMax + C[i][j]) % mod
                j += 1
            }
            var waysMin = 0
            let right = n - i - 1
            j = 0
            while j < k && j <= right {
                waysMin = (waysMin + C[right][j]) % mod
                j += 1
            }
            ans = (ans + nums[i] * waysMax % mod + nums[i] * waysMin % mod) % mod
        }
        return ans
    }
}
'''

FILES["3429_paint_house_iv"] = hdr("3429", "Paint House IV", "paint-house-iv") + '''
class Solution {
    func minCost(_ n: Int, _ cost: [[Int]]) -> Int {
        let inf = 1 << 60
        let m = n / 2
        var dp = Array(repeating: Array(repeating: 0, count: 3), count: 3)
        for a in 0..<3 {
            for b in 0..<3 {
                dp[a][b] = a == b ? inf : cost[0][a] + cost[n - 1][b]
            }
        }
        if m > 1 {
            for i in 1..<m {
                var ndp = Array(repeating: Array(repeating: inf, count: 3), count: 3)
                for pa in 0..<3 {
                    for pb in 0..<3 {
                        if dp[pa][pb] >= inf { continue }
                        for a in 0..<3 where a != pa {
                            for b in 0..<3 where b != pb && a != b {
                                let v = dp[pa][pb] + cost[i][a] + cost[n - 1 - i][b]
                                if v < ndp[a][b] { ndp[a][b] = v }
                            }
                        }
                    }
                }
                dp = ndp
            }
        }
        var ans = inf
        for a in 0..<3 {
            for b in 0..<3 where dp[a][b] < ans { ans = dp[a][b] }
        }
        return ans
    }
}
'''

FILES["3430_maximum_and_minimum_sums_of_at_most_size_k_subarrays"] = hdr("3430", "Maximum and Minimum Sums of at Most Size K Subarrays", "maximum-and-minimum-sums-of-at-most-size-k-subarrays") + '''
class Solution {
    func minMaxSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var mn = nums[i], mx = nums[i]
            var j = i
            while j < n && j - i + 1 <= k {
                if nums[j] < mn { mn = nums[j] }
                if nums[j] > mx { mx = nums[j] }
                ans += mn + mx
                j += 1
            }
        }
        return ans
    }
}
'''

FILES["3431_minimum_unlocked_indices_to_sort_nums"] = hdr("3431", "Minimum Unlocked Indices to Sort Nums", "minimum-unlocked-indices-to-sort-nums") + '''
class Solution {
    func minUnlockedIndices(_ nums: [Int], _ locked: [Int]) -> Int {
        let n = nums.count
        var need = false
        for i in 1..<n where nums[i] < nums[i - 1] { need = true; break }
        if !need { return 0 }
        var left = n, right = -1
        for i in 0..<n {
            for j in (i + 1)..<n where nums[i] > nums[j] {
                if i < left { left = i }
                if j > right { right = j }
            }
        }
        if right < left { return 0 }
        var ans = 0
        for i in left...right where locked[i] == 1 { ans += 1 }
        var tmp = nums
        var lock = locked
        for i in left...right { lock[i] = 0 }
        var changed = true
        while changed {
            changed = false
            for i in 0..<(n - 1) {
                if lock[i] == 0 && lock[i + 1] == 0 && tmp[i] > tmp[i + 1] {
                    tmp.swapAt(i, i + 1)
                    changed = true
                }
            }
        }
        for i in 1..<n where tmp[i] < tmp[i - 1] { return -1 }
        return ans
    }
}
'''

FILES["3432_count_partitions_with_even_sum_difference"] = hdr("3432", "Count Partitions with Even Sum Difference", "count-partitions-with-even-sum-difference") + '''
class Solution {
    func countPartitions(_ nums: [Int]) -> Int {
        let total = nums.reduce(0, +)
        var ans = 0, left = 0
        for i in 0..<(nums.count - 1) {
            left += nums[i]
            if (left - (total - left)) % 2 == 0 { ans += 1 }
        }
        return ans
    }
}
'''

FILES["3433_count_mentions_per_user"] = hdr("3433", "Count Mentions Per User", "count-mentions-per-user") + '''
class Solution {
    func countMentions(_ numberOfUsers: Int, _ events: [[String]]) -> [Int] {
        var events = events
        events.sort { a, b in
            let ti = Int(a[1])!, tj = Int(b[1])!
            if ti != tj { return ti < tj }
            return a[0] > b[0]
        }
        var online = Array(repeating: true, count: numberOfUsers)
        var offlineUntil = Array(repeating: 0, count: numberOfUsers)
        var ans = Array(repeating: 0, count: numberOfUsers)
        for e in events {
            let t = Int(e[1])!
            for i in 0..<numberOfUsers {
                if !online[i] && offlineUntil[i] <= t { online[i] = true }
            }
            if e[0] == "OFFLINE" {
                let id = Int(e[2])!
                online[id] = false
                offlineUntil[id] = t + 60
            } else {
                let msg = e[2]
                if msg == "ALL" {
                    for i in 0..<numberOfUsers { ans[i] += 1 }
                } else if msg == "HERE" {
                    for i in 0..<numberOfUsers where online[i] { ans[i] += 1 }
                } else {
                    for part in msg.split(separator: " ") {
                        let id = Int(part.dropFirst(2))!
                        ans[id] += 1
                    }
                }
            }
        }
        return ans
    }
}
'''

FILES["3434_maximum_frequency_after_subarray_operation"] = hdr("3434", "Maximum Frequency After Subarray Operation", "maximum-frequency-after-subarray-operation") + '''
class Solution {
    func maxFrequency(_ nums: [Int], _ k: Int) -> Int {
        var base = 0
        for x in nums where x == k { base += 1 }
        var ans = base
        for v in Set(nums) where v != k {
            var best = 0, cur = 0
            for x in nums {
                var delta = 0
                if x == v { delta = 1 }
                else if x == k { delta = -1 }
                cur += delta
                if cur < 0 { cur = 0 }
                if cur > best { best = cur }
            }
            if base + best > ans { ans = base + best }
        }
        return ans
    }
}
'''

FILES["3435_frequencies_of_shortest_supersequences"] = hdr("3435", "Frequencies of Shortest Supersequences", "frequencies-of-shortest-supersequences") + '''
class Solution {
    func supersequences(_ words: [String]) -> [[Int]] {
        var used = Array(repeating: false, count: 26)
        for w in words {
            let a = Array(w)
            used[Int(a[0].asciiValue! - 97)] = true
            used[Int(a[1].asciiValue! - 97)] = true
        }
        var letters = [Int]()
        for i in 0..<26 where used[i] { letters.append(i) }
        let m = letters.count
        var best = 1_000_000_000
        var bestFreqs = [[Int]]()
        var freq = Array(repeating: 0, count: 26)
        func dfs(_ i: Int) {
            if i == m {
                for w in words {
                    let a = Array(w)
                    let x = Int(a[0].asciiValue! - 97), y = Int(a[1].asciiValue! - 97)
                    if x == y {
                        if freq[x] < 2 { return }
                    } else if freq[x] < 1 || freq[y] < 1 { return }
                }
                let sum = freq.reduce(0, +)
                if sum < best {
                    best = sum
                    bestFreqs = [freq]
                } else if sum == best {
                    bestFreqs.append(freq)
                }
                return
            }
            let L = letters[i]
            for c in 1...2 {
                freq[L] = c
                dfs(i + 1)
            }
            freq[L] = 0
        }
        dfs(0)
        return bestFreqs
    }
}
'''

FILES["3437_permutations_iii"] = hdr("3437", "Permutations III", "permutations-iii") + '''
class Solution {
    func permute(_ n: Int) -> [[Int]] {
        var ans = [[Int]]()
        var used = Array(repeating: false, count: n + 1)
        var cur = [Int]()
        func dfs() {
            if cur.count == n {
                ans.append(cur)
                return
            }
            for i in 1...n {
                if used[i] { continue }
                if !cur.isEmpty && (cur.last! % 2 == i % 2) { continue }
                used[i] = true
                cur.append(i)
                dfs()
                cur.removeLast()
                used[i] = false
            }
        }
        dfs()
        return ans
    }
}
'''

FILES["3438_find_valid_pair_of_adjacent_digits_in_string"] = hdr("3438", "Find Valid Pair of Adjacent Digits in String", "find-valid-pair-of-adjacent-digits-in-string") + '''
class Solution {
    func findValidPair(_ s: String) -> String {
        let chars = Array(s)
        var freq = Array(repeating: 0, count: 10)
        for c in chars { freq[Int(c.asciiValue! - 48)] += 1 }
        if chars.count >= 2 {
            for i in 0..<(chars.count - 1) {
                let a = Int(chars[i].asciiValue! - 48)
                let b = Int(chars[i + 1].asciiValue! - 48)
                if a != b && freq[a] == a && freq[b] == b { return String(chars[i...i+1]) }
            }
        }
        return ""
    }
}
'''

FILES["3439_reschedule_meetings_for_maximum_free_time_i"] = hdr("3439", "Reschedule Meetings for Maximum Free Time I", "reschedule-meetings-for-maximum-free-time-i") + '''
class Solution {
    func maxFreeTime(_ eventTime: Int, _ k: Int, _ startTime: [Int], _ endTime: [Int]) -> Int {
        let n = startTime.count
        var gaps = Array(repeating: 0, count: n + 1)
        gaps[0] = startTime[0]
        for i in 1..<n { gaps[i] = startTime[i] - endTime[i - 1] }
        gaps[n] = eventTime - endTime[n - 1]
        let window = k + 1
        var sum = 0
        for i in 0..<min(window, gaps.count) { sum += gaps[i] }
        var ans = sum
        if window < gaps.count {
            for i in window..<gaps.count {
                sum += gaps[i] - gaps[i - window]
                if sum > ans { ans = sum }
            }
        }
        return ans
    }
}
'''

FILES["3440_reschedule_meetings_for_maximum_free_time_ii"] = hdr("3440", "Reschedule Meetings for Maximum Free Time II", "reschedule-meetings-for-maximum-free-time-ii") + '''
class Solution {
    func maxFreeTime(_ eventTime: Int, _ startTime: [Int], _ endTime: [Int]) -> Int {
        let n = startTime.count
        var gaps = Array(repeating: 0, count: n + 1)
        gaps[0] = startTime[0]
        for i in 1..<n { gaps[i] = startTime[i] - endTime[i - 1] }
        gaps[n] = eventTime - endTime[n - 1]
        var ans = gaps.max() ?? 0
        var leftMax = Array(repeating: 0, count: n + 1)
        var rightMax = Array(repeating: 0, count: n + 1)
        for i in 0...n {
            leftMax[i] = gaps[i]
            if i > 0 && leftMax[i - 1] > leftMax[i] { leftMax[i] = leftMax[i - 1] }
        }
        for i in stride(from: n, through: 0, by: -1) {
            rightMax[i] = gaps[i]
            if i < n && rightMax[i + 1] > rightMax[i] { rightMax[i] = rightMax[i + 1] }
        }
        for i in 0..<n {
            let dur = endTime[i] - startTime[i]
            let merged = gaps[i] + gaps[i + 1]
            var bestOther = 0
            if i > 0 && leftMax[i - 1] > bestOther { bestOther = leftMax[i - 1] }
            if i + 2 <= n && rightMax[i + 2] > bestOther { bestOther = rightMax[i + 2] }
            var cand = merged
            if bestOther >= dur { cand = merged + dur }
            if cand > ans { ans = cand }
        }
        return ans
    }
}
'''

FILES["3441_minimum_cost_good_caption"] = hdr("3441", "Minimum Cost Good Caption", "minimum-cost-good-caption") + '''
class Solution {
    func minCostGoodCaption(_ caption: String) -> String {
        var ans = Array(caption)
        let n = ans.count
        if n < 3 { return "" }
        var i = 0
        while i < n {
            var j = i
            while j < n && ans[j] == ans[i] { j += 1 }
            if j - i >= 3 { i = j; continue }
            let need = 3 - (j - i)
            if j + need <= n {
                for t in 0..<need { ans[j + t] = ans[i] }
                i = j + need
            } else {
                var ch: Character = "a"
                if i > 0 { ch = ans[i - 1] }
                else if j < n { ch = Array(caption)[j] }
                for t in i..<n { ans[t] = ch }
                break
            }
        }
        i = 0
        while i < n {
            var j = i
            while j < n && ans[j] == ans[i] { j += 1 }
            if j - i < 3 { return "" }
            i = j
        }
        return String(ans)
    }
}
'''

FILES["3442_maximum_difference_between_even_and_odd_frequency_i"] = hdr("3442", "Maximum Difference Between Even and Odd Frequency I", "maximum-difference-between-even-and-odd-frequency-i") + '''
class Solution {
    func maxDifference(_ s: String) -> Int {
        var freq = Array(repeating: 0, count: 26)
        for c in s { freq[Int(c.asciiValue! - 97)] += 1 }
        var maxOdd = 0, minEven = 1_000_000_000
        for f in freq {
            if f == 0 { continue }
            if f % 2 == 1 {
                if f > maxOdd { maxOdd = f }
            } else if f < minEven { minEven = f }
        }
        return maxOdd - minEven
    }
}
'''

FILES["3443_maximum_manhattan_distance_after_k_changes"] = hdr("3443", "Maximum Manhattan Distance After K Changes", "maximum-manhattan-distance-after-k-changes") + '''
class Solution {
    func maxDistance(_ s: String, _ k: Int) -> Int {
        var ans = 0, lat = 0, lon = 0
        for (i, c) in s.enumerated() {
            if c == "N" { lat += 1 }
            else if c == "S" { lat -= 1 }
            else if c == "E" { lon += 1 }
            else { lon -= 1 }
            let md = abs(lat) + abs(lon)
            let steps = i + 1
            var cur = md + 2 * k
            if cur > steps { cur = steps }
            if cur > ans { ans = cur }
        }
        return ans
    }
}
'''

FILES["3444_minimum_increments_for_target_multiples_in_an_array"] = hdr("3444", "Minimum Increments for Target Multiples in an Array", "minimum-increments-for-target-multiples-in-an-array") + '''
class Solution {
    func minimumIncrements(_ nums: [Int], _ target: [Int]) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        func lcm(_ a: Int, _ b: Int) -> Int { return a / gcd(a, b) * b }
        let m = target.count
        let N = 1 << m
        let inf = Int(1e18)
        var dp = Array(repeating: inf, count: N)
        dp[0] = 0
        for x in nums {
            var ndp = dp
            for mask in 0..<N {
                for sub in 1..<N {
                    var L = 1
                    var ok = true
                    for i in 0..<m where (sub & (1 << i)) != 0 {
                        L = lcm(L, target[i])
                        if L > 1_000_000_000 { ok = false; break }
                    }
                    if !ok { continue }
                    let cost = (L - x % L) % L
                    let nmask = mask | sub
                    if dp[mask] + cost < ndp[nmask] { ndp[nmask] = dp[mask] + cost }
                }
            }
            dp = ndp
        }
        return dp[N - 1]
    }
}
'''

FILES["3445_maximum_difference_between_even_and_odd_frequency_ii"] = hdr("3445", "Maximum Difference Between Even and Odd Frequency II", "maximum-difference-between-even-and-odd-frequency-ii") + '''
class Solution {
    func maxDifference(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var ans = -1_000_000_000
        for a in 0..<5 {
            for b in 0..<5 where a != b {
                var prefA = Array(repeating: 0, count: n + 1)
                var prefB = Array(repeating: 0, count: n + 1)
                for i in 0..<n {
                    prefA[i + 1] = prefA[i]
                    prefB[i + 1] = prefB[i]
                    if Int(chars[i].asciiValue! - 48) == a { prefA[i + 1] += 1 }
                    if Int(chars[i].asciiValue! - 48) == b { prefB[i + 1] += 1 }
                }
                for i in 0..<n {
                    var j = i + k - 1
                    while j < n {
                        let fa = prefA[j + 1] - prefA[i]
                        let fb = prefB[j + 1] - prefB[i]
                        if fa % 2 == 1 && fb % 2 == 0 && fb > 0 {
                            if fa - fb > ans { ans = fa - fb }
                        }
                        j += 1
                    }
                }
            }
        }
        return ans
    }
}
'''

FILES["3446_sort_matrix_by_diagonals"] = hdr("3446", "Sort Matrix by Diagonals", "sort-matrix-by-diagonals") + '''
class Solution {
    func sortMatrix(_ grid: [[Int]]) -> [[Int]] {
        var grid = grid
        let n = grid.count
        var diags = [Int: [Int]]()
        for i in 0..<n {
            for j in 0..<n {
                diags[i - j, default: []].append(grid[i][j])
            }
        }
        for (k, var v) in diags {
            if k >= 0 { v.sort(by: >) } else { v.sort() }
            diags[k] = v
        }
        var idx = [Int: Int]()
        for i in 0..<n {
            for j in 0..<n {
                let k = i - j
                let pos = idx[k, default: 0]
                grid[i][j] = diags[k]![pos]
                idx[k] = pos + 1
            }
        }
        return grid
    }
}
'''

FILES["3447_assign_elements_to_groups_with_constraints"] = hdr("3447", "Assign Elements to Groups with Constraints", "assign-elements-to-groups-with-constraints") + '''
class Solution {
    func assignElements(_ groups: [Int], _ elements: [Int]) -> [Int] {
        let maxV = 100001
        var first = Array(repeating: -1, count: maxV)
        for i in 0..<elements.count {
            let e = elements[i]
            if e < maxV && first[e] == -1 { first[e] = i }
        }
        var ans = Array(repeating: -1, count: groups.count)
        for gi in 0..<groups.count {
            let g = groups[gi]
            var best = -1
            var d = 1
            while d * d <= g {
                if g % d == 0 {
                    if first[d] != -1 && (best == -1 || first[d] < best) { best = first[d] }
                    let other = g / d
                    if first[other] != -1 && (best == -1 || first[other] < best) { best = first[other] }
                }
                d += 1
            }
            ans[gi] = best
        }
        return ans
    }
}
'''

FILES["3448_count_substrings_divisible_by_last_digit"] = hdr("3448", "Count Substrings Divisible By Last Digit", "count-substrings-divisible-by-last-digit") + '''
class Solution {
    func countSubstrings(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var ans = 0
        for r in 0..<n {
            let last = Int(chars[r].asciiValue! - 48)
            if last == 0 { continue }
            var mod = 0
            var p = 1 % last
            for l in stride(from: r, through: 0, by: -1) {
                mod = (mod + Int(chars[l].asciiValue! - 48) * p) % last
                p = (p * 10) % last
                if mod == 0 { ans += 1 }
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
