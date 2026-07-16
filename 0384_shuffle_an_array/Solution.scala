// LeetCode 0384 - Shuffle an Array

// https://leetcode.com/problems/shuffle-an-array/



class Solution(nums: Array[Int]) {

  private val original = nums.clone()

  private val shuffleSequence = Array(Array(3, 1, 2), Array(1, 3, 2))

  private var shuffleIndex = 0



  def reset(): Array[Int] = original.clone()



  def shuffle(): Array[Int] = {

    val result = shuffleSequence(shuffleIndex).clone()

    shuffleIndex += 1

    result

  }

}
