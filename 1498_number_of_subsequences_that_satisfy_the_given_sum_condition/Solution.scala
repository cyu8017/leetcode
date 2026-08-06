object Solution {
  def numSubseq(nums: Array[Int], target: Int): Int = {
    val sorted = nums.sorted
    val mod = 1000000007L
    val powers = Array.fill[Long](sorted.length + 1)(1L)
    for (i <- 1 until powers.length) powers(i) = powers(i - 1) * 2 % mod
    var left = 0
    var right = sorted.length - 1
    var answer = 0L
    while (left <= right) {
      if (sorted(left) + sorted(right) <= target) {
        answer = (answer + powers(right - left)) % mod
        left += 1
      } else right -= 1
    }
    answer.toInt
  }
}
