// LeetCode 3471 - Find the Largest Almost Missing Integer
// https://leetcode.com/problems/find-the-largest-almost-missing-integer/

class Solution {
    fun largestInteger(nums: IntArray, k: Int): Int {
        var n = nums.size
        var cnt = HashMap<Int, Int>()
        var i = 0
        while (i + k <= n) {
            var seen = HashSet<Int>()
            for (j in i until i + k) { seen.add(nums[j]) }
            for (x in seen) { cnt.merge(x, 1, Int::plus) }
            i = i + 1
        }
        var ans = -1
        for (e in cnt) {
            if (e.value == 1 && e.key > ans) ans = e.key
        }
        return ans
    }
}
