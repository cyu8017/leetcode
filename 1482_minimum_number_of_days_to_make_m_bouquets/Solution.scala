object Solution {
  def minDays(bloomDay: Array[Int], m: Int, k: Int): Int = {
    if (m.toLong * k > bloomDay.length) return -1
    def possible(day: Int): Boolean = {
      var bouquets = 0
      var run = 0
      for (value <- bloomDay) {
        run = if (value <= day) run + 1 else 0
        if (run == k) {
          bouquets += 1
          run = 0
        }
      }
      bouquets >= m
    }
    var low = bloomDay.min
    var high = bloomDay.max
    while (low < high) {
      val middle = low + (high - low) / 2
      if (possible(middle)) high = middle else low = middle + 1
    }
    low
  }
}
