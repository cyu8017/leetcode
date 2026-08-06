object Solution {
  def canConstruct(s: String, k: Int): Boolean = k <= s.length && s.groupMapReduce(identity)(_ => 1)(_ + _).values.count(_ % 2 == 1) <= k
}
