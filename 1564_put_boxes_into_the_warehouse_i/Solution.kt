// LeetCode 1564 - Put Boxes Into the Warehouse I
// https://leetcode.com/problems/put-boxes-into-the-warehouse-i/

class Solution {
    fun maxBoxesInWarehouse(boxes: IntArray, warehouse: IntArray): Int {
        for (i in 1 until warehouse.size) {
            warehouse[i] = minOf(warehouse[i], warehouse[i - 1])
        }
        boxes.sort()
        var room = warehouse.size - 1
        var used = 0
        for (box in boxes) {
            while (room >= 0 && warehouse[room] < box) room--
            if (room < 0) break
            used++
            room--
        }
        return used
    }
}
