// LeetCode 2975 - Maximum Square Area by Removing Fences From a Field
// https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    private Set<Integer> gaps(int[] fences, int bound) {
        List<Integer> list = new ArrayList<>();
        list.add(1);
        for (int f : fences) list.add(f);
        list.add(bound);
        Collections.sort(list);
        Set<Integer> gaps = new HashSet<>();
        for (int i = 0; i < list.size(); i++)
            for (int j = i + 1; j < list.size(); j++)
                gaps.add(list.get(j) - list.get(i));
        return gaps;
    }

    public int maximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {
        final int mod = 1_000_000_007;
        Set<Integer> hg = gaps(hFences, m);
        Set<Integer> vg = gaps(vFences, n);
        long best = -1;
        for (int g : hg) {
            if (vg.contains(g) && g > best) best = g;
        }
        if (best < 0) return -1;
        return (int) (best * best % mod);
    }
}
