// LeetCode 3491 - Phone Number Prefix
// https://leetcode.com/problems/phone-number-prefix/

#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    bool phonePrefix(std::vector<std::string>& numbers) {
        std::sort(numbers.begin(), numbers.end());
        for (int i = 0; i + 1 < (int)numbers.size(); i++) {
            if (numbers[i].size() <= numbers[i + 1].size() &&
                numbers[i + 1].compare(0, numbers[i].size(), numbers[i]) == 0)
                return false;
        }
        return true;
    }
};
