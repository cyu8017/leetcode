object Solution {
  def kLengthApart(nums: Array[Int], k: Int): Boolean = {
    var previous = -k - 1
    for (i <- nums.indices if nums(i) == 1) {
      if (i - previous <= k) return false
      previous = i
    }
    true
  }
}
