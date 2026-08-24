// LeetCode 3781 - Maximum Score After Binary Swaps
// https://leetcode.com/problems/maximum-score-after-binary-swaps/

class Solution {
    func maximumScore(_ nums: [Int], _ s: String) -> Int {
        let chars = Array(s)
        var ans = 0
        var pq = [Int]()
        for i in 0..<nums.count {
            pq.append(nums[i])
            pq.sort(by: >)
            if chars[i] == "1" {
                ans += pq.removeFirst()
            }
        }
        return ans
    }
}
