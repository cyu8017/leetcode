object Solution {
  def findGoodStrings(n: Int, s1: String, s2: String, evil: String): Int = {
    val mod = 1000000007; val m = evil.length; val pi = Array.fill(m)(0)
    for (i <- 1 until m) { var j = pi(i-1); while (j > 0 && evil(i) != evil(j)) j = pi(j-1); if (evil(i) == evil(j)) j += 1; pi(i) = j }
    val next = Array.ofDim[Int](m, 26)
    for (j <- 0 until m; x <- 0 until 26) { var p = j; val ch = ('a' + x).toChar; while (p > 0 && evil(p) != ch) p = pi(p-1); if (evil(p) == ch) p += 1; next(j)(x) = p }
    val memo = scala.collection.mutable.Map[(Int,Int,Boolean,Boolean), Int]()
    def dp(i: Int, j: Int, lo: Boolean, hi: Boolean): Int = if (j == m) 0 else if (i == n) 1 else memo.getOrElseUpdate((i,j,lo,hi), { val a = if(lo) s1(i)-'a' else 0; val b = if(hi) s2(i)-'a' else 25; var ans = 0L; for (x <- a to b) ans = (ans + dp(i+1,next(j)(x),lo && x==a,hi && x==b)) % mod; ans.toInt })
    dp(0,0,true,true)
  }
}
