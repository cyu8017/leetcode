// LeetCode 2433 - Find The Original Array of Prefix Xor
// https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

object Solution {
  def findArray(pref: Array[Int]): Array[Int] = {
    val ans = new Array[Int](pref.length)
    ans(0) = pref(0)
    var i = 1
    while (i < pref.length) {
      ans(i) = pref(i) ^ pref(i - 1)
      i += 1
    }
    ans
  }
}
