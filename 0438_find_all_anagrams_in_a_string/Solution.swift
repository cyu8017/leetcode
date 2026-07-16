// LeetCode 0438 - Find All Anagrams in a String
// https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution {
    func findAnagrams(_ s: String, _ p: String) -> [Int] {
        if p.count > s.count {
            return []
        }

        var need = Array(repeating: 0, count: 26)
        var window = Array(repeating: 0, count: 26)
        for char in p {
            need[Int(char.asciiValue! - Character("a").asciiValue!)] += 1
        }

        let chars = Array(s)
        var result: [Int] = []
        var left = 0
        for right in chars.indices {
            window[Int(chars[right].asciiValue! - Character("a").asciiValue!)] += 1
            if right - left + 1 > p.count {
                window[Int(chars[left].asciiValue! - Character("a").asciiValue!)] -= 1
                left += 1
            }
            if window == need {
                result.append(left)
            }
        }
        return result
    }
}
