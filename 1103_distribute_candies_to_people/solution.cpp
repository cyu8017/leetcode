// LeetCode 1103 - Distribute Candies to People
// https://leetcode.com/problems/distribute-candies-to-people/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> distributeCandies(int candies, int num_people) {
        std::vector<int> ans(num_people, 0);
        int give = 1;
        int i = 0;
        while (candies > 0) {
            int take = std::min(give, candies);
            ans[i] += take;
            candies -= take;
            ++give;
            i = (i + 1) % num_people;
        }
        return ans;
    }
};
