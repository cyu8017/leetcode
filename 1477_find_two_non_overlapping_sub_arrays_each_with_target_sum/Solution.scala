object Solution {
  def minSumOfLengths(arr: Array[Int], target: Int): Int = {
    val inf = Int.MaxValue / 4
    val shortest = Array.fill(arr.length)(inf)
    var left = 0
    var sum = 0
    var best = inf
    var answer = inf
    for (right <- arr.indices) {
      sum += arr(right)
      while (sum > target) {
        sum -= arr(left)
        left += 1
      }
      if (sum == target) {
        val length = right - left + 1
        if (left > 0) answer = math.min(answer, length + shortest(left - 1))
        best = math.min(best, length)
      }
      shortest(right) = best
    }
    if (answer == inf) -1 else answer
  }
}
