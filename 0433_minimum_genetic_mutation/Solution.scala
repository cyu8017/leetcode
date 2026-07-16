// LeetCode 0433 - Minimum Genetic Mutation
// https://leetcode.com/problems/minimum-genetic-mutation/

import scala.collection.mutable

object Solution {
  def minMutation(startGene: String, endGene: String, bank: Array[String]): Int = {
    if (startGene == endGene) {
      return 0
    }

    val valid = bank.toSet
    if (!valid.contains(endGene)) {
      return -1
    }

    val genes = "ACGT"
    val queue = mutable.Queue((startGene, 0))
    val visited = mutable.Set(startGene)

    while (queue.nonEmpty) {
      val (gene, steps) = queue.dequeue()
      if (gene == endGene) {
        return steps
      }

      val chars = gene.toCharArray
      for (index <- chars.indices) {
        val original = chars(index)
        for (letter <- genes) {
          if (letter != original) {
            chars(index) = letter
            val candidate = new String(chars)
            if (valid.contains(candidate) && !visited.contains(candidate)) {
              visited.add(candidate)
              queue.enqueue((candidate, steps + 1))
            }
            chars(index) = original
          }
        }
      }
    }

    -1
  }
}
