// LeetCode 3223 - Minimum Length of String After Operations
// https://leetcode.com/problems/minimum-length-of-string-after-operations/

class Solution {
    func minimumLength(_ s: String) -> Int {
        var cnt = Array(repeating: 0, count: 26)
        let a = Character("a").asciiValue!
        for c in s { cnt[Int(c.asciiValue! - a)] += 1 }
        var ans = 0
        for x in cnt where x > 0 { ans += (x & 1) != 0 ? 1 : 2 }
        return ans
    }
}
