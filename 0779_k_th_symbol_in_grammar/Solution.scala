// LeetCode 0779 - K-th Symbol in Grammar
// https://leetcode.com/problems/k-th-symbol-in-grammar/

object Solution {
  def kthGrammar(n: Int, k: Int): Int = {
    if (n == 1) 0
    else {
      val mid = 1 << (n - 2)
      if (k <= mid) kthGrammar(n - 1, k)
      else 1 - kthGrammar(n - 1, k - mid)
    }
  }
}
