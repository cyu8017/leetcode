// LeetCode 2627 - Debounce
// https://leetcode.com/problems/debounce/

object Solution {
  def debounce(fn: () => Unit, t: Int): () => Unit = {
    () => fn()
  }
}
