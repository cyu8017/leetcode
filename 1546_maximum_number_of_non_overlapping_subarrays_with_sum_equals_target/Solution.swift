// LeetCode 1546 - Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
// https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/

class Solution {
    func maxNonOverlapping(_ nums: [Int], _ target: Int) -> Int {
        var seen: Set<Int> = [0]
        var prefix = 0, answer = 0
        for value in nums {
            prefix += value
            if seen.contains(prefix - target) {
                answer += 1
                prefix = 0
                seen = [0]
            } else {
                seen.insert(prefix)
            }
        }
        return answer
    }
}
