// LeetCode 1542 - Find Longest Awesome Substring
// https://leetcode.com/problems/find-longest-awesome-substring/

int longestAwesome(char* s) {
    int first[1024];
    for (int i = 0; i < 1024; i++) first[i] = -2;
    first[0] = -1;
    int mask = 0, answer = 0;
    for (int i = 0; s[i]; i++) {
        mask ^= 1 << (s[i] - '0');
        if (first[mask] == -2) first[mask] = i;
        else if (i - first[mask] > answer) answer = i - first[mask];
        for (int bit = 0; bit < 10; bit++) {
            int candidate = mask ^ (1 << bit);
            if (first[candidate] != -2 && i - first[candidate] > answer)
                answer = i - first[candidate];
        }
    }
    return answer;
}
