object Solution {
  def minSteps(s: String, t: String): Int = {
    val count = Array.fill(26)(0)
    s.foreach(c => count(c - 'a') += 1); t.foreach(c => count(c - 'a') -= 1)
    count.filter(_ > 0).sum
  }
}
