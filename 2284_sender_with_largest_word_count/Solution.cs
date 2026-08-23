// LeetCode 2284 - Sender With Largest Word Count
// https://leetcode.com/problems/sender-with-largest-word-count/

using System.Collections.Generic;

public class Solution {
    public string LargestWordCount(string[] messages, string[] senders) {
        var count = new Dictionary<string, int>();
        string best = "";
        int bestCnt = -1;
        for (int i = 0; i < messages.Length; i++) {
            int words = 1;
            foreach (char c in messages[i]) if (c == ' ') words++;
            count.TryGetValue(senders[i], out int prev);
            count[senders[i]] = prev + words;
            int c2 = count[senders[i]];
            if (c2 > bestCnt || (c2 == bestCnt && string.CompareOrdinal(senders[i], best) > 0)) {
                bestCnt = c2;
                best = senders[i];
            }
        }
        return best;
    }
}
