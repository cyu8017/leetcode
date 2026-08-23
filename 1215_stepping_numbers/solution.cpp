// LeetCode 1215 - Stepping Numbers
// https://leetcode.com/problems/stepping-numbers/

#include <algorithm>
#include <queue>
#include <vector>

class Solution {
public:
    std::vector<int> countSteppingNumbers(int low, int high) {
        std::vector<int> answer;
        if (low == 0) {
            answer.push_back(0);
        }
        std::queue<long long> q;
        for (int i = 1; i <= 9; ++i) {
            q.push(i);
        }
        while (!q.empty()) {
            long long x = q.front();
            q.pop();
            if (x > high) {
                continue;
            }
            if (x >= low) {
                answer.push_back(static_cast<int>(x));
            }
            int last = static_cast<int>(x % 10);
            if (last > 0) {
                q.push(x * 10 + last - 1);
            }
            if (last < 9) {
                q.push(x * 10 + last + 1);
            }
        }
        std::sort(answer.begin(), answer.end());
        return answer;
    }
};
