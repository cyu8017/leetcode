// LeetCode 2534 - Time Taken to Cross the Door
// https://leetcode.com/problems/time-taken-to-cross-the-door/

#include <queue>
#include <vector>

class Solution {
public:
    std::vector<int> timeTaken(std::vector<int>& arrival, std::vector<int>& state) {
        int n = (int)arrival.size();
        std::vector<int> ans(n);
        std::queue<int> enter, exitq;
        int i = 0, t = 0, prev = 1;
        while (i < n || !enter.empty() || !exitq.empty()) {
            while (i < n && arrival[i] <= t) {
                if (state[i] == 0) enter.push(i);
                else exitq.push(i);
                i++;
            }
            if (enter.empty() && exitq.empty()) {
                if (i < n) {
                    t = arrival[i];
                    prev = 1;
                }
                continue;
            }
            if (prev == 1) {
                if (!exitq.empty()) {
                    ans[exitq.front()] = t;
                    exitq.pop();
                    prev = 1;
                } else {
                    ans[enter.front()] = t;
                    enter.pop();
                    prev = 0;
                }
            } else {
                if (!enter.empty()) {
                    ans[enter.front()] = t;
                    enter.pop();
                    prev = 0;
                } else {
                    ans[exitq.front()] = t;
                    exitq.pop();
                    prev = 1;
                }
            }
            t++;
        }
        return ans;
    }
};
