// LeetCode 2157 - Groups of Strings
// https://leetcode.com/problems/groups-of-strings/

object Solution {
  def groupStrings(words: Array[String]): Array[Int] = {
    def maskOf(w: String): Int = {
      var m = 0
      var i = 0
      while (i < w.length) {
        m |= 1 << (w.charAt(i) - 'a')
        i += 1
      }
      m
    }
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    words.foreach { w =>
      val m = maskOf(w)
      freq(m) = freq.getOrElse(m, 0) + 1
    }
    val parent = scala.collection.mutable.Map.empty[Int, Int]
    val size = scala.collection.mutable.Map.empty[Int, Int]
    freq.foreach { case (k, v) =>
      parent(k) = k
      size(k) = v
    }
    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }
    def unite(a: Int, b: Int): Unit = {
      var ra = find(a)
      var rb = find(b)
      if (ra != rb) {
        if (size(ra) < size(rb)) {
          val t = ra; ra = rb; rb = t
        }
        parent(rb) = ra
        size(ra) = size(ra) + size(rb)
      }
    }
    freq.keys.foreach { m =>
      var b = 0
      while (b < 26) {
        if ((m & (1 << b)) != 0) {
          val nm = m ^ (1 << b)
          if (freq.contains(nm)) unite(m, nm)
          var a = 0
          while (a < 26) {
            if ((nm & (1 << a)) == 0) {
              val rm = nm | (1 << a)
              if (freq.contains(rm)) unite(m, rm)
            }
            a += 1
          }
        } else {
          val nm = m | (1 << b)
          if (freq.contains(nm)) unite(m, nm)
        }
        b += 1
      }
    }
    var groups = 0
    var maxSize = 0
    val seen = scala.collection.mutable.Set.empty[Int]
    freq.keys.foreach { m =>
      val r = find(m)
      if (seen.add(r)) {
        groups += 1
        maxSize = math.max(maxSize, size(r))
      }
    }
    Array(groups, maxSize)
  }
}
