// LeetCode 1243 - Array Transformation
// https://leetcode.com/problems/array-transformation/

using System.Linq;

public class Solution {
    public IList<int> TransformArray(int[] arr) {
        while (true) {
            var nxt = arr.ToArray();
            for (int i = 1; i < arr.Length - 1; i++) {
                if (arr[i] < arr[i - 1] && arr[i] < arr[i + 1]) nxt[i]++;
                else if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) nxt[i]--;
            }
            if (nxt.SequenceEqual(arr)) return arr.ToList();
            arr = nxt;
        }
    }
}
