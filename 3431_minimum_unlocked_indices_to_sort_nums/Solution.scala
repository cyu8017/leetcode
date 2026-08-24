// LeetCode 3431 - Minimum Unlocked Indices to Sort Nums
// https://leetcode.com/problems/minimum-unlocked-indices-to-sort-nums/

object Solution {
  def minUnlockedIndices(nums: Array[Int], locked: Array[Int]): Int = {
    val n = nums.length
    var need = false
    var i = 1
    while (i < n) {
      if (nums(i) < nums(i - 1)) { need = true; i = n }
      else i += 1
    }
    if (!need) return 0
    var left = n
    var right = -1
    i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        if (nums(i) > nums(j)) {
          if (i < left) left = i
          if (j > right) right = j
        }
        j += 1
      }
      i += 1
    }
    if (right < left) return 0
    var ans = 0
    i = left
    while (i <= right) {
      if (locked(i) == 1) ans += 1
      i += 1
    }
    val tmp = nums.clone()
    val lock = locked.clone()
    i = left
    while (i <= right) {
      lock(i) = 0
      i += 1
    }
    var changed = true
    while (changed) {
      changed = false
      i = 0
      while (i + 1 < n) {
        if (lock(i) == 0 && lock(i + 1) == 0 && tmp(i) > tmp(i + 1)) {
          val t = tmp(i); tmp(i) = tmp(i + 1); tmp(i + 1) = t
          changed = true
        }
        i += 1
      }
    }
    i = 1
    while (i < n) {
      if (tmp(i) < tmp(i - 1)) return -1
      i += 1
    }
    ans
  }
}
