// LeetCode 3739 - Count Subarrays With Majority Element II
// https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

class Solution {
    class BIT {
        int n;
        int[] c;
        public BIT(int n_) {
            n = n_;
            c = new int[n_ + 1];
        }
        public void update(int x, int delta) {
            for (; x <= n; x += x & -x) c[x] += delta;
        }
        public int query(int x) {
            int s = 0;
            for (; x > 0; x -= x & -x) s += c[x];
            return s;
        }
    }

    public long countMajoritySubarrays(int[] nums, int target) {
        int n = nums.length;
        var tree = new BIT(2 * n + 1);
        int s = n + 1;
        tree.update(s, 1);
        long ans = 0;
        for (int x : nums) {
            if (x == target) s++;
            else s--;
            ans += tree.query(s - 1);
            tree.update(s, 1);
        }
        return ans;
    }
}
