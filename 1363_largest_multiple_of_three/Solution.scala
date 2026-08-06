object Solution {
  def largestMultipleOfThree(digits: Array[Int]): String = {
    val count = Array.fill(10)(0); var remainder = 0
    digits.foreach(d => { count(d) += 1; remainder = (remainder + d) % 3 })
    def remove(start: Int, needed: Int): Boolean = {
      var d = start; var remaining = needed
      while (d < 10 && remaining > 0) { while (count(d) > 0 && remaining > 0) { count(d) -= 1; remaining -= 1 }; d += 3 }
      remaining == 0
    }
    if (remainder != 0 && !remove(remainder, 1)) remove(3 - remainder, 2)
    val answer = (9 to 0 by -1).flatMap(d => List.fill(count(d))(d)).mkString
    if (answer.nonEmpty && answer.head == '0') "0" else answer
  }
}
