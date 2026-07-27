// LeetCode 1663 - Smallest String With A Given Numeric Value
// https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution {
    func getSmallestString(_ n: Int, _ k: Int) -> String {
        var a = Array(repeating: Character("a"), count: n)
        var k = k - n
        for i in stride(from: n - 1, through: 0, by: -1) {
            let d = min(25, k)
            a[i] = Character(UnicodeScalar(97 + d)!)
            k -= d
        }
        return String(a)
    }
}
