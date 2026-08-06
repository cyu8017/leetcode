// LeetCode 1925 - Count Square Sum Triples
// https://leetcode.com/problems/count-square-sum-triples/

object Solution {
  def countTriples(n: Int): Int = {
    val squares = (1 to n).map(i => i * i).toSet
    var ans = 0
    for (a <- 1 to n; b <- 1 to n) {
      if (squares.contains(a * a + b * b)) ans += 1
    }
    ans
  }
}
