// LeetCode 0900 - RLE Iterator
// https://leetcode.com/problems/rle-iterator/

class RLEIterator(_encoding: Array[Int]) {
  private val enc = _encoding.clone()
  private var i = 0

  def next(n: Int): Int = {
    var remain = n
    while (i < enc.length) {
      if (enc(i) >= remain) {
        enc(i) -= remain
        return enc(i + 1)
      }
      remain -= enc(i)
      i += 2
    }
    -1
  }
}
