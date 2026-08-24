// LeetCode 2805 - Custom Interval
// https://leetcode.com/problems/custom-interval/

class Solution {
    func customInterval(_ fn: @escaping () -> Void, _ delay: Int, _ period: Int) -> () -> Void {
        var cancelled = false
        return { cancelled = true }
    }
}
