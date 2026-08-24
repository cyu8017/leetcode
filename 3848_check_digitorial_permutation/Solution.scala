// LeetCode 3848 - Check Digitorial Permutation
// https://leetcode.com/problems/check-digitorial-permutation/

object Solution {
  def isDigitorialPermutation(n: Int): Boolean = {
    val f = new Array[Int](10)
    f(0) = 1
    var i = 1
    while (i < 10) {
      f(i) = f(i - 1) * i
      i += 1
    }
    var x = 0
    var y = n
    while (y > 0) {
      x += f(y % 10)
      y /= 10
    }
    val a = x.toString.toCharArray.sorted
    val b = n.toString.toCharArray.sorted
    a.sameElements(b)
  }
}
