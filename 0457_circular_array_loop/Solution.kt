// LeetCode 0457 - Circular Array Loop
// https://leetcode.com/problems/circular-array-loop/

class Solution {
    fun circularArrayLoop(nums: IntArray): Boolean {
        val length = nums.size

        fun nextIndex(index: Int): Int = Math.floorMod(index + nums[index], length)

        fun sameDirection(index: Int, forward: Boolean): Boolean =
            nums[index] * if (forward) 1 else -1 > 0

        for (start in 0 until length) {
            if (nums[start] == 0) {
                continue
            }
            val forward = nums[start] > 0
            var slow = start
            var fast = start
            while (true) {
                slow = nextIndex(slow)
                fast = nextIndex(nextIndex(fast))
                if (!sameDirection(slow, forward)
                    || !sameDirection(fast, forward)
                    || !sameDirection(nextIndex(fast), forward)
                ) {
                    break
                }
                if (slow == fast) {
                    if (slow == nextIndex(slow)) {
                        break
                    }
                    return true
                }
            }

            var index = start
            val value = nums[start]
            while (nums[index] * value > 0) {
                nums[index] = 0
                index = nextIndex(index)
            }
        }

        return false
    }
}
