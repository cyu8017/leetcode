// LeetCode 1999 - Smallest Greater Multiple Made of Two Digits
#include <algorithm>
#include <queue>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int findInteger(int k, int digit1, int digit2) {
        std::vector<int> digits = {digit1, digit2};
        std::sort(digits.begin(), digits.end());
        digits.erase(std::unique(digits.begin(), digits.end()), digits.end());
        std::queue<long long> q;
        std::unordered_set<long long> seen;
        for (int d : digits) {
            if (d != 0) {
                q.push(d);
                seen.insert(d);
            }
        }
        if (q.empty()) return -1;
        const long long LIMIT = 2147483647LL;
        while (!q.empty()) {
            long long x = q.front();
            q.pop();
            if (x > k && x % k == 0) return (int)x;
            for (int d : digits) {
                long long nx = x * 10 + d;
                if (nx <= LIMIT && !seen.count(nx)) {
                    seen.insert(nx);
                    q.push(nx);
                }
            }
        }
        return -1;
    }
};
