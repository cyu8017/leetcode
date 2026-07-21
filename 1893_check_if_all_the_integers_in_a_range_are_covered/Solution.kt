// LeetCode 1893 - Check if All the Integers in a Range Are Covered
// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

class Solution {
    fun isCovered(ranges: Array<IntArray>, left: Int, right: Int): Boolean {
        val covered = BooleanArray(51)
        for (range in ranges) {
            for (value in range[0]..range[1]) {
                covered[value] = true
            }
        }
        for (value in left..right) {
            if (!covered[value]) return false
        }
        return true
    }
}
