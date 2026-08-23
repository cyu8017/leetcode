// LeetCode 3767 - Maximize Points After Choosing K Tasks
// https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxPoints(std::vector<int>& technique1, std::vector<int>& technique2, int k) {
        int n = (int)technique1.size();
        std::vector<int> idx(n);
        for (int i = 0; i < n; i++) idx[i] = i;
        std::sort(idx.begin(), idx.end(), [&](int i, int j) {
            return technique1[j] - technique2[j] < technique1[i] - technique2[i];
        });
        long long ans = 0;
        for (int x : technique2) ans += x;
        for (int i = 0; i < k; i++) {
            int index = idx[i];
            ans -= technique2[index];
            ans += technique1[index];
        }
        for (int i = k; i < n; i++) {
            int index = idx[i];
            if (technique1[index] >= technique2[index]) {
                ans -= technique2[index];
                ans += technique1[index];
            }
        }
        return ans;
    }
};
