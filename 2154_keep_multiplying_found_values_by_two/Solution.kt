// LeetCode 2154 - Keep Multiplying Found Values by Two
// https://leetcode.com/problems/keep-multiplying-found-values-by-two/

class Solution {
    fun findFinalValue(nums: IntArray, original: Int): Int {
        var have = HashSet()
        for (x in nums) have.add(x)
        while (have.contains(original)) original *= 2
        return original
    }
}
