// LeetCode 0523 - Continuous Subarray Sum
// https://leetcode.com/problems/continuous-subarray-sum/

class Solution {
    func checkSubarraySum(_ nums: [Int], _ k: Int) -> Bool {
        var prefix = 0
        var remainders: [Int: Int] = [0: -1]
        for (index, num) in nums.enumerated() {
            prefix += num
            let mod = k == 0 ? prefix : prefix % k
            if let previous = remainders[mod] {
                if index - previous >= 2 {
                    return true
                }
            } else {
                remainders[mod] = index
            }
        }
        return false
    }
}
