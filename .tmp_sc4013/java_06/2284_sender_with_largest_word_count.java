// LeetCode 2284 - Sender With Largest Word Count
// https://leetcode.com/problems/sender-with-largest-word-count/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public String largestWordCount(String[] messages, String[] senders) {
        Map<String, Integer> count = new HashMap<>();
        String best = "";
        int bestCnt = -1;
        for (int i = 0; i < messages.length; i++) {
            int words = 1;
            for (char c : messages[i].toCharArray()) if (c == ' ') words++;
            int prev = count.getOrDefault(senders[i], 0);
            count.put(senders[i], prev + words);
            int c2 = count.get(senders[i]);
            if (c2 > bestCnt || (c2 == bestCnt && senders[i].compareTo(best) > 0)) {
                bestCnt = c2;
                best = senders[i];
            }
        }
        return best;
    }
}
