// LeetCode 1687 - Delivering Boxes from Storage to Ports
// https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

class Solution {
    fun boxDelivering(boxes: Array<IntArray>, portsCount: Int, maxBoxes: Int, maxWeight: Int): Int {
        val n = boxes.size
        val w = IntArray(n + 1)
        val changes = IntArray(n + 1)
        for (i in 1..n) {
            w[i] = w[i - 1] + boxes[i - 1][1]
            changes[i] = changes[i - 1] + if (i > 1 && boxes[i - 1][0] != boxes[i - 2][0]) 1 else 0
        }
        val dp = IntArray(n + 1)
        val q = ArrayDeque<Int>()
        q.add(0)
        for (i in 1..n) {
            while (q.isNotEmpty() && (i - q.first() > maxBoxes || w[i] - w[q.first()] > maxWeight)) {
                q.removeFirst()
            }
            val j = q.first()
            dp[i] = dp[j] + changes[i] - changes[j + 1] + 2
            if (i < n) {
                val `val` = dp[i] - changes[i + 1]
                while (q.isNotEmpty() && dp[q.last()] - changes[q.last() + 1] >= `val`) q.removeLast()
                q.addLast(i)
            }
        }
        return dp[n]
    }
}
