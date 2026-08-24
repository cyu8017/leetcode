// LeetCode 2263 - Make Array Non-decreasing or Non-increasing
// https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

class Solution {

    private fun cost(arr: IntArray): Int {

            var h = PriorityQueue({ a, b -> Integer.compare(b, a }))
            var ans = 0
            for (x in arr) {
                if (!h.isEmpty() && h.peek() > x) {
                    var t = h.poll()
                    ans += t - x
                    h.offer(x)
                }
                h.offer(x)
            }
            return ans

    }


    fun convertArray(nums: IntArray): Int {

            var rev = IntArray(nums.size)
            for (i in 0 until nums.size) { rev[i] = nums[nums.size - 1 - i] }
            return minOf(cost(nums), cost(rev))

    }

}
