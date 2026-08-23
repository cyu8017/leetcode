// LeetCode 2951 - Find the Peaks
// https://leetcode.com/problems/find-the-peaks/

#include <vector>

class Solution {
public:
    std::vector<int> findPeaks(std::vector<int>& mountain) {
        std::vector<int> ans;
        for (int i = 1; i + 1 < (int)mountain.size(); i++)
            if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1])
                ans.push_back(i);
        return ans;
    }
};
