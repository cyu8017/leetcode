// LeetCode 3739 - Count Subarrays With Majority Element II
// https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

public class Solution {
    class BIT {
        int n;
        int[] c;
        public BIT(int n_) {
            n = n_;
            c = new int[n_ + 1];
        }
        public void Update(int x, int delta) {
            for (; x <= n; x += x & -x) c[x] += delta;
        }
        public int Query(int x) {
            int s = 0;
            for (; x > 0; x -= x & -x) s += c[x];
            return s;
        }
    }

    public long CountMajoritySubarrays(int[] nums, int target) {
        int n = nums.Length;
        var tree = new BIT(2 * n + 1);
        int s = n + 1;
        tree.Update(s, 1);
        long ans = 0;
        foreach (int x in nums) {
            if (x == target) s++;
            else s--;
            ans += tree.Query(s - 1);
            tree.Update(s, 1);
        }
        return ans;
    }
}
