// LeetCode 0387 - First Unique Character in a String
// https://leetcode.com/problems/first-unique-character-in-a-string/

int firstUniqChar(char* s) {
    int counts[26] = {0};

    for (int index = 0; s[index] != '\0'; index++) {
        counts[s[index] - 'a'] += 1;
    }

    for (int index = 0; s[index] != '\0'; index++) {
        if (counts[s[index] - 'a'] == 1) {
            return index;
        }
    }

    return -1;
}
