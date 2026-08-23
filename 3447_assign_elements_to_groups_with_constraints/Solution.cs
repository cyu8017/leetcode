// LeetCode 3447 - Assign Elements to Groups with Constraints
// https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

public class Solution {
    public int[] AssignElements(int[] groups, int[] elements) {
        const int maxV = 100001;
        int[] first = new int[maxV];
        for (int i = 0; i < maxV; i++) first[i] = -1;
        for (int i = 0; i < elements.Length; i++) {
            int e = elements[i];
            if (e < maxV && first[e] == -1) first[e] = i;
        }
        int[] ans = new int[groups.Length];
        for (int gi = 0; gi < groups.Length; gi++) {
            int g = groups[gi];
            int best = -1;
            for (int d = 1; d * d <= g; d++) {
                if (g % d == 0) {
                    if (first[d] != -1 && (best == -1 || first[d] < best)) best = first[d];
                    int other = g / d;
                    if (first[other] != -1 && (best == -1 || first[other] < best)) best = first[other];
                }
            }
            ans[gi] = best;
        }
        return ans;
    }
}
