// LeetCode 2090 - K Radius Subarray Averages
// https://leetcode.com/problems/k-radius-subarray-averages/

class Solution {
    func getAverages(_ nums: [Int], _ k: Int) -> [Int] {
        let n = nums.count
        var ans = [Int](repeating: -1, count: n)
        if 2 * k + 1 > n { return ans }
        var sum = 0
        for i in 0..<(2 * k + 1) { sum += nums[i] }
        ans[k] = sum / (2 * k + 1)
        var i = k + 1
        while i + k < n {
            sum += nums[i + k] - nums[i - k - 1]
            ans[i] = sum / (2 * k + 1)
            i += 1
        }
        return ans
    }
}
