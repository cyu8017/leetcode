// LeetCode 1647 - Minimum Deletions to Make Character Frequencies Unique
// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

#include <string.h>
#include <stdbool.h>

int minDeletions(char* s) {
    int cnt[26] = {0};
    for (; *s; s++) cnt[*s - 'a']++;
    bool used[100001] = {false};
    int ans = 0;
    for (int i = 0; i < 26; i++) {
        int x = cnt[i];
        while (x && used[x]) { x--; ans++; }
        used[x] = true;
    }
    return ans;
}
