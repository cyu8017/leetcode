// LeetCode 0457 - Circular Array Loop
// https://leetcode.com/problems/circular-array-loop/

public class Solution {
    public bool CircularArrayLoop(int[] nums) {
        int length = nums.Length;

        for (int start = 0; start < length; start++) {
            if (nums[start] == 0) {
                continue;
            }
            bool forward = nums[start] > 0;
            int slow = start;
            int fast = start;
            while (true) {
                slow = NextIndex(nums, slow, length);
                fast = NextIndex(nums, NextIndex(nums, fast, length), length);
                if (!SameDirection(nums, slow, forward)
                        || !SameDirection(nums, fast, forward)
                        || !SameDirection(nums, NextIndex(nums, fast, length), forward)) {
                    break;
                }
                if (slow == fast) {
                    if (slow == NextIndex(nums, slow, length)) {
                        break;
                    }
                    return true;
                }
            }

            int index = start;
            int value = nums[start];
            while (nums[index] * value > 0) {
                nums[index] = 0;
                index = NextIndex(nums, index, length);
            }
        }

        return false;
    }

    private static int NextIndex(int[] nums, int index, int length) {
        return (index + nums[index] % length + length) % length;
    }

    private static bool SameDirection(int[] nums, int index, bool forward) {
        return nums[index] * (forward ? 1 : -1) > 0;
    }
}
