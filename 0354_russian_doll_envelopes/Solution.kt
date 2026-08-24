// LeetCode 0354 - Russian Doll Envelopes

// https://leetcode.com/problems/russian-doll-envelopes/



class Solution {

    fun maxEnvelopes(envelopes: Array<IntArray>): Int {

        envelopes.sortWith(compareBy<IntArray> { it[0] }.thenByDescending { it[1] })



        val tails = mutableListOf<Int>()

        for ((_, height) in envelopes) {

            val index = tails.binarySearch(height).let {

                if (it >= 0) it else -it - 1

            }

            if (index == tails.size) {

                tails.add(height)

            } else {

                tails[index] = height

            }

        }



        return tails.size

    }

}
