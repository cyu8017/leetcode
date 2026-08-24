// LeetCode 2216 - Minimum Deletions to Make Array Beautiful
// https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

class Solution {

    fun minDeletion(nums: IntArray): Int {

            var ans = 0; var i = 0; var n = nums.size
            while (i + 1 < n) {
                if (nums[i] == nums[i + 1]) { ans++; i++; }
                else i += 2
            }
            if ((n - ans) % 2 != 0) ans++
            return ans

    }

}
