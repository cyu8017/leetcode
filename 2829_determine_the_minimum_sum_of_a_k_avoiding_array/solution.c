// LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
// https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

#include <stdbool.h>
#include <string.h>

int minimumSum(int n, int k) {
    bool used[2005];
    memset(used, 0, sizeof(used));
    int sum = 0, x = 1, cnt = 0;
    while (cnt < n) {
        int other = k - x;
        if (other < 0 || other >= 2005 || !used[other]) {
            if (x < 2005) used[x] = true;
            sum += x;
            cnt++;
        }
        x++;
    }
    return sum;
}
