// LeetCode 0471 - Encode String with Shortest Length
// https://leetcode.com/problems/encode-string-with-shortest-length/

#include <string>
#include <vector>

class Solution {
    std::string encodeWord(const std::string& word) {
        const int size = static_cast<int>(word.size());
        std::string best = word;
        for (int unitLength = 1; unitLength <= size / 2; ++unitLength) {
            if (size % unitLength != 0) {
                continue;
            }
            const std::string unit = word.substr(0, unitLength);
            bool matches = true;
            for (int start = unitLength; start < size; start += unitLength) {
                if (word.compare(start, unitLength, unit) != 0) {
                    matches = false;
                    break;
                }
            }
            if (!matches) {
                continue;
            }
            const std::string encoded =
                std::to_string(size / unitLength) + "[" + unit + "]";
            if (encoded.size() < best.size() ||
                (encoded.size() == best.size() && encoded < best)) {
                best = encoded;
            }
        }
        return best;
    }

public:
    std::string encode(std::string s) {
        const int length = static_cast<int>(s.size());
        std::vector<std::string> dp(length + 1);
        for (int index = 1; index <= length; ++index) {
            dp[index] = encodeWord(s.substr(0, index));
            for (int split = 1; split < index; ++split) {
                const std::string candidate =
                    dp[index - split] + encodeWord(s.substr(index - split, split));
                if (candidate.size() < dp[index].size() ||
                    (candidate.size() == dp[index].size() && candidate < dp[index])) {
                    dp[index] = candidate;
                }
            }
        }
        return dp[length];
    }
};
