// LeetCode 3690 - Split and Merge Array Transformation
// https://leetcode.com/problems/split-and-merge-array-transformation/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MinSplitMerge(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        string Key(int[] a) => string.Join(",", a.Take(n));
        int[] ToArr(IList<int> nums) {
            int[] t = new int[n];
            for (int i = 0; i < n; i++) t[i] = nums[i];
            return t;
        }
        var start = ToArr(nums1);
        var target = ToArr(nums2);
        string targetKey = Key(target);
        var vis = new HashSet<string> { Key(start) };
        var q = new List<int[]> { start };
        for (int ans = 0; ; ans++) {
            var nq = new List<int[]>();
            foreach (var cur in q) {
                if (Key(cur) == targetKey) return ans;
                for (int l = 0; l < n; l++) {
                    for (int r = l; r < n; r++) {
                        var remain = new List<int>();
                        var sub = new List<int>();
                        for (int i = 0; i < l; i++) remain.Add(cur[i]);
                        for (int i = r + 1; i < n; i++) remain.Add(cur[i]);
                        for (int i = l; i <= r; i++) sub.Add(cur[i]);
                        for (int pos = 0; pos <= remain.Count; pos++) {
                            var nxtSlice = new List<int>();
                            nxtSlice.AddRange(remain.Take(pos));
                            nxtSlice.AddRange(sub);
                            nxtSlice.AddRange(remain.Skip(pos));
                            var nxt = ToArr(nxtSlice);
                            string nk = Key(nxt);
                            if (!vis.Contains(nk)) {
                                vis.Add(nk);
                                nq.Add(nxt);
                            }
                        }
                    }
                }
            }
            q = nq;
        }
    }
}
