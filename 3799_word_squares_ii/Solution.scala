// LeetCode 3799 - Word Squares II
// https://leetcode.com/problems/word-squares-ii/

object Solution {
  def wordSquares(words: Array[String]): List[List[String]] = {
    java.util.Arrays.sort(words, (a: String, b: String) => a.compareTo(b))
    val n = words.length
    val ans = new java.util.ArrayList[java.util.List[String]]()
    var i = 0
    while (i < n) {
      val top = words(i)
      var j = 0
      while (j < n) {
        if (j != i) {
          val left = words(j)
          var k = 0
          while (k < n) {
            if (k != j && k != i) {
              val right = words(k)
              var h = 0
              while (h < n) {
                if (h != k && h != j && h != i) {
                  val bottom = words(h)
                  if (top.charAt(0) == left.charAt(0) && top.charAt(3) == right.charAt(0) &&
                      bottom.charAt(0) == left.charAt(3) && bottom.charAt(3) == right.charAt(3)) {
                    ans.add(java.util.Arrays.asList(top, left, right, bottom))
                  }
                }
                h += 1
              }
            }
            k += 1
          }
        }
        j += 1
      }
      i += 1
    }
    val out = new scala.collection.mutable.ListBuffer[List[String]]()
    val it = ans.iterator()
    while (it.hasNext) {
      val row = it.next()
      out += List(row.get(0), row.get(1), row.get(2), row.get(3))
    }
    out.toList
  }
}
