// LeetCode 0599 - Minimum Index Sum of Two Lists
// https://leetcode.com/problems/minimum-index-sum-of-two-lists/

#include <climits>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::string> findRestaurant(std::vector<std::string>& list1,
                                            std::vector<std::string>& list2) {
        std::unordered_map<std::string, int> index1;
        for (int i = 0; i < static_cast<int>(list1.size()); ++i) {
            index1[list1[i]] = i;
        }

        int best = INT_MAX;
        std::vector<std::string> answer;
        for (int j = 0; j < static_cast<int>(list2.size()); ++j) {
            auto it = index1.find(list2[j]);
            if (it == index1.end()) {
                continue;
            }
            int total = it->second + j;
            if (total < best) {
                best = total;
                answer = {list2[j]};
            } else if (total == best) {
                answer.push_back(list2[j]);
            }
        }
        return answer;
    }
};
