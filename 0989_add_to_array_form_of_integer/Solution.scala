// LeetCode 0989 - Add to Array-Form of Integer
// https://leetcode.com/problems/add-to-array-form-of-integer/

object Solution {
  def addToArrayForm(num: Array[Int], k: Int): List[Int] = {
    val list = scala.collection.mutable.ArrayBuffer(num: _*)
    var carry = k
    var i = list.length - 1
    while (carry > 0 || i >= 0) {
      if (i >= 0) {
        carry += list(i)
        list(i) = carry % 10
        i -= 1
      } else {
        list.prepend(carry % 10)
      }
      carry /= 10
    }
    list.toList
  }
}
