class Solution {
  def largestNumber(nums: Array[Int]): String = {
    val parts = nums.map(_.toString).sortWith((a, b) => a + b > b + a)
    if (parts(0) == "0") "0" else parts.mkString
  }
}
