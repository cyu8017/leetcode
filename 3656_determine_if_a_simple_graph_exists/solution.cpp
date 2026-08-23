// LeetCode 3656 - Determine if a Simple Graph Exists
// https://leetcode.com/problems/determine-if-a-simple-graph-exists/

#include <algorithm>
#include <vector>

class Solution {
public:
    bool simpleGraphExists(std::vector<int>& degrees) {
        int n = (int)degrees.size();
        std::vector<int> d = degrees;
        std::sort(d.begin(), d.end(), std::greater<int>());
        long long sum = 0;
        for (int x : d) {
            if (x < 0 || x >= n) return false;
            sum += x;
        }
        if (sum % 2 == 1) return false;
        std::vector<long long> prefix(n + 1);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + d[i];
        for (int k = 1; k <= n; k++) {
            long long right = 0;
            for (int i = k; i < n; i++) right += d[i] < k ? d[i] : k;
            if (prefix[k] > 1LL * k * (k - 1) + right) return false;
        }
        return true;
    }
};
