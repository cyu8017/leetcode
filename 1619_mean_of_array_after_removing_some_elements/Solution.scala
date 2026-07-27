// LeetCode 1619 - Mean of Array After Removing Some Elements
// https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

object Solution {
  def trimMean(arr: Array[Int]): Double = {
    val sorted = arr.sorted
    val k = sorted.length / 20
    sorted.slice(k, sorted.length - k).sum.toDouble / (sorted.length - 2 * k)
  }
}
