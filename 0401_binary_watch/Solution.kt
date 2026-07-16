// LeetCode 0401 - Binary Watch

// https://leetcode.com/problems/binary-watch/



class Solution {

    fun readBinaryWatch(turnedOn: Int): List<String> {

        val result = mutableListOf<String>()



        for (hour in 0 until 12) {

            for (minute in 0 until 60) {

                if (Integer.bitCount(hour) + Integer.bitCount(minute) == turnedOn) {

                    result.add("$hour:${minute.toString().padStart(2, '0')}")

                }

            }

        }



        return result

    }

}
