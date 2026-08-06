object Solution {
  def longestPrefix(s: String): String = { val pi = Array.fill(s.length)(0); for (i <- 1 until s.length) { var j = pi(i-1); while (j > 0 && s(i) != s(j)) j = pi(j-1); if (s(i) == s(j)) j += 1; pi(i) = j }; s.substring(0, if (s.isEmpty) 0 else pi.last) }
}
