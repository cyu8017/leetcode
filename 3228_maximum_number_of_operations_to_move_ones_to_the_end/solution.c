// LeetCode 3228 - Maximum Number of Operations to Move Ones to the End
// https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

int maxOperations(char* s) {
    int ans = 0, cnt = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == '1') cnt++;
        else if (i > 0 && s[i - 1] == '1') ans += cnt;
    }
    return ans;
}
