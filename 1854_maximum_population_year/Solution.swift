// LeetCode 1854 - Maximum Population Year
// https://leetcode.com/problems/maximum-population-year/

class Solution {
    func maximumPopulation(_ logs: [[Int]]) -> Int {
        var diff = Array(repeating: 0, count: 101)

        for log in logs {
            diff[log[0] - 1950] += 1
            diff[log[1] - 1950] -= 1
        }

        var bestYear = 1950
        var bestPopulation = 0
        var population = 0

        for offset in 0..<101 {
            population += diff[offset]
            if population > bestPopulation {
                bestPopulation = population
                bestYear = 1950 + offset
            }
        }

        return bestYear
    }
}
