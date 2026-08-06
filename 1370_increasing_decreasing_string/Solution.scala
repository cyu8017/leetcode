object Solution {
  def sortString(s: String): String = {
    val count = Array.fill(26)(0); s.foreach(c => count(c - 'a') += 1); val out = new StringBuilder
    while (out.length < s.length) { (0 until 26).foreach(i => if (count(i) > 0) { out += ('a' + i).toChar; count(i) -= 1 }); (25 to 0 by -1).foreach(i => if (count(i) > 0) { out += ('a' + i).toChar; count(i) -= 1 }) }
    out.result()
  }
}
