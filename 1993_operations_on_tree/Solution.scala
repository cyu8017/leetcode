// LeetCode 1993 - Operations on Tree
// https://leetcode.com/problems/operations-on-tree/

class LockingTree(parent: Array[Int]) {
  private val n = parent.length
  private val locked = Array.fill(n)(-1)
  private val children = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
  for (son <- 1 until n) children(parent(son)) += son

  def lock(num: Int, user: Int): Boolean = {
    if (locked(num) == -1) {
      locked(num) = user
      true
    } else false
  }

  def unlock(num: Int, user: Int): Boolean = {
    if (locked(num) == user) {
      locked(num) = -1
      true
    } else false
  }

  def upgrade(num: Int, user: Int): Boolean = {
    var x = num
    while (x != -1) {
      if (locked(x) != -1) return false
      x = parent(x)
    }
    var find = false
    def dfs(u: Int): Unit = {
      for (v <- children(u)) {
        if (locked(v) != -1) {
          locked(v) = -1
          find = true
        }
        dfs(v)
      }
    }
    dfs(num)
    if (!find) return false
    locked(num) = user
    true
  }
}
