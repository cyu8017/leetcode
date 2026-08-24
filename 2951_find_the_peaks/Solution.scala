// LeetCode 2951 - Find the Peaks
// https://leetcode.com/problems/find-the-peaks/

object Solution {
  def findPeaks(mountain: Array[Int]): List[Int] = {
    val ans = scala.collection.mutable.ListBuffer.empty[Int]
    var i = 1
    while (i + 1 < mountain.length) {
      if (mountain(i) > mountain(i - 1) && mountain(i) > mountain(i + 1)) ans += i
      i += 1
    }
    ans.toList
  }
}
