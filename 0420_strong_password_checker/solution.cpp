// LeetCode 0420 - Strong Password Checker
// https://leetcode.com/problems/strong-password-checker/

#include <algorithm>
#include <cctype>
#include <string>

using namespace std;

class Solution {
public:
    int strongPasswordChecker(string password) {
        int length = (int)password.size();
        int missing = 3;

        bool hasLower = false;
        bool hasUpper = false;
        bool hasDigit = false;
        for (char ch : password) {
            if (islower(static_cast<unsigned char>(ch))) {
                hasLower = true;
            } else if (isupper(static_cast<unsigned char>(ch))) {
                hasUpper = true;
            } else if (isdigit(static_cast<unsigned char>(ch))) {
                hasDigit = true;
            }
        }
        if (hasLower) {
            --missing;
        }
        if (hasUpper) {
            --missing;
        }
        if (hasDigit) {
            --missing;
        }

        int replace = 0;
        int oneRepeat = 0;
        int twoRepeat = 0;
        int index = 0;
        while (index < length) {
            int run = 1;
            while (index + run < length && password[index + run] == password[index]) {
                ++run;
            }
            if (run >= 3) {
                replace += run / 3;
                if (run % 3 == 0) {
                    ++oneRepeat;
                } else if (run % 3 == 1) {
                    ++twoRepeat;
                }
            }
            index += run;
        }

        if (length < 6) {
            return max(6 - length, missing);
        }
        if (length <= 20) {
            return max(missing, replace);
        }

        int deleteCount = length - 20;
        replace -= min(deleteCount, oneRepeat);
        deleteCount -= min(deleteCount, oneRepeat);
        replace -= min(deleteCount / 2, twoRepeat);
        deleteCount -= min(deleteCount / 2, twoRepeat) * 2;
        replace -= deleteCount / 3;
        return length - 20 + max(missing, replace);
    }
};
