// LeetCode 1832 - Check if the Sentence Is Pangram
// https://leetcode.com/problems/check-if-the-sentence-is-pangram/

#include <stdbool.h>

bool checkIfPangram(char* sentence) {
    int seen = 0;
    for (int i = 0; sentence[i]; i++) {
        seen |= 1 << (sentence[i] - 'a');
    }
    return seen == (1 << 26) - 1;
}
