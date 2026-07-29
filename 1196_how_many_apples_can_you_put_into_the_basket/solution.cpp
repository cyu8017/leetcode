// LeetCode 1196 - How Many Apples Can You Put into the Basket
// https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxNumberOfApples(std::vector<int>& weight) {
        std::sort(weight.begin(), weight.end());
        int total = 0;
        for (int i = 0; i < static_cast<int>(weight.size()); ++i) {
            total += weight[i];
            if (total > 5000) return i;
        }
        return static_cast<int>(weight.size());
    }
};
