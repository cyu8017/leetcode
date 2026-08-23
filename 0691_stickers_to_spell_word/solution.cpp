// LeetCode 0691 - Stickers to Spell Word
// https://leetcode.com/problems/stickers-to-spell-word/

#include <algorithm>
#include <climits>
#include <map>
#include <string>
#include <vector>

class Solution {
    std::vector<char> chars_;
    std::vector<std::vector<int>> sticks_;
    std::map<std::vector<int>, int> memo_;

    int dfs(std::vector<int> state) {
        if (memo_.count(state)) {
            return memo_[state];
        }
        int i = 0;
        while (i < static_cast<int>(state.size()) && state[i] == 0) {
            ++i;
        }
        if (i == static_cast<int>(state.size())) {
            return memo_[state] = 0;
        }
        const char first = chars_[i];
        int best = INT_MAX / 4;
        for (const auto& stick : sticks_) {
            if (stick[first - 'a'] == 0) {
                continue;
            }
            std::vector<int> nxt = state;
            for (int j = 0; j < static_cast<int>(chars_.size()); ++j) {
                nxt[j] = std::max(0, nxt[j] - stick[chars_[j] - 'a']);
            }
            best = std::min(best, 1 + dfs(nxt));
        }
        return memo_[state] = best;
    }

public:
    int minStickers(std::vector<std::string>& stickers, std::string target) {
        std::vector<int> need(26, 0);
        for (char ch : target) {
            ++need[ch - 'a'];
        }
        chars_.clear();
        for (int i = 0; i < 26; ++i) {
            if (need[i]) {
                chars_.push_back(static_cast<char>('a' + i));
            }
        }
        sticks_.clear();
        for (const std::string& sticker : stickers) {
            std::vector<int> counts(26, 0);
            for (char ch : sticker) {
                ++counts[ch - 'a'];
            }
            bool useful = false;
            for (char ch : chars_) {
                if (counts[ch - 'a']) {
                    useful = true;
                    break;
                }
            }
            if (useful) {
                sticks_.push_back(counts);
            }
        }
        memo_.clear();
        std::vector<int> state;
        for (char ch : chars_) {
            state.push_back(need[ch - 'a']);
        }
        const int result = dfs(state);
        return result >= INT_MAX / 4 ? -1 : result;
    }
};
