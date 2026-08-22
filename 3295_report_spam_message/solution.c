// LeetCode 3295 - Report Spam Message
// https://leetcode.com/problems/report-spam-message/

#include <stdbool.h>
#include <string.h>

bool reportSpam(char** message, int messageSize, char** bannedWords, int bannedWordsSize) {
    int cnt = 0;
    for (int i = 0; i < messageSize; i++) {
        for (int j = 0; j < bannedWordsSize; j++) {
            if (strcmp(message[i], bannedWords[j]) == 0) {
                cnt++;
                if (cnt >= 2) return true;
                break;
            }
        }
    }
    return false;
}
