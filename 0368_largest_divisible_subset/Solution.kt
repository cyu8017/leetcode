// LeetCode 0368 - Largest Divisible Subset

// https://leetcode.com/problems/largest-divisible-subset/



class Solution {

    fun largestDivisibleSubset(nums: IntArray): List<Int> {

        val sorted = nums.sorted()

        val chains = sorted.associateWith { mutableListOf(it) }.toMutableMap()

        var best = emptyList<Int>()



        for (num in sorted) {

            for (prev in chains.keys) {

                if (prev < num && num % prev == 0 && chains[prev]!!.size + 1 > chains[num]!!.size) {

                    chains[num] = (chains[prev]!! + num).toMutableList()

                }

            }

            if (chains[num]!!.size > best.size) {

                best = chains[num]!!

            }

        }



        return best

    }

}
