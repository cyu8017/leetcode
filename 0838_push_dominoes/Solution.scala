// LeetCode 0838 - Push Dominoes
// https://leetcode.com/problems/push-dominoes/

object Solution {
  def pushDominoes(dominoes: String): String = {
    val arr = dominoes.toCharArray
    val n = arr.length
    val force = Array.ofDim[Int](n)
    var f = 0
    var i = 0
    while (i < n) {
      if (arr(i) == 'R') f = n
      else if (arr(i) == 'L') f = 0
      else f = math.max(f - 1, 0)
      force(i) += f
      i += 1
    }
    f = 0
    i = n - 1
    while (i >= 0) {
      if (arr(i) == 'L') f = n
      else if (arr(i) == 'R') f = 0
      else f = math.max(f - 1, 0)
      force(i) -= f
      i -= 1
    }
    i = 0
    while (i < n) {
      if (force(i) > 0) arr(i) = 'R'
      else if (force(i) < 0) arr(i) = 'L'
      else arr(i) = '.'
      i += 1
    }
    new String(arr)
  }
}
