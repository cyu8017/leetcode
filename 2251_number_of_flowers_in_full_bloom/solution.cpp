// LeetCode 2251 - Number of Flowers in Full Bloom
// https://leetcode.com/problems/number-of-flowers-in-full-bloom/

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> fullBloomFlowers(std::vector<std::vector<int>>& flowers, std::vector<int>& people) {
        std::vector<int> start, end;
        for (auto& f : flowers) { start.push_back(f[0]); end.push_back(f[1]); }
        std::sort(start.begin(), start.end());
        std::sort(end.begin(), end.end());
        std::vector<int> ans(people.size());
        for (size_t i = 0; i < people.size(); ++i) {
            int t = people[i];
            int started = (int)(std::upper_bound(start.begin(), start.end(), t) - start.begin());
            int ended = (int)(std::lower_bound(end.begin(), end.end(), t) - end.begin());
            ans[i] = started - ended;
        }
        return ans;
    }
};
