object Solution {
  def checkIfCanBreak(s1: String, s2: String): Boolean = {
    val a = s1.sorted; val b = s2.sorted
    a.indices.forall(i => a(i) >= b(i)) || a.indices.forall(i => a(i) <= b(i))
  }
}
