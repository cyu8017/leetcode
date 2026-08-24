// LeetCode 3155 - Maximum Number of Upgradable Servers
// https://leetcode.com/problems/maximum-number-of-upgradable-servers/

object Solution {
  def maxUpgrades(count: Array[Int], upgrade: Array[Int], sell: Array[Int], money: Array[Int]): Array[Int] = {
    val ans = new Array[Int](count.length)
    var i = 0
    while (i < count.length) {
      val cnt = count(i).toLong
      ans(i) = math.min(cnt, (cnt * sell(i) + money(i)) / (upgrade(i) + sell(i))).toInt
      i += 1
    }
    ans
  }
}
