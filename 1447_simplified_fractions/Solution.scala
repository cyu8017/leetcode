object Solution {
  def simplifiedFractions(n: Int): List[String] = {
    def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)
    (for (a <- 1 until n; b <- a + 1 to n if gcd(a, b) == 1) yield s"$a/$b").toList
  }
}
