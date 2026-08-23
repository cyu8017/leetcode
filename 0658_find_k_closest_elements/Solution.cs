// LeetCode 0658 - Find K Closest Elements
// https://leetcode.com/problems/find-k-closest-elements/

using System.Collections.Generic;

public class Solution {
    public IList<int> FindClosestElements(int[] arr, int k, int x) {
        int left = 0, right = arr.Length - k;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (x - arr[mid] > arr[mid + k] - x) left = mid + 1;
            else right = mid;
        }
        var result = new List<int>();
        for (int i = left; i < left + k; ++i) result.Add(arr[i]);
        return result;
    }
}
