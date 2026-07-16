// LeetCode 0126 - Word Ladder II
// https://leetcode.com/problems/word-ladder-ii/

class Solution {
    func findLadders(_ beginWord: String, _ endWord: String, _ wordList: [String]) -> [[String]] {
        let words = Set(wordList)
        guard words.contains(endWord) else { return [] }

        var parents = [String: [String]]()
        var visited: Set<String> = [beginWord]
        var queue = [beginWord]
        var found = false

        while !queue.isEmpty && !found {
            var nextQueue = [String]()
            var levelVisited = Set<String>()
            for word in queue {
                var characters = Array(word)
                for index in characters.indices {
                    let original = characters[index]
                    for scalar in UInt8(ascii: "a")...UInt8(ascii: "z") {
                        characters[index] = Character(UnicodeScalar(scalar))
                        let next = String(characters)
                        guard words.contains(next), !visited.contains(next) else { continue }
                        if levelVisited.insert(next).inserted {
                            nextQueue.append(next)
                        }
                        parents[next, default: []].append(word)
                        if next == endWord { found = true }
                    }
                    characters[index] = original
                }
            }
            visited.formUnion(levelVisited)
            queue = nextQueue
        }

        guard found else { return [] }
        var results = [[String]]()
        func build(_ word: String, _ path: [String]) {
            if word == beginWord {
                results.append(Array(path.reversed()))
                return
            }
            for parent in parents[word, default: []] {
                build(parent, path + [parent])
            }
        }
        build(endWord, [endWord])
        return results.sorted { $0.lexicographicallyPrecedes($1) }
    }
}