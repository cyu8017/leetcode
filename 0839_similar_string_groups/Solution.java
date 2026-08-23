// LeetCode 0839 - Similar String Groups
// https://leetcode.com/problems/similar-string-groups/

class Solution {
    private int[] parent;

    public int numSimilarGroups(String[] strs) {
        int n = strs.length;
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int groups = n;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (similar(strs[i], strs[j])) {
                    int pi = find(i), pj = find(j);
                    if (pi != pj) {
                        parent[pi] = pj;
                        groups--;
                    }
                }
            }
        }
        return groups;
    }

    private int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private boolean similar(String a, String b) {
        int d0 = -1, d1 = -1, diffs = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                diffs++;
                if (diffs > 2) return false;
                if (d0 < 0) d0 = i;
                else d1 = i;
            }
        }
        return diffs == 0 || (diffs == 2 && a.charAt(d0) == b.charAt(d1) && a.charAt(d1) == b.charAt(d0));
    }
}
