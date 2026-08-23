// LeetCode 0632 - Smallest Range Covering Elements from K Lists
// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

using System.Collections.Generic;

public class Solution {
    public int[] SmallestRange(IList<IList<int>> nums) {
        var heap = new PriorityQueue<(int value, int listIndex, int index), int>();
        int currentMax = int.MinValue;
        for (int i = 0; i < nums.Count; ++i) {
            heap.Enqueue((nums[i][0], i, 0), nums[i][0]);
            if (nums[i][0] > currentMax) currentMax = nums[i][0];
        }
        int bestLeft = heap.Peek().value;
        int bestRight = currentMax;
        while (true) {
            var (value, listIndex, index) = heap.Dequeue();
            if (currentMax - value < bestRight - bestLeft) {
                bestLeft = value;
                bestRight = currentMax;
            }
            if (index + 1 == nums[listIndex].Count) break;
            int nxt = nums[listIndex][index + 1];
            heap.Enqueue((nxt, listIndex, index + 1), nxt);
            if (nxt > currentMax) currentMax = nxt;
        }
        return new[] { bestLeft, bestRight };
    }
}
