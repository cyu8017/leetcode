// LeetCode 2692 - Make Object Immutable
// https://leetcode.com/problems/make-object-immutable/

object Solution {
  def makeImmutable(obj: scala.collection.mutable.TreeMap[String, Int]): scala.collection.mutable.TreeMap[String, Int] =
    scala.collection.mutable.TreeMap.empty[String, Int] ++ obj
}
