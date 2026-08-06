object Solution {
  def maxPower(s: String): Int = {
    var answer = 1; var run = 1
    for (i <- 1 until s.length) { run = if (s(i) == s(i - 1)) run + 1 else 1; answer = answer.max(run) }
    answer
  }
}
