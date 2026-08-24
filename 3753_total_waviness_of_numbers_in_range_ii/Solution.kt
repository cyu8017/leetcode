// LeetCode 3753 - Total Waviness Of Numbers In Range Ii
// https://leetcode.com/problems/total_waviness_of_numbers_in_range_ii/

class Solution {
    private class Result(var count: Long = 0, var sum: Long = 0)

    private fun wavinessUpTo(limit: Long): Long {
        if (limit < 0) return 0
        val digits = ArrayList<Int>()
        if (limit == 0L) {
            digits.add(0)
        } else {
            var value = limit
            while (value > 0) {
                digits.add((value % 10).toInt())
                value /= 10
            }
            digits.reverse()
        }
        val memo = HashMap<String, Result>()
        return dfs(0, 10, 10, false, true, digits, memo).sum
    }

    private fun dfs(
        position: Int,
        secondLast: Int,
        last: Int,
        started: Boolean,
        tight: Boolean,
        digits: MutableList<Int>,
        memo: HashMap<String, Result>,
    ): Result {
        if (position == digits.size) return Result(1, 0)
        val key = "$position,$secondLast,$last,$started"
        if (!tight && memo.containsKey(key)) return memo[key]!!
        val upper = if (tight) digits[position] else 9
        val result = Result()
        for (digit in 0..upper) {
            val nextTight = tight && digit == upper
            var nextSecondLast = secondLast
            var nextLast = last
            val nextStarted = started || digit != 0
            var add = 0L
            if (!nextStarted) {
                nextSecondLast = 10
                nextLast = 10
            } else if (!started) {
                nextSecondLast = 10
                nextLast = digit
            } else {
                if (secondLast != 10 &&
                    ((last > secondLast && last > digit) || (last < secondLast && last < digit))
                ) {
                    add = 1
                }
                nextSecondLast = last
                nextLast = digit
            }
            val child = dfs(position + 1, nextSecondLast, nextLast, nextStarted, nextTight, digits, memo)
            result.count += child.count
            result.sum += child.sum + add * child.count
        }
        if (!tight) memo[key] = result
        return result
    }

    fun totalWaviness(a: Long, b: Long): Long {
        return wavinessUpTo(b) - wavinessUpTo(a - 1)
    }
}
