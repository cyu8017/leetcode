// LeetCode 3085 - Minimum Deletions to Make String K-Special
// https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

#include <string.h>

int minimumDeletions(char* word, int k) {
    int freq[26] = {0}, n = (int)strlen(word);
    for (int i = 0; i < n; i++) freq[word[i] - 'a']++;
    int nums[26], m = 0;
    for (int i = 0; i < 26; i++) if (freq[i] > 0) nums[m++] = freq[i];
    int ans = n;
    for (int v = 0; v <= n; v++) {
        int cur = 0;
        for (int i = 0; i < m; i++) {
            if (nums[i] < v) cur += nums[i];
            else if (nums[i] > v + k) cur += nums[i] - v - k;
        }
        if (cur < ans) ans = cur;
    }
    return ans;
}
