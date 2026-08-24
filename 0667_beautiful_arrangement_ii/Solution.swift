// LeetCode 0667 - Beautiful Arrangement II
// https://leetcode.com/problems/beautiful-arrangement-ii/

class Solution {
    func constructArray(_ n: Int, _ k: Int) -> [Int] {
        var res = Array(repeating: 0, count: n)
        var idx = 0
        if n - k >= 1 {
            for i in 1...(n - k) {
                res[idx] = i
                idx += 1
            }
        }
        var left = n - k + 1
        var right = n
        var takeHigh = true
        while left <= right {
            if takeHigh {
                res[idx] = right
                right -= 1
            } else {
                res[idx] = left
                left += 1
            }
            idx += 1
            takeHigh.toggle()
        }
        return res
    }
}
