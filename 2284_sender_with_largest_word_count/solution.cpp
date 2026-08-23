// LeetCode 2284 - Sender With Largest Word Count
// https://leetcode.com/problems/sender-with-largest-word-count/

#include <vector>
#include <string>
#include <unordered_map>

class Solution {
public:
    std::string largestWordCount(std::vector<std::string>& messages, std::vector<std::string>& senders) {
        std::unordered_map<std::string, int> count;
        std::string best;
        int bestCnt = -1;
        for (size_t i = 0; i < messages.size(); ++i) {
            int words = 1;
            for (char c : messages[i]) if (c == ' ') words++;
            count[senders[i]] += words;
            int c = count[senders[i]];
            if (c > bestCnt || (c == bestCnt && senders[i] > best)) {
                bestCnt = c;
                best = senders[i];
            }
        }
        return best;
    }
};
