// LeetCode 0480 - Sliding Window Median
// https://leetcode.com/problems/sliding-window-median/

public class Solution {
    public double[] MedianSlidingWindow(int[] nums, int k) {
        List<int> window = nums.Take(k).OrderBy(x => x).ToList();
        List<double> result = new();
        AppendMedian(window, k, result);

        for (int index = k; index < nums.Length; index++) {
            int outgoing = nums[index - k];
            int incoming = nums[index];
            window.RemoveAt(window.BinarySearch(outgoing));
            int insertPos = window.BinarySearch(incoming);
            if (insertPos < 0) {
                insertPos = ~insertPos;
            }
            window.Insert(insertPos, incoming);
            AppendMedian(window, k, result);
        }
        return result.ToArray();
    }

    private static void AppendMedian(List<int> window, int k, List<double> result) {
        if (k % 2 == 1) {
            result.Add(window[k / 2]);
        } else {
            result.Add((window[k / 2 - 1] + window[k / 2]) / 2.0);
        }
    }
}
