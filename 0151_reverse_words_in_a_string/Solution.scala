object Solution {
  def reverseWords(s: String): String = s.trim.split("\\s+").filter(_.nonEmpty).reverse.mkString(" ")
}