// LeetCode 0414 - Third Maximum Number
// https://leetcode.com/problems/third-maximum-number/

#include <optional>
#include <vector>

using namespace std;

class Solution {
public:
    int thirdMax(vector<int>& nums) {
        optional<int> first;
        optional<int> second;
        optional<int> third;

        for (int value : nums) {
            if ((first && value == *first) || (second && value == *second) ||
                (third && value == *third)) {
                continue;
            }
            if (!first || value > *first) {
                third = second;
                second = first;
                first = value;
            } else if (!second || value > *second) {
                third = second;
                second = value;
            } else if (!third || value > *third) {
                third = value;
            }
        }

        return third ? *third : *first;
    }
};
