// LeetCode 4013 - Count Subarrays With Even Odd Ratio II
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/


class Solution {
    func countRatioSubarrays(_ nums: [Int], _ a: Int, _ b: Int) -> Int {
        let n = nums.count
        var s = Array(repeating: 0, count: n + 1)
        for i in 0..<n {
            if nums[i] % 2 == 1 { s[i + 1] = s[i] + a }
            else { s[i + 1] = s[i] - b }
        }
        var st = s
        st.sort()
        var uniq = 0
        for i in 0..<st.count {
            if uniq == 0 || st[i] != st[uniq - 1] {
                st[uniq] = st[i]
                uniq += 1
            }
        }
        st = Array(st.prefix(uniq))
        var bit = BIT(st.count + 1)
        var ans = 0
        for v in s {
            let x = lowerBound(st, v) + 1
            ans += bit.query(x)
            bit.update(x, 1)
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

    private class BIT {
        let n: Int
        var c: [Int]
        init(_ n: Int) {
            self.n = n
            c = Array(repeating: 0, count: n + 1)
        }
        func update(_ x0: Int, _ delta: Int) {
            var x = x0
            while x <= n {
                c[x] += delta
                x += x & -x
            }
        }
        func query(_ x0: Int) -> Int {
            var x = x0, sum = 0
            while x > 0 {
                sum += c[x]
                x -= x & -x
            }
            return sum
        }
    }
}
