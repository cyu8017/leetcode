class Solution {
    func canCompleteCircuit(_ gas: [Int], _ cost: [Int]) -> Int {
        var total = 0
        var tank = 0
        var start = 0

        for i in gas.indices {
            let difference = gas[i] - cost[i]
            total += difference
            tank += difference
            if tank < 0 {
                start = i + 1
                tank = 0
            }
        }
        return total >= 0 ? start : -1
    }
}