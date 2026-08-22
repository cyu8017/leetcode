// LeetCode 2380 - Time Needed to Rearrange a Binary String
// https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

int secondsToRemoveOccurrences(char* s) {
    int ans = 0, zeros = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == '0') zeros++;
        else if (zeros > 0) {
            if (ans + 1 > zeros) ans = ans + 1;
            else ans = zeros;
        }
    }
    return ans;
}
