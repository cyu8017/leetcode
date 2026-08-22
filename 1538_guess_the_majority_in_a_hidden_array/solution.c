// LeetCode 1538 - Guess the Majority in a Hidden Array
// https://leetcode.com/problems/guess-the-majority-in-a-hidden-array/

struct ArrayReader;

/* Forward declarations of ArrayReader API (provided by judge). */
int query(struct ArrayReader* reader, int a, int b, int c, int d);
int length(struct ArrayReader* reader);

int guessMajority(struct ArrayReader* reader) {
    int n = length(reader);
    int first_four = query(reader, 0, 1, 2, 3);
    int shifted = query(reader, 1, 2, 3, 4);
    int same = 1, different = 0, different_index = -1, later_different = -1;
    int four_same = first_four == shifted;
    if (four_same) same++;
    else {
        different++;
        different_index = 4;
    }
    int checks[3][4] = {{0, 2, 3, 4}, {0, 1, 3, 4}, {0, 1, 2, 4}};
    for (int index = 1; index <= 3; index++) {
        if (query(reader, checks[index - 1][0], checks[index - 1][1], checks[index - 1][2], checks[index - 1][3]) == shifted)
            same++;
        else {
            different++;
            different_index = index;
        }
    }
    for (int i = 5; i < n; i++) {
        int i_same_as_four = query(reader, 1, 2, 3, i) == shifted;
        if (i_same_as_four == four_same) same++;
        else {
            different++;
            different_index = i;
            if (later_different == -1) later_different = i;
        }
    }
    if (same == different) return -1;
    return same > different ? 0 : (later_different != -1 ? later_different : different_index);
}
