// LeetCode 3948 - Lexicographically Maximum MEX Array
// https://leetcode.com/problems/lexicographically-maximum-mex-array/

#include <vector>

class Solution {
public:
    std::vector<int> maxMexArray(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> remaining(n + 2, 0);
        for (int x : nums) {
            if (x <= n + 1) remaining[x]++;
        }
        int mex = 0;
        while (remaining[mex] > 0) mex++;
        std::vector<int> answer;
        std::vector<int> seen(n + 2, 0);
        int stamp = 0, index = 0;
        while (index < n) {
            if (mex == 0) {
                answer.push_back(0);
                int x = nums[index];
                if (x <= n + 1) remaining[x]--;
                index++;
                continue;
            }
            stamp++;
            int need = mex;
            while (need > 0) {
                int x = nums[index];
                if (x < mex && seen[x] != stamp) {
                    seen[x] = stamp;
                    need--;
                }
                if (x <= n + 1) remaining[x]--;
                index++;
            }
            answer.push_back(mex);
            mex = 0;
            while (remaining[mex] > 0) mex++;
        }
        return answer;
    }
};
