// LeetCode 0345 - Reverse Vowels of a String

// https://leetcode.com/problems/reverse-vowels-of-a-string/



object Solution {

  private val vowels = Set('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')



  def reverseVowels(s: String): String = {

    val chars = s.toCharArray

    var left = 0

    var right = chars.length - 1



    while (left < right) {

      while (left < right && !vowels.contains(chars(left))) {

        left += 1

      }

      while (left < right && !vowels.contains(chars(right))) {

        right -= 1

      }

      val temp = chars(left)

      chars(left) = chars(right)

      chars(right) = temp

      left += 1

      right -= 1

    }



    new String(chars)

  }

}
