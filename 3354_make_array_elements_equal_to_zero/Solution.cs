// LeetCode 3354 - Make Array Elements Equal to Zero
// https://leetcode.com/problems/make-array-elements-equal-to-zero/

public class Solution {
    public int CountValidSelections(int[] nums) {
        int n = nums.Length;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) continue;
            foreach (int dir in new int[] { -1, 1 }) {
                int[] a = (int[])nums.Clone();
                int cur = i, d = dir;
                while (cur >= 0 && cur < n) {
                    if (a[cur] == 0) cur += d;
                    else {
                        a[cur]--;
                        d = -d;
                        cur += d;
                    }
                }
                bool ok = true;
                foreach (int v in a) if (v != 0) { ok = false; break; }
                if (ok) ans++;
            }
        }
        return ans;
    }
}
