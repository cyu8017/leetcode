// LeetCode 1220 - Count Vowels Permutation
// https://leetcode.com/problems/count-vowels-permutation/

class Solution {
public:
    int countVowelPermutation(int n) {
        const int mod = 1000000007;
        long long a = 1, e = 1, i = 1, o = 1, u = 1;
        for (int k = 0; k < n - 1; ++k) {
            long long na = (e + i + u) % mod;
            long long ne = (a + i) % mod;
            long long ni = (e + o) % mod;
            long long no = i;
            long long nu = (i + o) % mod;
            a = na;
            e = ne;
            i = ni;
            o = no;
            u = nu;
        }
        return static_cast<int>((a + e + i + o + u) % mod);
    }
};
