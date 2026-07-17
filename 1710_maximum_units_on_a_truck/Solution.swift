// LeetCode 1710 - Maximum Units on a Truck
// https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution {
    func maximumUnits(_ boxTypes: [[Int]], _ truckSize: Int) -> Int {
        var remaining = truckSize
        var total = 0
        for box in boxTypes.sorted(by: { $0[1] > $1[1] }) {
            let take = min(box[0], remaining)
            total += take * box[1]
            remaining -= take
            if remaining == 0 {
                break
            }
        }
        return total
    }
}
