// LeetCode 3354 - Make Array Elements Equal to Zero
// https://leetcode.com/problems/make-array-elements-equal-to-zero/

class Solution {
    public int countValidSelections(int[] nums) {
        int n = nums.length;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) continue;
            for (int dir : new int[] { -1, 1 }) {
                int[] a = nums.clone();
                int cur = i, d = dir;
                while (cur >= 0 && cur < n) {
                    if (a[cur] == 0) cur += d;
                    else {
                        a[cur]--;
                        d = -d;
                        cur += d;
                    }
                }
                boolean ok = true;
                for (int v : a) if (v != 0) { ok = false; break; }
                if (ok) ans++;
            }
        }
        return ans;
    }
}
