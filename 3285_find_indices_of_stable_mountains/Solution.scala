// LeetCode 3285 - Find Indices of Stable Mountains
// https://leetcode.com/problems/find-indices-of-stable-mountains/

object Solution {
  def stableMountains(height: Array[Int], threshold: Int): Array[Int] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 1
    while (i < height.length) {
      if (height(i - 1) > threshold) ans += i
      i += 1
    }
    ans.toArray
  }
}
