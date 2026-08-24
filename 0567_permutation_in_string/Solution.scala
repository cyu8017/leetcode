// LeetCode 0567 - Permutation in String
// https://leetcode.com/problems/permutation-in-string/

object Solution {
  def checkInclusion(s1: String, s2: String): Boolean = {
    val n1 = s1.length
    val n2 = s2.length
    if (n1 > n2) return false
    val need = Array.fill(26)(0)
    val window = Array.fill(26)(0)
    var i = 0
    while (i < n1) {
      need(s1.charAt(i) - 'a') += 1
      window(s2.charAt(i) - 'a') += 1
      i += 1
    }
    var matches = 0
    i = 0
    while (i < 26) {
      if (need(i) == window(i)) matches += 1
      i += 1
    }
    if (matches == 26) return true
    var right = n1
    while (right < n2) {
      val add = s2.charAt(right) - 'a'
      val remove = s2.charAt(right - n1) - 'a'
      if (window(add) == need(add)) matches -= 1
      window(add) += 1
      if (window(add) == need(add)) matches += 1
      if (window(remove) == need(remove)) matches -= 1
      window(remove) -= 1
      if (window(remove) == need(remove)) matches += 1
      if (matches == 26) return true
      right += 1
    }
    false
  }
}
