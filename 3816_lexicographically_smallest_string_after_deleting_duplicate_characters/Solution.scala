// LeetCode 3816 - Lexicographically Smallest String After Deleting Duplicate Characters
// https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/

object Solution {
  def lexSmallestAfterDeletion(s: String): String = {
    val cnt = new Array[Int](26)
    s.foreach(c => cnt(c - 'a') += 1)
    val stk = new StringBuilder
    s.foreach { c =>
      while (stk.length > 0 && stk.charAt(stk.length - 1) > c
          && cnt(stk.charAt(stk.length - 1) - 'a') > 1) {
        cnt(stk.charAt(stk.length - 1) - 'a') -= 1
        stk.deleteCharAt(stk.length - 1)
      }
      stk.append(c)
    }
    while (cnt(stk.charAt(stk.length - 1) - 'a') > 1) {
      cnt(stk.charAt(stk.length - 1) - 'a') -= 1
      stk.deleteCharAt(stk.length - 1)
    }
    stk.toString
  }
}
