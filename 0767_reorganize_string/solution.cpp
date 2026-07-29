// LeetCode 0767 - Reorganize String
// https://leetcode.com/problems/reorganize-string/

#include <queue>
#include <string>
#include <utility>

class Solution {
public:
    std::string reorganizeString(std::string s) {
        int freq[26] = {};
        for (char ch : s) {
            ++freq[ch - 'a'];
        }
        using Item = std::pair<int, char>;
        std::priority_queue<Item> heap;
        for (int i = 0; i < 26; ++i) {
            if (freq[i]) {
                heap.push({freq[i], static_cast<char>('a' + i)});
            }
        }
        if (!heap.empty() && heap.top().first > (static_cast<int>(s.size()) + 1) / 2) {
            return "";
        }
        std::string result;
        while (heap.size() >= 2) {
            auto [c1, a] = heap.top();
            heap.pop();
            auto [c2, b] = heap.top();
            heap.pop();
            result.push_back(a);
            result.push_back(b);
            if (--c1) {
                heap.push({c1, a});
            }
            if (--c2) {
                heap.push({c2, b});
            }
        }
        if (!heap.empty()) {
            result.push_back(heap.top().second);
        }
        return result;
    }
};
