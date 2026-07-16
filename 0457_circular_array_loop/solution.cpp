// LeetCode 0457 - Circular Array Loop
// https://leetcode.com/problems/circular-array-loop/

#include <cstdlib>
#include <vector>

class Solution {
public:
    bool circularArrayLoop(std::vector<int>& nums) {
        const int length = static_cast<int>(nums.size());

        auto nextIndex = [&](int index) {
            int step = nums[index];
            return ((index + step) % length + length) % length;
        };

        for (int start = 0; start < length; ++start) {
            if (nums[start] == 0) {
                continue;
            }

            const int direction = nums[start] > 0 ? 1 : -1;
            int slow = start;
            int fast = start;

            while (true) {
                slow = nextIndex(slow);
                fast = nextIndex(nextIndex(fast));

                if (nums[slow] * direction <= 0 || nums[fast] * direction <= 0 ||
                    nums[nextIndex(fast)] * direction <= 0) {
                    break;
                }
                if (slow == fast) {
                    if (slow == nextIndex(slow)) {
                        break;
                    }
                    return true;
                }
            }

            int index = start;
            const int value = nums[start];
            while (nums[index] * value > 0) {
                nums[index] = 0;
                index = nextIndex(index);
            }
        }

        return false;
    }
};
