// LeetCode 1538 - Guess the Majority in a Hidden Array
// https://leetcode.com/problems/guess-the-majority-in-a-hidden-array/

trait ArrayReader {
  def query(a: Int, b: Int, c: Int, d: Int): Int
  def length(): Int
}

object Solution {
  def guessMajority(nums: Array[Int]): Int = {
    val reader = new ArrayReader {
      def query(a: Int, b: Int, c: Int, d: Int): Int = {
        val ones = nums(a) + nums(b) + nums(c) + nums(d)
        if (ones == 0 || ones == 4) 4 else if (ones == 1 || ones == 3) 2 else 0
      }
      def length(): Int = nums.length
    }
    guessMajority(reader)
  }

  def guessMajority(reader: ArrayReader): Int = {
    val n = reader.length()
    val firstFour = reader.query(0, 1, 2, 3)
    val shifted = reader.query(1, 2, 3, 4)
    var same = 1
    var different = 0
    var differentIndex = -1
    var laterDifferent = -1
    val fourSame = firstFour == shifted
    if (fourSame) same += 1
    else { different += 1; differentIndex = 4 }
    val checks = Array((0, 2, 3, 4), (0, 1, 3, 4), (0, 1, 2, 4))
    for ((args, index) <- checks.zipWithIndex) {
      if (reader.query(args._1, args._2, args._3, args._4) == shifted) same += 1
      else { different += 1; differentIndex = index + 1 }
    }
    for (i <- 5 until n) {
      val iSameAsFour = reader.query(1, 2, 3, i) == shifted
      if (iSameAsFour == fourSame) same += 1
      else {
        different += 1
        differentIndex = i
        if (laterDifferent == -1) laterDifferent = i
      }
    }
    if (same == different) -1
    else if (same > different) 0
    else if (laterDifferent != -1) laterDifferent
    else differentIndex
  }
}
