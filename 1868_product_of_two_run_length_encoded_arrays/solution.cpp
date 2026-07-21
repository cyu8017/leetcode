// LeetCode 1868 - Product of Two Run-Length Encoded Arrays
// https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> findRLEArray(std::vector<std::vector<int>>& encoded1,
                                               std::vector<std::vector<int>>& encoded2) {
        std::vector<std::vector<int>> result;
        int i = 0;
        int j = 0;
        int rem1 = encoded1[0][1];
        int rem2 = encoded2[0][1];
        while (i < static_cast<int>(encoded1.size())) {
            int take = std::min(rem1, rem2);
            int value = encoded1[i][0] * encoded2[j][0];
            if (!result.empty() && result.back()[0] == value) {
                result.back()[1] += take;
            } else {
                result.push_back({value, take});
            }
            rem1 -= take;
            rem2 -= take;
            if (rem1 == 0) {
                i++;
                if (i < static_cast<int>(encoded1.size())) {
                    rem1 = encoded1[i][1];
                }
            }
            if (rem2 == 0) {
                j++;
                if (j < static_cast<int>(encoded2.size())) {
                    rem2 = encoded2[j][1];
                }
            }
        }
        return result;
    }
};
