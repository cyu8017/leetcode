// LeetCode 0974 - Subarray Sums Divisible by K
// https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution {
    func subarraysDivByK(_ nums: [Int], _ k: Int) -> Int {
        var count = [0: 1]
        var prefix = 0, ans = 0
        for x in nums {
            prefix = ((prefix + x) % k + k) % k
            ans += count[prefix, default: 0]
            count[prefix, default: 0] += 1
        }
        return ans
    }
}
