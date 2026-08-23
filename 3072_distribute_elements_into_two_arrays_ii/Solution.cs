// LeetCode 3072 - Distribute Elements Into Two Arrays II
// https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

using System;
using System.Collections.Generic;

public class Solution {
    class BIT {
        int n;
        int[] c;
        public BIT(int n_) { n = n_; c = new int[n_ + 1]; }
        public void Update(int x, int delta) { for (; x <= n; x += x & -x) c[x] += delta; }
        public int Query(int x) { int s = 0; for (; x > 0; x -= x & -x) s += c[x]; return s; }
    }

    public int[] ResultArray(int[] nums) {
        int[] st = (int[])nums.Clone();
        Array.Sort(st);
        int n = st.Length;
        var tree1 = new BIT(n + 1);
        var tree2 = new BIT(n + 1);
        int Idx(int x) {
            int lo = 0, hi = st.Length;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (st[mid] < x) lo = mid + 1;
                else hi = mid;
            }
            return lo + 1;
        }
        tree1.Update(Idx(nums[0]), 1);
        tree2.Update(Idx(nums[1]), 1);
        var arr1 = new List<int> { nums[0] };
        var arr2 = new List<int> { nums[1] };
        for (int i = 2; i < nums.Length; i++) {
            int x = nums[i];
            int id = Idx(x);
            int a = arr1.Count - tree1.Query(id);
            int b = arr2.Count - tree2.Query(id);
            if (a > b || (a == b && arr1.Count <= arr2.Count)) {
                arr1.Add(x);
                tree1.Update(id, 1);
            } else {
                arr2.Add(x);
                tree2.Update(id, 1);
            }
        }
        arr1.AddRange(arr2);
        return arr1.ToArray();
    }
}
