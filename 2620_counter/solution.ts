// LeetCode 2620 - Counter
// https://leetcode.com/problems/counter/

export function createCounter(n: any): any {
    return function() {
        return n++;
    };
}
