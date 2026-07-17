// LeetCode 1865 - Finding Pairs With a Certain Sum
// https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

import java.util.HashMap;
import java.util.Map;

class FindSumPairs {
    private final int[] nums1;
    private final int[] nums2;
    private final Map<Integer, Integer> counts = new HashMap<>();

    public FindSumPairs(int[] nums1, int[] nums2) {
        this.nums1 = nums1;
        this.nums2 = nums2;
        for (int num : nums2) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }
    }

    public void add(int index, int val) {
        int oldValue = nums2[index];
        counts.put(oldValue, counts.get(oldValue) - 1);
        nums2[index] += val;
        int newValue = nums2[index];
        counts.put(newValue, counts.getOrDefault(newValue, 0) + 1);
    }

    public int count(int tot) {
        int result = 0;
        for (int num : nums1) {
            result += counts.getOrDefault(tot - num, 0);
        }
        return result;
    }
}
