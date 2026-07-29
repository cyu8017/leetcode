// LeetCode 0763 - Partition Labels
// https://leetcode.com/problems/partition-labels/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> partitionLabels(std::string s) {
        int last[26] = {};
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            last[s[i] - 'a'] = i;
        }
        int start = 0;
        int end = 0;
        std::vector<int> answer;
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            end = std::max(end, last[s[i] - 'a']);
            if (i == end) {
                answer.push_back(end - start + 1);
                start = i + 1;
            }
        }
        return answer;
    }
};
