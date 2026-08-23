// LeetCode 3507 - Minimum Pair Removal to Sort Array I
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private boolean isNonDecreasing(List<Integer> a) {
        for (int i = 1; i < a.size(); i++) if (a.get(i) < a.get(i - 1)) return false;
        return true;
    }
    public int minimumPairRemoval(int[] nums) {
        List<Integer> arr = new ArrayList<>();
        for (int x : nums) arr.add(x);
        int ans = 0;
        while (!isNonDecreasing(arr)) {
            int k = 0, s = arr.get(0) + arr.get(1);
            for (int i = 1; i + 1 < arr.size(); i++) {
                int t = arr.get(i) + arr.get(i + 1);
                if (s > t) { s = t; k = i; }
            }
            arr.set(k, s);
            arr.remove(k + 1);
            ans++;
        }
        return ans;
    }
}
