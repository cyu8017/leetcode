// LeetCode 1518 - Water Bottles
// https://leetcode.com/problems/water-bottles/

class Solution {
    func numWaterBottles(_ numBottles: Int, _ numExchange: Int) -> Int {
        var bottles = numBottles
        var total = numBottles
        while bottles >= numExchange {
            let new = bottles / numExchange
            let rem = bottles % numExchange
            total += new
            bottles = new + rem
        }
        return total
    }
}
