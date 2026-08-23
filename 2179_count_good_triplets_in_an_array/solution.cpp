// LeetCode 2179 - Count Good Triplets in an Array
// https://leetcode.com/problems/count-good-triplets-in-an-array/

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
        Fenwick(int n) : bit(n) {}
        void add(int i, int v) { for (; i < (int)bit.size(); i += i & -i) bit[i] += v; }
        int sum(int i) { int s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; }
    };
public:
    long long goodTriplets(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        vector<int> pos2(n), mapped(n), left(n), right(n);
        for (int i = 0; i < n; i++) pos2[nums2[i]] = i;
        for (int i = 0; i < n; i++) mapped[i] = pos2[nums1[i]];
        Fenwick fw(n + 2);
        for (int i = 0; i < n; i++) {
            left[i] = fw.sum(mapped[i]);
            fw.add(mapped[i] + 1, 1);
        }
        fw = Fenwick(n + 2);
        for (int i = n - 1; i >= 0; i--) {
            right[i] = fw.sum(n) - fw.sum(mapped[i] + 1);
            fw.add(mapped[i] + 1, 1);
        }
        long long ans = 0;
        for (int i = 0; i < n; i++) ans += 1LL * left[i] * right[i];
        return ans;
    }
};
