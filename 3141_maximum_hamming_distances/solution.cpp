// LeetCode 3141 - Maximum Hamming Distances
// https://leetcode.com/problems/maximum-hamming-distances/

#include <vector>

class Solution {
public:
    std::vector<int> maxHammingDistances(std::vector<int>& nums, int m) {
        std::vector<int> dist(1 << m, -1);
        std::vector<int> q;
        for (int x : nums) {
            dist[x] = 0;
            q.push_back(x);
        }
        for (int k = 1; !q.empty(); k++) {
            std::vector<int> t;
            for (int x : q) {
                for (int i = 0; i < m; i++) {
                    int y = x ^ (1 << i);
                    if (dist[y] == -1) {
                        dist[y] = k;
                        t.push_back(y);
                    }
                }
            }
            q.swap(t);
        }
        for (int i = 0; i < (int)nums.size(); i++) {
            int x = nums[i];
            nums[i] = m - dist[x ^ ((1 << m) - 1)];
        }
        return nums;
    }
};
