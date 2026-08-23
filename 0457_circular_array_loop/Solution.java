// LeetCode 0457 - Circular Array Loop
// https://leetcode.com/problems/circular-array-loop/

class Solution {
    public boolean circularArrayLoop(int[] nums) {
        int length = nums.length;

        for (int start = 0; start < length; start++) {
            if (nums[start] == 0) {
                continue;
            }
            boolean forward = nums[start] > 0;
            int slow = start;
            int fast = start;
            while (true) {
                slow = nextIndex(nums, slow, length);
                fast = nextIndex(nums, nextIndex(nums, fast, length), length);
                if (!sameDirection(nums, slow, forward)
                        || !sameDirection(nums, fast, forward)
                        || !sameDirection(nums, nextIndex(nums, fast, length), forward)) {
                    break;
                }
                if (slow == fast) {
                    if (slow == nextIndex(nums, slow, length)) {
                        break;
                    }
                    return true;
                }
            }

            int index = start;
            int value = nums[start];
            while (nums[index] * value > 0) {
                nums[index] = 0;
                index = nextIndex(nums, index, length);
            }
        }

        return false;
    }

    private int nextIndex(int[] nums, int index, int length) {
        return Math.floorMod(index + nums[index], length);
    }

    private boolean sameDirection(int[] nums, int index, boolean forward) {
        return nums[index] * (forward ? 1 : -1) > 0;
    }
}
