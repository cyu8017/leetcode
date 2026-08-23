// LeetCode 2262 - Total Appeal of A String
// https://leetcode.com/problems/total-appeal-of-a-string/

#include <string>
#include <vector>

class Solution {
public:
    long long appealSum(std::string s) {
        std::vector<int> last(26, -1);
        long long ans = 0, cur = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            int c = s[i] - 'a';
            cur += i - last[c];
            last[c] = i;
            ans += cur;
        }
        return ans;
    }
};
