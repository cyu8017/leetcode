// LeetCode 3574 - Maximize Subarray GCD Score
// https://leetcode.com/problems/maximize-subarray-gcd-score/

class Solution {
    func gcd(_ a0: Int, _ b0: Int) -> Int {
        var a = a0, b = b0
        while b != 0 { let t = a % b; a = b; b = t }
        return a
    }

    func maxGCDScore(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var cnt = Array(repeating: 0, count: n)
        for i in 0..<n {
            var x = nums[i]
            while x % 2 == 0 { cnt[i] += 1; x /= 2 }
        }
        var ans = 0
        for l in 0..<n {
            var g = 0, mi = Int.max, t = 0
            for r in l..<n {
                g = gcd(g, nums[r])
                if cnt[r] < mi { mi = cnt[r]; t = 1 }
                else if cnt[r] == mi { t += 1 }
                var score = g * (r - l + 1)
                if t <= k { score *= 2 }
                ans = max(ans, score)
            }
        }
        return ans
    }
}
