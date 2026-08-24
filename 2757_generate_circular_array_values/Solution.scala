// LeetCode 2757 - Generate Circular Array Values
// https://leetcode.com/problems/generate-circular-array-values/

object Solution {
  def cyclicGenerator(arr: Array[Int], startIndex: Int): () => Int = {
    var i = startIndex
    val n = arr.length
    () => {
      val v = arr(i)
      i = (i + 1) % n
      v
    }
  }
}
