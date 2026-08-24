// LeetCode 2284 - Sender With Largest Word Count
// https://leetcode.com/problems/sender-with-largest-word-count/

class Solution {
    fun largestWordCount(messages: Array<String>, senders: Array<String>): String {
        val count = HashMap<String, Int>()
        var best = ""
        var bestCnt = -1
        for (i in messages.indices) {
            var words = 1
            for (c in messages[i]) if (c == ' ') words++
            val prev = count.getOrDefault(senders[i], 0)
            count[senders[i]] = prev + words
            val c2 = count[senders[i]]!!
            if (c2 > bestCnt || (c2 == bestCnt && senders[i] > best)) {
                bestCnt = c2
                best = senders[i]
            }
        }
        return best
    }
}
