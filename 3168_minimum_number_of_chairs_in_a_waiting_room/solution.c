// LeetCode 3168 - Minimum Number of Chairs in a Waiting Room
// https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

int minimumChairs(char* s) {
    int cnt = 0, left = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == 'E') {
            if (left > 0) left--;
            else cnt++;
        } else left++;
    }
    return cnt;
}
