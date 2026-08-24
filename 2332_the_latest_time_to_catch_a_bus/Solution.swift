// LeetCode 2332 - The Latest Time to Catch a Bus
// https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

class Solution {
    func latestTimeCatchTheBus(_ buses: [Int], _ passengers: [Int], _ capacity: Int) -> Int {
        let buses = buses.sorted()
        let passengers = passengers.sorted()
        var pos = 0
        for bi in 0..<buses.count {
            let bus = buses[bi]
            var cap = capacity
            while cap > 0 && pos < passengers.count && passengers[pos] <= bus {
                pos += 1
                cap -= 1
            }
            if bi == buses.count - 1 {
                var cand = cap == 0 ? passengers[pos - 1] : bus
                let taken = Set(passengers)
                while taken.contains(cand) { cand -= 1 }
                return cand
            }
        }
        return -1
    }
}
