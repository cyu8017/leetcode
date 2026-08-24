// LeetCode 2169 - Count Operations to Obtain Zero
// https://leetcode.com/problems/count-operations-to-obtain-zero/

class Solution {
    func countOperations(_ num1: Int, _ num2: Int) -> Int {
        var num1 = num1, num2 = num2, ans = 0
        while num1 > 0 && num2 > 0 {
            if num1 >= num2 { ans += num1 / num2; num1 %= num2 }
            else { ans += num2 / num1; num2 %= num1 }
        }
        return ans
    }
}
