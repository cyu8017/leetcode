// LeetCode 1213 - Intersection of Three Sorted Arrays
// https://leetcode.com/problems/intersection-of-three-sorted-arrays/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<int> ArraysIntersection(int[] arr1, int[] arr2, int[] arr3) {
        return arr1.Intersect(arr2).Intersect(arr3).OrderBy(x => x).ToList();
    }
}
