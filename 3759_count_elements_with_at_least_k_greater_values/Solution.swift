// LeetCode 3759 - Count Elements With At Least K Greater Values
// https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

class Solution {
    func countElements(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        if k == 0 { return n }
        let a = nums.sorted()
        var ans = 0
        for i in 0..<(n - k) {
            if a[n - k] > a[i] { ans += 1 }
        }
        return ans
    }
}
