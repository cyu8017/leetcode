// LeetCode 1031 - Maximum Sum of Two Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

class Solution {
    func maxSumTwoNoOverlap(_ nums: [Int], _ firstLen: Int, _ secondLen: Int) -> Int {
        var prefix = [0]
        for x in nums { prefix.append(prefix.last! + x) }
        func best(_ a: Int, _ b: Int) -> Int {
            var bestA = 0, ans = 0
            for i in (a + b)..<prefix.count {
                bestA = max(bestA, prefix[i - b] - prefix[i - b - a])
                ans = max(ans, bestA + prefix[i] - prefix[i - b])
            }
            return ans
        }
        return max(best(firstLen, secondLen), best(secondLen, firstLen))
    }
}
