// LeetCode 1093 - Statistics from a Large Sample
// https://leetcode.com/problems/statistics-from-a-large-sample/

object Solution {
  def sampleStats(count: Array[Int]): Array[Double] = {
    val total = count.sum.toLong
    val minimum = count.indexWhere(_ > 0)
    val maximum = count.lastIndexWhere(_ > 0)
    val mean = count.indices.map(i => i.toLong * count(i)).sum.toDouble / total
    val mode = count.zipWithIndex.maxBy(_._1)._2.toDouble
    val mid1 = (total + 1) / 2
    val mid2 = (total + 2) / 2
    var seen = 0L
    var first = -1
    var second = -1
    var i = 0
    while (i < 256 && second < 0) {
      seen += count(i)
      if (first < 0 && seen >= mid1) first = i
      if (second < 0 && seen >= mid2) second = i
      i += 1
    }
    val median = (first + second) / 2.0
    Array(minimum.toDouble, maximum.toDouble, mean, median, mode)
  }
}
