object Solution {
  def maxDotProduct(nums1: Array[Int], nums2: Array[Int]): Int = {
    val dp = Array.fill[Long](nums2.length + 1)(Long.MinValue / 4)
    for (a <- nums1) {
      val previous = dp.clone()
      for (j <- 1 to nums2.length) {
        val product = a.toLong * nums2(j - 1)
        dp(j) = Seq(dp(j - 1), previous(j), product, product + previous(j - 1).max(0L)).max
      }
    }
    dp.last.toInt
  }
}
