// LeetCode 3866 - First Unique Even Element
// https://leetcode.com/problems/first-unique-even-element/

object Solution {
  def firstUniqueEven(nums: Array[Int]): Int = {
    val cnt = new Array[Int](101)
    nums.foreach { x => cnt(x) += 1 }
    nums.foreach { x =>
      if (x % 2 == 0 && cnt(x) == 1) return x
    }
    -1
  }
}
