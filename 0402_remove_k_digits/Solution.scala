// LeetCode 0402 - Remove K Digits

// https://leetcode.com/problems/remove-k-digits/



import scala.collection.mutable



object Solution {

  def removeKdigits(num: String, k: Int): String = {

    val stack = mutable.ArrayDeque.empty[Char]

    var remaining = k



    for (digit <- num) {

      while (remaining > 0 && stack.nonEmpty && stack.last > digit) {

        stack.removeLast()

        remaining -= 1

      }

      stack += digit

    }



    while (remaining > 0 && stack.nonEmpty) {

      stack.removeLast()

      remaining -= 1

    }



    val result = stack.mkString.dropWhile(_ == '0')

    if (result.isEmpty) "0" else result

  }

}
