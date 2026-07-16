// LeetCode 0127 - Word Ladder
// https://leetcode.com/problems/word-ladder/

class Solution {
    func ladderLength(_ beginWord: String, _ endWord: String, _ wordList: [String]) -> Int {
        let words = Set(wordList)
        guard words.contains(endWord) else { return 0 }

        var queue = [(beginWord, 1)]
        var head = 0
        var visited: Set<String> = [beginWord]
        while head < queue.count {
            let (word, steps) = queue[head]
            head += 1
            if word == endWord { return steps }

            var characters = Array(word)
            for index in characters.indices {
                let original = characters[index]
                for scalar in UInt8(ascii: "a")...UInt8(ascii: "z") {
                    characters[index] = Character(UnicodeScalar(scalar))
                    let next = String(characters)
                    if words.contains(next) && visited.insert(next).inserted {
                        queue.append((next, steps + 1))
                    }
                }
                characters[index] = original
            }
        }
        return 0
    }
}