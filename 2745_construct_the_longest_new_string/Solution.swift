// LeetCode 2745 - Construct the Longest New String
// https://leetcode.com/problems/construct-the-longest-new-string/

class Solution {
    func longestString(_ x: Int, _ y: Int, _ z: Int) -> Int {
        if x < y { return (2 * x + 1 + z) * 2 }
        if y < x { return (2 * y + 1 + z) * 2 }
        return (x + y + z) * 2
    }
}
