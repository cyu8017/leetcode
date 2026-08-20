// LeetCode 1564 - Put Boxes Into the Warehouse I
// https://leetcode.com/problems/put-boxes-into-the-warehouse-i/

class Solution {
    func maxBoxesInWarehouse(_ boxes: [Int], _ warehouse: [Int]) -> Int {
        var warehouse = warehouse
        for i in 1..<warehouse.count {
            warehouse[i] = min(warehouse[i], warehouse[i - 1])
        }
        let boxes = boxes.sorted()
        var room = warehouse.count - 1
        var used = 0
        for box in boxes {
            while room >= 0 && warehouse[room] < box { room -= 1 }
            if room < 0 { break }
            used += 1
            room -= 1
        }
        return used
    }
}
