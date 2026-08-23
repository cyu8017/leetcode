// LeetCode 3019 - Number of Changing Keys
// https://leetcode.com/problems/number-of-changing-keys/

class Solution {
    public int countKeyChanges(String s) {
        s = s.toLowerCase();
        int ans = 0;
        for (int i = 1; i < s.length(); i++)
            if (s.charAt(i) != s.charAt(i - 1)) ans++;
        return ans;
    }
}
