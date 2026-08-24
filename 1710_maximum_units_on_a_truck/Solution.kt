// LeetCode 1710 - Maximum Units on a Truck
// https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution {
    fun maximumUnits(boxTypes: Array<IntArray>, truckSize: Int): Int {
        boxTypes.sortByDescending { it[1] }
        var remaining = truckSize
        var total = 0
        for (box in boxTypes) {
            val take = minOf(box[0], remaining)
            total += take * box[1]
            remaining -= take
            if (remaining == 0) {
                break
            }
        }
        return total
    }
}
