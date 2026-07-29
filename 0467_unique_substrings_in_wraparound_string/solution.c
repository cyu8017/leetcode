// LeetCode 0467 - Unique Substrings in Wraparound String
// https://leetcode.com/problems/unique-substrings-in-wraparound-string/

int findSubstringInWraproundString(char* s) {
    int counts[26] = {0};
    int length = 0;
    for (int index = 0; s[index]; index++) {
        if (index > 0 && (s[index] - s[index - 1] + 26) % 26 == 1) {
            length++;
        } else {
            length = 1;
        }
        int position = s[index] - 'a';
        if (length > counts[position]) {
            counts[position] = length;
        }
    }
    int total = 0;
    for (int i = 0; i < 26; i++) {
        total += counts[i];
    }
    return total;
}
