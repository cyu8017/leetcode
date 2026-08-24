// LeetCode 3092 - Most Frequent IDs
// https://leetcode.com/problems/most-frequent-ids/

class Solution {
    fun mostFrequentIDs(nums: IntArray, freq: IntArray): LongArray {
        var n = nums.size
        var cnt = HashMap<Int, Int>()
        var lazy = HashMap<Int, Int>()
        var ans = LongArray(n)
        var pq = PriorityQueue((a, b) -> b - a)
        for (i in 0 until n) {
            var x = nums[i]
            var f = freq[i]
            var old = cnt.getOrDefault(x, 0)
            lazy[old] = lazy.getOrDefault(old, 0) + 1
            var neu = old + f
            cnt[x] = neu
            pq.offer(neu)
            while (!pq.isEmpty() && lazy.getOrDefault(pq.peek(), 0) > 0) {
                var top = pq.poll()
                lazy[top] = lazy[top] - 1
            }
            if (!pq.isEmpty()) ans[i] = pq.peek()
        }
        return ans
    }
}
