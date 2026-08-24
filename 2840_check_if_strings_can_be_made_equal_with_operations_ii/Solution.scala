// LeetCode 2840 - Check if Strings Can be Made Equal With Operations II
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

object Solution {
  def checkStrings(s1: String, s2: String): Boolean = {
    val even1 = Array.fill(26)(0)
    val odd1 = Array.fill(26)(0)
    val even2 = Array.fill(26)(0)
    val odd2 = Array.fill(26)(0)
    for (i <- s1.indices) {
      if (i % 2 == 0) {
        even1(s1.charAt(i) - 'a') += 1
        even2(s2.charAt(i) - 'a') += 1
      } else {
        odd1(s1.charAt(i) - 'a') += 1
        odd2(s2.charAt(i) - 'a') += 1
      }
    }
    even1.sameElements(even2) && odd1.sameElements(odd2)
  }
}
