// LeetCode 3526 - Range XOR Queries with Subarray Reversals
// https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> getResults(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        std::vector<int> a = nums;
        std::vector<int> ans;
        for (auto& q : queries) {
            int typ = q[0];
            if (typ == 1) {
                int l = q[1], r = q[2];
                while (l < r) { std::swap(a[l], a[r]); l++; r--; }
            } else if (typ == 2) {
                int l = q[1], r = q[2], x = 0;
                for (int i = l; i <= r; i++) x ^= a[i];
                ans.push_back(x);
            } else {
                a[q[1]] = q[2];
            }
        }
        return ans;
    }
};
