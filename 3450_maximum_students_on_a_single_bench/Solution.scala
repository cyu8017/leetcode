// LeetCode 3450 - Maximum Students on a Single Bench
// https://leetcode.com/problems/maximum-students-on-a-single-bench/

object Solution {
  def maxStudentsOnBench(students: Array[Array[Int]]): Int = {
    val bench = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.Set[Int]]
    students.foreach { s =>
      bench.getOrElseUpdate(s(1), scala.collection.mutable.Set.empty[Int]) += s(0)
    }
    var ans = 0
    bench.values.foreach { set => if (set.size > ans) ans = set.size }
    ans
  }
}
