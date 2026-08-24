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


write("3843_first_element_with_unique_frequency", """// LeetCode 3843 - First Element With Unique Frequency
// https://leetcode.com/problems/first-element-with-unique-frequency/

class Solution {
    func firstUniqueFreq(_ nums: [Int]) -> Int {
        var cnt = [Int: Int]()
        for x in nums { cnt[x, default: 0] += 1 }
        var freq = [Int: Int]()
        for v in cnt.values { freq[v, default: 0] += 1 }
        for x in nums {
            if freq[cnt[x]!] == 1 { return x }
        }
        return -1
    }
}
""")

write("3844_longest_almost_palindromic_substring", """// LeetCode 3844 - Longest Almost Palindromic Substring
// https://leetcode.com/problems/longest-almost-palindromic-substring/

class Solution {
    func almostPalindromic(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var ans = 0
        for i in 0..<n {
            ans = max(ans, max(expand(chars, i, i), expand(chars, i, i + 1)))
        }
        return ans
    }

    private func expand(_ s: [Character], _ l: Int, _ r: Int) -> Int {
        let n = s.count
        var l = l, r = r
        while l >= 0 && r < n && s[l] == s[r] { l -= 1; r += 1 }
        var l1 = l - 1, r1 = r, l2 = l, r2 = r + 1
        while l1 >= 0 && r1 < n && s[l1] == s[r1] { l1 -= 1; r1 += 1 }
        while l2 >= 0 && r2 < n && s[l2] == s[r2] { l2 -= 1; r2 += 1 }
        return min(n, max(r1 - l1 - 1, r2 - l2 - 1))
    }
}
""")

write("3845_maximum_subarray_xor_with_bounded_range", """// LeetCode 3845 - Maximum Subarray XOR with Bounded Range
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

class Solution {
    private class Node {
        var next = [0, 0]
        var count = 0
    }

    private var nodes = [Node]()

    private func add(_ x: Int, _ delta: Int) {
        var u = 0
        nodes[u].count += delta
        for b in stride(from: 15, through: 0, by: -1) {
            let bit = (x >> b) & 1
            if nodes[u].next[bit] == 0 {
                nodes[u].next[bit] = nodes.count
                nodes.append(Node())
            }
            u = nodes[u].next[bit]
            nodes[u].count += delta
        }
    }

    private func query(_ x: Int) -> Int {
        var u = 0, res = 0
        for b in stride(from: 15, through: 0, by: -1) {
            let bit = (x >> b) & 1
            let want = bit ^ 1
            let v = nodes[u].next[want]
            if v != 0 && nodes[v].count > 0 {
                res |= 1 << b
                u = v
            } else {
                u = nodes[u].next[bit]
            }
        }
        return res
    }

    func maxSubarrayXor(_ nums: [Int], _ k: Int) -> Int {
        nodes = [Node()]
        let n = nums.count
        var pref = [Int](repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] ^ nums[i] }
        var maxQ = [Int]()
        var minQ = [Int]()
        var left = 0, trieLeft = 0, ans = 0
        for r in 0..<n {
            let x = nums[r]
            while !maxQ.isEmpty && nums[maxQ.last!] <= x { maxQ.removeLast() }
            maxQ.append(r)
            while !minQ.isEmpty && nums[minQ.last!] >= x { minQ.removeLast() }
            minQ.append(r)
            while nums[maxQ[0]] - nums[minQ[0]] > k {
                if maxQ[0] == left { maxQ.removeFirst() }
                if minQ[0] == left { minQ.removeFirst() }
                left += 1
            }
            add(pref[r], 1)
            while trieLeft < left {
                add(pref[trieLeft], -1)
                trieLeft += 1
            }
            let cur = query(pref[r + 1])
            if cur > ans { ans = cur }
        }
        return ans
    }
}
""")

write("3846_total_distance_to_type_a_string_using_one_finger", """// LeetCode 3846 - Total Distance To Type A String Using One Finger
// https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

class Solution {
    private static let POS: [Character: (Int, Int)] = {
        var pos = [Character: (Int, Int)]()
        let keys = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for i in 0..<3 {
            let row = Array(keys[i])
            for j in 0..<row.count { pos[row[j]] = (i, j) }
        }
        return pos
    }()

    func totalDistance(_ s: String) -> Int {
        var pre: Character = "a"
        var ans = 0
        for cur in s {
            let p1 = Solution.POS[pre]!
            let p2 = Solution.POS[cur]!
            ans += abs(p1.0 - p2.0) + abs(p1.1 - p2.1)
            pre = cur
        }
        return ans
    }
}
""")

write("3847_find_the_score_difference_in_a_game", """// LeetCode 3847 - Find The Score Difference In A Game
// https://leetcode.com/problems/find-the-score-difference-in-a-game/

class Solution {
    func scoreDifference(_ nums: [Int]) -> Int {
        var ans = 0, k = 1
        for i in 0..<nums.count {
            if nums[i] % 2 != 0 { k = -k }
            if i % 6 == 5 { k = -k }
            ans += k * nums[i]
        }
        return ans
    }
}
""")

write("3848_check_digitorial_permutation", """// LeetCode 3848 - Check Digitorial Permutation
// https://leetcode.com/problems/check-digitorial-permutation/

class Solution {
    func isDigitorialPermutation(_ n: Int) -> Bool {
        var f = [Int](repeating: 0, count: 10)
        f[0] = 1
        for i in 1..<10 { f[i] = f[i - 1] * i }
        var x = 0, y = n
        while y > 0 {
            x += f[y % 10]
            y /= 10
        }
        return String(String(x).sorted()) == String(String(n).sorted())
    }
}
""")

write("3849_maximum_bitwise_xor_after_rearrangement", """// LeetCode 3849 - Maximum Bitwise Xor After Rearrangement
// https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

class Solution {
    func maximumXor(_ s: String, _ t: String) -> String {
        var cnt = [0, 0]
        for c in t { cnt[Int(c.asciiValue! - 48)] += 1 }
        let sc = Array(s)
        var ans = [Character](repeating: "0", count: sc.count)
        for i in 0..<sc.count {
            let x = Int(sc[i].asciiValue! - 48)
            if cnt[x ^ 1] > 0 {
                cnt[x ^ 1] -= 1
                ans[i] = "1"
            } else {
                cnt[x] -= 1
                ans[i] = "0"
            }
        }
        return String(ans)
    }
}
""")

write("3850_count_sequences_to_k", """// LeetCode 3850 - Count Sequences To K
// https://leetcode.com/problems/count-sequences-to-k/

class Solution {
    private var nums = [Int]()
    private var k = 0
    private var f = [String: Int]()

    func countSequences(_ nums: [Int], _ k: Int) -> Int {
        self.nums = nums
        self.k = k
        f = [:]
        return dfs(0, 1, 1)
    }

    private func gcd(_ a: Int, _ b: Int) -> Int {
        var a = a, b = b
        while b != 0 {
            let t = a % b
            a = b
            b = t
        }
        return a
    }

    private func dfs(_ i: Int, _ p: Int, _ q: Int) -> Int {
        if i == nums.count { return (p == k && q == 1) ? 1 : 0 }
        let key = "\\(i),\\(p),\\(q)"
        if let cached = f[key] { return cached }
        var res = dfs(i + 1, p, q)
        let x = nums[i]
        let g1 = gcd(p * x, q)
        res += dfs(i + 1, (p * x) / g1, q / g1)
        let g2 = gcd(p, q * x)
        res += dfs(i + 1, p / g2, (q * x) / g2)
        f[key] = res
        return res
    }
}
""")

write("3851_maximum_requests_without_violating_the_limit", """// LeetCode 3851 - Maximum Requests Without Violating The Limit
// https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

class Solution {
    func maxRequests(_ requests: [[Int]], _ k: Int, _ window: Int) -> Int {
        var g = [Int: [Int]]()
        for r in requests {
            g[r[0], default: []].append(r[1])
        }
        var ans = requests.count
        for var ts in g.values {
            ts.sort()
            var kept = [Int]()
            for t in ts {
                while !kept.isEmpty && t - kept[0] > window { kept.removeFirst() }
                if kept.count < k { kept.append(t) }
                else { ans -= 1 }
            }
        }
        return ans
    }
}
""")

write("3852_smallest_pair_with_different_frequencies", """// LeetCode 3852 - Smallest Pair With Different Frequencies
// https://leetcode.com/problems/smallest-pair-with-different-frequencies/

class Solution {
    func minDistinctFreqPair(_ nums: [Int]) -> [Int] {
        var cnt = [Int: Int]()
        for v in nums { cnt[v, default: 0] += 1 }
        var x = nums[0]
        for v in nums { x = min(x, v) }
        var minY = Int.max
        for y in cnt.keys {
            if y < minY && cnt[x] != cnt[y] { minY = y }
        }
        if minY == Int.max { return [-1, -1] }
        return [x, minY]
    }
}
""")

write("3853_merge_close_characters", """// LeetCode 3853 - Merge Close Characters
// https://leetcode.com/problems/merge-close-characters/

class Solution {
    func mergeCharacters(_ s: String, _ k: Int) -> String {
        var last = [Character: Int]()
        var ans = [Character]()
        for c in s {
            let cur = ans.count
            if let p = last[c], cur - p <= k { continue }
            ans.append(c)
            last[c] = cur
        }
        return String(ans)
    }
}
""")

write("3854_minimum_operations_to_make_array_parity_alternating", """// LeetCode 3854 - Minimum Operations To Make Array Parity Alternating
// https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

class Solution {
    func makeParityAlternating(_ nums: [Int]) -> [Int] {
        if nums.count == 1 { return [0, 0] }
        var mn = nums[0], mx = nums[0]
        for x in nums { mn = min(mn, x); mx = max(mx, x) }
        let r0 = f(nums, 0, mn, mx)
        let r1 = f(nums, 1, mn, mx)
        if r0[0] != r1[0] { return r0[0] < r1[0] ? r0 : r1 }
        return r0[1] <= r1[1] ? r0 : r1
    }

    private func f(_ nums: [Int], _ k: Int, _ mn: Int, _ mx: Int) -> [Int] {
        var cnt = 0, a = Int.max, b = Int.min
        for i in 0..<nums.count {
            var x = nums[i]
            if ((x - i) & 1) != k {
                cnt += 1
                if x == mn { x += 1 }
                else if x == mx { x -= 1 }
            }
            a = min(a, x)
            b = max(b, x)
        }
        return [cnt, max(1, b - a)]
    }
}
""")

write("3855_sum_of_k_digit_numbers_in_a_range", """// LeetCode 3855 - Sum Of K Digit Numbers In A Range
// https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/

class Solution {
    private func qpow(_ a: Int, _ n: Int, _ mod: Int) -> Int {
        var a = a % mod, n = n, ans = 1
        while n > 0 {
            if (n & 1) != 0 { ans = ans * a % mod }
            a = a * a % mod
            n >>= 1
        }
        return ans
    }

    func sumOfNumbers(_ l: Int, _ r: Int, _ k: Int) -> Int {
        let MOD = 1_000_000_007
        let n = r - l + 1
        let sum = (l + r) * n / 2 % MOD
        let part1 = qpow(n % MOD, k - 1, MOD)
        let part2 = (qpow(10, k, MOD) - 1 + MOD) % MOD
        let inv9 = qpow(9, MOD - 2, MOD)
        var ans = sum
        ans = ans * part1 % MOD
        ans = ans * part2 % MOD
        ans = ans * inv9 % MOD
        return ans
    }
}
""")

write("3856_trim_trailing_vowels", """// LeetCode 3856 - Trim Trailing Vowels
// https://leetcode.com/problems/trim-trailing-vowels/

class Solution {
    func trimTrailingVowels(_ s: String) -> String {
        var chars = Array(s)
        while !chars.isEmpty && isVowel(chars.last!) { chars.removeLast() }
        return String(chars)
    }

    private func isVowel(_ c: Character) -> Bool {
        return "aeiou".contains(c)
    }
}
""")

write("3857_minimum_cost_to_split_into_ones", """// LeetCode 3857 - Minimum Cost To Split Into Ones
// https://leetcode.com/problems/minimum-cost-to-split-into-ones/

class Solution {
    func minCost(_ n: Int) -> Int {
        return n * (n - 1) / 2
    }
}
""")

write("3858_minimum_bitwise_or_from_grid", """// LeetCode 3858 - Minimum Bitwise Or From Grid
// https://leetcode.com/problems/minimum-bitwise-or-from-grid/

class Solution {
    private func bitLen(_ x: Int) -> Int {
        if x == 0 { return 0 }
        var x = x, n = 0
        while x > 0 { n += 1; x >>= 1 }
        return n
    }

    func minimumOR(_ grid: [[Int]]) -> Int {
        var mx = 0
        for row in grid {
            for x in row { mx = max(mx, x) }
        }
        let m = bitLen(mx)
        var ans = 0
        if m > 0 {
            for i in stride(from: m - 1, through: 0, by: -1) {
                let mask = ans | ((1 << i) - 1)
                for row in grid {
                    var found = false
                    for x in row {
                        if (x | mask) == mask { found = true; break }
                    }
                    if !found {
                        ans |= 1 << i
                        break
                    }
                }
            }
        }
        return ans
    }
}
""")

write("3859_count_subarrays_with_k_distinct_integers", """// LeetCode 3859 - Count Subarrays With K Distinct Integers
// https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

class Solution {
    private var nums = [Int]()
    private var k = 0, m = 0

    func countSubarrays(_ nums: [Int], _ k: Int, _ m: Int) -> Int {
        self.nums = nums
        self.k = k
        self.m = m
        return f(k) - f(k + 1)
    }

    private func f(_ lim: Int) -> Int {
        var cnt = [Int: Int]()
        var ans = 0
        var l = 0, t = 0
        for x in nums {
            let c = (cnt[x] ?? 0) + 1
            cnt[x] = c
            if c == m { t += 1 }
            while cnt.count >= lim && t >= k {
                let y = nums[l]
                l += 1
                let cy = cnt[y]! - 1
                if cy == m - 1 { t -= 1 }
                if cy == 0 { cnt.removeValue(forKey: y) }
                else { cnt[y] = cy }
            }
            ans += l
        }
        return ans
    }
}
""")

write("3860_unique_email_groups", """// LeetCode 3860 - Unique Email Groups
// https://leetcode.com/problems/unique-email-groups/

class Solution {
    func uniqueEmailGroups(_ emails: [String]) -> Int {
        var st = Set<String>()
        for email in emails {
            let at = email.firstIndex(of: "@")!
            var local = String(email[..<at])
            let domain = email[email.index(after: at)...].lowercased()
            if let plus = local.firstIndex(of: "+") {
                local = String(local[..<plus])
            }
            var cleaned = ""
            for c in local where c != "." { cleaned.append(Character(c.lowercased())) }
            st.insert(cleaned + domain)
        }
        return st.count
    }
}
""")

write("3861_minimum_capacity_box", """// LeetCode 3861 - Minimum Capacity Box
// https://leetcode.com/problems/minimum-capacity-box/

class Solution {
    func minimumIndex(_ capacity: [Int], _ itemSize: Int) -> Int {
        var ans = -1
        for i in 0..<capacity.count {
            if capacity[i] >= itemSize && (ans == -1 || capacity[i] < capacity[ans]) { ans = i }
        }
        return ans
    }
}
""")

write("3862_find_the_smallest_balanced_index", """// LeetCode 3862 - Find The Smallest Balanced Index
// https://leetcode.com/problems/find-the-smallest-balanced-index/

class Solution {
    func smallestBalancedIndex(_ nums: [Int]) -> Int {
        var s = 0, p = 1
        for x in nums { s += x }
        for i in stride(from: nums.count - 1, through: 0, by: -1) {
            s -= nums[i]
            if s == p { return i }
            p *= nums[i]
            if p >= s { break }
        }
        return -1
    }
}
""")
