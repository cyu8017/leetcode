// LeetCode 1580 - Put Boxes Into the Warehouse II
// https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/

class Solution {
    fun maxBoxesInWarehouse(boxes: IntArray, warehouse: IntArray): Int {
        val n = warehouse.size
        val left = warehouse.copyOf()
        val right = warehouse.copyOf()
        for (i in 1 until n) left[i] = minOf(left[i], left[i - 1])
        for (i in n - 2 downTo 0) right[i] = minOf(right[i], right[i + 1])
        val capacity = IntArray(n) { i -> maxOf(left[i], right[i]) }
        capacity.sort()
        boxes.sort()
        var i = 0
        for (room in capacity) {
            if (i < boxes.size && boxes[i] <= room) i++
        }
        return i
    }
}
