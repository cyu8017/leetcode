// LeetCode 1580 - Put Boxes Into the Warehouse II
// https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/

class Solution {
    func maxBoxesInWarehouse(_ boxes: [Int], _ warehouse: [Int]) -> Int {
        let n = warehouse.count
        var left = warehouse, right = warehouse
        for i in 1..<n { left[i] = min(left[i], left[i - 1]) }
        for i in stride(from: n - 2, through: 0, by: -1) {
            right[i] = min(right[i], right[i + 1])
        }
        let capacity = (0..<n).map { max(left[$0], right[$0]) }.sorted()
        let boxes = boxes.sorted()
        var i = 0
        for room in capacity {
            if i < boxes.count && boxes[i] <= room { i += 1 }
        }
        return i
    }
}
