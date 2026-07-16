// LeetCode 0465 - Optimal Account Balancing
// https://leetcode.com/problems/optimal-account-balancing/

object Solution {
  def minTransfers(transactions: Array[Array[Int]]): Int = {
    val balances = scala.collection.mutable.Map.empty[Int, Int]
    for (Array(source, target, amount) <- transactions) {
      balances.update(source, balances.getOrElse(source, 0) - amount)
      balances.update(target, balances.getOrElse(target, 0) + amount)
    }

    val debts = balances.values.filter(_ != 0).toArray
    dfs(debts, 0)
  }

  private def dfs(debts: Array[Int], index: Int): Int = {
    var current = index
    while (current < debts.length && debts(current) == 0) {
      current += 1
    }
    if (current == debts.length) {
      return 0
    }

    var best = debts.length
    var nextIndex = current + 1
    while (nextIndex < debts.length) {
      if (debts(current) * debts(nextIndex) < 0) {
        debts(nextIndex) += debts(current)
        best = math.min(best, 1 + dfs(debts, current + 1))
        debts(nextIndex) -= debts(current)
      }
      nextIndex += 1
    }
    best
  }
}
