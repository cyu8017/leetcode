// LeetCode 2363 - Merge Similar Items
// https://leetcode.com/problems/merge-similar-items/

object Solution {
  def mergeSimilarItems(items1: Array[Array[Int]], items2: Array[Array[Int]]): List[List[Int]] = {
    val mp = scala.collection.mutable.TreeMap.empty[Int, Int]
    items1.foreach(it => mp(it(0)) = mp.getOrElse(it(0), 0) + it(1))
    items2.foreach(it => mp(it(0)) = mp.getOrElse(it(0), 0) + it(1))
    mp.toList.map { case (k, v) => List(k, v) }
  }
}
