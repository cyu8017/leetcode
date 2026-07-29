// LeetCode 1090 - Largest Values From Labels
// https://leetcode.com/problems/largest-values-from-labels/

object Solution {
  def largestValsFromLabels(values: Array[Int], labels: Array[Int], numWanted: Int, useLimit: Int): Int = {
    val items = values.zip(labels).sortBy(-_._1)
    val used = scala.collection.mutable.Map.empty[Int, Int].withDefaultValue(0)
    var ans = 0
    var taken = 0
    for ((value, label) <- items if taken < numWanted) {
      if (used(label) < useLimit) {
        used(label) += 1
        ans += value
        taken += 1
      }
    }
    ans
  }
}
