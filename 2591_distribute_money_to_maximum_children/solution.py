# LeetCode 2591 - Distribute Money to Maximum Children
# https://leetcode.com/problems/distribute-money-to-maximum-children/

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        ans = money // 7
        if ans > children:
            ans = children
        remain_money = money - ans * 7
        remain_child = children - ans
        if remain_child == 0 and remain_money > 0:
            ans -= 1
        elif remain_child == 1 and remain_money == 3:
            ans -= 1
        if ans < 0:
            return 0
        return ans
