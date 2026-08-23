// LeetCode 0358 - Rearrange String k Distance Apart
// https://leetcode.com/problems/rearrange-string-k-distance-apart/

#include <algorithm>
#include <deque>
#include <queue>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

class Solution {
public:
    std::string rearrangeString(std::string s, int k) {
        std::unordered_map<char, int> counts;
        for (char ch : s) {
            counts[ch] += 1;
        }

        int maxFreq = 0;
        for (const auto& entry : counts) {
            maxFreq = std::max(maxFreq, entry.second);
        }

        int maxFreqChars = 0;
        for (const auto& entry : counts) {
            if (entry.second == maxFreq) {
                maxFreqChars += 1;
            }
        }

        if ((static_cast<int>(s.size()) - maxFreqChars) < (maxFreq - 1) * (k - 1)) {
            return "";
        }

        auto compare = [](const std::pair<int, char>& left, const std::pair<int, char>& right) {
            if (left.first != right.first) {
                return left.first > right.first;
            }
            return left.second > right.second;
        };

        std::priority_queue<std::pair<int, char>, std::vector<std::pair<int, char>>, decltype(compare)> heap(compare);
        for (const auto& entry : counts) {
            heap.push({entry.second, entry.first});
        }

        std::deque<std::tuple<int, char, int>> queue;
        std::string result;
        int index = 0;

        while (!heap.empty() || !queue.empty()) {
            while (!queue.empty() && std::get<2>(queue.front()) <= index) {
                auto item = queue.front();
                queue.pop_front();
                heap.push({std::get<0>(item), std::get<1>(item)});
            }

            if (heap.empty()) {
                return "";
            }

            auto top = heap.top();
            heap.pop();
            result.push_back(top.second);
            if (top.first - 1 > 0) {
                queue.push_back({top.first - 1, top.second, index + k});
            }
            index += 1;
        }

        return result;
    }
};
