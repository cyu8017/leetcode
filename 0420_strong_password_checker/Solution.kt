// LeetCode 0420 - Strong Password Checker

// https://leetcode.com/problems/strong-password-checker/



class Solution {

    fun strongPasswordChecker(password: String): Int {

        val length = password.length

        var missing = 3



        if (password.any { it.isLowerCase() }) {

            missing--

        }



        if (password.any { it.isUpperCase() }) {

            missing--

        }



        if (password.any { it.isDigit() }) {

            missing--

        }



        var replace = 0

        var oneRepeat = 0

        var twoRepeat = 0

        var index = 0



        while (index < length) {

            var run = 1



            while (index + run < length && password[index + run] == password[index]) {

                run++

            }



            if (run >= 3) {

                replace += run / 3



                when (run % 3) {

                    0 -> oneRepeat++

                    1 -> twoRepeat++

                }

            }



            index += run

        }



        if (length < 6) {

            return maxOf(6 - length, missing)

        }



        if (length <= 20) {

            return maxOf(missing, replace)

        }



        var delete = length - 20

        replace -= minOf(delete, oneRepeat)

        delete -= minOf(delete, oneRepeat)

        replace -= minOf(delete / 2, twoRepeat)

        delete -= minOf(delete / 2, twoRepeat) * 2

        replace -= delete / 3



        return length - 20 + maxOf(missing, replace)

    }

}
