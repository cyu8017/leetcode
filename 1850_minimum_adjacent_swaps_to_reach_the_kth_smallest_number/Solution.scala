// LeetCode 1850 - Minimum Adjacent Swaps to Reach the Kth Smallest Number
// https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

object Solution {
  def getMinSwaps(num: String, k: Int): Int = {
    def nextPermutation(arr: Array[Char]): Unit = {
      var i = arr.length - 2
      while (i >= 0 && arr(i) >= arr(i + 1)) i -= 1
      if (i < 0) {
        var l = 0
        var r = arr.length - 1
        while (l < r) {
          val t = arr(l); arr(l) = arr(r); arr(r) = t
          l += 1; r -= 1
        }
        return
      }
      var j = arr.length - 1
      while (arr(j) <= arr(i)) j -= 1
      val tmp = arr(i); arr(i) = arr(j); arr(j) = tmp
      var l = i + 1
      var r = arr.length - 1
      while (l < r) {
        val t = arr(l); arr(l) = arr(r); arr(r) = t
        l += 1; r -= 1
      }
    }

    val target = num.toArray
    for (_ <- 0 until k) nextPermutation(target)
    val source = num.toArray
    var swaps = 0
    for (i <- source.indices if source(i) != target(i)) {
      var j = i
      while (source(j) != target(i)) j += 1
      while (j > i) {
        val t = source(j); source(j) = source(j - 1); source(j - 1) = t
        swaps += 1
        j -= 1
      }
    }
    swaps
  }
}
