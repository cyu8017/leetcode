// LeetCode 3155 - Maximum Number of Upgradable Servers
// https://leetcode.com/problems/maximum-number-of-upgradable-servers/

class Solution {
    func maxUpgrades(_ count: [Int], _ upgrade: [Int], _ sell: [Int], _ money: [Int]) -> [Int] {
        (0..<count.count).map { i in
            min(count[i], (count[i] * sell[i] + money[i]) / (upgrade[i] + sell[i]))
        }
    }
}
