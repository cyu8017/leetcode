// LeetCode 1985 - Find the Kth Largest Integer in the Array
// https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

import java.util.*;

class Solution {
    public String kthLargestNumber(String[] nums, int k) {
        Arrays.sort(nums, (a, b) -> {
            if (a.length() != b.length()) return Integer.compare(b.length(), a.length());
            return b.compareTo(a);
        });
        return nums[k - 1];
    }
}
