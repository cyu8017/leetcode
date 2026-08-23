// LeetCode 0260 - Single Number III
// https://leetcode.com/problems/single-number-iii/

#include <vector>
using namespace std;

class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int xorAll = 0;
        for (int num : nums) {
            xorAll ^= num;
        }
        int diff = xorAll & -xorAll;
        int first = 0;
        int second = 0;
        for (int num : nums) {
            if (num & diff) {
                first ^= num;
            } else {
                second ^= num;
            }
        }
        return { first, second };
    }
};
