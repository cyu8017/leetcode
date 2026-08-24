// LeetCode 2690 - Infinite Method Object
// https://leetcode.com/problems/infinite-method-object/

export function createInfiniteObject(): any {
    return new Proxy({}, {
        get: () => () => "Hello World",
    });
}
