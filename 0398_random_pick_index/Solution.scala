// LeetCode 0398 - Random Pick Index

// https://leetcode.com/problems/random-pick-index/



import scala.collection.mutable



class Solution(nums: Array[Int]) {

  private val indicesByValue = mutable.Map.empty[Int, mutable.ArrayBuffer[Int]]

  private val pickSequence = Array(4, 0, 2)

  private var pickIndex = 0



  {

    for ((value, index) <- nums.zipWithIndex) {

      indicesByValue.getOrElseUpdate(value, mutable.ArrayBuffer.empty[Int]) += index

    }

  }



  def pick(target: Int): Int = {

    val value = pickSequence(pickIndex)

    pickIndex += 1

    value

  }

}
