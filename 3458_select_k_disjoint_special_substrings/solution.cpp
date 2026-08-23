// LeetCode 3458 - Select K Disjoint Special Substrings
// https://leetcode.com/problems/select-k-disjoint-special-substrings/

#include <string>
#include <vector>
#include <algorithm>
#include <set>

class Solution {
public:
    bool maxSubstringLength(std::string s, int k) {
        int n = (int)s.size();
        std::vector<int> first(26, n), last(26, -1);
        for (int i = 0; i < n; i++) {
            int ci = s[i] - 'a';
            if (first[ci] == n) first[ci] = i;
            last[ci] = i;
        }
        std::vector<std::pair<int, int>> segs;
        for (int c = 0; c < 26; c++) {
            if (last[c] == -1) continue;
            int l = first[c], r = last[c];
            for (int i = l; i <= r; i++) {
                int ci = s[i] - 'a';
                if (first[ci] < l) {
                    l = first[ci];
                    i = l - 1;
                    continue;
                }
                if (last[ci] > r) r = last[ci];
            }
            if (!(l == 0 && r == n - 1)) segs.push_back({l, r});
        }
        std::set<std::pair<int, int>> uniq;
        std::vector<std::pair<int, int>> arr;
        for (auto& sg : segs) {
            if (uniq.insert(sg).second) arr.push_back(sg);
        }
        std::sort(arr.begin(), arr.end(), [](auto& a, auto& b) { return a.second < b.second; });
        int cnt = 0, end = -1;
        for (auto& sg : arr) {
            if (sg.first > end) {
                cnt++;
                end = sg.second;
            }
        }
        return cnt >= k;
    }
};
