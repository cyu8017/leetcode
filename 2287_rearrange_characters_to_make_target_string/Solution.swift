// LeetCode 2287 - Rearrange Characters to Make Target String
// https://leetcode.com/problems/rearrange-characters-to-make-target-string/

class Solution {
    func rearrangeCharacters(_ s: String, _ target: String) -> Int {
        var sc = [Int](repeating: 0, count: 26)
        var tc = [Int](repeating: 0, count: 26)
        for c in s.utf8 { sc[Int(c - 97)] += 1 }
        for c in target.utf8 { tc[Int(c - 97)] += 1 }
        var ans = Int.max
        for i in 0..<26 where tc[i] > 0 {
            ans = min(ans, sc[i] / tc[i])
        }
        return ans
    }
}
