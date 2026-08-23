// LeetCode 2723 - Add Two Promises
// https://leetcode.com/problems/add-two-promises/

var addTwoPromises = async function(promise1, promise2) {
    return (await promise1) + (await promise2);
};
