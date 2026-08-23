// LeetCode 0239 - Sliding Window Maximum
// https://leetcode.com/problems/sliding-window-maximum/

using System.Collections.Generic;

public class Solution {
    public int[] MaxSlidingWindow(int[] nums, int k) {
        LinkedList<int> window = new LinkedList<int>();
        int[] result = new int[nums.Length - k + 1];
        int resultIndex = 0;

        for (int index = 0; index < nums.Length; index++) {
            while (window.Count > 0 && nums[window.Last.Value] <= nums[index]) {
                window.RemoveLast();
            }
            window.AddLast(index);
            if (window.First.Value <= index - k) {
                window.RemoveFirst();
            }
            if (index >= k - 1) {
                result[resultIndex++] = nums[window.First.Value];
            }
        }

        return result;
    }
}
