// LeetCode 3168 - Minimum Number of Chairs in a Waiting Room
// https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

class Solution {
    func minimumChairs(_ s: String) -> Int {
        var cnt = 0, left = 0
        for c in s {
            if c == "E" {
                if left > 0 { left -= 1 }
                else { cnt += 1 }
            } else {
                left += 1
            }
        }
        return cnt
    }
}
