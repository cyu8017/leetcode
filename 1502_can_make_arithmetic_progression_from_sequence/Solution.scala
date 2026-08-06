// LeetCode 1502 - Can Make Arithmetic Progression From Sequence
// https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

object Solution {
  def canMakeArithmeticProgression(arr: Array[Int]): Boolean = {
    val a = arr.sorted
    val d = a(1) - a(0)
    (2 until a.length).forall(i => a(i) - a(i - 1) == d)
  }
}
