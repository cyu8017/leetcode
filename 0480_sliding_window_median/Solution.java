// LeetCode 0480 - Sliding Window Median
// https://leetcode.com/problems/sliding-window-median/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        List<Integer> window = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            window.add(nums[i]);
        }
        Collections.sort(window);
        List<Double> result = new ArrayList<>();
        appendMedian(window, k, result);

        for (int index = k; index < nums.length; index++) {
            int outgoing = nums[index - k];
            int incoming = nums[index];
            window.remove(Collections.binarySearch(window, outgoing));
            int insertPos = Collections.binarySearch(window, incoming);
            if (insertPos < 0) {
                insertPos = -insertPos - 1;
            }
            window.add(insertPos, incoming);
            appendMedian(window, k, result);
        }

        double[] medians = new double[result.size()];
        for (int i = 0; i < result.size(); i++) {
            medians[i] = result.get(i);
        }
        return medians;
    }

    private void appendMedian(List<Integer> window, int k, List<Double> result) {
        if (k % 2 == 1) {
            result.add((double) window.get(k / 2));
        } else {
            result.add((window.get(k / 2 - 1) + window.get(k / 2)) / 2.0);
        }
    }
}
