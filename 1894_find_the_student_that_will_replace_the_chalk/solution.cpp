// LeetCode 1894 - Find the Student that Will Replace the Chalk
// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

#include <numeric>
#include <vector>

class Solution {
public:
    int chalkReplacer(std::vector<int>& chalk, int k) {
        long long total = 0;
        for (int need : chalk) {
            total += need;
        }
        long long remaining = k % total;
        for (int index = 0; index < static_cast<int>(chalk.size()); index++) {
            if (remaining < chalk[index]) {
                return index;
            }
            remaining -= chalk[index];
        }
        return 0;
    }
};
