// LeetCode 0403 - Frog Jump

// https://leetcode.com/problems/frog-jump/



import scala.collection.mutable



object Solution {

  def canCross(stones: Array[Int]): Boolean = {

    val stoneSet = stones.toSet

    val jumps = mutable.Map.from(stones.map(stone => stone -> mutable.Set.empty[Int]))

    jumps(0).add(0)



    for (stone <- stones) {

      for (jump <- jumps(stone).toSeq) {

        for (nextJump <- Seq(jump - 1, jump, jump + 1)) {

          if (nextJump > 0) {

            val nextStone = stone + nextJump

            if (stoneSet.contains(nextStone)) {

              jumps.getOrElseUpdate(nextStone, mutable.Set.empty[Int]).add(nextJump)

            }

          }

        }

      }

    }



    jumps(stones.last).nonEmpty

  }

}
