// LeetCode 0393 - UTF-8 Validation

// https://leetcode.com/problems/utf-8-validation/



class Solution {

    fun validUtf8(data: IntArray): Boolean {

        var remaining = 0



        for (value in data) {

            val byteValue = value and 0xFF



            if (remaining == 0) {

                when {

                    byteValue shr 7 == 0b0 -> continue

                    byteValue shr 5 == 0b110 -> remaining = 1

                    byteValue shr 4 == 0b1110 -> remaining = 2

                    byteValue shr 3 == 0b11110 -> remaining = 3

                    else -> return false

                }

            } else {

                if (byteValue shr 6 != 0b10) {

                    return false

                }

                remaining--

            }

        }



        return remaining == 0

    }

}
