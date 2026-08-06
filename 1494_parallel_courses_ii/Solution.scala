object Solution {
  def minNumberOfSemesters(n: Int, relations: Array[Array[Int]], k: Int): Int = {
    val prerequisites = Array.fill(n)(0)
    for (edge <- relations) prerequisites(edge(1) - 1) |= 1 << (edge(0) - 1)
    val full = (1 << n) - 1
    val inf = Int.MaxValue / 4
    val dp = Array.fill(1 << n)(inf)
    dp(0) = 0
    for (mask <- 0 until (1 << n) if dp(mask) != inf) {
      var available = 0
      for (course <- 0 until n if (mask & (1 << course)) == 0 && (prerequisites(course) & mask) == prerequisites(course))
        available |= 1 << course
      if (Integer.bitCount(available) <= k) dp(mask | available) = math.min(dp(mask | available), dp(mask) + 1)
      else {
        var subset = available
        while (subset > 0) {
          if (Integer.bitCount(subset) == k) dp(mask | subset) = math.min(dp(mask | subset), dp(mask) + 1)
          subset = (subset - 1) & available
        }
      }
    }
    dp(full)
  }
}
