// LeetCode 2092 - Find All People With Secret
// https://leetcode.com/problems/find-all-people-with-secret/

import java.util.*;

class Solution {
    private int[] parent;

    private int find(int x) {
        return parent[x] == x ? x : (parent[x] = find(parent[x]));
    }

    private void unite(int a, int b) {
        a = find(a); b = find(b);
        if (a != b) parent[a] = b;
    }

    public List<Integer> findAllPeople(int n, int[][] meetings, int firstPerson) {
        Arrays.sort(meetings, (a, b) -> Integer.compare(a[2], b[2]));
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        boolean[] know = new boolean[n];
        know[0] = know[firstPerson] = true;
        unite(0, firstPerson);
        for (int i = 0; i < meetings.length; ) {
            int j = i;
            while (j < meetings.length && meetings[j][2] == meetings[i][2]) j++;
            for (int k = i; k < j; k++) unite(meetings[k][0], meetings[k][1]);
            int root0 = find(0);
            List<Integer> reset = new ArrayList<>();
            for (int k = i; k < j; k++) {
                int a = meetings[k][0], b = meetings[k][1];
                if (find(a) != root0) { reset.add(a); reset.add(b); }
                else { know[a] = know[b] = true; }
            }
            for (int x : reset) parent[x] = x;
            i = j;
        }
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < n; i++) if (find(i) == find(0) || know[i]) ans.add(i);
        return ans;
    }
}
