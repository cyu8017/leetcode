// LeetCode 1520 - Maximum Number of Non-Overlapping Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/

#include <algorithm>
#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<std::string> maxNumOfSubstrings(std::string s) {
        std::vector<int> first(26, -1);
        std::vector<int> last(26, -1);
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            const int idx = s[i] - 'a';
            if (first[idx] == -1) {
                first[idx] = i;
            }
            last[idx] = i;
        }

        std::vector<std::pair<int, int>> intervals;
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            if (first[s[i] - 'a'] != i) {
                continue;
            }
            int end = last[s[i] - 'a'];
            int j = i;
            bool valid = true;
            while (j <= end) {
                if (first[s[j] - 'a'] < i) {
                    valid = false;
                    break;
                }
                end = std::max(end, last[s[j] - 'a']);
                ++j;
            }
            if (valid) {
                intervals.emplace_back(end, i);
            }
        }

        std::sort(intervals.begin(), intervals.end());
        std::vector<std::string> answer;
        int previous_end = -1;
        for (const auto& [end, start] : intervals) {
            if (start > previous_end) {
                answer.push_back(s.substr(start, end - start + 1));
                previous_end = end;
            }
        }
        std::sort(answer.begin(), answer.end(),
                  [](const std::string& a, const std::string& b) { return a.size() < b.size(); });
        return answer;
    }
};
