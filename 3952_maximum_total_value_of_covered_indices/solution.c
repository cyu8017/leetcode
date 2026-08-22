// LeetCode 3952 - Maximum Total Value of Covered Indices
// https://leetcode.com/problems/maximum-total-value-of-covered-indices/

#include <string.h>

int maxTotalValue(int* nums, int numsSize, char* s) {
    (void)numsSize;
    int answer = 0;
    int len = (int)strlen(s);
    for (int i = 0; i < len; ) {
        if (s[i] == '0') { i++; continue; }
        int start = i;
        while (i < len && s[i] == '1') i++;
        int end = i - 1;
        if (start == 0) {
            for (int index = start; index <= end; index++) answer += nums[index];
            continue;
        }
        int minimum = nums[start - 1];
        int total = 0;
        for (int index = start - 1; index <= end; index++) {
            total += nums[index];
            if (nums[index] < minimum) minimum = nums[index];
        }
        answer += total - minimum;
    }
    return answer;
}
