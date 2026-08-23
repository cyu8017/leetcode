// LeetCode 3431 - Minimum Unlocked Indices to Sort Nums
// https://leetcode.com/problems/minimum-unlocked-indices-to-sort-nums/

class Solution {
    public int minUnlockedIndices(int[] nums, int[] locked) {
        int n = nums.length;
        boolean need = false;
        for (int i = 1; i < n; i++) {
            if (nums[i] < nums[i - 1]) { need = true; break; }
        }
        if (!need) return 0;
        int left = n, right = -1;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] > nums[j]) {
                    if (i < left) left = i;
                    if (j > right) right = j;
                }
            }
        }
        if (right < left) return 0;
        int ans = 0;
        for (int i = left; i <= right; i++) if (locked[i] == 1) ans++;
        int[] tmp = nums.clone();
        int[] lock = locked.clone();
        for (int i = left; i <= right; i++) lock[i] = 0;
        boolean changed = true;
        while (changed) {
            changed = false;
            for (int i = 0; i + 1 < n; i++) {
                if (lock[i] == 0 && lock[i + 1] == 0 && tmp[i] > tmp[i + 1]) {
                    int t = tmp[i]; tmp[i] = tmp[i + 1]; tmp[i + 1] = t;
                    changed = true;
                }
            }
        }
        for (int i = 1; i < n; i++) if (tmp[i] < tmp[i - 1]) return -1;
        return ans;
    }
}
