// LeetCode 0394 - Decode String

// https://leetcode.com/problems/decode-string/



class Solution {

    fun decodeString(s: String): String {

        val stack = ArrayDeque<Pair<String, Int>>()

        var current = StringBuilder()

        var number = 0



        for (character in s) {

            if (character.isDigit()) {

                number = number * 10 + character.digitToInt()

            } else if (character == '[') {

                stack.addLast(current.toString() to number)

                current = StringBuilder()

                number = 0

            } else if (character == ']') {

                val (previous, count) = stack.removeLast()

                current = StringBuilder(previous).append(current.toString().repeat(count))

            } else {

                current.append(character)

            }

        }



        return current.toString()

    }

}
