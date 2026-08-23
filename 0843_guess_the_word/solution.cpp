// LeetCode 0843 - Guess the Word
// https://leetcode.com/problems/guess-the-word/

#include <algorithm>
#include <string>
#include <vector>

/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *  public:
 *   int guess(std::string word);
 * };
 */
class Master {
public:
    virtual int guess(std::string word) = 0;
    virtual ~Master() = default;
};

class Solution {
public:
    void findSecretWord(std::vector<std::string>& words, Master& master) {
        auto match = [](const std::string& a, const std::string& b) {
            int m = 0;
            for (size_t i = 0; i < a.size(); ++i) {
                if (a[i] == b[i]) {
                    ++m;
                }
            }
            return m;
        };

        std::vector<std::string> candidates = words;
        while (!candidates.empty()) {
            std::string best = candidates[0];
            int bestWorst = static_cast<int>(candidates.size()) + 1;
            for (const auto& w : candidates) {
                int buckets[7] = {};
                for (const auto& c : candidates) {
                    ++buckets[match(w, c)];
                }
                int worst = *std::max_element(buckets, buckets + 7);
                if (worst < bestWorst) {
                    bestWorst = worst;
                    best = w;
                }
            }
            int score = master.guess(best);
            if (score == 6) {
                return;
            }
            std::vector<std::string> next;
            for (const auto& c : candidates) {
                if (match(c, best) == score) {
                    next.push_back(c);
                }
            }
            candidates.swap(next);
        }
    }
};
