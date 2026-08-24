// LeetCode 3435 - Frequencies of Shortest Supersequences
// https://leetcode.com/problems/frequencies-of-shortest-supersequences/

object Solution {
  private var words: Array[String] = _
  private var letters: Array[Int] = _
  private var m = 0
  private var best = 0
  private val freq = new Array[Int](26)
  private var bestFreqs: java.util.ArrayList[Array[Int]] = _

  def supersequences(words0: Array[String]): List[List[Int]] = {
    words = words0
    val used = Array.fill(26)(false)
    words.foreach { w =>
      used(w.charAt(0) - 'a') = true
      used(w.charAt(1) - 'a') = true
    }
    val lettersList = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < 26) {
      if (used(i)) lettersList += i
      i += 1
    }
    m = lettersList.length
    letters = lettersList.toArray
    best = 1000000000
    bestFreqs = new java.util.ArrayList[Array[Int]]()
    i = 0
    while (i < 26) { freq(i) = 0; i += 1 }
    dfs(0)
    val res = scala.collection.mutable.ListBuffer.empty[List[Int]]
    val it = bestFreqs.iterator()
    while (it.hasNext) {
      val f = it.next()
      res += f.toList
    }
    res.toList
  }

  private def dfs(i: Int): Unit = {
    if (i == m) {
      words.foreach { w =>
        val a = w.charAt(0) - 'a'
        val b = w.charAt(1) - 'a'
        if (a == b) {
          if (freq(a) < 2) return
        } else if (freq(a) < 1 || freq(b) < 1) return
      }
      var sum = 0
      val f = new Array[Int](26)
      var j = 0
      while (j < 26) { f(j) = freq(j); sum += freq(j); j += 1 }
      if (sum < best) {
        best = sum
        bestFreqs = new java.util.ArrayList[Array[Int]]()
        bestFreqs.add(f)
      } else if (sum == best) bestFreqs.add(f)
      return
    }
    val L = letters(i)
    var c = 1
    while (c <= 2) {
      freq(L) = c
      dfs(i + 1)
      c += 1
    }
    freq(L) = 0
  }
}
