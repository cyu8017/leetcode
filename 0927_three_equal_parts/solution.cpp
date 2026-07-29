// LeetCode 0927 - Three Equal Parts
// https://leetcode.com/problems/three-equal-parts/

#include <vector>

class Solution {
public:
    std::vector<int> threeEqualParts(std::vector<int>& arr) {
        std::vector<int> ones;
        for (int i = 0; i < (int)arr.size(); i++) if (arr[i]) ones.push_back(i);
        int n = (int)ones.size();
        if (n % 3) return {-1, -1};
        if (n == 0) return {0, (int)arr.size() - 1};
        int third = n / 3;
        int length = ones.back() - ones[2 * third] + 1;
        int a = ones[0], b = ones[third], c = ones[2 * third];
        if (a + length > (int)arr.size() || b + length > (int)arr.size() || c + length > (int)arr.size())
            return {-1, -1};
        for (int i = 0; i < length; i++) {
            if (arr[a + i] != arr[b + i] || arr[a + i] != arr[c + i]) return {-1, -1};
        }
        return {a + length - 1, b + length};
    }
};
