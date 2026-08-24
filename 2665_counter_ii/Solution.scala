// LeetCode 2665 - Counter II
// https://leetcode.com/problems/counter-ii/

class CounterII(_init: Int) {
  private val init = _init
  private var cur = _init

  def increment(): Int = {
    cur += 1
    cur
  }

  def decrement(): Int = {
    cur -= 1
    cur
  }

  def reset(): Int = {
    cur = init
    cur
  }
}

object Solution {
  def createCounter(init: Int): CounterII = new CounterII(init)
}
