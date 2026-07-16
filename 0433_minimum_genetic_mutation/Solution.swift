// LeetCode 0433 - Minimum Genetic Mutation
// https://leetcode.com/problems/minimum-genetic-mutation/

class Solution {
    func minMutation(_ startGene: String, _ endGene: String, _ bank: [String]) -> Int {
        if startGene == endGene {
            return 0
        }

        let valid = Set(bank)
        if !valid.contains(endGene) {
            return -1
        }

        let genes: [Character] = ["A", "C", "G", "T"]
        var queue: [(String, Int)] = [(startGene, 0)]
        var visited: Set<String> = [startGene]

        while !queue.isEmpty {
            let (gene, steps) = queue.removeFirst()
            if gene == endGene {
                return steps
            }

            var chars = Array(gene)
            for index in chars.indices {
                let original = chars[index]
                for letter in genes where letter != original {
                    chars[index] = letter
                    let candidate = String(chars)
                    if valid.contains(candidate) && !visited.contains(candidate) {
                        visited.insert(candidate)
                        queue.append((candidate, steps + 1))
                    }
                    chars[index] = original
                }
            }
        }

        return -1
    }
}
