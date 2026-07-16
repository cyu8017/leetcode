// LeetCode 0336 - Palindrome Pairs
// https://leetcode.com/problems/palindrome-pairs/

class Solution {
    func palindromePairs(_ words: [String]) -> [[Int]] {
        var wordMap: [String: Int] = [:]
        for (index, word) in words.enumerated() {
            wordMap[word] = index
        }
        var result = Set<[Int]>()

        for (index, word) in words.enumerated() {
            for split in 0...word.count {
                let left = String(word.prefix(split))
                let right = String(word.suffix(word.count - split))
                if left == String(left.reversed()) {
                    let reversedRight = String(right.reversed())
                    if let other = wordMap[reversedRight], other != index {
                        result.insert([other, index])
                    }
                }
                if right == String(right.reversed()) {
                    let reversedLeft = String(left.reversed())
                    if let other = wordMap[reversedLeft], other != index {
                        result.insert([index, other])
                    }
                }
            }
        }

        return result.sorted {
            if $0[0] != $1[0] {
                return $0[0] < $1[0]
            }
            return $0[1] < $1[1]
        }
    }
}
