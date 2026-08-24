// LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
// https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        let n = nums.count
        let ones = nums.filter { $0 == 1 }.count
        if ones > 0 { return n - ones }
        var best = n + 1
        for i in 0..<n {
            var g = 0
            for j in i..<n {
                g = gcd(g, nums[j])
                if g == 1 {
                    best = min(best, j - i)
                    break
                }
            }
        }
        if best == n + 1 { return -1 }
        return best + n - 1
    }

    private func gcd(_ a0: Int, _ b0: Int) -> Int {
        var a = a0, b = b0
        while b != 0 {
            let t = a % b
            a = b
            b = t
        }
        return a
    }
}
