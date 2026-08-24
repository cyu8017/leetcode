// LeetCode 2143 - Choose Numbers From Two Arrays in Range
// https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/

class Solution {
    func countSubranges(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let MOD = 1_000_000_007
        var dp = [Int: Int]()
        var ans = 0
        for i in 0..<nums1.count {
            var ndp = [Int: Int]()
            ndp[nums1[i], default: 0] = (ndp[nums1[i], default: 0] + 1) % MOD
            ndp[-nums2[i], default: 0] = (ndp[-nums2[i], default: 0] + 1) % MOD
            for (diff, cnt) in dp {
                ndp[diff + nums1[i], default: 0] = (ndp[diff + nums1[i], default: 0] + cnt) % MOD
                ndp[diff - nums2[i], default: 0] = (ndp[diff - nums2[i], default: 0] + cnt) % MOD
            }
            dp = ndp
            ans = (ans + dp[0, default: 0]) % MOD
        }
        return ans
    }
}
