// LeetCode 3948 - Lexicographically Maximum MEX Array
// https://leetcode.com/problems/lexicographically-maximum-mex-array/

using System.Collections.Generic;

public class Solution {
    public int[] MaxMexArray(int[] nums) {
        int n = nums.Length;
        int[] remaining = new int[n + 2];
        foreach (int x in nums) {
            if (x <= n + 1) remaining[x]++;
        }
        int mex = 0;
        while (remaining[mex] > 0) mex++;
        var answer = new List<int>();
        int[] seen = new int[n + 2];
        int stamp = 0, index = 0;
        while (index < n) {
            if (mex == 0) {
                answer.Add(0);
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
            answer.Add(mex);
            mex = 0;
            while (remaining[mex] > 0) mex++;
        }
        return answer.ToArray();
    }
}
