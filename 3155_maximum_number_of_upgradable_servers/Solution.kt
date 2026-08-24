// LeetCode 3155 - Maximum Number of Upgradable Servers
// https://leetcode.com/problems/maximum-number-of-upgradable-servers/

class Solution {
    fun maxUpgrades(count: IntArray, upgrade: IntArray, sell: IntArray, money: IntArray): IntArray {
        var ans = IntArray(count.size)
        for (i in 0 until count.size) {
            var cnt = count[i]
            ans[i] = minOf(cnt, (cnt * sell[i] + money[i]) / (upgrade[i] + sell[i]))
        }
        return ans
    }
}
