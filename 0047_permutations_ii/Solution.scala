// LeetCode 0047 - Permutations II
// https://leetcode.com/problems/permutations-ii/

object Solution {
  def permuteUnique(nums: Array[Int]): List[List[Int]] = {
    val sorted = nums.sorted
    val result = scala.collection.mutable.ListBuffer.empty[List[Int]]
    val path = scala.collection.mutable.ArrayBuffer.empty[Int]
    val used = Array.fill(sorted.length)(false)

    def backtrack(): Unit = {
      if (path.length == sorted.length) {
        result += path.toList
        return
      }

      for (i <- sorted.indices) {
        if (!used(i) && (i == 0 || sorted(i) != sorted(i - 1) || used(i - 1))) {
          used(i) = true
          path += sorted(i)
          backtrack()
          path.remove(path.length - 1)
          used(i) = false
        }
      }
    }

    backtrack()
    result.toList
  }
}
