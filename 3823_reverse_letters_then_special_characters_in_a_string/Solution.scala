// LeetCode 3823 - Reverse Letters Then Special Characters In A String
// https://leetcode.com/problems/reverse_letters_then_special_characters_in_a_string/

object Solution {
  def reverseByType(s: String): String = {
    val a = scala.collection.mutable.ArrayBuffer.empty[Char]
    val b = scala.collection.mutable.ArrayBuffer.empty[Char]
    s.foreach { c =>
      if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')) a += c
      else b += c
    }
    var j = a.length
    var k = b.length
    val arr = s.toCharArray
    var i = 0
    while (i < arr.length) {
      if ((arr(i) >= 'A' && arr(i) <= 'Z') || (arr(i) >= 'a' && arr(i) <= 'z')) {
        j -= 1
        arr(i) = a(j)
      } else {
        k -= 1
        arr(i) = b(k)
      }
      i += 1
    }
    new String(arr)
  }
}
