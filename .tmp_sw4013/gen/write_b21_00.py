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


write("3719_longest_balanced_subarray_i", """// LeetCode 3719 - Longest Balanced Subarray I
// https://leetcode.com/problems/longest-balanced-subarray-i/

class Solution {
    func longestBalanced(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var vis = Set<Int>()
            var cnt = [0, 0]
            for j in i..<n {
                if !vis.contains(nums[j]) {
                    vis.insert(nums[j])
                    cnt[nums[j] & 1] += 1
                }
                if cnt[0] == cnt[1] { ans = max(ans, j - i + 1) }
            }
        }
        return ans
    }
}
""")

write("3720_lexicographically_smallest_permutation_greater_than_target", """// LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

class Solution {
    private var cnt = [Int]()
    private var ans = [Character]()
    private var targetChars = [Character]()
    private var n = 0

    func lexGreaterPermutation(_ s: String, _ target: String) -> String {
        cnt = [Int](repeating: 0, count: 26)
        for c in s { cnt[Int(c.asciiValue! - 97)] += 1 }
        n = s.count
        targetChars = Array(target)
        ans = [Character](repeating: "a", count: n)
        if dfs(0, false) { return String(ans) }
        return ""
    }

    private func dfs(_ pos: Int, _ greater: Bool) -> Bool {
        if pos == n { return greater }
        let start = greater ? 0 : Int(targetChars[pos].asciiValue! - 97)
        if start < 0 { return false }
        for c in start..<26 {
            if cnt[c] == 0 { continue }
            cnt[c] -= 1
            ans[pos] = Character(UnicodeScalar(97 + c)!)
            let ng = greater || c > Int(targetChars[pos].asciiValue! - 97)
            if dfs(pos + 1, ng) { return true }
            cnt[c] += 1
        }
        return false
    }
}
""")

write("3721_longest_balanced_subarray_ii", """// LeetCode 3721 - Longest Balanced Subarray II
// https://leetcode.com/problems/longest-balanced-subarray-ii/

class Solution {
    private class Node {
        var l = 0, r = 0, mn = 0, mx = 0, lazy = 0
    }

    private class SegmentTree {
        var tr: [Node]
        init(_ n: Int) {
            tr = (0..<(n << 2)).map { _ in Node() }
            build(1, 0, n)
        }
        func build(_ u: Int, _ l: Int, _ r: Int) {
            tr[u].l = l; tr[u].r = r; tr[u].mn = 0; tr[u].mx = 0; tr[u].lazy = 0
            if l == r { return }
            let mid = (l + r) >> 1
            build(u << 1, l, mid)
            build(u << 1 | 1, mid + 1, r)
        }
        func apply(_ u: Int, _ v: Int) {
            tr[u].mn += v
            tr[u].mx += v
            tr[u].lazy += v
        }
        func pushup(_ u: Int) {
            tr[u].mn = min(tr[u << 1].mn, tr[u << 1 | 1].mn)
            tr[u].mx = max(tr[u << 1].mx, tr[u << 1 | 1].mx)
        }
        func pushdown(_ u: Int) {
            if tr[u].lazy != 0 {
                let v = tr[u].lazy
                apply(u << 1, v)
                apply(u << 1 | 1, v)
                tr[u].lazy = 0
            }
        }
        func modify(_ u: Int, _ l: Int, _ r: Int, _ v: Int) {
            if tr[u].l >= l && tr[u].r <= r {
                apply(u, v)
                return
            }
            pushdown(u)
            let mid = (tr[u].l + tr[u].r) >> 1
            if l <= mid { modify(u << 1, l, r, v) }
            if r > mid { modify(u << 1 | 1, l, r, v) }
            pushup(u)
        }
        func query(_ u: Int, _ target: Int) -> Int {
            if tr[u].l == tr[u].r { return tr[u].l }
            pushdown(u)
            let left = u << 1, right = u << 1 | 1
            if tr[left].mn <= target && target <= tr[left].mx { return query(left, target) }
            return query(right, target)
        }
    }

    func longestBalanced(_ nums: [Int]) -> Int {
        let n = nums.count
        let st = SegmentTree(n)
        var last = [Int: Int]()
        var now = 0, ans = 0
        for i in 1...n {
            let x = nums[i - 1]
            let det = (x & 1) != 0 ? 1 : -1
            if let prev = last[x] {
                st.modify(1, prev, n, -det)
                now -= det
            }
            last[x] = i
            st.modify(1, i, n, det)
            now += det
            let pos = st.query(1, now)
            ans = max(ans, i - pos)
        }
        return ans
    }
}
""")

write("3722_lexicographically_smallest_string_after_reverse", """// LeetCode 3722 - Lexicographically Smallest String After Reverse
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

class Solution {
    func lexSmallest(_ s: String) -> String {
        var ans = s
        let n = s.count
        for k in 1...n {
            var a1 = Array(s)
            reverse(&a1, 0, k)
            let t1 = String(a1)
            var a2 = Array(s)
            reverse(&a2, n - k, n)
            let t2 = String(a2)
            if t1 < ans { ans = t1 }
            if t2 < ans { ans = t2 }
        }
        return ans
    }

    private func reverse(_ a: inout [Character], _ l: Int, _ r: Int) {
        var i = l, j = r - 1
        while i < j {
            a.swapAt(i, j)
            i += 1
            j -= 1
        }
    }
}
""")

write("3723_maximize_sum_of_squares_of_digits", """// LeetCode 3723 - Maximize Sum Of Squares Of Digits
// https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

class Solution {
    func maxSumOfSquares(_ num: Int, _ sum: Int) -> String {
        if num * 9 < sum { return "" }
        let k = sum / 9, s = sum % 9
        var ans = String(repeating: "9", count: k)
        if s > 0 { ans.append(Character(UnicodeScalar(48 + s)!)) }
        while ans.count < num { ans.append("0") }
        return ans
    }
}
""")

write("3724_minimum_operations_to_transform_array", """// LeetCode 3724 - Minimum Operations to Transform Array
// https://leetcode.com/problems/minimum-operations-to-transform-array/

class Solution {
    func minOperations(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var ans = 1
        let n = nums1.count
        var ok = false
        var d = 1 << 30
        for i in 0..<n {
            let x = max(nums1[i], nums2[i])
            let y = min(nums1[i], nums2[i])
            ans += x - y
            d = min(d, min(abs(x - nums2[n]), abs(y - nums2[n])))
            if nums2[n] >= y && nums2[n] <= x { ok = true }
        }
        if !ok { ans += d }
        return ans
    }
}
""")

write("3725_count_ways_to_choose_coprime_integers_from_rows", """// LeetCode 3725 - Count Ways To Choose Coprime Integers From Rows
// https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

class Solution {
    func countCoprime(_ mat: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        let m = mat.count
        var dp = [Int: Int]()
        for v in mat[0] { dp[v, default: 0] += 1 }
        if m > 1 {
            for i in 1..<m {
                var ndp = [Int: Int]()
                for v in mat[i] {
                    for (key, val) in dp {
                        let ng = gcd(key, v)
                        ndp[ng, default: 0] = (ndp[ng, default: 0] + val) % MOD
                    }
                }
                dp = ndp
            }
        }
        return dp[1, default: 0]
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
}
""")

write("3726_remove_zeros_in_decimal_representation", """// LeetCode 3726 - Remove Zeros in Decimal Representation
// https://leetcode.com/problems/remove-zeros-in-decimal-representation/

class Solution {
    func removeZeros(_ n: Int) -> Int {
        var n = n
        var ans = 0, k = 1
        while n > 0 {
            let x = n % 10
            if x > 0 {
                ans = k * x + ans
                k *= 10
            }
            n /= 10
        }
        return ans
    }
}
""")

write("3727_maximum_alternating_sum_of_squares", """// LeetCode 3727 - Maximum Alternating Sum of Squares
// https://leetcode.com/problems/maximum-alternating-sum-of-squares/

class Solution {
    func maxAlternatingSum(_ nums: [Int]) -> Int {
        var a = nums.map { $0 * $0 }
        a.sort()
        let m = a.count / 2
        var ans = 0
        for i in 0..<m { ans -= a[i] }
        for i in m..<a.count { ans += a[i] }
        return ans
    }
}
""")

write("3728_stable_subarrays_with_equal_boundary_and_interior_sum", """// LeetCode 3728 - Stable Subarrays With Equal Boundary And Interior Sum
// https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/

class Solution {
    func countStableSubarrays(_ capacity: [Int]) -> Int {
        let n = capacity.count
        var s = [Int](repeating: 0, count: n + 1)
        for i in 1...n { s[i] = s[i - 1] + capacity[i - 1] }
        var cnt = [String: Int]()
        var ans = 0
        if n > 2 {
            for r in 2..<n {
                let l = r - 2
                let keyL = "\\(capacity[l])#\\(capacity[l] + s[l + 1])"
                cnt[keyL, default: 0] += 1
                let keyR = "\\(capacity[r])#\\(s[r])"
                ans += cnt[keyR, default: 0]
            }
        }
        return ans
    }
}
""")

write("3729_count_distinct_subarrays_divisible_by_k_in_sorted_array", """// LeetCode 3729 - Count Distinct Subarrays Divisible By K In Sorted Array
// https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/

class Solution {
    func numGoodSubarrays(_ nums: [Int], _ k: Int) -> Int {
        var ans = 0
        var s = 0
        var cnt = [Int: Int]()
        cnt[0] = 1
        for x in nums {
            s = (s + x) % k
            ans += cnt[s, default: 0]
            cnt[s, default: 0] += 1
        }
        let n = nums.count
        var i = 0
        while i < n {
            var j = i + 1
            while j < n && nums[j] == nums[i] { j += 1 }
            let m = j - i
            for h in 1...m {
                if nums[i] * h % k == 0 { ans -= (m - h) }
            }
            i = j
        }
        return ans
    }
}
""")

write("3730_maximum_calories_burnt_from_jumps", """// LeetCode 3730 - Maximum Calories Burnt from Jumps
// https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

class Solution {
    func maxCaloriesBurnt(_ heights: [Int]) -> Int {
        let h = heights.sorted()
        var ans = 0
        var pre = 0, l = 0, r = h.count - 1
        while l < r {
            let d1 = h[r] - pre
            ans += d1 * d1
            let d2 = h[l] - h[r]
            ans += d2 * d2
            pre = h[l]
            l += 1
            r -= 1
        }
        let d = h[r] - pre
        ans += d * d
        return ans
    }
}
""")

write("3731_find_missing_elements", """// LeetCode 3731 - Find Missing Elements
// https://leetcode.com/problems/find-missing-elements/

class Solution {
    func findMissingElements(_ nums: [Int]) -> [Int] {
        var mn = 100, mx = 0
        var s = Set<Int>()
        for x in nums {
            mn = min(mn, x)
            mx = max(mx, x)
            s.insert(x)
        }
        var ans = [Int]()
        if mn + 1 < mx {
            for x in (mn + 1)..<mx {
                if !s.contains(x) { ans.append(x) }
            }
        }
        return ans
    }
}
""")

write("3732_maximum_product_of_three_elements_after_one_replacement", """// LeetCode 3732 - Maximum Product of Three Elements After One Replacement
// https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

class Solution {
    func maxProduct(_ nums: [Int]) -> Int {
        let a = nums.sorted()
        let n = a.count
        let x0 = a[0], x1 = a[1], x2 = a[n - 2], x3 = a[n - 1]
        let x = 100000
        return max(max(x0 * x1 * x, x2 * x3 * x), -x0 * x3 * x)
    }
}
""")

write("3733_minimum_time_to_complete_all_deliveries", """// LeetCode 3733 - Minimum Time To Complete All Deliveries
// https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/

class Solution {
    func minimumTime(_ d: [Int], _ r: [Int]) -> Int {
        var lo = 1, hi = Int(8e18)
        while lo < hi {
            let mid = lo + (hi - lo) / 2
            if ok(mid, d, r) { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }

    private func ok(_ T: Int, _ d: [Int], _ r: [Int]) -> Bool {
        let w0 = T - T / r[0]
        let w1 = T - T / r[1]
        return w0 + w1 >= d[0] + d[1]
    }
}
""")

write("3734_lexicographically_smallest_palindromic_permutation_greater_than_target", """// LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

class Solution {
    private var half = [Int]()
    private var left = [Character]()
    private var targetChars = [Character]()
    private var halfLen = 0
    private var mid = -1

    func lexPalindromicPermutation(_ s: String, _ target: String) -> String {
        var cnt = [Int](repeating: 0, count: 26)
        for c in s { cnt[Int(c.asciiValue! - 97)] += 1 }
        var odd = 0
        mid = -1
        for i in 0..<26 {
            if cnt[i] % 2 == 1 { odd += 1; mid = i }
        }
        if odd > 1 { return "" }
        half = [Int](repeating: 0, count: 26)
        for i in 0..<26 { half[i] = cnt[i] / 2 }
        let n = s.count
        halfLen = n / 2
        targetChars = Array(target)
        left = [Character](repeating: "a", count: max(halfLen, 1))
        if !dfs(0, false) { return "" }
        var res = String(left.prefix(halfLen))
        if mid >= 0 { res.append(Character(UnicodeScalar(97 + mid)!)) }
        for i in stride(from: halfLen - 1, through: 0, by: -1) { res.append(left[i]) }
        if res <= target { return "" }
        return res
    }

    private func dfs(_ pos: Int, _ greater: Bool) -> Bool {
        if pos == halfLen {
            if mid >= 0 {
                if greater { return true }
                return Character(UnicodeScalar(97 + mid)!) > targetChars[halfLen]
            }
            return greater
        }
        let start = greater ? 0 : Int(targetChars[pos].asciiValue! - 97)
        for c in start..<26 {
            if half[c] == 0 { continue }
            half[c] -= 1
            left[pos] = Character(UnicodeScalar(97 + c)!)
            if dfs(pos + 1, greater || c > Int(targetChars[pos].asciiValue! - 97)) { return true }
            half[c] += 1
        }
        return false
    }
}
""")

write("3735_lexicographically_smallest_string_after_reverse_ii", """// LeetCode 3735 - Lexicographically Smallest String After Reverse II
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

class Solution {
    func lexSmallest(_ s: String) -> String {
        let n = s.count
        var best = s
        if n >= 1 {
            for i in 1...n {
                var t = Array(s)
                reverse(&t, 0, i)
                let ts = String(t)
                if ts < best { best = ts }
            }
        }
        for i in 0..<n {
            var t = Array(s)
            reverse(&t, i, n)
            let ts = String(t)
            if ts < best { best = ts }
        }
        return best
    }

    private func reverse(_ a: inout [Character], _ l: Int, _ r: Int) {
        var i = l, j = r - 1
        while i < j {
            a.swapAt(i, j)
            i += 1
            j -= 1
        }
    }
}
""")

write("3736_minimum_moves_to_equal_array_elements_iii", """// LeetCode 3736 - Minimum Moves to Equal Array Elements III
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

class Solution {
    func minMoves(_ nums: [Int]) -> Int {
        var mx = 0, s = 0
        for x in nums {
            mx = max(mx, x)
            s += x
        }
        return mx * nums.count - s
    }
}
""")

write("3737_count_subarrays_with_majority_element_i", """// LeetCode 3737 - Count Subarrays With Majority Element I
// https://leetcode.com/problems/count-subarrays-with-majority-element-i/

class Solution {
    func countMajoritySubarrays(_ nums: [Int], _ target: Int) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var cnt = 0
            for j in i..<n {
                if nums[j] == target { cnt += 1 }
                if cnt * 2 > j - i + 1 { ans += 1 }
            }
        }
        return ans
    }
}
""")

write("3738_longest_non_decreasing_subarray_after_replacing_at_most_one_element", """// LeetCode 3738 - Longest Non-Decreasing Subarray After Replacing at Most One Element
// https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

class Solution {
    func longestSubarray(_ nums: [Int]) -> Int {
        let n = nums.count
        var left = [Int](repeating: 1, count: n)
        var right = [Int](repeating: 1, count: n)
        if n > 1 {
            for i in 1..<n {
                if nums[i] >= nums[i - 1] { left[i] = left[i - 1] + 1 }
            }
            for i in stride(from: n - 2, through: 0, by: -1) {
                if nums[i] <= nums[i + 1] { right[i] = right[i + 1] + 1 }
            }
        }
        var ans = 0
        for v in left { ans = max(ans, v) }
        for i in 0..<n {
            let a = i > 0 ? left[i - 1] : 0
            let b = i + 1 < n ? right[i + 1] : 0
            if i > 0 && i + 1 < n && nums[i - 1] > nums[i + 1] {
                ans = max(ans, max(a + 1, b + 1))
            } else {
                ans = max(ans, a + b + 1)
            }
        }
        return ans
    }
}
""")
