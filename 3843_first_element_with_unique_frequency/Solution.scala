// LeetCode 3843 - First Element With Unique Frequency
// https://leetcode.com/problems/first-element-with-unique-frequency/

object Solution {
  def firstUniqueFreq(nums: Array[Int]): Int = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    nums.foreach { x => cnt(x) = cnt.getOrElse(x, 0) + 1 }
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    cnt.values.foreach { v => freq(v) = freq.getOrElse(v, 0) + 1 }
    nums.foreach { x =>
      if (freq(cnt(x)) == 1) return x
    }
    -1
  }
}
