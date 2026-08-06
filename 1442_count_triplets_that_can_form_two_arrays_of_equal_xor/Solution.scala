object Solution {
  def countTriplets(arr: Array[Int]): Int = {
    var answer = 0
    for (i <- arr.indices) {
      var value = 0
      for (k <- i until arr.length) { value ^= arr(k); if (value == 0) answer += k - i }
    }
    answer
  }
}
