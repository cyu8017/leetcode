// LeetCode 2950 - Number of Divisible Substrings
// https://leetcode.com/problems/number-of-divisible-substrings/

#include <string>

class Solution {
public:
    int countDivisibleSubstrings(std::string word) {
        int vals[26] = {1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9};
        int ans = 0, n = (int)word.size();
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = i; j < n; j++) {
                sum += vals[word[j] - 'a'];
                if (sum % (j - i + 1) == 0) ans++;
            }
        }
        return ans;
    }
};
