object Solution {
  def rob(nums: Array[Int]): Int = {
    var previousTwo = 0
    var previousOne = 0
    for (num <- nums) {
      val current = math.max(previousOne, previousTwo + num)
      previousTwo = previousOne
      previousOne = current
    }
    previousOne
  }
}
