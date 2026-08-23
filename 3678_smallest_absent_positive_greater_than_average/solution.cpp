// LeetCode 3678 - Smallest Absent Positive Greater Than Average
// https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int smallestAbsent(std::vector<int>& nums) {
        std::unordered_set<int> s;
        int sum = 0;
        for (int x : nums) {
            s.insert(x);
            sum += x;
        }
        int ans = std::max(1, sum / (int)nums.size() + 1);
        while (s.count(ans)) ans++;
        return ans;
    }
};
