// LeetCode 0244 - Shortest Word Distance II
// https://leetcode.com/problems/shortest-word-distance-ii/

class WordDistance {
    private var positions: [String: [Int]] = [:]

    init(_ wordsDict: [String]) {
        for (index, word) in wordsDict.enumerated() {
            positions[word, default: []].append(index)
        }
    }

    func shortest(_ word1: String, _ word2: String) -> Int {
        let left = positions[word1]!
        let right = positions[word2]!
        var i = 0
        var j = 0
        var best = Int.max
        while i < left.count && j < right.count {
            best = min(best, abs(left[i] - right[j]))
            if left[i] <= right[j] {
                i += 1
            } else {
                j += 1
            }
        }
        return best
    }
}
