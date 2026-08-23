// LeetCode 2345 - Finding the Number of Visible Mountains
// https://leetcode.com/problems/finding-the-number-of-visible-mountains/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int visibleMountains(std::vector<std::vector<int>>& peaks) {
        struct Mt { int l, r; };
        std::vector<Mt> arr;
        arr.reserve(peaks.size());
        for (auto& p : peaks) {
            arr.push_back({p[0] - p[1], p[0] + p[1]});
        }
        std::sort(arr.begin(), arr.end(), [](const Mt& a, const Mt& b) {
            if (a.l == b.l) return a.r > b.r;
            return a.l < b.l;
        });
        int ans = 0;
        int maxR = INT_MIN;
        for (int i = 0; i < (int)arr.size(); ) {
            int j = i;
            while (j < (int)arr.size() && arr[j].l == arr[i].l && arr[j].r == arr[i].r) j++;
            if (arr[i].r > maxR) {
                if (j - i == 1) ans++;
                maxR = arr[i].r;
            }
            i = j;
        }
        return ans;
    }
};
