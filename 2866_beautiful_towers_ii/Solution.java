// LeetCode 2866 - Beautiful Towers II
// https://leetcode.com/problems/beautiful-towers-ii/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public long maximumSumOfHeights(List<Integer> maxHeights) {
        int n = maxHeights.size();
        long[] left = new long[n];
        List<Integer> st = new ArrayList<>();
        st.add(-1);
        long sum = 0;
        for (int i = 0; i < n; i++) {
            while (st.size() > 1 && maxHeights.get(st.get(st.size() - 1)) >= maxHeights.get(i)) {
                int j = st.remove(st.size() - 1);
                sum -= 1L * maxHeights.get(j) * (j - st.get(st.size() - 1));
            }
            sum += 1L * maxHeights.get(i) * (i - st.get(st.size() - 1));
            left[i] = sum;
            st.add(i);
        }
        long[] right = new long[n];
        st = new ArrayList<>();
        st.add(n);
        sum = 0;
        for (int i = n - 1; i >= 0; i--) {
            while (st.size() > 1 && maxHeights.get(st.get(st.size() - 1)) >= maxHeights.get(i)) {
                int j = st.remove(st.size() - 1);
                sum -= 1L * maxHeights.get(j) * (st.get(st.size() - 1) - j);
            }
            sum += 1L * maxHeights.get(i) * (st.get(st.size() - 1) - i);
            right[i] = sum;
            st.add(i);
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            long cand = left[i] + right[i] - maxHeights.get(i);
            if (cand > ans) ans = cand;
        }
        return ans;
    }
}
