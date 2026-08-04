// LeetCode 1538 - Guess the Majority in a Hidden Array
// https://leetcode.com/problems/guess-the-majority-in-a-hidden-array/

class ArrayReader(private val nums: IntArray) {
    fun query(a: Int, b: Int, c: Int, d: Int): Int {
        val ones = nums[a] + nums[b] + nums[c] + nums[d]
        return when (ones) {
            0, 4 -> 4
            1, 3 -> 2
            else -> 0
        }
    }

    fun length(): Int = nums.size
}

class Solution {
    fun guessMajority(nums: IntArray): Int = guessMajority(ArrayReader(nums))

    fun guessMajority(reader: ArrayReader): Int {
        val n = reader.length()
        val firstFour = reader.query(0, 1, 2, 3)
        val shifted = reader.query(1, 2, 3, 4)
        var same = 1
        var different = 0
        var differentIndex = -1
        var laterDifferent = -1
        val fourSame = firstFour == shifted
        if (fourSame) same++ else {
            different++
            differentIndex = 4
        }
        val checks = arrayOf(
            intArrayOf(0, 2, 3, 4),
            intArrayOf(0, 1, 3, 4),
            intArrayOf(0, 1, 2, 4)
        )
        for (index in checks.indices) {
            val args = checks[index]
            if (reader.query(args[0], args[1], args[2], args[3]) == shifted) {
                same++
            } else {
                different++
                differentIndex = index + 1
            }
        }
        for (i in 5 until n) {
            val iSameAsFour = reader.query(1, 2, 3, i) == shifted
            if (iSameAsFour == fourSame) {
                same++
            } else {
                different++
                differentIndex = i
                if (laterDifferent == -1) laterDifferent = i
            }
        }
        if (same == different) return -1
        return if (same > different) 0 else if (laterDifferent != -1) laterDifferent else differentIndex
    }
}
