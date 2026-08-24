// LeetCode 3973 - Distinct Gate Paths to LCA
// https://leetcode.com/problems/distinct-gate-paths-to-lca/

import scala.collection.mutable

object Solution {
  private val MOD = 1000000007L

  private def multiply(a: Array[Array[Long]], b: Array[Array[Long]]): Array[Array[Long]] = {
    val c = Array.ofDim[Long](2, 2)
    var i = 0
    while (i < 2) {
      var j = 0
      while (j < 2) {
        var k = 0
        while (k < 2) {
          c(i)(j) = (c(i)(j) + a(i)(k) * b(k)(j)) % MOD
          k += 1
        }
        j += 1
      }
      i += 1
    }
    c
  }

  def gatePathXor(n: Int, parent: Array[Int], gates: Array[Array[Int]], queries: Array[Array[Int]]): Int = {
    var logn = 1
    while ((1 << logn) <= n) logn += 1
    val up = Array.ofDim[Int](logn, n)
    val product = Array.ofDim[Array[Array[Long]]](logn, n)
    val children = Array.fill(n)(mutable.ArrayBuffer.empty[Int])
    var node = 1
    while (node < n) {
      children(parent(node)) += node
      node += 1
    }
    val depth = new Array[Int](n)
    val order = mutable.ArrayBuffer(0)
    var i = 0
    while (i < order.size) {
      val u = order(i)
      for (v <- children(u)) {
        depth(v) = depth(u) + 1
        order += v
      }
      i += 1
    }
    var u = 0
    while (u < n) {
      up(0)(u) = if (u == 0) 0 else parent(u)
      product(0)(u) = Array(Array(gates(u)(1).toLong, gates(u)(2).toLong), Array(gates(u)(2).toLong, gates(u)(0).toLong))
      u += 1
    }
    var level = 1
    while (level < logn) {
      u = 0
      while (u < n) {
        val mid = up(level - 1)(u)
        up(level)(u) = up(level - 1)(mid)
        product(level)(u) = multiply(product(level - 1)(u), product(level - 1)(mid))
        u += 1
      }
      level += 1
    }
    var answer = 0
    for (query <- queries) {
      val ancestor = lca(query(0), query(2), depth, up, logn)
      val alice = ways(query(0), query(1), depth(query(0)) - depth(ancestor), up, product)
      val bob = ways(query(2), query(3), depth(query(2)) - depth(ancestor), up, product)
      val total = (alice * bob % MOD).toInt
      answer ^= total
    }
    answer
  }

  private def liftNode(start: Int, startDistance: Int, up: Array[Array[Int]]): Int = {
    var node = start
    var distance = startDistance
    var level = 0
    while (distance > 0) {
      if ((distance & 1) != 0) node = up(level)(node)
      distance >>= 1
      level += 1
    }
    node
  }

  private def lca(aa: Int, bb: Int, depth: Array[Int], up: Array[Array[Int]], logn: Int): Int = {
    var a = aa
    var b = bb
    if (depth(a) > depth(b)) a = liftNode(a, depth(a) - depth(b), up)
    else if (depth(b) > depth(a)) b = liftNode(b, depth(b) - depth(a), up)
    if (a == b) return a
    var level = logn - 1
    while (level >= 0) {
      if (up(level)(a) != up(level)(b)) {
        a = up(level)(a)
        b = up(level)(b)
      }
      level -= 1
    }
    up(0)(a)
  }

  private def ways(
      start: Int,
      card: Int,
      startDistance: Int,
      up: Array[Array[Int]],
      product: Array[Array[Array[Array[Long]]]]
  ): Long = {
    var node = start
    var distance = startDistance
    var vector = Array(0L, 0L)
    vector(card) = 1
    var level = 0
    while (distance > 0) {
      if ((distance & 1) != 0) {
        val matrix = product(level)(node)
        vector = Array(
          (vector(0) * matrix(0)(0) + vector(1) * matrix(1)(0)) % MOD,
          (vector(0) * matrix(0)(1) + vector(1) * matrix(1)(1)) % MOD
        )
        node = up(level)(node)
      }
      distance >>= 1
      level += 1
    }
    (vector(0) + vector(1)) % MOD
  }
}
