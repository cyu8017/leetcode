// LeetCode 0555 - Split Concatenated Strings
// https://leetcode.com/problems/split-concatenated-strings/

object Solution {
  def splitLoopedString(strs: Array[String]): String = {
    val bestForms = strs.map { s =>
      val rev = s.reverse
      if (s.compareTo(rev) >= 0) s else rev
    }
    var answer = ""
    for (i <- strs.indices) {
      val midBuilder = new StringBuilder
      var j = i + 1
      while (j < strs.length) { midBuilder.append(bestForms(j)); j += 1 }
      j = 0
      while (j < i) { midBuilder.append(bestForms(j)); j += 1 }
      val mid = midBuilder.toString
      val original = strs(i)
      val reversed = original.reverse
      for (candidate <- Array(original, reversed)) {
        var cut = 0
        while (cut < candidate.length) {
          val formed = candidate.substring(cut) + mid + candidate.substring(0, cut)
          if (formed.compareTo(answer) > 0) answer = formed
          cut += 1
        }
      }
    }
    answer
  }
}
