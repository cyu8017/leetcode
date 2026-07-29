// LeetCode 1414 - Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
// https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

#include <stdlib.h>

int findMinFibonacciNumbers(int k) {
    int* fib = (int*)malloc(50 * sizeof(int));
    int fn = 0;
    fib[fn++] = 1; fib[fn++] = 1;
    while (fib[fn - 1] < k) {
        fib[fn] = fib[fn - 1] + fib[fn - 2];
        fn++;
    }
    int answer = 0;
    for (int i = fn - 1; i >= 0; i--) {
        if (fib[i] <= k) { k -= fib[i]; answer++; }
    }
    free(fib);
    return answer;
}
