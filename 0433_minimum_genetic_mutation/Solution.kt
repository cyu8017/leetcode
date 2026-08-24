// LeetCode 0433 - Minimum Genetic Mutation
// https://leetcode.com/problems/minimum-genetic-mutation/

class Solution {
    fun minMutation(startGene: String, endGene: String, bank: Array<String>): Int {
        if (startGene == endGene) {
            return 0
        }

        val valid = bank.toSet()
        if (endGene !in valid) {
            return -1
        }

        val queue = ArrayDeque<Pair<String, Int>>()
        queue.add(startGene to 0)
        val visited = hashSetOf(startGene)
        val genes = "ACGT"

        while (queue.isNotEmpty()) {
            val (gene, steps) = queue.removeFirst()
            if (gene == endGene) {
                return steps
            }
            val chars = gene.toCharArray()
            for (index in chars.indices) {
                val original = chars[index]
                for (letter in genes) {
                    if (letter == original) {
                        continue
                    }
                    chars[index] = letter
                    val candidate = String(chars)
                    if (candidate in valid && candidate !in visited) {
                        visited.add(candidate)
                        queue.add(candidate to steps + 1)
                    }
                }
                chars[index] = original
            }
        }

        return -1
    }
}
