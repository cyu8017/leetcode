// LeetCode 3479 - Fruits Into Baskets III
// https://leetcode.com/problems/fruits-into-baskets-iii/

object Solution {
  private var tree: Array[Int] = _
  private var size = 0
  private var n = 0

  def numOfUnplacedFruits(fruits: Array[Int], baskets: Array[Int]): Int = {
    n = baskets.length
    size = 1
    while (size < n) size <<= 1
    tree = new Array[Int](size * 2)
    var i = 0
    while (i < n) { tree(size + i) = baskets(i); i += 1 }
    i = size - 1
    while (i > 0) {
      tree(i) = math.max(tree(i * 2), tree(i * 2 + 1))
      i -= 1
    }
    var unplaced = 0
    fruits.foreach { f =>
      val idx = find(1, 0, size - 1, f)
      if (idx == -1 || idx >= n) unplaced += 1
      else update(idx)
    }
    unplaced
  }

  private def find(node: Int, nl: Int, nr: Int, need: Int): Int = {
    if (tree(node) < need) return -1
    if (nl == nr) return nl
    val mid = (nl + nr) / 2
    val left = find(node * 2, nl, mid, need)
    if (left != -1) left else find(node * 2 + 1, mid + 1, nr, need)
  }

  private def update(idx: Int): Unit = {
    var p = size + idx
    tree(p) = -1
    p >>= 1
    while (p > 0) {
      tree(p) = math.max(tree(p * 2), tree(p * 2 + 1))
      p >>= 1
    }
  }
}
