// LeetCode 0344 - Reverse String

// https://leetcode.com/problems/reverse-string/



object Solution {

  def reverseString(s: Array[Char]): Unit = {

    var left = 0

    var right = s.length - 1



    while (left < right) {

      val temp = s(left)

      s(left) = s(right)

      s(right) = temp

      left += 1

      right -= 1

    }

  }

}
