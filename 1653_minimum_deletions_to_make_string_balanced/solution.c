// LeetCode 1653 - Minimum Deletions to Make String Balanced
// https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

int minimumDeletions(char* s) {
    int b = 0, ans = 0;
    for (; *s; s++) {
        if (*s == 'b') b++;
        else {
            int delA = ans + 1;
            ans = delA < b ? delA : b;
        }
    }
    return ans;
}
