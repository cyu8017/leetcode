object Solution {
  def numberOfSubstrings(s: String): Int = {
    val last = Array(-1, -1, -1); var answer = 0
    s.indices.foreach(i => { last(s(i) - 'a') = i; answer += last.min + 1 })
    answer
  }
}
