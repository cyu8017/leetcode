// LeetCode 2591 - Distribute Money to Maximum Children
// https://leetcode.com/problems/distribute-money-to-maximum-children/

class Solution {
    fun distMoney(money: Int, children: Int): Int {
        if (money < children) return -1
        var m = money - children
        var ans = m / 7
        if (ans > children) ans = children
        val remainMoney = m - ans * 7
        val remainChild = children - ans
        if (remainChild == 0 && remainMoney > 0) ans -= 1
        else if (remainChild == 1 && remainMoney == 3) ans -= 1
        if (ans < 0) return 0
        return ans
    }
}
