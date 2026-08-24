// LeetCode 3437 - Permutations III
// https://leetcode.com/problems/permutations-iii/

object Solution {
  def permute(n: Int): Array[Array[Int]] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    val used = new Array[Boolean](n + 1)
    val cur = scala.collection.mutable.ArrayBuffer.empty[Int]
    dfs(n, used, cur, ans)
    ans.toArray
  }

  private def dfs(n: Int, used: Array[Boolean], cur: scala.collection.mutable.ArrayBuffer[Int], ans: scala.collection.mutable.ArrayBuffer[Array[Int]]): Unit = {
    if (cur.length == n) {
      ans += cur.toArray
      return
    }
    var i = 1
    while (i <= n) {
      if (!used(i) && (cur.isEmpty || cur.last % 2 != i % 2)) {
        used(i) = true
        cur += i
        dfs(n, used, cur, ans)
        cur.remove(cur.length - 1)
        used(i) = false
      }
      i += 1
    }
  }
}
