object Solution {
  def hasAllCodes(s: String, k: Int): Boolean =
    s.length >= k && (0 to s.length - k).map(i => s.substring(i, i + k)).toSet.size == (1 << k)
}
