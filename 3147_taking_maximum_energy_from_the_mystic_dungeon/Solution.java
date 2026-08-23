// LeetCode 3147 - Taking Maximum Energy From the Mystic Dungeon
// https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

class Solution {
    public int maximumEnergy(int[] energy, int k) {
        int ans = -(1 << 30);
        int n = energy.length;
        for (int i = n - k; i < n; i++) {
            for (int j = i, s = 0; j >= 0; j -= k) {
                s += energy[j];
                ans = Math.max(ans, s);
            }
        }
        return ans;
    }
}
