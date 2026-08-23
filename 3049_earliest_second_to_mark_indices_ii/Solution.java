// LeetCode 3049 - Earliest Second to Mark Indices II
// https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    private Map<Integer, Integer> getSecondToIndex(int[] nums, int[] changeIndices) {
        Map<Integer, Integer> indexToFirstSecond = new HashMap<>();
        for (int second = 0; second < changeIndices.length; second++) {
            int index = changeIndices[second] - 1;
            if (nums[index] > 0 && !indexToFirstSecond.containsKey(index))
                indexToFirstSecond.put(index, second);
        }
        Map<Integer, Integer> secondToIndex = new HashMap<>();
        for (Map.Entry<Integer, Integer> e : indexToFirstSecond.entrySet())
            secondToIndex.put(e.getValue(), e.getKey());
        return secondToIndex;
    }

    private boolean canMark(int[] nums, Map<Integer, Integer> secondToIndex, int maxSecond, long numsSum) {
        PriorityQueue<Integer> h = new PriorityQueue<>();
        int marks = 0;
        for (int second = maxSecond - 1; second >= 0; second--) {
            if (secondToIndex.containsKey(second)) {
                h.offer(nums[secondToIndex.get(second)]);
                if (marks == 0) {
                    h.poll();
                    marks++;
                } else {
                    marks--;
                }
            } else {
                marks++;
            }
        }
        int heapSize = h.size();
        long heapSum = 0;
        while (!h.isEmpty()) heapSum += h.poll();
        long decrementAndMarkCost = numsSum - heapSum + (nums.length - heapSize);
        long zeroAndMarkCost = (long) heapSize + heapSize;
        return decrementAndMarkCost + zeroAndMarkCost <= maxSecond;
    }

    public int earliestSecondToMarkIndices(int[] nums, int[] changeIndices) {
        Map<Integer, Integer> secondToIndex = getSecondToIndex(nums, changeIndices);
        long numsSum = 0;
        for (int v : nums) numsSum += v;
        int l = 0, r = changeIndices.length + 1;
        while (l < r) {
            int m = (l + r) / 2;
            if (canMark(nums, secondToIndex, m, numsSum)) r = m;
            else l = m + 1;
        }
        return l <= changeIndices.length ? l : -1;
    }
}
