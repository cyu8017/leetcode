// LeetCode 2333 - Minimum Sum of Squared Difference
// https://leetcode.com/problems/minimum-sum-of-squared-difference/

class Solution {
    func minSumSquareDiff(_ nums1: [Int], _ nums2: [Int], _ k1: Int, _ k2: Int) -> Int {
        let n = nums1.count
        var maxD = 0
        var diff = [Int](repeating: 0, count: n)
        for i in 0..<n {
            diff[i] = abs(nums1[i] - nums2[i])
            maxD = max(maxD, diff[i])
        }
        var k = k1 + k2
        var freq = [Int](repeating: 0, count: maxD + 1)
        for d in diff { freq[d] += 1 }
        var d = maxD
        while d > 0 && k > 0 {
            if freq[d] > 0 {
                var take = freq[d]
                if take > k { take = k }
                freq[d] -= take
                freq[d - 1] += take
                k -= take
            }
            d -= 1
        }
        var ans = 0
        for d in 0...maxD { ans += d * d * freq[d] }
        return ans
    }
}
