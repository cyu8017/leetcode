// LeetCode 1897 - Redistribute Characters to Make All Strings Equal
// https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

class Solution {
    func makeEqual(_ words: [String]) -> Bool {
        var counts = [Character: Int]()
        for word in words {
            for char in word {
                counts[char, default: 0] += 1
            }
        }
        let n = words.count
        return counts.values.allSatisfy { $0 % n == 0 }
    }
}
