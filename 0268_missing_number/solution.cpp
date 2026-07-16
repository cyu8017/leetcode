// LeetCode 0268 - Missing Number
// https://leetcode.com/problems/missing-number/

#include <numeric>
#include <vector>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int length = nums.size();
        int expected = length * (length + 1) / 2;
        int total = accumulate(nums.begin(), nums.end(), 0);
        return expected - total;
    }
};
