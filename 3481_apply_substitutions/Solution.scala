// LeetCode 3481 - Apply Substitutions
// https://leetcode.com/problems/apply-substitutions/

object Solution {
  private var mp: java.util.HashMap[String, String] = _

  def applySubstitutions(replacements: List[List[String]], text: String): String = {
    mp = new java.util.HashMap[String, String]()
    replacements.foreach { r => mp.put(r(0), r(1)) }
    resolve(text)
  }

  private def resolve(s: String): String = {
    val out = new StringBuilder
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == '%') {
        var j = i + 1
        while (j < s.length && s.charAt(j) != '%') j += 1
        val key = s.substring(i + 1, j)
        out.append(resolve(mp.get(key)))
        i = j + 1
      } else {
        out.append(s.charAt(i))
        i += 1
      }
    }
    out.toString
  }
}
