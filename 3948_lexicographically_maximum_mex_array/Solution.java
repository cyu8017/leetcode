// LeetCode 3948 - Lexicographically Maximum MEX Array
// https://leetcode.com/problems/lexicographically-maximum-mex-array/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] maxMexArray(int[] nums) {
        int n = nums.length;
        int[] remaining = new int[n + 2];
        for (int x : nums) {
            if (x <= n + 1) remaining[x]++;
        }
        int mex = 0;
        while (remaining[mex] > 0) mex++;
        List<Integer> answer = new ArrayList<>();
        int[] seen = new int[n + 2];
        int stamp = 0, index = 0;
        while (index < n) {
            if (mex == 0) {
                answer.add(0);
                int x = nums[index];
                if (x <= n + 1) remaining[x]--;
                index++;
                continue;
            }
            stamp++;
            int need = mex;
            while (need > 0) {
                int x = nums[index];
                if (x < mex && seen[x] != stamp) {
                    seen[x] = stamp;
                    need--;
                }
                if (x <= n + 1) remaining[x]--;
                index++;
            }
            answer.add(mex);
            mex = 0;
            while (remaining[mex] > 0) mex++;
        }
        int[] out = new int[answer.size()];
        for (int i = 0; i < out.length; i++) out[i] = answer.get(i);
        return out;
    }
}
