// LeetCode 3259 - Maximum Energy Boost From Two Drinks
// https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

class Solution {
    func maxEnergyBoost(_ energyDrinkA: [Int], _ energyDrinkB: [Int]) -> Int {
        let n = energyDrinkA.count
        var dpA = Array(repeating: 0, count: n)
        var dpB = Array(repeating: 0, count: n)
        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]
        if n == 1 { return max(dpA[0], dpB[0]) }
        dpA[1] = energyDrinkA[1] + dpA[0]
        dpB[1] = energyDrinkB[1] + dpB[0]
        if n >= 3 {
            for i in 2..<n {
                dpA[i] = energyDrinkA[i] + max(dpA[i - 1], dpB[i - 2])
                dpB[i] = energyDrinkB[i] + max(dpB[i - 1], dpA[i - 2])
            }
        }
        return max(dpA[n - 1], dpB[n - 1])
    }
}
