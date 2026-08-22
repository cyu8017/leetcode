// LeetCode 2405 - Optimal Partition of String
// https://leetcode.com/problems/optimal-partition-of-string/

int partitionString(char* s) {
    int ans = 1, seen = 0;
    for (int i = 0; s[i]; i++) {
        int bit = 1 << (s[i] - 'a');
        if (seen & bit) { ans++; seen = 0; }
        seen |= bit;
    }
    return ans;
}
