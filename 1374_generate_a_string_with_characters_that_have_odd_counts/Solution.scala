object Solution {
  def generateTheString(n: Int): String = if (n % 2 == 1) "a" * n else "a" * (n - 1) + "b"
}
