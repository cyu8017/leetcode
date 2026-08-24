// LeetCode 2657 - Find the Prefix Common Array of Two Arrays
// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

object Solution {
  def findThePrefixCommonArray(A: Array[Int], B: Array[Int]): Array[Int] = {
    val n = A.length
    val seenA = new Array[Boolean](n + 1)
    val seenB = new Array[Boolean](n + 1)
    val ans = new Array[Int](n)
    var common = 0
    var i = 0
    while (i < n) {
      if (seenB(A(i))) common += 1
      seenA(A(i)) = true
      if (seenA(B(i))) common += 1
      seenB(B(i)) = true
      ans(i) = common
      i += 1
    }
    ans
  }
}
