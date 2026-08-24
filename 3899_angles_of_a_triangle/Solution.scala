// LeetCode 3899 - Angles Of A Triangle
// https://leetcode.com/problems/angles-of-a-triangle/

object Solution {
  def internalAngles(sides: Array[Int]): Array[Double] = {
    java.util.Arrays.sort(sides)
    val a = sides(0)
    val b = sides(1)
    val c = sides(2)
    if (a + b <= c) return Array.emptyDoubleArray
    val PI = math.acos(-1.0)
    val A = math.acos((b.toLong * b + c.toLong * c - a.toLong * a).toDouble / (2.0 * b * c)) * 180.0 / PI
    val B = math.acos((a.toLong * a + c.toLong * c - b.toLong * b).toDouble / (2.0 * a * c)) * 180.0 / PI
    val C = 180.0 - A - B
    Array(A, B, C)
  }
}
