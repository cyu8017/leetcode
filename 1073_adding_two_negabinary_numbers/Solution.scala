// LeetCode 1073 - Adding Two Negabinary Numbers
// https://leetcode.com/problems/adding-two-negabinary-numbers/

object Solution {
  def addNegabinary(arr1: Array[Int], arr2: Array[Int]): Array[Int] = {
    var i = arr1.length - 1
    var j = arr2.length - 1
    var carry = 0
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    while (i >= 0 || j >= 0 || carry != 0) {
      var total = carry
      if (i >= 0) { total += arr1(i); i -= 1 }
      if (j >= 0) { total += arr2(j); j -= 1 }
      ans += (total & 1)
      carry = -(total >> 1)
    }
    while (ans.length > 1 && ans.last == 0) ans.remove(ans.length - 1)
    ans.reverse.toArray
  }
}
