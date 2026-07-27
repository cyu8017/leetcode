// LeetCode 1619 - Mean of Array After Removing Some Elements
// https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

import java.util.*;

class Solution {
    public double trimMean(int[] arr) {
        Arrays.sort(arr);
        int k = arr.length / 20;
        long sum = 0;
        for (int i = k; i < arr.length - k; i++) sum += arr[i];
        return (double) sum / (arr.length - 2 * k);
    }
}
