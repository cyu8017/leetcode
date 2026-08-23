// LeetCode 2031 - Count Subarrays With More Ones Than Zeros
// https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/

#include <algorithm>
#include <array>
#include <bitset>
#include <cmath>
#include <cstdint>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

class Solution {
    struct Fenwick {
        vector<int> bit;
        Fenwick(int n) : bit(n + 2) {}
        void add(int i, int v) { for (; i < (int)bit.size(); i += i & -i) bit[i] += v; }
        int sum(int i) { int s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; }
    };
public:
    int subarraysWithMoreZerosThanOnes(vector<int>& nums) {
        const int MOD = 1'000'000'007;
        int n = (int)nums.size(), offset = n + 1;
        Fenwick fw(2 * n + 5);
        int pref = 0, ans = 0;
        fw.add(offset, 1);
        for (int x : nums) {
            pref += (x == 1) ? 1 : -1;
            int idx = pref + offset;
            ans = (ans + fw.sum(idx - 1)) % MOD;
            fw.add(idx, 1);
        }
        return ans;
    }
};
