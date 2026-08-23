// LeetCode 2122 - Recover the Original Array
// https://leetcode.com/problems/recover-the-original-array/

public class Solution {
    public int[] RecoverArray(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        for (int i = 1; i < n; i++) {
            int diff = nums[i] - nums[0];
            if (diff == 0 || diff % 2 != 0) continue;
            int k = diff / 2;
            bool[] used = new bool[n];
            used[0] = used[i] = true;
            var ans = new List<int> { (nums[0] + nums[i]) / 2 };
            int l = 0, r = i;
            bool ok = true;
            while (ans.Count < n / 2) {
                while (l < n && used[l]) l++;
                if (l == n) { ok = false; break; }
                int need = nums[l] + 2 * k;
                while (r < n && (used[r] || nums[r] < need)) r++;
                if (r == n || nums[r] != need) { ok = false; break; }
                used[l] = used[r] = true;
                ans.Add(nums[l] + k);
            }
            if (ok) return ans.ToArray();
        }
        return Array.Empty<int>();
    }
}
