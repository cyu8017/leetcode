// LeetCode 2938 - Separate Black and White Balls
// https://leetcode.com/problems/separate-black-and-white-balls/

class Solution {
    func minimumSteps(_ s: String) -> Int {
        var ans = 0, zeros = 0
        for ch in s.reversed() {
            if ch == "0" { zeros += 1 }
            else { ans += zeros }
        }
        return ans
    }
}
