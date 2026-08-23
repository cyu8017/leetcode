// LeetCode 2409 - Count Days Spent Together
// https://leetcode.com/problems/count-days-spent-together/

#include <algorithm>
#include <string>

class Solution {
public:
    int countDaysTogether(std::string arriveAlice, std::string leaveAlice, std::string arriveBob, std::string leaveBob) {
        int days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        auto toDay = [&](const std::string& s) {
            int m = (s[0] - '0') * 10 + (s[1] - '0');
            int d = (s[3] - '0') * 10 + (s[4] - '0');
            int res = d;
            for (int i = 0; i < m - 1; i++) res += days[i];
            return res;
        };
        int a1 = toDay(arriveAlice), a2 = toDay(leaveAlice);
        int b1 = toDay(arriveBob), b2 = toDay(leaveBob);
        int start = std::max(a1, b1);
        int end = std::min(a2, b2);
        if (end < start) return 0;
        return end - start + 1;
    }
};
