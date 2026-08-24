// LeetCode 2512 - Reward Top K Students
// https://leetcode.com/problems/reward-top-k-students/

object Solution {
  def topStudents(positive_feedback: Array[String], negative_feedback: Array[String], report: Array[String], student_id: Array[Int], k: Int): Array[Int] = {
    val pos = positive_feedback.toSet
    val neg = negative_feedback.toSet
    val arr = Array.ofDim[Int](report.length, 2)
    var i = 0
    while (i < report.length) {
      var score = 0
      report(i).split(" ").foreach { w =>
        if (w.nonEmpty) {
          if (pos.contains(w)) score += 3
          else if (neg.contains(w)) score -= 1
        }
      }
      arr(i)(0) = student_id(i)
      arr(i)(1) = score
      i += 1
    }
    scala.util.Sorting.stableSort(arr, (a: Array[Int], b: Array[Int]) =>
      if (a(1) != b(1)) a(1) > b(1) else a(0) < b(0)
    )
    val ans = new Array[Int](k)
    i = 0
    while (i < k) {
      ans(i) = arr(i)(0)
      i += 1
    }
    ans
  }
}
