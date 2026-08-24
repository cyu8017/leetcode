// LeetCode 2019 - The Score of Students Solving Math Expression
// https://leetcode.com/problems/the-score-of-students-solving-math-expression/

object Solution {
  def scoreOfStudents(s: String, answers: Array[Int]): Int = {
    def evalCorrect(expr: String): Int = {
      val nums = scala.collection.mutable.ArrayBuffer.empty[Int]
      val ops = scala.collection.mutable.ArrayBuffer.empty[Char]
      expr.foreach { c =>
        if (c >= '0' && c <= '9') nums += c - '0'
        else ops += c
      }
      val newNums = scala.collection.mutable.ArrayBuffer(nums(0))
      val newOps = scala.collection.mutable.ArrayBuffer.empty[Char]
      var j = 0
      while (j < ops.length) {
        if (ops(j) == '*') newNums(newNums.length - 1) = newNums.last * nums(j + 1)
        else { newOps += ops(j); newNums += nums(j + 1) }
        j += 1
      }
      var res = newNums(0)
      j = 0
      while (j < newOps.length) { res += newNums(j + 1); j += 1 }
      res
    }
    val n = s.length
    val correct = evalCorrect(s)
    val dp = Array.ofDim[Option[Set[Int]]](n, n)
    def dfs(l: Int, r: Int): Set[Int] = {
      if (dp(l)(r) != null) return dp(l)(r).get
      if (l == r) {
        val res = Set(s.charAt(l) - '0')
        dp(l)(r) = Some(res)
        return res
      }
      val res = scala.collection.mutable.HashSet.empty[Int]
      var i = l + 1
      while (i < r) {
        for (a <- dfs(l, i - 1); b <- dfs(i + 1, r)) {
          val v = if (s.charAt(i) == '+') a + b else a * b
          if (v <= 1000) res += v
        }
        i += 2
      }
      val frozen = res.toSet
      dp(l)(r) = Some(frozen)
      frozen
    }
    val possible = dfs(0, n - 1)
    var ans = 0
    answers.foreach { a =>
      if (a == correct) ans += 5
      else if (possible.contains(a)) ans += 2
    }
    ans
  }
}
