// LeetCode 0403 - Frog Jump

// https://leetcode.com/problems/frog-jump/



class Solution {

    fun canCross(stones: IntArray): Boolean {

        val stoneSet = stones.toSet()

        val jumps = stones.associateWith { mutableSetOf<Int>() }.toMutableMap()

        jumps[0]!!.add(0)



        for (stone in stones) {

            for (jump in jumps[stone]!!) {

                for (nextJump in intArrayOf(jump - 1, jump, jump + 1)) {

                    if (nextJump > 0) {

                        val nextStone = stone + nextJump

                        if (nextStone in stoneSet) {

                            jumps.getOrPut(nextStone) { mutableSetOf() }.add(nextJump)

                        }

                    }

                }

            }

        }



        return jumps[stones.last()]!!.isNotEmpty()

    }

}
