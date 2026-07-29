// LeetCode 1234 - Replace the Substring for Balanced String
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

#include <limits.h>
#include <string.h>

int balancedString(char* s) {
    int n = (int)strlen(s);
    int limit = n / 4;
    int count[256] = {0};
    for (int i = 0; s[i]; i++) count[(unsigned char)s[i]]++;
    int left = 0;
    int answer = n;
    for (int right = 0; right < n; right++) {
        count[(unsigned char)s[right]]--;
        while (left < n && count['Q'] <= limit && count['W'] <= limit && count['E'] <= limit && count['R'] <= limit) {
            if (right - left + 1 < answer) answer = right - left + 1;
            count[(unsigned char)s[left]]++;
            left++;
        }
    }
    return answer;
}
