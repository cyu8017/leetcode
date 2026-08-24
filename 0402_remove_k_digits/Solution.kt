// LeetCode 0402 - Remove K Digits

// https://leetcode.com/problems/remove-k-digits/



class Solution {

    fun removeKdigits(num: String, k: Int): String {

        val stack = ArrayDeque<Char>()

        var remaining = k



        for (digit in num) {

            while (remaining > 0 && stack.isNotEmpty() && stack.last() > digit) {

                stack.removeLast()

                remaining--

            }

            stack.addLast(digit)

        }



        while (remaining > 0 && stack.isNotEmpty()) {

            stack.removeLast()

            remaining--

        }



        val result = stack.joinToString("").trimStart('0')

        return result.ifEmpty { "0" }

    }

}
