// LeetCode 2591 - Distribute Money to Maximum Children
// https://leetcode.com/problems/distribute-money-to-maximum-children/

public class Solution {
    public int DistMoney(int money, int children) {
        if (money < children) return -1;
        money -= children;
        int ans = money / 7;
        if (ans > children) ans = children;
        int remainMoney = money - ans * 7;
        int remainChild = children - ans;
        if (remainChild == 0 && remainMoney > 0) ans--;
        else if (remainChild == 1 && remainMoney == 3) ans--;
        if (ans < 0) return 0;
        return ans;
    }
}
