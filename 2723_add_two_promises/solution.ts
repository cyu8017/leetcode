// LeetCode 2723 - Add Two Promises
// https://leetcode.com/problems/add-two-promises/

export async function addTwoPromises(promise1: any, promise2: any): any {
    return (await promise1) + (await promise2);
}
