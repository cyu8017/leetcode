// LeetCode 0342 - Power of Four
// https://leetcode.com/problems/power-of-four/

class Solution {
    func isPowerOfFour(_ n: Int) -> Bool {
        n > 0 && (n & (n - 1)) == 0 && n % 3 == 1
    }
}
