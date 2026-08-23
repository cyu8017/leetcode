// LeetCode 0136 - Single Number
#include <vector>
using namespace std;
class Solution { public:
    int singleNumber(vector<int>& nums) { int answer = 0; for (int value : nums) answer ^= value; return answer; }
};