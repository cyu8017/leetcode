#include <algorithm>
#include <unordered_map>

class Solution {
    int digitSum(int x) {
        int s = 0;
        while (x) { s += x % 10; x /= 10; }
        return s;
    }
public:
    int countLargestGroup(int n) {
        std::unordered_map<int, int> c;
        int mx = 0;
        for (int x = 1; x <= n; ++x) {
            int s = digitSum(x);
            mx = std::max(mx, ++c[s]);
        }
        int ans = 0;
        for (auto [_, v] : c) ans += v == mx;
        return ans;
    }
};
