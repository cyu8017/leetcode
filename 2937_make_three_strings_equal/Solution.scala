// LeetCode 2937 - Make Three Strings Equal
// https://leetcode.com/problems/make-three-strings-equal/

object Solution {
  def findMinimumOperations(s1: String, s2: String, s3: String): Int = {
    val n = math.min(s1.length, math.min(s2.length, s3.length))
    var i = 0
    while (i < n && s1.charAt(i) == s2.charAt(i) && s2.charAt(i) == s3.charAt(i)) i += 1
    if (i == 0) -1 else s1.length + s2.length + s3.length - 3 * i
  }
}
