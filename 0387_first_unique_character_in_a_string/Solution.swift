// LeetCode 0387 - First Unique Character in a String
// https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution {
    func firstUniqChar(_ s: String) -> Int {
        var counts: [Character: Int] = [:]
        for char in s {
            counts[char, default: 0] += 1
        }

        for (index, char) in s.enumerated() {
            if counts[char] == 1 {
                return index
            }
        }

        return -1
    }
}
