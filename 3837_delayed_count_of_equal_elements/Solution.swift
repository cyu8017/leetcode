// LeetCode 3837 - Delayed Count Of Equal Elements
// https://leetcode.com/problems/delayed-count-of-equal-elements/

class Solution {
    func delayedCount(_ nums: [Int], _ k: Int) -> [Int] {
        let n = nums.count
        var cnt = [Int: Int]()
        var ans = [Int](repeating: 0, count: n)
        let start = n - k - 2
        if start >= 0 {
            for i in stride(from: start, through: 0, by: -1) {
                let key = nums[i + k + 1]
                cnt[key, default: 0] += 1
                ans[i] = cnt[nums[i], default: 0]
            }
        }
        return ans
    }
}
