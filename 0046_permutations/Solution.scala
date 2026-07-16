// LeetCode 0046 - Permutations
// https://leetcode.com/problems/permutations/

object Solution {
  def permute(nums: Array[Int]): List[List[Int]] = {
    val result = scala.collection.mutable.ListBuffer.empty[List[Int]]
    val path = scala.collection.mutable.ListBuffer.empty[Int]
    val used = Array.fill(nums.length)(false)

    def backtrack(): Unit = {
      if (path.length == nums.length) {
        result += path.toList
        return
      }

      for (i <- nums.indices if !used(i)) {
        used(i) = true
        path += nums(i)
        backtrack()
        path.remove(path.length - 1)
        used(i) = false
      }
    }

    backtrack()
    result.toList
  }
}
