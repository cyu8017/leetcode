// LeetCode 1689 - Partitioning Into Minimum Number Of Deci-Binary Numbers
// https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

int minPartitions(char* n) {
    int best = 0;
    for (; *n; n++) {
        int d = *n - '0';
        if (d > best) best = d;
    }
    return best;
}
