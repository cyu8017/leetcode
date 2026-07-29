// LeetCode 0923 - 3Sum With Multiplicity
// https://leetcode.com/problems/3sum-with-multiplicity/

#include <vector>

class Solution {
public:
    int threeSumMulti(std::vector<int>& arr, int target) {
        const int MOD = 1000000007;
        long long count[101] = {};
        for (int x : arr) count[x]++;
        long long ans = 0;
        for (int a = 0; a <= 100; a++) if (count[a]) {
            for (int b = a; b <= 100; b++) if (count[b]) {
                int c = target - a - b;
                if (c < b || c > 100 || !count[c]) continue;
                if (a == b && b == c) ans += count[a] * (count[a] - 1) * (count[a] - 2) / 6;
                else if (a == b) ans += count[a] * (count[a] - 1) / 2 * count[c];
                else if (b == c) ans += count[a] * count[b] * (count[b] - 1) / 2;
                else ans += count[a] * count[b] * count[c];
            }
        }
        return (int)(ans % MOD);
    }
};
