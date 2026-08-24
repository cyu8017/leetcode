// LeetCode 2166 - Design Bitset
// https://leetcode.com/problems/design-bitset/

class Bitset(_size: Int) {
  private val bits = Array.fill(_size)(0.toChar)
  private var ones = 0
  private var flipped = false
  private val size = _size

  def fix(idx: Int): Unit = {
    val target = if (flipped) 0.toChar else 1.toChar
    if (bits(idx) != target) {
      bits(idx) = target
      ones += (if (flipped) -1 else 1)
    }
  }

  def unfix(idx: Int): Unit = {
    val target = if (flipped) 1.toChar else 0.toChar
    if (bits(idx) != target) {
      bits(idx) = target
      ones += (if (flipped) 1 else -1)
    }
  }

  def flip(): Unit = {
    flipped = !flipped
    ones = size - ones
  }

  def all(): Boolean = ones == size
  def one(): Boolean = ones > 0
  def count(): Int = ones

  override def toString: String = {
    val b = Array.fill(size)('0')
    var i = 0
    while (i < size) {
      var v = bits(i)
      if (flipped) v = (v ^ 1).toChar
      b(i) = ('0' + v).toChar
      i += 1
    }
    new String(b)
  }
}
