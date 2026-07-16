// LeetCode 0457 - Circular Array Loop
// https://leetcode.com/problems/circular-array-loop/

class Solution {
    circularArrayLoop(nums) {
        const length = nums.length;

        const nextIndex = (index) => {
            const step = ((index + nums[index]) % length + length) % length;
            return step;
        };

        for (let start = 0; start < length; start += 1) {
            if (nums[start] === 0) continue;
            const forward = nums[start] > 0;
            let slow = start;
            let fast = start;
            while (true) {
                slow = nextIndex(slow);
                fast = nextIndex(nextIndex(fast));
                const slowSign = nums[slow] > 0 ? 1 : -1;
                const fastSign = nums[fast] > 0 ? 1 : -1;
                const fastNextSign = nums[nextIndex(fast)] > 0 ? 1 : -1;
                const direction = forward ? 1 : -1;
                if (
                    slowSign * direction <= 0
                    || fastSign * direction <= 0
                    || fastNextSign * direction <= 0
                ) {
                    break;
                }
                if (slow === fast) {
                    if (slow === nextIndex(slow)) break;
                    return true;
                }
            }

            let index = start;
            const value = nums[start];
            while (nums[index] * value > 0) {
                nums[index] = 0;
                index = nextIndex(index);
            }
        }

        return false;
    }
}

module.exports = { Solution };
