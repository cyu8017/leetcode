// LeetCode 3049 - Earliest Second to Mark Indices II
// https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

using System.Collections.Generic;

public class Solution {
    private static Dictionary<int, int> GetSecondToIndex(int[] nums, int[] changeIndices) {
        var indexToFirstSecond = new Dictionary<int, int>();
        for (int second = 0; second < changeIndices.Length; second++) {
            int index = changeIndices[second] - 1;
            if (nums[index] > 0 && !indexToFirstSecond.ContainsKey(index))
                indexToFirstSecond[index] = second;
        }
        var secondToIndex = new Dictionary<int, int>();
        foreach (var kv in indexToFirstSecond) secondToIndex[kv.Value] = kv.Key;
        return secondToIndex;
    }

    private static bool CanMark(int[] nums, Dictionary<int, int> secondToIndex, int maxSecond, long numsSum) {
        var h = new PriorityQueue<int, int>();
        int marks = 0;
        for (int second = maxSecond - 1; second >= 0; second--) {
            if (secondToIndex.TryGetValue(second, out int idx)) {
                h.Enqueue(nums[idx], nums[idx]);
                if (marks == 0) {
                    h.Dequeue();
                    marks++;
                } else {
                    marks--;
                }
            } else {
                marks++;
            }
        }
        int heapSize = h.Count;
        long heapSum = 0;
        while (h.Count > 0) heapSum += h.Dequeue();
        long decrementAndMarkCost = numsSum - heapSum + (nums.Length - heapSize);
        long zeroAndMarkCost = (long)heapSize + heapSize;
        return decrementAndMarkCost + zeroAndMarkCost <= maxSecond;
    }

    public int EarliestSecondToMarkIndices(int[] nums, int[] changeIndices) {
        var secondToIndex = GetSecondToIndex(nums, changeIndices);
        long numsSum = 0;
        foreach (int v in nums) numsSum += v;
        int l = 0, r = changeIndices.Length + 1;
        while (l < r) {
            int m = (l + r) / 2;
            if (CanMark(nums, secondToIndex, m, numsSum)) r = m;
            else l = m + 1;
        }
        return l <= changeIndices.Length ? l : -1;
    }
}
