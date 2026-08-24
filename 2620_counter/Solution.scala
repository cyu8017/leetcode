// LeetCode 2620 - Counter
// https://leetcode.com/problems/counter/

object Solution {
  def createCounter(n: Int): () => Int = {
    var cur = n
    () => {
      val v = cur
      cur += 1
      v
    }
  }
}
