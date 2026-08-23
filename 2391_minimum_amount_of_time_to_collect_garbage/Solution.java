// LeetCode 2391 - Minimum Amount of Time to Collect Garbage
// https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

class Solution {
    public int garbageCollection(String[] garbage, int[] travel) {
        int ans = 0;
        int lastM = 0, lastP = 0, lastG = 0;
        for (int i = 0; i < garbage.length; i++) {
            ans += garbage[i].length();
            for (int j = 0; j < garbage[i].length(); j++) {
                char c = garbage[i].charAt(j);
                if (c == 'M') lastM = i;
                else if (c == 'P') lastP = i;
                else lastG = i;
            }
        }
        int[] pref = new int[travel.length + 1];
        for (int i = 0; i < travel.length; i++) pref[i + 1] = pref[i] + travel[i];
        ans += pref[lastM] + pref[lastP] + pref[lastG];
        return ans;
    }
}
