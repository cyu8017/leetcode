// LeetCode 3100 - Water Bottles II
// https://leetcode.com/problems/water-bottles-ii/

class Solution {
    func maxBottlesDrunk(_ numBottles: Int, _ numExchange: Int) -> Int {
        var bottles = numBottles, ex = numExchange, ans = numBottles
        while bottles >= ex {
            bottles -= ex
            ex += 1
            ans += 1
            bottles += 1
        }
        return ans
    }
}
