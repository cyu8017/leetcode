// LeetCode 1224 - Maximum Equal Frequency
// https://leetcode.com/problems/maximum-equal-frequency/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MaxEqualFreq(int[] nums) {
        var count = new Dictionary<int, int>();
        var frequencies = new Dictionary<int, int>();
        int answer = 0;
        for (int i = 0; i < nums.Length; i++) {
            int x = nums[i];
            count.TryGetValue(x, out int old);
            if (old > 0) {
                frequencies[old]--;
                if (frequencies[old] == 0) frequencies.Remove(old);
            }
            count[x] = old + 1;
            int nf = old + 1;
            frequencies[nf] = frequencies.GetValueOrDefault(nf) + 1;
            int high = frequencies.Keys.Max();
            if (high == 1
                || frequencies[high] * high + 1 == i + 1
                || (frequencies.GetValueOrDefault(high) == 1
                    && frequencies.GetValueOrDefault(high - 1) * (high - 1) + high == i + 1)) {
                answer = i + 1;
            }
        }
        return answer;
    }
}
