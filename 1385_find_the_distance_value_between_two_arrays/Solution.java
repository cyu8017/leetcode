// LeetCode 1385 - Find The Distance Value Between Two Arrays
// https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

import java.util.*;

class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        Arrays.sort(arr2);
        int ans = 0;
        for (int x : arr1) {
            int i = Arrays.binarySearch(arr2, x);
            if (i < 0) i = -i - 1;
            boolean close = (i < arr2.length && Math.abs(arr2[i] - x) <= d)
                    || (i > 0 && Math.abs(arr2[i - 1] - x) <= d);
            if (!close) ans++;
        }
        return ans;
    }
}
