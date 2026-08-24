// LeetCode 2591 - Distribute Money to Maximum Children
// https://leetcode.com/problems/distribute-money-to-maximum-children/

object Solution {
  def distMoney(money0: Int, children: Int): Int = {
    if (money0 < children) return -1
    var money = money0 - children
    var ans = money / 7
    if (ans > children) ans = children
    val remainMoney = money - ans * 7
    val remainChild = children - ans
    if (remainChild == 0 && remainMoney > 0) ans -= 1
    else if (remainChild == 1 && remainMoney == 3) ans -= 1
    if (ans < 0) 0 else ans
  }
}
