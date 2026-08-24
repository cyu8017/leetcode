// LeetCode 2545 - Sort the Students by Their Kth Score
// https://leetcode.com/problems/sort-the-students-by-their-kth-score/

object Solution {
  def sortTheStudents(score: Array[Array[Int]], k: Int): Array[Array[Int]] = {
    score.sortBy(-_(k))
  }
}
