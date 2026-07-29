// LeetCode 1017 - Convert to Base -2
// https://leetcode.com/problems/convert-to-base-2/

class Solution {
    func baseNeg2(_ n: Int) -> String {
        if n == 0 { return "0" }
        var n = n
        var ans = [Character]()
        while n != 0 {
            var rem = n % -2
            n /= -2
            if rem < 0 {
                n += 1
                rem += 2
            }
            ans.append(Character(String(rem)))
        }
        return String(ans.reversed())
    }
}
