// LeetCode 1656 - Design an Ordered Stream
// https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream(_n: Int) {
  private val a = Array.fill[String](_n + 1)(null)
  private var p = 1

  def insert(idKey: Int, value: String): List[String] = {
    a(idKey) = value
    val out = scala.collection.mutable.ListBuffer[String]()
    while (p < a.length && a(p) != null) {
      out += a(p)
      p += 1
    }
    out.toList
  }
}
