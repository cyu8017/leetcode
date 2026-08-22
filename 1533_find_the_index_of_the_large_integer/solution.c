// LeetCode 1533 - Find the Index of the Large Integer
// https://leetcode.com/problems/find-the-index-of-the-large-integer/

struct ArrayReader;

/* Forward declarations of ArrayReader API (provided by judge). */
int compareSub(struct ArrayReader* reader, int l, int r, int x, int y);
int length(struct ArrayReader* reader);

int getIndex(struct ArrayReader* reader) {
    int left = 0, right = length(reader) - 1;
    while (left < right) {
        int len = right - left + 1;
        int half = len / 2;
        int result = compareSub(reader, left, left + half - 1, right - half + 1, right);
        if (result == 0) return left + half;
        if (result > 0) right = left + half - 1;
        else left = right - half + 1;
    }
    return left;
}
