// LeetCode 0299 - Bulls and Cows
// https://leetcode.com/problems/bulls-and-cows/

import scala.collection.mutable

object Solution {
  def getHint(secret: String, guess: String): String = {
    var bulls = 0
    val secretCounts = mutable.Map.empty[Char, Int].withDefaultValue(0)
    val guessCounts = mutable.Map.empty[Char, Int].withDefaultValue(0)
    secret.indices.foreach { index =>
      val secretDigit = secret(index)
      val guessDigit = guess(index)
      if (secretDigit == guessDigit) {
        bulls += 1
      } else {
        secretCounts(secretDigit) += 1
        guessCounts(guessDigit) += 1
      }
    }
    val cows = guessCounts.map { case (digit, count) =>
      math.min(count, secretCounts.getOrElse(digit, 0))
    }.sum
    s"${bulls}A${cows}B"
  }
}
