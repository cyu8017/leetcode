object Solution {
  def maxProduct(nums: Array[Int]): Int = {
    var best = nums(0); var max = nums(0); var min = nums(0)
    for (value <- nums.drop(1)) {
      val previousMax = max; val previousMin = min
      max = Seq(value, previousMax * value, previousMin * value).max
      min = Seq(value, previousMax * value, previousMin * value).min
      best = math.max(best, max)
    }
    best
  }
}