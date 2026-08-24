// LeetCode 2073 - Time Needed to Buy Tickets
// https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution {
    fun timeRequiredToBuy(tickets: IntArray, k: Int): Int {
var ans: Int = 0
for (i in 0 until tickets.size) {
if (i <= k) {
ans += minOf(tickets[i], tickets[k])
}
else {
ans += minOf(tickets[i], tickets[k] - 1)
}
}
return ans
}
}
