// LeetCode 3337 - Total Characters in String After Transformations II
// https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

#include <string>
#include <vector>

class Solution {
    using Mat = std::vector<std::vector<int>>;

    Mat matMul(const Mat& a, const Mat& b, int mod) {
        int n = (int)a.size();
        Mat c(n, std::vector<int>(n, 0));
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n; k++) {
                if (a[i][k] == 0) continue;
                for (int j = 0; j < n; j++) {
                    c[i][j] = (c[i][j] + (int)((long long)a[i][k] * b[k][j] % mod)) % mod;
                }
            }
        }
        return c;
    }

    Mat matPow(Mat a, int e, int mod) {
        int n = (int)a.size();
        Mat r(n, std::vector<int>(n, 0));
        for (int i = 0; i < n; i++) r[i][i] = 1;
        while (e > 0) {
            if (e & 1) r = matMul(r, a, mod);
            a = matMul(a, a, mod);
            e >>= 1;
        }
        return r;
    }

public:
    int lengthAfterTransformations(std::string s, int t, std::vector<int>& nums) {
        const int mod = 1000000007;
        Mat mat(26, std::vector<int>(26, 0));
        for (int i = 0; i < 26; i++) {
            for (int j = 1; j <= nums[i]; j++) mat[i][(i + j) % 26] = 1;
        }
        mat = matPow(mat, t, mod);
        std::vector<int> cnt(26, 0);
        for (char c : s) cnt[c - 'a']++;
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                ans = (ans + (int)((long long)cnt[i] * mat[i][j] % mod)) % mod;
            }
        }
        return ans;
    }
};
