// LeetCode 3273 - Minimum Amount of Damage Dealt to Bob
// https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

object Solution {
  class Enemy(var dmg: Int, var hits: Int)
  def minDamage(power: Int, damage: Array[Int], health: Array[Int]): Long = {
    val n = damage.length
    val arr = new Array[Enemy](n)
    var totalDmg = 0
    var i = 0
    while (i < n) {
      val hits = (health(i) + power - 1) / power
      arr(i) = new Enemy(damage(i), hits)
      totalDmg += damage(i)
      i += 1
    }
    java.util.Arrays.sort(arr, (a: Enemy, b: Enemy) =>
      java.lang.Long.compare(a.hits.toLong * b.dmg, b.hits.toLong * a.dmg)
    )
    var ans = 0L
    var cur = totalDmg.toLong
    for (e <- arr) {
      ans += cur * e.hits
      cur -= e.dmg
    }
    ans
  }
}
