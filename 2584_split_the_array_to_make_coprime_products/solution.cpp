// LeetCode 2584 - Split the Array to Make Coprime Products
// https://leetcode.com/problems/split-the-array-to-make-coprime-products/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int findValidSplit(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::unordered_map<int, int> first, last;
        auto factorize = [&](int x, int idx) {
            for (int p = 2; p * p <= x; ++p) {
                if (x % p == 0) {
                    if (!first.count(p)) first[p] = idx;
                    last[p] = idx;
                    while (x % p == 0) x /= p;
                }
            }
            if (x > 1) {
                if (!first.count(x)) first[x] = idx;
                last[x] = idx;
            }
        };
        for (int i = 0; i < n; ++i) factorize(nums[i], i);
        int far = 0;
        for (int i = 0; i < n - 1; ++i) {
            int x = nums[i];
            for (int p = 2; p * p <= x; ++p) {
                if (x % p == 0) {
                    if (last[p] > far) far = last[p];
                    while (x % p == 0) x /= p;
                }
            }
            if (x > 1 && last[x] > far) far = last[x];
            if (far == i) return i;
        }
        return -1;
    }
};
