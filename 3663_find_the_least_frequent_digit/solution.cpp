// LeetCode 3663 - Find The Least Frequent Digit
// https://leetcode.com/problems/find-the-least-frequent-digit/


class Solution {
public:
    int getLeastFrequentDigit(int n) {
        int cnt[10] = {}, ans = 0, f = 1 << 30;
        for (; n > 0; n /= 10) cnt[n % 10]++;
        for (int x = 0; x < 10; x++) {
            if (cnt[x] > 0 && cnt[x] < f) {
                f = cnt[x];
                ans = x;
            }
        }
        return ans;
    }
};
