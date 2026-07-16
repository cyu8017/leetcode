// LeetCode 0187 - Repeated DNA Sequences
// https://leetcode.com/problems/repeated-dna-sequences/

class Solution {
    func findRepeatedDnaSequences(_ s: String) -> [String] {
        let characters = Array(s)
        guard characters.count >= 10 else {
            return []
        }
        var seen = Set<String>()
        var repeated = Set<String>()

        for index in 0..<(characters.count - 9) {
            let sequence = String(characters[index..<(index + 10)])
            if seen.contains(sequence) {
                repeated.insert(sequence)
            } else {
                seen.insert(sequence)
            }
        }

        return Array(repeated)
    }
}