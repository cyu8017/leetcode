// LeetCode 0394 - Decode String

// https://leetcode.com/problems/decode-string/



import scala.collection.mutable



object Solution {

  def decodeString(s: String): String = {

    val stack = mutable.ArrayStack.empty[(String, Int)]

    var current = new StringBuilder

    var number = 0



    for (character <- s) {

      if (character.isDigit) {

        number = number * 10 + character.asDigit

      } else if (character == '[') {

        stack.push((current.toString, number))

        current = new StringBuilder

        number = 0

      } else if (character == ']') {

        val (previous, count) = stack.pop()

        current = new StringBuilder(previous).append(current.toString * count)

      } else {

        current.append(character)

      }

    }



    current.toString

  }

}
