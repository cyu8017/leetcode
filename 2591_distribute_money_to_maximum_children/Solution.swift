// LeetCode 2591 - Distribute Money to Maximum Children
// https://leetcode.com/problems/distribute-money-to-maximum-children/

class Solution {
    func distMoney(_ money: Int, _ children: Int) -> Int {
        if money < children { return -1 }
        var money = money - children
        var ans = min(money / 7, children)
        let remainMoney = money - ans * 7
        let remainChild = children - ans
        if remainChild == 0 && remainMoney > 0 { ans -= 1 }
        else if remainChild == 1 && remainMoney == 3 { ans -= 1 }
        return max(ans, 0)
    }
}
