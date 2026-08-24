// LeetCode 2818 - Apply Operations to Maximize Score
// https://leetcode.com/problems/apply-operations-to-maximize-score/

object Solution {
  private val MOD = 1000000007

  def maximumScore(nums: List[Int], k: Int): Int = {
    val n = nums.length
    var maxV = 0
    nums.foreach(v => maxV = math.max(maxV, v))
    val spf = Array.ofDim[Int](maxV + 1)
    var i = 2
    while (i <= maxV) {
      if (spf(i) == 0) {
        var j = i
        while (j <= maxV) {
          if (spf(j) == 0) spf(j) = i
          j += i
        }
      }
      i += 1
    }
    val score = Array.tabulate(n)(i => primeScore(nums(i), spf))
    val left = Array.ofDim[Int](n)
    val right = Array.ofDim[Int](n)
    val st = scala.collection.mutable.ArrayBuffer.empty[Int]
    i = 0
    while (i < n) {
      while (st.nonEmpty && score(st.last) < score(i)) st.remove(st.length - 1)
      left(i) = if (st.isEmpty) -1 else st.last
      st += i
      i += 1
    }
    st.clear()
    i = n - 1
    while (i >= 0) {
      while (st.nonEmpty && score(st.last) <= score(i)) st.remove(st.length - 1)
      right(i) = if (st.isEmpty) n else st.last
      st += i
      i -= 1
    }
    val arr = Array.tabulate(n)(i => Array(nums(i).toLong, (i - left(i)).toLong * (right(i) - i)))
    java.util.Arrays.sort(arr, (a: Array[Long], b: Array[Long]) => java.lang.Long.compare(b(0), a(0)))
    var ans = 1L
    var remain = k.toLong
    arr.foreach { pair =>
      if (remain > 0) {
        val use = math.min(pair(1), remain)
        ans = ans * modPow(pair(0), use) % MOD
        remain -= use
      }
    }
    ans.toInt
  }

  private def primeScore(x0: Int, spf: Array[Int]): Int = {
    var x = x0
    val seen = scala.collection.mutable.HashSet.empty[Int]
    while (x > 1) {
      val p = spf(x)
      seen += p
      while (x % p == 0) x /= p
    }
    seen.size
  }

  private def modPow(a0: Long, b0: Long): Long = {
    var res = 1L
    var a = a0 % MOD
    var b = b0
    while (b > 0) {
      if ((b & 1) != 0) res = res * a % MOD
      a = a * a % MOD
      b >>= 1
    }
    res
  }
}
