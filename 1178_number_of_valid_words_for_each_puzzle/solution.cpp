// LeetCode 1178 - Number of Valid Words for Each Puzzle
// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> findNumOfValidWords(std::vector<std::string>& words, std::vector<std::string>& puzzles) {
        auto maskOf = [](const std::string& s) {
            int mask = 0;
            for (char ch : s) mask |= 1 << (ch - 'a');
            return mask;
        };
        std::unordered_map<int, int> freq;
        for (const auto& w : words) ++freq[maskOf(w)];
        std::vector<int> ans;
        for (const auto& puzzle : puzzles) {
            int first = 1 << (puzzle[0] - 'a');
            int full = maskOf(puzzle);
            int sub = full, total = 0;
            while (true) {
                if (sub & first) total += freq[sub];
                if (sub == 0) break;
                sub = (sub - 1) & full;
            }
            ans.push_back(total);
        }
        return ans;
    }
};
