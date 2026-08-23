// LeetCode 2818 - Apply Operations to Maximize Score
// https://leetcode.com/problems/apply-operations-to-maximize-score/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int maximumScore(std::vector<int>& nums, int k) {
        const int MOD = 1000000007;
        int n = (int)nums.size();
        int maxV = *std::max_element(nums.begin(), nums.end());
        std::vector<int> spf(maxV + 1, 0);
        for (int i = 2; i <= maxV; i++) {
            if (spf[i] == 0) {
                for (int j = i; j <= maxV; j += i) if (spf[j] == 0) spf[j] = i;
            }
        }
        auto primeScore = [&](int x) {
            std::unordered_set<int> seen;
            while (x > 1) {
                int p = spf[x];
                seen.insert(p);
                while (x % p == 0) x /= p;
            }
            return (int)seen.size();
        };
        std::vector<int> score(n);
        for (int i = 0; i < n; i++) score[i] = primeScore(nums[i]);
        std::vector<int> left(n), right(n), st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && score[st.back()] < score[i]) st.pop_back();
            left[i] = st.empty() ? -1 : st.back();
            st.push_back(i);
        }
        st.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!st.empty() && score[st.back()] <= score[i]) st.pop_back();
            right[i] = st.empty() ? n : st.back();
            st.push_back(i);
        }
        std::vector<std::pair<int, long long>> arr(n);
        for (int i = 0; i < n; i++)
            arr[i] = {nums[i], 1LL * (i - left[i]) * (right[i] - i)};
        std::sort(arr.begin(), arr.end(), [](auto& a, auto& b) { return a.first > b.first; });
        auto modPow = [&](long long a, long long b) {
            long long res = 1;
            a %= MOD;
            while (b > 0) {
                if (b & 1) res = res * a % MOD;
                a = a * a % MOD;
                b >>= 1;
            }
            return (int)res;
        };
        long long ans = 1;
        long long remain = k;
        for (auto& [v, cnt] : arr) {
            if (remain <= 0) break;
            long long use = std::min(cnt, remain);
            ans = ans * modPow(v, use) % MOD;
            remain -= use;
        }
        return (int)ans;
    }
};
