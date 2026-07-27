// LeetCode 1622 - Fancy Sequence
// https://leetcode.com/problems/fancy-sequence/

class Fancy {
  private val MOD = 1000000007L
  private val vals = scala.collection.mutable.ArrayBuffer.empty[Long]
  private var mul = 1L
  private var add = 0L

  def append(`val`: Int): Unit = {
    val v = ((`val`.toLong - add) % MOD + MOD) % MOD
    vals += v * modInverse(mul) % MOD
  }

  def addAll(inc: Int): Unit = {
    if (vals.nonEmpty) add = (add + inc) % MOD
  }

  def multAll(m: Int): Unit = {
    if (vals.isEmpty) return
    mul = mul * m % MOD
    add = add * m % MOD
  }

  def getIndex(idx: Int): Int = {
    if (idx >= vals.length) -1
    else ((vals(idx) * mul + add) % MOD).toInt
  }

  private def modInverse(a: Long): Long = {
    var x = a % MOD
    var y = MOD - 2
    var res = 1L
    while (y > 0) {
      if ((y & 1) == 1) res = res * x % MOD
      x = x * x % MOD
      y >>= 1
    }
    res
  }
}
