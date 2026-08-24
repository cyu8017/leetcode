// LeetCode 3841 - Palindromic Path Queries in a Tree
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

object Solution {
  private var bit: Array[Int] = _
  private var n: Int = _
  private var parent: Array[Int] = _
  private var depth: Array[Int] = _
  private var size: Array[Int] = _
  private var heavy: Array[Int] = _
  private var head: Array[Int] = _
  private var position: Array[Int] = _
  private var graph: Array[scala.collection.mutable.ArrayBuffer[Int]] = _

  def palindromicPathQueries(n: Int, edges: Array[Array[Int]], s: String, queries: Array[String]): Array[Boolean] = {
    this.n = n
    graph = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { edge =>
      graph(edge(0)) += edge(1)
      graph(edge(1)) += edge(0)
    }
    parent = Array.fill(n)(-2)
    depth = new Array[Int](n)
    parent(0) = -1
    val order = scala.collection.mutable.ArrayBuffer[Int](0)
    var i = 0
    while (i < order.length) {
      val u = order(i)
      graph(u).foreach { v =>
        if (parent(v) == -2) {
          parent(v) = u
          depth(v) = depth(u) + 1
          order += v
        }
      }
      i += 1
    }
    size = new Array[Int](n)
    heavy = Array.fill(n)(-1)
    i = n - 1
    while (i >= 0) {
      val u = order(i)
      size(u) = 1
      graph(u).foreach { v =>
        if (parent(v) == u) {
          size(u) += size(v)
          if (heavy(u) == -1 || size(v) > size(heavy(u))) heavy(u) = v
        }
      }
      i -= 1
    }
    head = new Array[Int](n)
    position = new Array[Int](n)
    val stack = scala.collection.mutable.ArrayBuffer[Array[Int]](Array(0, 0))
    var nextPosition = 0
    while (stack.nonEmpty) {
      val chain = stack.remove(stack.length - 1)
      var u = chain(0)
      while (u != -1) {
        head(u) = chain(1)
        position(u) = nextPosition
        nextPosition += 1
        graph(u).foreach { v =>
          if (parent(v) == u && v != heavy(u)) stack += Array(v, v)
        }
        u = heavy(u)
      }
    }
    bit = new Array[Int](n + 1)
    val current = s.toCharArray
    var node = 0
    while (node < n) {
      update(position(node), 1 << (current(node) - 'a'))
      node += 1
    }
    val answer = scala.collection.mutable.ArrayBuffer.empty[Boolean]
    queries.foreach { query =>
      val parts = query.split(" ")
      val op = parts(0)
      val nd = parts(1).toInt
      if (op == "update") {
        val newCharacter = parts(2).charAt(0)
        val delta = (1 << (current(nd) - 'a')) ^ (1 << (newCharacter - 'a'))
        update(position(nd), delta)
        current(nd) = newCharacter
      } else {
        val other = parts(2).toInt
        val mask = pathMask(nd, other)
        answer += ((mask & (mask - 1)) == 0)
      }
    }
    answer.toArray
  }

  private def update(index0: Int, value: Int): Unit = {
    var index = index0 + 1
    while (index <= n) {
      bit(index) ^= value
      index += index & -index
    }
  }

  private def prefix(index0: Int): Int = {
    var result = 0
    var index = index0
    while (index > 0) {
      result ^= bit(index)
      index -= index & -index
    }
    result
  }

  private def pathMask(u0: Int, v0: Int): Int = {
    var u = u0
    var v = v0
    var result = 0
    while (head(u) != head(v)) {
      if (depth(head(u)) < depth(head(v))) {
        val tmp = u; u = v; v = tmp
      }
      result ^= prefix(position(u) + 1) ^ prefix(position(head(u)))
      u = parent(head(u))
    }
    if (position(u) > position(v)) {
      val tmp = u; u = v; v = tmp
    }
    result ^ prefix(position(v) + 1) ^ prefix(position(u))
  }
}
