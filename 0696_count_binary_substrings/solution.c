// LeetCode 0696 - Count Binary Substrings
// https://leetcode.com/problems/count-binary-substrings/

int countBinarySubstrings(char* s) {
    int prev = 0, cur = 1, answer = 0;
    for (int i = 1; s[i]; i++) {
        if (s[i] == s[i - 1]) cur++;
        else {
            answer += prev < cur ? prev : cur;
            prev = cur;
            cur = 1;
        }
    }
    answer += prev < cur ? prev : cur;
    return answer;
}
