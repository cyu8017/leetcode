// LeetCode 1055 - Shortest Way to Form String
// https://leetcode.com/problems/shortest-way-to-form-string/

class Solution {
    public int shortestWay(String source, String target) {
        boolean[] sourceSet = new boolean[26];
        for (int i = 0; i < source.length(); i++) {
            sourceSet[source.charAt(i) - 'a'] = true;
        }
        for (int i = 0; i < target.length(); i++) {
            if (!sourceSet[target.charAt(i) - 'a']) {
                return -1;
            }
        }
        int ans = 0;
        int i = 0;
        int n = target.length();
        while (i < n) {
            ans++;
            for (int j = 0; j < source.length(); j++) {
                if (i < n && target.charAt(i) == source.charAt(j)) {
                    i++;
                }
            }
        }
        return ans;
    }
}
