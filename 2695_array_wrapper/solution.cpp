// LeetCode 2695 - Array Wrapper
// https://leetcode.com/problems/array-wrapper/

#include <vector>
#include <string>
#include <sstream>

// JS ArrayWrapper stand-in
class ArrayWrapper {
    std::vector<int> nums;
public:
    ArrayWrapper(std::vector<int> nums) : nums(std::move(nums)) {}
    int valueOf() const {
        int s = 0;
        for (int x : nums) s += x;
        return s;
    }
    std::string toString() const {
        std::ostringstream oss;
        oss << '[';
        for (int i = 0; i < (int)nums.size(); i++) {
            if (i) oss << ',';
            oss << nums[i];
        }
        oss << ']';
        return oss.str();
    }
};

class Solution {
public:
    ArrayWrapper ArrayWrapperCreate(std::vector<int> nums) { return ArrayWrapper(std::move(nums)); }
};
