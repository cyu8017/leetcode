// LeetCode 1301 - Number Of Paths With Max Score
// https://leetcode.com/problems/number-of-paths-with-max-score/

object Solution {
  def pathsWithMaxScore(board: List[String]): Array[Int] = {
    val mod = 1000000007
    val n = board.length
    val score = Array.fill(n, n)(-1)
    val ways = Array.ofDim[Int](n, n)
    score(n - 1)(n - 1) = 0
    ways(n - 1)(n - 1) = 1
    for (r <- n - 1 to 0 by -1; c <- n - 1 to 0 by -1) {
      if (!(board(r)(c) == 'X' || (r == n - 1 && c == n - 1))) {
        var best = -1
        var count = 0
        for ((nr, nc) <- Seq((r + 1, c), (r, c + 1), (r + 1, c + 1))) {
          if (nr < n && nc < n && score(nr)(nc) >= 0) {
            if (score(nr)(nc) > best) {
              best = score(nr)(nc)
              count = ways(nr)(nc)
            } else if (score(nr)(nc) == best) {
              count = (count + ways(nr)(nc)) % mod
            }
          }
        }
        if (best >= 0) {
          val ch = board(r)(c)
          val add = if (ch.isDigit) ch - '0' else 0
          score(r)(c) = best + add
          ways(r)(c) = count
        }
      }
    }
    Array(math.max(score(0)(0), 0), ways(0)(0))
  }
}
