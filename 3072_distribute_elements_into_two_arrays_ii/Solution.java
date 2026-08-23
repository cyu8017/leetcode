// LeetCode 3072 - Distribute Elements Into Two Arrays II
// https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    static class BIT {
        int n;
        int[] c;
        BIT(int n_) { n = n_; c = new int[n_ + 1]; }
        void update(int x, int delta) { for (; x <= n; x += x & -x) c[x] += delta; }
        int query(int x) { int s = 0; for (; x > 0; x -= x & -x) s += c[x]; return s; }
    }

    public int[] resultArray(int[] nums) {
        int[] st = nums.clone();
        Arrays.sort(st);
        int n = st.length;
        BIT tree1 = new BIT(n + 1);
        BIT tree2 = new BIT(n + 1);
        List<Integer> arr1 = new ArrayList<>();
        List<Integer> arr2 = new ArrayList<>();
        arr1.add(nums[0]);
        arr2.add(nums[1]);
        tree1.update(idx(st, nums[0]), 1);
        tree2.update(idx(st, nums[1]), 1);
        for (int i = 2; i < nums.length; i++) {
            int x = nums[i];
            int id = idx(st, x);
            int a = arr1.size() - tree1.query(id);
            int b = arr2.size() - tree2.query(id);
            if (a > b || (a == b && arr1.size() <= arr2.size())) {
                arr1.add(x);
                tree1.update(id, 1);
            } else {
                arr2.add(x);
                tree2.update(id, 1);
            }
        }
        arr1.addAll(arr2);
        int[] ans = new int[arr1.size()];
        for (int i = 0; i < arr1.size(); i++) ans[i] = arr1.get(i);
        return ans;
    }

    private int idx(int[] st, int x) {
        int lo = 0, hi = st.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (st[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo + 1;
    }
}
