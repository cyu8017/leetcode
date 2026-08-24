// LeetCode 2502 - Design Memory Allocator
// https://leetcode.com/problems/design-memory-allocator/

class Allocator(_n: Int) {
  private val mem = new Array[Int](_n)

  def allocate(size: Int, mID: Int): Int = {
    var freeCnt = 0
    var i = 0
    while (i < mem.length) {
      if (mem(i) == 0) {
        freeCnt += 1
        if (freeCnt == size) {
          val start = i - size + 1
          var j = start
          while (j <= i) {
            mem(j) = mID
            j += 1
          }
          return start
        }
      } else {
        freeCnt = 0
      }
      i += 1
    }
    -1
  }

  def freeMemory(mID: Int): Int = {
    var cnt = 0
    var i = 0
    while (i < mem.length) {
      if (mem(i) == mID) {
        mem(i) = 0
        cnt += 1
      }
      i += 1
    }
    cnt
  }
}
