// LeetCode 1224 - Maximum Equal Frequency
// https://leetcode.com/problems/maximum-equal-frequency/

#include <string.h>

int maxEqualFreq(int* nums, int numsSize) {
    int count[100001];
    int freq[100001];
    memset(count, 0, sizeof(count));
    memset(freq, 0, sizeof(freq));
    int answer = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        int old = count[x];
        if (old > 0) freq[old]--;
        count[x]++;
        freq[old + 1]++;
        int high = 0;
        for (int f = 1; f <= numsSize; f++) {
            if (freq[f] > 0) high = f;
        }
        if (high == 1 || freq[high] * high + 1 == i + 1 ||
            (freq[high] == 1 && freq[high - 1] * (high - 1) + high == i + 1)) {
            answer = i + 1;
        }
    }
    return answer;
}
