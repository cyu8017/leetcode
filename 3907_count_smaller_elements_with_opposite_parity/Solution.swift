// LeetCode 3907 - Count Smaller Elements With Opposite Parity
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
