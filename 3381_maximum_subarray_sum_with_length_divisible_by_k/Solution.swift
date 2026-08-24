// LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K
// https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

class Solution {
    func maxSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var pref = Array(repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] + nums[i] }
        let INF = 1 << 62
        var best = Array(repeating: INF, count: k)
        best[0] = 0
        var ans = -(1 << 62)
        for i in 1...n {
            let r = i % k
            if best[r] != INF {
                let cand = pref[i] - best[r]
                if cand > ans { ans = cand }
            }
            if pref[i] < best[r] { best[r] = pref[i] }
        }
        return ans
    }
}
