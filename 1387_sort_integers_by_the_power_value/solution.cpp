#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
    std::unordered_map<int, int> memo;
    int power(int x) {
        if (x == 1) return 0;
        if (memo.count(x)) return memo[x];
        return memo[x] = 1 + power(x % 2 == 0 ? x / 2 : 3 * x + 1);
    }
public:
    int getKth(int lo, int hi, int k) {
        std::vector<int> vals;
        for (int x = lo; x <= hi; ++x) vals.push_back(x);
        std::sort(vals.begin(), vals.end(), [&](int a, int b) {
            int pa = power(a), pb = power(b);
            return pa != pb ? pa < pb : a < b;
        });
        return vals[k - 1];
    }
};
