// LeetCode 2621 - Sleep
// https://leetcode.com/problems/sleep/

var sleep = async function(millis) {
    return new Promise(function(resolve) {
        setTimeout(resolve, millis);
    });
};
