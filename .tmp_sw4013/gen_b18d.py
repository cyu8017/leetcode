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

FILES["3477_fruits_into_baskets_ii"] = hdr("3477", "Fruits Into Baskets II", "fruits-into-baskets-ii") + '''
class Solution {
    func numOfUnplacedFruits(_ fruits: [Int], _ baskets: [Int]) -> Int {
        var used = Array(repeating: false, count: baskets.count)
        var unplaced = 0
        for f in fruits {
            var placed = false
            for j in 0..<baskets.count where !used[j] && baskets[j] >= f {
                used[j] = true
                placed = true
                break
            }
            if !placed { unplaced += 1 }
        }
        return unplaced
    }
}
'''

FILES["3478_choose_k_elements_with_maximum_sum"] = hdr("3478", "Choose K Elements With Maximum Sum", "choose-k-elements-with-maximum-sum") + MINHEAP + '''
class Solution {
    func findMaxSum(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> [Int] {
        let n = nums1.count
        var arr = [(Int, Int, Int)]()
        for i in 0..<n { arr.append((nums1[i], nums2[i], i)) }
        arr.sort { $0.0 < $1.0 }
        var ans = Array(repeating: 0, count: n)
        var h = MinHeap()
        var sum = 0
        var i = 0
        while i < n {
            let v = arr[i].0
            let start = i
            while i < n && arr[i].0 == v { i += 1 }
            for t in start..<i { ans[arr[t].2] = sum }
            for t in start..<i {
                h.push(arr[t].1)
                sum += arr[t].1
                if h.count > k { sum -= h.pop() }
            }
        }
        return ans
    }
}
'''

FILES["3479_fruits_into_baskets_iii"] = hdr("3479", "Fruits Into Baskets III", "fruits-into-baskets-iii") + '''
class Solution {
    func numOfUnplacedFruits(_ fruits: [Int], _ baskets: [Int]) -> Int {
        let n = baskets.count
        var size = 1
        while size < n { size <<= 1 }
        var tree = Array(repeating: 0, count: size * 2)
        for i in 0..<n { tree[size + i] = baskets[i] }
        for i in stride(from: size - 1, through: 1, by: -1) {
            tree[i] = max(tree[i * 2], tree[i * 2 + 1])
        }
        func find(_ node: Int, _ nl: Int, _ nr: Int, _ need: Int) -> Int {
            if tree[node] < need { return -1 }
            if nl == nr { return nl }
            let mid = (nl + nr) / 2
            let left = find(node * 2, nl, mid, need)
            if left != -1 { return left }
            return find(node * 2 + 1, mid + 1, nr, need)
        }
        func update(_ idx: Int) {
            var p = size + idx
            tree[p] = -1
            p >>= 1
            while p > 0 {
                tree[p] = max(tree[p * 2], tree[p * 2 + 1])
                p >>= 1
            }
        }
        var unplaced = 0
        for f in fruits {
            let idx = find(1, 0, size - 1, f)
            if idx == -1 || idx >= n { unplaced += 1 }
            else { update(idx) }
        }
        return unplaced
    }
}
'''

FILES["3480_maximize_subarrays_after_removing_one_conflicting_pair"] = hdr("3480", "Maximize Subarrays After Removing One Conflicting Pair", "maximize-subarrays-after-removing-one-conflicting-pair") + '''
class Solution {
    func maxSubarrays(_ n: Int, _ conflictingPairs: [[Int]]) -> Int {
        let m = conflictingPairs.count
        var best = 0
        for skip in 0..<m {
            var rightLimit = Array(repeating: n + 1, count: n + 2)
            for i in 0..<m where i != skip {
                var a = conflictingPairs[i][0], b = conflictingPairs[i][1]
                if a > b { swap(&a, &b) }
                if b < rightLimit[a] { rightLimit[a] = b }
            }
            var minRight = n + 1
            var cnt = 0
            for l in stride(from: n, through: 1, by: -1) {
                if rightLimit[l] < minRight { minRight = rightLimit[l] }
                cnt += minRight - l
            }
            if cnt > best { best = cnt }
        }
        return best
    }
}
'''

FILES["3481_apply_substitutions"] = hdr("3481", "Apply Substitutions", "apply-substitutions") + '''
class Solution {
    func applySubstitutions(_ replacements: [[String]], _ text: String) -> String {
        var mp = [String: String]()
        for r in replacements { mp[r[0]] = r[1] }
        func resolve(_ s: String) -> String {
            let chars = Array(s)
            var out = ""
            var i = 0
            while i < chars.count {
                if chars[i] == "%" {
                    var j = i + 1
                    while j < chars.count && chars[j] != "%" { j += 1 }
                    let key = String(chars[(i + 1)..<j])
                    out += resolve(mp[key] ?? "")
                    i = j + 1
                } else {
                    out.append(chars[i])
                    i += 1
                }
            }
            return out
        }
        return resolve(text)
    }
}
'''

FILES["3483_unique_3_digit_even_numbers"] = hdr("3483", "Unique 3-Digit Even Numbers", "unique-3-digit-even-numbers") + '''
class Solution {
    func totalNumbers(_ digits: [Int]) -> Int {
        var seen = Set<Int>()
        let n = digits.count
        for i in 0..<n {
            for j in 0..<n where j != i {
                for k in 0..<n where k != i && k != j {
                    if digits[i] == 0 { continue }
                    if digits[k] % 2 != 0 { continue }
                    seen.insert(digits[i] * 100 + digits[j] * 10 + digits[k])
                }
            }
        }
        return seen.count
    }
}
'''

FILES["3484_design_spreadsheet"] = hdr("3484", "Design Spreadsheet", "design-spreadsheet") + '''
class Spreadsheet {
    private var cells = [String: Int]()

    init(_ rows: Int) {}

    func setCell(_ cell: String, _ value: Int) { cells[cell] = value }

    func resetCell(_ cell: String) { cells.removeValue(forKey: cell) }

    func getValue(_ formula: String) -> Int {
        var formula = formula
        if !formula.isEmpty && formula.first == "=" { formula.removeFirst() }
        var sum = 0
        var start = formula.startIndex
        while start < formula.endIndex {
            let plus = formula[start...].firstIndex(of: "+")
            let p = plus == nil ? String(formula[start...]) : String(formula[start..<plus!])
            var isNum = !p.isEmpty && (p.first!.isNumber || (p.first == "-" && p.count > 1))
            if isNum {
                for ch in p.dropFirst() where !ch.isNumber { isNum = false; break }
            }
            if isNum { sum += Int(p) ?? 0 }
            else { sum += cells[p, default: 0] }
            if plus == nil { break }
            start = formula.index(after: plus!)
        }
        return sum
    }
}
'''

FILES["3485_longest_common_prefix_of_k_strings_after_removal"] = hdr("3485", "Longest Common Prefix of K Strings After Removal", "longest-common-prefix-of-k-strings-after-removal") + '''
class Solution {
    func longestCommonPrefix(_ words: [String], _ k: Int) -> [Int] {
        let n = words.count
        var ans = Array(repeating: 0, count: n)
        for i in 0..<n {
            var rest = [String]()
            for j in 0..<n where j != i { rest.append(words[j]) }
            if rest.count < k { ans[i] = 0; continue }
            rest.sort()
            var best = 0
            if rest.count >= k {
                for j in 0...(rest.count - k) {
                    best = max(best, lcpOf(Array(rest[j..<(j + k)])))
                }
            }
            ans[i] = best
        }
        return ans
    }

    private func lcpOf(_ a: [String]) -> Int {
        if a.isEmpty { return 0 }
        var pref = Array(a[0])
        for t in 1..<a.count {
            let s = Array(a[t])
            var i = 0
            while i < pref.count && i < s.count && pref[i] == s[i] { i += 1 }
            pref = Array(pref[..<i])
            if pref.isEmpty { return 0 }
        }
        return pref.count
    }
}
'''

FILES["3486_longest_special_path_ii"] = hdr("3486", "Longest Special Path II", "longest-special-path-ii") + '''
class Solution {
    func longestSpecialPath(_ edges: [[Int]], _ nums: [Int]) -> [Int] {
        let n = nums.count
        var g = Array(repeating: [(Int, Int)](), count: n)
        for e in edges {
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        }
        var bestLen = 0, bestNodes = 1
        func dfs(_ u: Int, _ p: Int, _ dist: Int, _ pathVals: inout [Int], _ pathDist: inout [Int]) {
            pathVals.append(nums[u])
            pathDist.append(dist)
            var freq = [Int: Int]()
            var dups = 0, left = 0
            for right in 0..<pathVals.count {
                let v = pathVals[right]
                freq[v, default: 0] += 1
                if freq[v] == 2 { dups += 1 }
                while dups > 1 {
                    let lv = pathVals[left]
                    if freq[lv] == 2 { dups -= 1 }
                    freq[lv]! -= 1
                    left += 1
                }
            }
            let length = dist - pathDist[left]
            let nodes = pathVals.count - left
            if length > bestLen || (length == bestLen && nodes < bestNodes) {
                bestLen = length
                bestNodes = nodes
            }
            for (v, w) in g[u] where v != p {
                dfs(v, u, dist + w, &pathVals, &pathDist)
            }
            pathVals.removeLast()
            pathDist.removeLast()
        }
        var pv = [Int](), pd = [Int]()
        dfs(0, -1, 0, &pv, &pd)
        return [bestLen, bestNodes]
    }
}
'''

FILES["3487_maximum_unique_subarray_sum_after_deletion"] = hdr("3487", "Maximum Unique Subarray Sum After Deletion", "maximum-unique-subarray-sum-after-deletion") + '''
class Solution {
    func maxSum(_ nums: [Int]) -> Int {
        var seen = Set<Int>()
        var sum = 0
        var hasPos = false
        var maxNeg = Int(-1e9)
        for x in nums {
            if x < 0 {
                if x > maxNeg { maxNeg = x }
                continue
            }
            hasPos = true
            if seen.insert(x).inserted { sum += x }
        }
        return hasPos ? sum : maxNeg
    }
}
'''

FILES["3488_closest_equal_element_queries"] = hdr("3488", "Closest Equal Element Queries", "closest-equal-element-queries") + '''
class Solution {
    func solveQueries(_ nums: [Int], _ queries: [Int]) -> [Int] {
        let n = nums.count
        var pos = [Int: [Int]]()
        for i in 0..<n { pos[nums[i], default: []].append(i) }
        var ans = Array(repeating: 0, count: queries.count)
        for qi in 0..<queries.count {
            let idx = queries[qi]
            let arr = pos[nums[idx]]!
            if arr.count == 1 { ans[qi] = -1; continue }
            var best = n
            for p in arr where p != idx {
                var d = abs(p - idx)
                d = min(d, n - d)
                if d < best { best = d }
            }
            ans[qi] = best
        }
        return ans
    }
}
'''

FILES["3489_zero_array_transformation_iv"] = hdr("3489", "Zero Array Transformation IV", "zero-array-transformation-iv") + '''
class Solution {
    func minZeroArray(_ nums: [Int], _ queries: [[Int]]) -> Int {
        if ok(nums, queries, 0) { return 0 }
        var lo = 1, hi = queries.count + 1
        while lo < hi {
            let mid = (lo + hi) / 2
            if mid <= queries.count && ok(nums, queries, mid) { hi = mid }
            else { lo = mid + 1 }
        }
        return lo > queries.count ? -1 : lo
    }

    private func canSubsetSum(_ vals: [Int], _ target: Int) -> Bool {
        if target == 0 { return true }
        var dp = Array(repeating: false, count: target + 1)
        dp[0] = true
        for v in vals {
            for s in stride(from: target, through: v, by: -1) where dp[s - v] { dp[s] = true }
        }
        return dp[target]
    }

    private func ok(_ nums: [Int], _ queries: [[Int]], _ k: Int) -> Bool {
        for i in 0..<nums.count {
            if nums[i] == 0 { continue }
            var vals = [Int]()
            for q in 0..<k {
                if queries[q][0] <= i && i <= queries[q][1] { vals.append(queries[q][2]) }
            }
            if !canSubsetSum(vals, nums[i]) { return false }
        }
        return true
    }
}
'''

FILES["3490_count_beautiful_numbers"] = hdr("3490", "Count Beautiful Numbers", "count-beautiful-numbers") + '''
class Solution {
    func beautifulNumbers(_ l: Int, _ r: Int) -> Int {
        return countBeautiful(r) - countBeautiful(l - 1)
    }

    private func countBeautiful(_ n: Int) -> Int {
        if n <= 0 { return 0 }
        let s = Array(String(n))
        func dfs(_ pos: Int, _ tight: Bool, _ sum: Int, _ prod: Int, _ started: Bool) -> Int {
            if pos == s.count {
                if !started { return 0 }
                return (sum > 0 && prod % sum == 0) ? 1 : 0
            }
            let up = tight ? Int(s[pos].asciiValue! - 48) : 9
            var ans = 0
            for d in 0...up {
                let nt = tight && d == up
                if !started && d == 0 { ans += dfs(pos + 1, nt, 0, 1, false) }
                else {
                    let ns = sum + d
                    let np = !started ? d : prod * d
                    ans += dfs(pos + 1, nt, ns, np, true)
                }
            }
            return ans
        }
        return dfs(0, true, 0, 1, false)
    }
}
'''

FILES["3491_phone_number_prefix"] = hdr("3491", "Phone Number Prefix", "phone-number-prefix") + '''
class Solution {
    func phonePrefix(_ numbers: [String]) -> Bool {
        let numbers = numbers.sorted()
        if numbers.count >= 2 {
            for i in 0..<(numbers.count - 1) {
                if numbers[i].count <= numbers[i + 1].count && numbers[i + 1].hasPrefix(numbers[i]) {
                    return false
                }
            }
        }
        return true
    }
}
'''

FILES["3492_maximum_containers_on_a_ship"] = hdr("3492", "Maximum Containers on a Ship", "maximum-containers-on-a-ship") + '''
class Solution {
    func maxContainers(_ n: Int, _ w: Int, _ maxWeight: Int) -> Int {
        let cap = n * n
        let byW = maxWeight / w
        return min(cap, byW)
    }
}
'''

FILES["3493_properties_graph"] = hdr("3493", "Properties Graph", "properties-graph") + '''
class Solution {
    func numberOfComponents(_ properties: [[Int]], _ k: Int) -> Int {
        let n = properties.count
        var sets = properties.map { Set($0) }
        var parent = Array(0..<n)
        func find(_ x: Int) -> Int {
            if parent[x] != x { parent[x] = find(parent[x]) }
            return parent[x]
        }
        func unite(_ a: Int, _ b: Int) {
            let ra = find(a), rb = find(b)
            if ra != rb { parent[ra] = rb }
        }
        for i in 0..<n {
            for j in (i + 1)..<n {
                var cnt = 0
                for v in sets[i] where sets[j].contains(v) { cnt += 1 }
                if cnt >= k { unite(i, j) }
            }
        }
        return Set((0..<n).map { find($0) }).count
    }
}
'''

FILES["3494_find_the_minimum_amount_of_time_to_brew_potions"] = hdr("3494", "Find the Minimum Amount of Time to Brew Potions", "find-the-minimum-amount-of-time-to-brew-potions") + '''
class Solution {
    func minTime(_ skill: [Int], _ mana: [Int]) -> Int {
        let n = skill.count, m = mana.count
        var done = Array(repeating: 0, count: n)
        for j in 0..<m {
            var t = 0
            for i in 0..<n {
                if done[i] > t { t = done[i] }
                t += skill[i] * mana[j]
                done[i] = t
            }
            for i in stride(from: n - 2, through: 0, by: -1) {
                done[i] = done[i + 1] - skill[i + 1] * mana[j]
            }
        }
        return done[n - 1]
    }
}
'''

FILES["3495_minimum_operations_to_make_array_elements_zero"] = hdr("3495", "Minimum Operations to Make Array Elements Zero", "minimum-operations-to-make-array-elements-zero") + '''
class Solution {
    func minOperations(_ queries: [[Int]]) -> Int {
        var ans = 0
        for q in queries {
            var sum = 0
            for x in q[0]...q[1] { sum += opsToZero(x) }
            ans += (sum + 1) / 2
        }
        return ans
    }

    private func opsToZero(_ x: Int) -> Int {
        var x = x, ops = 0
        while x > 0 { x /= 4; ops += 1 }
        return ops
    }
}
'''

FILES["3496_maximize_score_after_pair_deletions"] = hdr("3496", "Maximize Score After Pair Deletions", "maximize-score-after-pair-deletions") + '''
class Solution {
    func maximizeScore(_ nums: [Int]) -> Int {
        let n = nums.count
        let total = nums.reduce(0, +)
        if n % 2 == 1 { return total - (nums.min() ?? 0) }
        var mn = nums[0] + nums[1]
        for i in 0..<(n - 1) { mn = min(mn, nums[i] + nums[i + 1]) }
        return total - mn
    }
}
'''

FILES["3498_reverse_degree_of_a_string"] = hdr("3498", "Reverse Degree of a String", "reverse-degree-of-a-string") + '''
class Solution {
    func reverseDegree(_ s: String) -> Int {
        var ans = 0
        for (i, c) in s.enumerated() {
            ans += (26 - Int(c.asciiValue! - 97)) * (i + 1)
        }
        return ans
    }
}
'''

FILES["3499_maximize_active_section_with_trade_i"] = hdr("3499", "Maximize Active Section with Trade I", "maximize-active-section-with-trade-i") + '''
class Solution {
    func maxActiveSectionsAfterTrade(_ s: String) -> Int {
        let chars = Array(s)
        var ones = 0
        for c in chars where c == "1" { ones += 1 }
        var zeros = [[Int]]()
        let n = chars.count
        var i = 0
        while i < n {
            if chars[i] != "0" { i += 1; continue }
            var j = i
            while j < n && chars[j] == "0" { j += 1 }
            zeros.append([i, j - 1])
            i = j
        }
        var best = 0
        if zeros.count >= 2 {
            for i in 0..<(zeros.count - 1) {
                let gain = (zeros[i][1] - zeros[i][0] + 1) + (zeros[i + 1][1] - zeros[i + 1][0] + 1)
                if gain > best { best = gain }
            }
        }
        return ones + best
    }
}
'''

FILES["3500_minimum_cost_to_divide_array_into_subarrays"] = hdr("3500", "Minimum Cost to Divide Array Into Subarrays", "minimum-cost-to-divide-array-into-subarrays") + '''
class Solution {
    func minimumCost(_ nums: [Int], _ cost: [Int], _ k: Int) -> Int {
        let n = nums.count
        var pn = Array(repeating: 0, count: n + 1)
        var pc = Array(repeating: 0, count: n + 1)
        for i in 0..<n {
            pn[i + 1] = pn[i] + nums[i]
            pc[i + 1] = pc[i] + cost[i]
        }
        let inf = 1 << 62
        var dp = Array(repeating: inf, count: n + 1)
        dp[n] = 0
        for i in stride(from: n - 1, through: 0, by: -1) {
            for j in i..<n {
                let cand = pn[j + 1] * (pc[j + 1] - pc[i]) + k * (pc[n] - pc[i]) + dp[j + 1]
                if cand < dp[i] { dp[i] = cand }
            }
        }
        return dp[0]
    }
}
'''

FILES["3501_maximize_active_section_with_trade_ii"] = hdr("3501", "Maximize Active Section with Trade II", "maximize-active-section-with-trade-ii") + '''
class Solution {
    func maxActiveSectionsAfterTrade(_ s: String, _ queries: [[Int]]) -> [Int] {
        let chars = Array(s)
        var ones = 0
        for c in chars where c == "1" { ones += 1 }
        var zeros = [[Int]]()
        let n = chars.count
        var i = 0
        while i < n {
            if chars[i] != "0" { i += 1; continue }
            var j = i
            while j < n && chars[j] == "0" { j += 1 }
            zeros.append([i, j - 1])
            i = j
        }
        var ans = Array(repeating: ones, count: queries.count)
        for qi in 0..<queries.count {
            let L = queries[qi][0], R = queries[qi][1]
            var best = 0
            if zeros.count >= 2 {
                for i in 0..<(zeros.count - 1) {
                    let a = zeros[i], b = zeros[i + 1]
                    if a[0] >= L && b[1] <= R {
                        let gain = (a[1] - a[0] + 1) + (b[1] - b[0] + 1)
                        if gain > best { best = gain }
                    }
                }
            }
            ans[qi] = ones + best
        }
        return ans
    }
}
'''

FILES["3502_minimum_cost_to_reach_every_position"] = hdr("3502", "Minimum Cost to Reach Every Position", "minimum-cost-to-reach-every-position") + '''
class Solution {
    func minCosts(_ cost: [Int]) -> [Int] {
        var ans = Array(repeating: 0, count: cost.count)
        var mi = cost[0]
        for i in 0..<cost.count {
            mi = min(mi, cost[i])
            ans[i] = mi
        }
        return ans
    }
}
'''

FILES["3503_longest_palindrome_after_substring_concatenation_i"] = hdr("3503", "Longest Palindrome After Substring Concatenation I", "longest-palindrome-after-substring-concatenation-i") + '''
class Solution {
    func longestPalindrome(_ s: String, _ t: String) -> Int {
        let s = Array(s)
        var t = Array(t).reversed() as [Character]
        let m = s.count, n = t.count
        func calc(_ str: [Character]) -> [Int] {
            let nn = str.count
            var g = Array(repeating: 0, count: nn)
            func expand(_ l0: Int, _ r0: Int) {
                var l = l0, r = r0
                while l >= 0 && r < nn && str[l] == str[r] {
                    g[l] = max(g[l], r - l + 1)
                    l -= 1; r += 1
                }
            }
            for i in 0..<nn {
                expand(i, i)
                expand(i, i + 1)
            }
            return g
        }
        let g1 = calc(s), g2 = calc(t)
        var ans = 0
        for v in g1 { ans = max(ans, v) }
        for v in g2 { ans = max(ans, v) }
        var f = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        if m >= 1 && n >= 1 {
            for i in 1...m {
                for j in 1...n {
                    if s[i - 1] == t[j - 1] {
                        f[i][j] = f[i - 1][j - 1] + 1
                        let a = i < m ? g1[i] : 0
                        let b = j < n ? g2[j] : 0
                        ans = max(ans, f[i][j] * 2 + a)
                        ans = max(ans, f[i][j] * 2 + b)
                    }
                }
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
