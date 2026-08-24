// LeetCode 0412 - Fizz Buzz

// https://leetcode.com/problems/fizz-buzz/



class Solution {

    fun fizzBuzz(n: Int): List<String> {

        val result = mutableListOf<String>()



        for (value in 1..n) {

            when {

                value % 15 == 0 -> result.add("FizzBuzz")

                value % 3 == 0 -> result.add("Fizz")

                value % 5 == 0 -> result.add("Buzz")

                else -> result.add(value.toString())

            }

        }



        return result

    }

}
