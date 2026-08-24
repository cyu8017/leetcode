// LeetCode 2177 - Find Three Consecutive Integers That Sum to a Given Number
// https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

object Solution {
  def sumOfThree(num: Long): Array[Long] = {
    if (num % 3 != 0) Array.empty[Long]
    else {
      val x = num / 3
      Array(x - 1, x, x + 1)
    }
  }
}
