// LeetCode 2866 - Beautiful Towers II
// https://leetcode.com/problems/beautiful-towers-ii/

#include <vector>

class Solution {
public:
    long long maximumSumOfHeights(std::vector<int>& maxHeights) {
        int n = (int)maxHeights.size();
        std::vector<long long> left(n);
        std::vector<int> st = {-1};
        long long sum = 0;
        for (int i = 0; i < n; i++) {
            while ((int)st.size() > 1 && maxHeights[st.back()] >= maxHeights[i]) {
                int j = st.back();
                st.pop_back();
                sum -= 1LL * maxHeights[j] * (j - st.back());
            }
            sum += 1LL * maxHeights[i] * (i - st.back());
            left[i] = sum;
            st.push_back(i);
        }
        std::vector<long long> right(n);
        st = {n};
        sum = 0;
        for (int i = n - 1; i >= 0; i--) {
            while ((int)st.size() > 1 && maxHeights[st.back()] >= maxHeights[i]) {
                int j = st.back();
                st.pop_back();
                sum -= 1LL * maxHeights[j] * (st.back() - j);
            }
            sum += 1LL * maxHeights[i] * (st.back() - i);
            right[i] = sum;
            st.push_back(i);
        }
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            long long cand = left[i] + right[i] - maxHeights[i];
            if (cand > ans) ans = cand;
        }
        return ans;
    }
};
