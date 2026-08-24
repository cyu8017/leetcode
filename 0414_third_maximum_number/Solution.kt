// LeetCode 0414 - Third Maximum Number

// https://leetcode.com/problems/third-maximum-number/



class Solution {

    fun thirdMax(nums: IntArray): Int {

        var first: Int? = null

        var second: Int? = null

        var third: Int? = null



        for (value in nums) {

            if (value == first || value == second || value == third) {

                continue

            }



            when {

                first == null || value > first -> {

                    third = second

                    second = first

                    first = value

                }

                second == null || value > second -> {

                    third = second

                    second = value

                }

                third == null || value > third -> {

                    third = value

                }

            }

        }



        return third ?: first!!

    }

}
