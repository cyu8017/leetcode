// LeetCode 1876 - Substrings of Size Three with Distinct Characters
// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution {
    func countGoodSubstrings(_ s: String) -> Int {
        let chars = Array(s)
        if chars.count < 3 {
            return 0
        }

        var count = 0
        for i in 0...(chars.count - 3) {
            let window = chars[i..<(i + 3)]
            if Set(window).count == 3 {
                count += 1
            }
        }
        return count
    }
}
