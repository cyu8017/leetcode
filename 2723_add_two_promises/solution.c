// LeetCode 2723 - Add Two Promises
// https://leetcode.com/problems/add-two-promises/

typedef int (*PromiseFn)(void);

int addTwoPromises(PromiseFn promise1, PromiseFn promise2) {
    return (promise1 ? promise1() : 0) + (promise2 ? promise2() : 0);
}
