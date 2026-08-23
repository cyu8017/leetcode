// LeetCode 2449 - Minimum Number of Operations to Make Arrays Similar
// https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public long makeSimilar(int[] nums, int[] target) {
        Arrays.sort(nums);
        Arrays.sort(target);
        var oddN = new ArrayList<Integer>();
        var evenN = new ArrayList<Integer>();
        var oddT = new ArrayList<Integer>();
        var evenT = new ArrayList<Integer>();
        for (int x : nums) {
            if (x % 2 == 0) evenN.add(x);
            else oddN.add(x);
        }
        for (int x : target) {
            if (x % 2 == 0) evenT.add(x);
            else oddT.add(x);
        }
        long ans = 0;
        for (int i = 0; i < oddN.size(); i++) {
            int diff = oddN.get(i) - oddT.get(i);
            if (diff > 0) ans += diff / 2;
        }
        for (int i = 0; i < evenN.size(); i++) {
            int diff = evenN.get(i) - evenT.get(i);
            if (diff > 0) ans += diff / 2;
        }
        return ans;
    }
}
