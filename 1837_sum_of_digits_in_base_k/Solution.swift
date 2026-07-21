// LeetCode 1837 - Sum of Digits in Base K
// https://leetcode.com/problems/sum-of-digits-in-base-k/

class Solution {
    func sumBase(_ n: Int, _ k: Int) -> Int {
        var value = n
        var total = 0
        while value > 0 {
            total += value % k
            value /= k
        }
        return total
    }
}
