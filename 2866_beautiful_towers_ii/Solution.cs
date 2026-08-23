// LeetCode 2866 - Beautiful Towers II
// https://leetcode.com/problems/beautiful-towers-ii/

using System.Collections.Generic;

public class Solution {
    public long MaximumSumOfHeights(IList<int> maxHeights) {
        int n = maxHeights.Count;
        long[] left = new long[n];
        var st = new List<int> { -1 };
        long sum = 0;
        for (int i = 0; i < n; i++) {
            while (st.Count > 1 && maxHeights[st[st.Count - 1]] >= maxHeights[i]) {
                int j = st[st.Count - 1];
                st.RemoveAt(st.Count - 1);
                sum -= 1L * maxHeights[j] * (j - st[st.Count - 1]);
            }
            sum += 1L * maxHeights[i] * (i - st[st.Count - 1]);
            left[i] = sum;
            st.Add(i);
        }
        long[] right = new long[n];
        st = new List<int> { n };
        sum = 0;
        for (int i = n - 1; i >= 0; i--) {
            while (st.Count > 1 && maxHeights[st[st.Count - 1]] >= maxHeights[i]) {
                int j = st[st.Count - 1];
                st.RemoveAt(st.Count - 1);
                sum -= 1L * maxHeights[j] * (st[st.Count - 1] - j);
            }
            sum += 1L * maxHeights[i] * (st[st.Count - 1] - i);
            right[i] = sum;
            st.Add(i);
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            long cand = left[i] + right[i] - maxHeights[i];
            if (cand > ans) ans = cand;
        }
        return ans;
    }
}
