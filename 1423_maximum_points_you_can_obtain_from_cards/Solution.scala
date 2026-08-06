object Solution {
  def maxScore(cardPoints: Array[Int], k: Int): Int = {
    val window = cardPoints.length - k
    var current = cardPoints.take(window).sum
    var smallest = current
    for (i <- window until cardPoints.length) {
      current += cardPoints(i) - cardPoints(i - window)
      smallest = smallest.min(current)
    }
    cardPoints.sum - smallest
  }
}
