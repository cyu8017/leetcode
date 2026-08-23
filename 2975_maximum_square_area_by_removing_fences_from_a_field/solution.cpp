// LeetCode 2975 - Maximum Square Area by Removing Fences From a Field
// https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

#include <vector>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    int maximizeSquareArea(int m, int n, std::vector<int>& hFences, std::vector<int>& vFences) {
        const int mod = 1000000007;
        auto hGaps = [](std::vector<int> fences, int bound) {
            fences.push_back(1);
            fences.push_back(bound);
            std::sort(fences.begin(), fences.end());
            std::unordered_set<int> gaps;
            for (int i = 0; i < (int)fences.size(); i++) {
                for (int j = i + 1; j < (int)fences.size(); j++) {
                    gaps.insert(fences[j] - fences[i]);
                }
            }
            return gaps;
        };
        auto hg = hGaps(hFences, m);
        auto vg = hGaps(vFences, n);
        long long best = -1;
        for (int g : hg) {
            if (vg.count(g) && g > best) best = g;
        }
        if (best < 0) return -1;
        return (int)(best * best % mod);
    }
};
