// LeetCode 0264 - Ugly Number II
// https://leetcode.com/problems/ugly-number-ii/

#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> ugly = { 1 };
        int index2 = 0;
        int index3 = 0;
        int index5 = 0;
        while ((int)ugly.size() < n) {
            int nextUgly = min({
                ugly[index2] * 2,
                ugly[index3] * 3,
                ugly[index5] * 5,
            });
            ugly.push_back(nextUgly);
            if (nextUgly == ugly[index2] * 2) {
                index2++;
            }
            if (nextUgly == ugly[index3] * 3) {
                index3++;
            }
            if (nextUgly == ugly[index5] * 5) {
                index5++;
            }
        }
        return ugly.back();
    }
};
