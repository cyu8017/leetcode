// LeetCode 2383 - Minimum Hours of Training to Win a Competition
// https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

class Solution {
    public int minNumberOfHours(int initialEnergy, int initialExperience, int[] energy, int[] experience) {
        int ans = 0;
        int en = initialEnergy, ex = initialExperience;
        for (int i = 0; i < energy.length; i++) {
            if (en <= energy[i]) {
                int need = energy[i] - en + 1;
                ans += need;
                en += need;
            }
            if (ex <= experience[i]) {
                int need = experience[i] - ex + 1;
                ans += need;
                ex += need;
            }
            en -= energy[i];
            ex += experience[i];
        }
        return ans;
    }
}
