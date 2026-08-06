object Solution {
  def numOfSubarrays(arr: Array[Int], k: Int, threshold: Int): Int = {
    var sum = arr.take(k).sum; var answer = if (sum >= k * threshold) 1 else 0
    for (i <- k until arr.length) { sum += arr(i) - arr(i - k); if (sum >= k * threshold) answer += 1 }
    answer
  }
}
