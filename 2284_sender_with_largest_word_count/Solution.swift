// LeetCode 2284 - Sender With Largest Word Count
// https://leetcode.com/problems/sender-with-largest-word-count/

class Solution {
    func largestWordCount(_ messages: [String], _ senders: [String]) -> String {
        var count: [String: Int] = [:]
        var best = ""
        var bestCnt = -1
        for i in 0..<messages.count {
            let words = messages[i].split(separator: " ").count
            count[senders[i], default: 0] += words
            let c2 = count[senders[i]]!
            if c2 > bestCnt || (c2 == bestCnt && senders[i] > best) {
                bestCnt = c2
                best = senders[i]
            }
        }
        return best
    }
}
