// LeetCode 3081 - Replace Question Marks in String to Minimize Its Value
// https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

#include <algorithm>
#include <queue>
#include <string>
#include <vector>

class Solution {
public:
    std::string minimizeStringValue(std::string s) {
        int cnt[26] = {};
        int k = 0;
        for (char c : s) {
            if (c == '?') k++;
            else cnt[c - 'a']++;
        }
        using P = std::pair<int, int>;
        std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
        for (int i = 0; i < 26; i++) pq.push({cnt[i], i});
        std::vector<int> t(k);
        for (int i = 0; i < k; i++) {
            auto p = pq.top(); pq.pop();
            t[i] = p.second;
            p.first++;
            pq.push(p);
        }
        std::sort(t.begin(), t.end());
        int j = 0;
        for (char& c : s) {
            if (c == '?') {
                c = (char)(t[j] + 'a');
                j++;
            }
        }
        return s;
    }
};
