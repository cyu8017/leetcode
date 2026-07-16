// LeetCode 0258 - Add Digits
// https://leetcode.com/problems/add-digits/

class Solution {
    func addDigits(_ num: Int) -> Int {
        if num == 0 {
            return 0
        }
        return 1 + (num - 1) % 9
    }
}
