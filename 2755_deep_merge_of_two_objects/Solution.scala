// LeetCode 2755 - Deep Merge of Two Objects
// https://leetcode.com/problems/deep-merge-of-two-objects/

object Solution {
  def deepMerge(obj1: scala.collection.Map[String, String], obj2: scala.collection.Map[String, String]): scala.collection.mutable.Map[String, String] = {
    val output = scala.collection.mutable.Map.empty[String, String]
    obj1.foreach { case (k, v) => output(k) = v }
    obj2.foreach { case (k, v) => output(k) = v }
    output
  }
}
