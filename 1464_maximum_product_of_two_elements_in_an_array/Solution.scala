object Solution {
  def maxProduct(nums: Array[Int]): Int = {
    val sorted = nums.sorted
    (sorted(sorted.length - 2) - 1) * (sorted.last - 1)
  }
}
