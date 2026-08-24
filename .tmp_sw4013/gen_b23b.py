from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def hdr(num, title, slug):
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n\n"

def write(folder, content):
    p = ROOT / folder / "Solution.swift"
    p.write_text(content)
    print("W", folder)

FILES = {}

FILES["3938_maximum_path_intersection_sum_in_a_grid"] = hdr("3938", "Maximum Path Intersection Sum in a Grid", "maximum-path-intersection-sum-in-a-grid") + r'''
class Solution {
    func maxPathSum(_ grid: [[Int]]) -> Int {
        let rows = grid.count, cols = grid[0].count
        var answer = Int.min
        for row in 0..<rows {
            answer = max(answer, checkLine(cols) { grid[row][$0] })
        }
        for col in 0..<cols {
            answer = max(answer, checkLine(rows) { grid[$0][col] })
        }
        if rows > 2 && cols > 2 {
            for row in 1..<(rows - 1) {
                for col in 1..<(cols - 1) {
                    if grid[row][col] > answer { answer = grid[row][col] }
                }
            }
        }
        return answer
    }

    private func checkLine(_ length: Int, _ value: (Int) -> Int) -> Int {
        var answer = Int.min
        var bestEnding = value(0) + value(1)
        if bestEnding > answer { answer = bestEnding }
        if length > 2 {
            for i in 2..<length {
                if value(i - 1) + value(i) > bestEnding + value(i) {
                    bestEnding = value(i - 1) + value(i)
                } else {
                    bestEnding += value(i)
                }
                if bestEnding > answer { answer = bestEnding }
            }
        }
        return answer
    }
}
'''

FILES["3939_count_non_adjacent_subsets_in_a_rooted_tree"] = hdr("3939", "Count Non Adjacent Subsets in a Rooted Tree", "count-non-adjacent-subsets-in-a-rooted-tree") + r'''
class Solution {
    func countNonAdjacentSubsets(_ parent: [Int], _ nums: [Int], _ k: Int) -> Int {
        let mod = 1_000_000_007
        let n = parent.count
        var children = Array(repeating: [Int](), count: n)
        for i in 1..<n { children[parent[i]].append(i) }
        var dp0 = Array(repeating: [Int](), count: n)
        var dp1 = Array(repeating: [Int](), count: n)
        for u in stride(from: n - 1, through: 0, by: -1) {
            var a = Array(repeating: 0, count: k)
            var b = Array(repeating: 0, count: k)
            a[0] = 1
            b[((nums[u] % k) + k) % k] = 1
            for v in children[u] {
                var na = Array(repeating: 0, count: k)
                var nb = Array(repeating: 0, count: k)
                for x in 0..<k {
                    for y in 0..<k {
                        let allChild = (dp0[v][y] + dp1[v][y]) % mod
                        na[(x + y) % k] = (na[(x + y) % k] + a[x] * allChild) % mod
                        nb[(x + y) % k] = (nb[(x + y) % k] + b[x] * dp0[v][y]) % mod
                    }
                }
                a = na
                b = nb
            }
            dp0[u] = a
            dp1[u] = b
        }
        var ans = (dp0[0][0] + dp1[0][0] - 1) % mod
        if ans < 0 { ans += mod }
        return ans
    }
}
'''

FILES["3940_limit_occurrences_in_sorted_array"] = hdr("3940", "Limit Occurrences in Sorted Array", "limit-occurrences-in-sorted-array") + r'''
class Solution {
    func limitOccurrences(_ nums: [Int], _ k: Int) -> [Int] {
        if nums.isEmpty { return [] }
        var nums = nums
        var cnt = 1, l = 1
        for r in 1..<nums.count {
            if nums[r] != nums[r - 1] { cnt = 1 }
            else { cnt += 1 }
            if cnt <= k {
                nums[l] = nums[r]
                l += 1
            }
        }
        return Array(nums.prefix(l))
    }
}
'''

FILES["3941_password_strength"] = hdr("3941", "Password Strength", "password-strength") + r'''
class Solution {
    func passwordStrength(_ password: String) -> Int {
        var st = Set<Character>()
        for ch in password { st.insert(ch) }
        var ans = 0
        for ch in st {
            if ch.isLowercase { ans += 1 }
            else if ch.isUppercase { ans += 2 }
            else if ch.isNumber { ans += 3 }
            else { ans += 5 }
        }
        return ans
    }
}
'''

FILES["3942_minimum_operations_to_sort_a_permutation"] = hdr("3942", "Minimum Operations to Sort a Permutation", "minimum-operations-to-sort-a-permutation") + r'''
class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        let n = nums.count
        var zero = 0
        for i in 0..<n {
            if nums[i] == 0 { zero = i; break }
        }
        var ans = Int.max
        if check(nums, zero, 1) {
            ans = min(ans, zero)
            ans = min(ans, n - zero + 2)
        }
        if check(nums, zero, -1) {
            ans = min(ans, zero + 2)
            ans = min(ans, n - zero)
        }
        return ans == Int.max ? -1 : ans
    }

    private func check(_ nums: [Int], _ zero: Int, _ step: Int) -> Bool {
        let n = nums.count
        for i in 1..<n {
            let prev = ((zero + (i - 1) * step) % n + n) % n
            let curr = ((zero + i * step) % n + n) % n
            if nums[prev] > nums[curr] { return false }
        }
        return true
    }
}
'''

FILES["3943_number_of_pairs_after_increment"] = hdr("3943", "Number of Pairs After Increment", "number-of-pairs-after-increment") + r'''
class Solution {
    func numberOfPairs(_ nums1: [Int], _ nums2: [Int], _ queries: [[Int]]) -> [Int] {
        let blockSize = 225
        var nums2 = nums2
        let n = nums2.count
        let blocks = (n + blockSize - 1) / blockSize
        var lazy = Array(repeating: 0, count: max(blocks, 1))
        var freq = Array(repeating: [Int: Int](), count: max(blocks, 1))
        func rebuild(_ b: Int) {
            freq[b].removeAll()
            let end = min((b + 1) * blockSize, n)
            if b * blockSize < end {
                for i in (b * blockSize)..<end {
                    freq[b][nums2[i], default: 0] += 1
                }
            }
        }
        func push(_ b: Int) {
            if lazy[b] != 0 {
                let end = min((b + 1) * blockSize, n)
                if b * blockSize < end {
                    for i in (b * blockSize)..<end { nums2[i] += lazy[b] }
                }
                lazy[b] = 0
            }
        }
        if n > 0 {
            for b in 0..<blocks { rebuild(b) }
        }
        var fixed = [Int: Int]()
        for x in nums1 { fixed[x, default: 0] += 1 }
        var answer = [Int]()
        for q in queries {
            if q[0] == 1 {
                let l = q[1], r = q[2], delta = q[3]
                let first = l / blockSize, last = r / blockSize
                if first == last {
                    push(first)
                    for i in l...r { nums2[i] += delta }
                    rebuild(first)
                    continue
                }
                push(first)
                for i in l..<((first + 1) * blockSize) { nums2[i] += delta }
                rebuild(first)
                push(last)
                for i in (last * blockSize)...r { nums2[i] += delta }
                rebuild(last)
                if first + 1 < last {
                    for b in (first + 1)..<last { lazy[b] += delta }
                }
            } else {
                var total = 0
                for (a, countA) in fixed {
                    let target = q[1] - a
                    for b in 0..<blocks {
                        if let c = freq[b][target - lazy[b]] {
                            total += countA * c
                        }
                    }
                }
                answer.append(total)
            }
        }
        return answer
    }
}
'''

FILES["3944_minimum_operations_to_make_array_modulo_alternating_ii"] = hdr("3944", "Minimum Operations to Make Array Modulo Alternating II", "minimum-operations-to-make-array-modulo-alternating-ii") + r'''
class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        var evenFreq = Array(repeating: 0, count: k)
        var oddFreq = Array(repeating: 0, count: k)
        for i in 0..<nums.count {
            if i % 2 == 0 { evenFreq[nums[i] % k] += 1 }
            else { oddFreq[nums[i] % k] += 1 }
        }
        let evenCost = costs(evenFreq, k)
        let oddCost = costs(oddFreq, k)
        var best1 = Int.max / 4, best2 = Int.max / 4
        var bestIndex = -1
        for i in 0..<k {
            let x = oddCost[i]
            if x < best1 {
                best2 = best1
                best1 = x
                bestIndex = i
            } else if x < best2 {
                best2 = x
            }
        }
        var ans = Int.max / 4
        for x in 0..<k {
            let other = (x == bestIndex) ? best2 : best1
            ans = min(ans, evenCost[x] + other)
        }
        return ans
    }

    private func costs(_ freq: [Int], _ k: Int) -> [Int] {
        var dbl = Array(repeating: 0, count: 2 * k)
        for i in 0..<(2 * k) { dbl[i] = freq[i % k] }
        var countPrefix = Array(repeating: 0, count: 2 * k + 1)
        var weightedPrefix = Array(repeating: 0, count: 2 * k + 1)
        for i in 0..<(2 * k) {
            countPrefix[i + 1] = countPrefix[i] + dbl[i]
            weightedPrefix[i + 1] = weightedPrefix[i] + i * dbl[i]
        }
        var res = Array(repeating: 0, count: k)
        let cw = k / 2, cc = (k - 1) / 2
        for t in 0..<k {
            let cnt = countPrefix[t + cw + 1] - countPrefix[t]
            let sum = weightedPrefix[t + cw + 1] - weightedPrefix[t]
            res[t] += sum - t * cnt
            if cc > 0 {
                let cnt2 = countPrefix[t + k] - countPrefix[t + k - cc]
                let sum2 = weightedPrefix[t + k] - weightedPrefix[t + k - cc]
                res[t] += (t + k) * cnt2 - sum2
            }
        }
        return res
    }
}
'''

FILES["3945_digit_frequency_score"] = hdr("3945", "Digit Frequency Score", "digit-frequency-score") + r'''
class Solution {
    func digitFrequencyScore(_ n: Int) -> Int {
        var n = n, ans = 0
        while n > 0 {
            ans += n % 10
            n /= 10
        }
        return ans
    }
}
'''

FILES["3946_maximum_number_of_items_from_sale_i"] = hdr("3946", "Maximum Number of Items From Sale I", "maximum-number-of-items-from-sale-i") + r'''
class Solution {
    func maximumSaleItems(_ items: [[Int]], _ budget: Int) -> Int {
        var f = Array(repeating: 0, count: budget + 1)
        var mn = Int.max
        for item in items {
            let factor = item[0], price = item[1]
            mn = min(mn, price)
            var cnt = 0
            for jItem in items {
                if jItem[0] % factor == 0 { cnt += 1 }
            }
            if price <= budget {
                for j in stride(from: budget, through: price, by: -1) {
                    f[j] = max(f[j], f[j - price] + cnt)
                }
            }
        }
        var ans = 0
        for i in 0...budget {
            let extra = mn == 0 ? 0 : (budget - i) / mn
            ans = max(ans, f[i] + extra)
        }
        return ans
    }
}
'''

FILES["3947_maximum_number_of_items_from_sale_ii"] = hdr("3947", "Maximum Number of Items From Sale II", "maximum-number-of-items-from-sale-ii") + r'''
class Solution {
    func maxItems(_ items: [[Int]], _ budget: Int) -> Int {
        let n = items.count
        var frequency = Array(repeating: 0, count: n + 1)
        var minimumPrice = items[0][1]
        for item in items {
            frequency[item[0]] += 1
            minimumPrice = min(minimumPrice, item[1])
        }
        var batches = [(Int, Int)]()
        for item in items {
            var gain = 0
            var multiple = item[0]
            while multiple <= n {
                gain += frequency[multiple]
                multiple += item[0]
            }
            gain -= 1
            if gain > 0 && item[1] < 2 * minimumPrice {
                batches.append((item[1], gain))
            }
        }
        batches.sort { $0.0 < $1.0 }
        var remaining = budget
        var answer = budget / minimumPrice
        var boosted = 0
        for current in batches {
            var count = current.1
            let affordable = remaining / current.0
            if affordable < count { count = affordable }
            remaining -= count * current.0
            boosted += count
            let total = 2 * boosted + remaining / minimumPrice
            if total > answer { answer = total }
            if count < current.1 { break }
        }
        return answer
    }
}
'''

FILES["3948_lexicographically_maximum_mex_array"] = hdr("3948", "Lexicographically Maximum MEX Array", "lexicographically-maximum-mex-array") + r'''
class Solution {
    func maxMexArray(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var remaining = Array(repeating: 0, count: n + 2)
        for x in nums {
            if x <= n + 1 { remaining[x] += 1 }
        }
        var mex = 0
        while remaining[mex] > 0 { mex += 1 }
        var answer = [Int]()
        var seen = Array(repeating: 0, count: n + 2)
        var stamp = 0, index = 0
        while index < n {
            if mex == 0 {
                answer.append(0)
                let x = nums[index]
                if x <= n + 1 { remaining[x] -= 1 }
                index += 1
                continue
            }
            stamp += 1
            var need = mex
            while need > 0 {
                let x = nums[index]
                if x < mex && seen[x] != stamp {
                    seen[x] = stamp
                    need -= 1
                }
                if x <= n + 1 { remaining[x] -= 1 }
                index += 1
            }
            answer.append(mex)
            mex = 0
            while remaining[mex] > 0 { mex += 1 }
        }
        return answer
    }
}
'''

FILES["3949_subtree_inversion_sum_ii"] = hdr("3949", "Subtree Inversion Sum II", "subtree-inversion-sum-ii") + r'''
class Solution {
    func maxSubtreeInversionSum(_ edges: [[Int]], _ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var graph = Array(repeating: [Int](), count: n)
        for edge in edges {
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        }
        var parent = Array(repeating: -2, count: n)
        parent[0] = -1
        var order = [0]
        var i = 0
        while i < order.count {
            let u = order[i]
            for v in graph[u] {
                if parent[v] == -2 {
                    parent[v] = u
                    order.append(v)
                }
            }
            i += 1
        }
        let infinity = Int.max / 4
        var maximum = Array(repeating: [Int](), count: n)
        var minimum = Array(repeating: [Int](), count: n)
        for oi in stride(from: n - 1, through: 0, by: -1) {
            let u = order[oi]
            var currentMax = Array(repeating: -infinity, count: k + 1)
            var currentMin = Array(repeating: infinity, count: k + 1)
            currentMax[k] = nums[u]
            currentMin[k] = nums[u]
            for v in graph[u] {
                if parent[v] != u { continue }
                var nextMax = Array(repeating: -infinity, count: k + 1)
                var nextMin = Array(repeating: infinity, count: k + 1)
                for first in 0...k {
                    if currentMax[first] == -infinity { continue }
                    for childDistance in 0...k {
                        if maximum[v][childDistance] == -infinity { continue }
                        var second = childDistance + 1
                        if second > k { second = k }
                        if first < k && second < k && first + second < k { continue }
                        let distance = min(first, second)
                        let maxValue = currentMax[first] + maximum[v][childDistance]
                        let minValue = currentMin[first] + minimum[v][childDistance]
                        nextMax[distance] = max(nextMax[distance], maxValue)
                        nextMin[distance] = min(nextMin[distance], minValue)
                    }
                }
                currentMax = nextMax
                currentMin = nextMin
            }
            if -currentMin[k] > currentMax[0] { currentMax[0] = -currentMin[k] }
            if -currentMax[k] < currentMin[0] { currentMin[0] = -currentMax[k] }
            maximum[u] = currentMax
            minimum[u] = currentMin
        }
        var answer = -infinity
        for value in maximum[0] { answer = max(answer, value) }
        return answer
    }
}
'''

FILES["3950_exactly_one_consecutive_set_bits_pair"] = hdr("3950", "Exactly One Consecutive Set Bits Pair", "exactly-one-consecutive-set-bits-pair") + r'''
class Solution {
    func consecutiveSetBits(_ n: Int) -> Bool {
        var n = n
        var vis = false
        var pre = 0
        while n > 0 {
            let cur = n & 1
            if pre == cur && cur == 1 {
                if vis { return false }
                vis = true
            }
            pre = cur
            n >>= 1
        }
        return vis
    }
}
'''

FILES["3951_minimum_energy_to_maintain_brightness"] = hdr("3951", "Minimum Energy to Maintain Brightness", "minimum-energy-to-maintain-brightness") + r'''
class Solution {
    func minEnergy(_ n: Int, _ brightness: Int, _ intervals: [[Int]]) -> Int {
        var intervals = intervals.sorted { $0[0] < $1[0] }
        var merged = [[intervals[0][0], intervals[0][1]]]
        for i in 1..<intervals.count {
            let x = intervals[i]
            if merged[merged.count - 1][1] < x[0] {
                merged.append([x[0], x[1]])
            } else if x[1] > merged[merged.count - 1][1] {
                merged[merged.count - 1][1] = x[1]
            }
        }
        var ans = 0
        for interval in merged {
            let m = interval[1] - interval[0] + 1
            ans += ((brightness + 2) / 3) * m
        }
        return ans
    }
}
'''

FILES["3952_maximum_total_value_of_covered_indices"] = hdr("3952", "Maximum Total Value of Covered Indices", "maximum-total-value-of-covered-indices") + r'''
class Solution {
    func maxTotalValue(_ nums: [Int], _ s: String) -> Int {
        let chars = Array(s)
        var answer = 0
        var i = 0
        while i < chars.count {
            if chars[i] == "0" { i += 1; continue }
            let start = i
            while i < chars.count && chars[i] == "1" { i += 1 }
            let end = i - 1
            if start == 0 {
                for index in start...end { answer += nums[index] }
                continue
            }
            var minimum = nums[start - 1]
            var total = 0
            for index in (start - 1)...end {
                total += nums[index]
                if nums[index] < minimum { minimum = nums[index] }
            }
            answer += total - minimum
        }
        return answer
    }
}
'''

FILES["3953_maximum_score_with_co_prime_element"] = hdr("3953", "Maximum Score with Co-Prime Element", "maximum-score-with-co-prime-element") + r'''
class Solution {
    func maxScore(_ nums: [Int], _ maxVal: Int) -> Int {
        var limit = maxVal
        var frequency = Array(repeating: 0, count: 100001)
        for x in nums {
            frequency[x] += 1
            if x > limit { limit = x }
        }
        var divisible = Array(repeating: 0, count: limit + 1)
        for d in 1...limit {
            var multiple = d
            while multiple <= limit {
                if multiple < frequency.count { divisible[d] += frequency[multiple] }
                multiple += d
            }
        }
        var best = -nums.count
        var checked = Array(repeating: false, count: limit + 1)
        func badCount(_ x: Int) -> Int {
            var primes = [Int]()
            var y = x
            var p = 2
            while p * p <= y {
                if y % p == 0 {
                    primes.append(p)
                    while y % p == 0 { y /= p }
                }
                p += 1
            }
            if y > 1 { primes.append(y) }
            var bad = 0
            let psz = primes.count
            for mask in 1..<(1 << psz) {
                var product = 1, bits = 0
                for i in 0..<psz {
                    if ((mask >> i) & 1) != 0 {
                        product *= primes[i]
                        bits += 1
                    }
                }
                if bits % 2 == 1 { bad += divisible[product] }
                else { bad -= divisible[product] }
            }
            return bad
        }
        func evaluate(_ x: Int, _ exists: Bool) -> Int {
            if checked[x] { return Int.min / 4 }
            checked[x] = true
            let bad = badCount(x)
            let cost: Int
            if exists { cost = x > 1 ? bad - 1 : 0 }
            else { cost = bad > 0 ? bad : 1 }
            return x - cost
        }
        for x in 1...maxVal {
            best = max(best, evaluate(x, x < frequency.count && frequency[x] > 0))
        }
        for x in nums {
            best = max(best, evaluate(x, true))
        }
        return best
    }
}
'''

FILES["3954_sum_of_compatible_numbers_in_range_i"] = hdr("3954", "Sum of Compatible Numbers in Range I", "sum-of-compatible-numbers-in-range-i") + r'''
class Solution {
    func sumOfGoodIntegers(_ n: Int, _ k: Int) -> Int {
        let start = max(1, n - k)
        let end = n + k
        var ans = 0
        for x in start...end {
            if (n & x) == 0 { ans += x }
        }
        return ans
    }
}
'''

FILES["3955_valid_binary_strings_with_cost_limit"] = hdr("3955", "Valid Binary Strings With Cost Limit", "valid-binary-strings-with-cost-limit") + r'''
class Solution {
    func generateValidStrings(_ n: Int, _ k: Int) -> [String] {
        var ans = [String]()
        var path = [Character]()
        func dfs(_ i: Int, _ tot: Int) {
            if i >= n {
                ans.append(String(path))
                return
            }
            path.append("0")
            dfs(i + 1, tot)
            path.removeLast()
            if (path.isEmpty || path.last == "0") && tot + i <= k {
                path.append("1")
                dfs(i + 1, tot + i)
                path.removeLast()
            }
        }
        dfs(0, 0)
        return ans
    }
}
'''

FILES["3956_maximum_sum_of_m_non_overlapping_subarrays_i"] = hdr("3956", "Maximum Sum of M Non-Overlapping Subarrays I", "maximum-sum-of-m-non-overlapping-subarrays-i") + r'''
class Solution {
    func maxSum(_ nums: [Int], _ m: Int, _ l: Int, _ r: Int) -> Int {
        let n = nums.count
        var prefix = Array(repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + nums[i] }
        var dp = Array(repeating: 0, count: n + 1)
        var bestSelected = -(Int.max / 4)
        for _ in 1...m {
            var next = dp
            var deque = [Int]()
            for end in 1...n {
                let addIndex = end - l
                if addIndex >= 0 {
                    let value = dp[addIndex] - prefix[addIndex]
                    while !deque.isEmpty {
                        let last = deque[deque.count - 1]
                        if dp[last] - prefix[last] > value { break }
                        deque.removeLast()
                    }
                    deque.append(addIndex)
                }
                let minIndex = end - r
                while !deque.isEmpty && deque[0] < minIndex { deque.removeFirst() }
                if !deque.isEmpty {
                    let candidate = prefix[end] + dp[deque[0]] - prefix[deque[0]]
                    if candidate > next[end] { next[end] = candidate }
                    if candidate > bestSelected { bestSelected = candidate }
                }
                if next[end - 1] > next[end] { next[end] = next[end - 1] }
            }
            dp = next
        }
        return bestSelected
    }
}
'''

FILES["3957_maximum_sum_of_m_non_overlapping_subarrays_ii"] = hdr("3957", "Maximum Sum of M Non-Overlapping Subarrays II", "maximum-sum-of-m-non-overlapping-subarrays-ii") + r'''
class Solution {
    private struct State {
        var value: Int
        var count: Int
        init() { value = 0; count = 0 }
        init(_ value: Int, _ count: Int) { self.value = value; self.count = count }
    }

    private func better(_ a: State, _ b: State) -> Bool {
        a.value > b.value || (a.value == b.value && a.count > b.count)
    }

    func maxSum(_ nums: [Int], _ m: Int, _ l: Int, _ r: Int) -> Int {
        let n = nums.count
        var prefix = Array(repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + nums[i] }
        let unconstrained = run(prefix, n, l, r, 0)
        if unconstrained.count > 0 && unconstrained.count <= m { return unconstrained.value }
        if unconstrained.count > m {
            var bound = 0
            for value in nums { bound += value >= 0 ? value : -value }
            var low = 0, high = bound + 1
            while low < high {
                let mid = low + (high - low + 1) / 2
                if run(prefix, n, l, r, mid).count >= m { low = mid }
                else { high = mid - 1 }
            }
            let state = run(prefix, n, l, r, low)
            return state.value + low * m
        }
        let infinity = Int.max / 4
        var bestSingle = -infinity
        var deque = [Int]()
        for end in 1...n {
            let addIndex = end - l
            if addIndex >= 0 {
                while !deque.isEmpty && prefix[deque.last!] >= prefix[addIndex] { deque.removeLast() }
                deque.append(addIndex)
            }
            let minIndex = end - r
            while !deque.isEmpty && deque[0] < minIndex { deque.removeFirst() }
            if !deque.isEmpty {
                let sum = prefix[end] - prefix[deque[0]]
                if sum > bestSingle { bestSingle = sum }
            }
        }
        return bestSingle
    }

    private func run(_ prefix: [Int], _ n: Int, _ l: Int, _ r: Int, _ penalty: Int) -> State {
        var dp = Array(repeating: State(), count: n + 1)
        var deque = [Int]()
        for end in 1...n {
            let addIndex = end - l
            if addIndex >= 0 {
                while !deque.isEmpty && candidateBetter(dp, prefix, addIndex, deque.last!) { deque.removeLast() }
                deque.append(addIndex)
            }
            let minIndex = end - r
            while !deque.isEmpty && deque[0] < minIndex { deque.removeFirst() }
            dp[end] = State(dp[end - 1].value, dp[end - 1].count)
            if !deque.isEmpty {
                let start = deque[0]
                let take = State(dp[start].value + prefix[end] - prefix[start] - penalty, dp[start].count + 1)
                if better(take, dp[end]) { dp[end] = take }
            }
        }
        return dp[n]
    }

    private func candidateBetter(_ dp: [State], _ prefix: [Int], _ a: Int, _ b: Int) -> Bool {
        let left = State(dp[a].value - prefix[a], dp[a].count)
        let right = State(dp[b].value - prefix[b], dp[b].count)
        return better(left, right)
    }
}
'''

FILES["3958_minimum_cost_to_split_into_ones_ii"] = hdr("3958", "Minimum Cost to Split into Ones II", "minimum-cost-to-split-into-ones-ii") + r'''
class Solution {
    func minCost(_ n: Int) -> Int {
        n * (n - 1) / 2
    }
}
'''

FILES["3959_check_good_integer"] = hdr("3959", "Check Good Integer", "check-good-integer") + r'''
class Solution {
    func checkGoodInteger(_ n: Int) -> Bool {
        var n = n, s = 0
        while n > 0 {
            let x = n % 10
            s += x * (x - 1)
            n /= 10
        }
        return s >= 50
    }
}
'''

FILES["3960_frequency_balance_subarray"] = hdr("3960", "Frequency Balance Subarray", "frequency-balance-subarray") + r'''
class Solution {
    func getLength(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 1
        for l in 0..<n {
            var cnt = [Int: Int]()
            var freq = [Int: Int]()
            for r in l..<n {
                let x = nums[r]
                let c = cnt[x, default: 0]
                if let fc0 = freq[c], fc0 > 0 {
                    let fc = fc0 - 1
                    if fc == 0 { freq.removeValue(forKey: c) }
                    else { freq[c] = fc }
                }
                cnt[x] = c + 1
                freq[cnt[x]!, default: 0] += 1
                let cx = cnt[x]!
                if cnt.count == 1 || (freq.count == 2 && (freq[cx * 2, default: 0] > 0 || (cx % 2 == 0 && freq[cx / 2, default: 0] > 0))) {
                    ans = max(ans, r - l + 1)
                }
            }
        }
        return ans
    }
}
'''

for folder, content in FILES.items():
    write(folder, content)
print("done", len(FILES))
