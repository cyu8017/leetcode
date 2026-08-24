// LeetCode 4000 - Largest Integer With Given Digit Sum
// https://leetcode.com/problems/largest-integer-with-given-digit-sum/


class Solution {
    func largestInteger(_ n: Int, _ s: Int) -> Int {
        if n * 9 < s { return -1 }
        var s = s, ans = 0
        for _ in 0..<n {
            let x = s < 9 ? s : 9
            ans = ans * 10 + x
            s -= x
        }
        return ans
    }
}
