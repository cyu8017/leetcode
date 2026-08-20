// LeetCode 1181 - Before and After Puzzle
// https://leetcode.com/problems/before-and-after-puzzle/

class Solution {
    func beforeAndAfterPuzzles(_ phrases: [String]) -> [String] {
        let split = phrases.map { $0.split(separator: " ").map(String.init) }
        var result = Set<String>()
        for i in 0..<split.count {
            for j in 0..<split.count where i != j {
                if split[i].last! == split[j][0] {
                    var parts = split[i]
                    parts.append(contentsOf: split[j].dropFirst())
                    result.insert(parts.joined(separator: " "))
                }
            }
        }
        return result.sorted()
    }
}
