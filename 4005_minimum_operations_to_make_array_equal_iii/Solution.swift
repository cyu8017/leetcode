// LeetCode 4005 - Minimum Operations to Make Array Equal III
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-iii/


class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        func cost(_ x: Int, _ t: Int) -> Int {
            if x == t { return 0 }
            if x % t == 0 || t % x == 0 { return 1 }
            return 2
        }
        func gcd(_ a0: Int, _ b0: Int) -> Int {
            var a = a0, b = b0
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        let n = nums.count
        if n <= 1 { return 0 }
        var g = nums[0], mn = nums[0]
        for i in 1..<n {
            g = gcd(g, nums[i])
            mn = min(mn, nums[i])
        }
        var cands = Set<Int>()
        for x in nums { cands.insert(x) }
        var d = 1
        while d * d <= mn {
            if mn % d == 0 {
                cands.insert(d)
                cands.insert(mn / d)
            }
            d += 1
        }
        cands.insert(g)
        var ans = Int.max
        for t in cands {
            var sum = 0
            for x in nums {
                sum += cost(x, t)
                if sum >= ans { break }
            }
            ans = min(ans, sum)
        }
        return ans
    }
}
