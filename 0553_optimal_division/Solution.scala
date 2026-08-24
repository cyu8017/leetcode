// LeetCode 0553 - Optimal Division
// https://leetcode.com/problems/optimal-division/

object Solution {
  def optimalDivision(nums: Array[Int]): String = {
    if (nums.length == 1) return nums(0).toString
    if (nums.length == 2) return s"${nums(0)}/${nums(1)}"
    val result = new StringBuilder
    result.append(nums(0)).append("/(")
    var i = 1
    while (i < nums.length) {
      if (i > 1) result.append('/')
      result.append(nums(i))
      i += 1
    }
    result.append(')')
    result.toString
  }
}
