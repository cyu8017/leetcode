// LeetCode 3769 - Sort Integers By Binary Reflection
// https://leetcode.com/problems/sort-integers-by-binary-reflection/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> sortByReflection(std::vector<int>& nums) {
        auto f = [](int x) {
            int y = 0;
            while (x != 0) {
                y = (y << 1) | (x & 1);
                x >>= 1;
            }
            return y;
        };
        std::sort(nums.begin(), nums.end(), [&](int a, int b) {
            int fa = f(a), fb = f(b);
            if (fa != fb) return fa < fb;
            return a < b;
        });
        return nums;
    }
};
