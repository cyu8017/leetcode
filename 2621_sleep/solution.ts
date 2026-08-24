// LeetCode 2621 - Sleep
// https://leetcode.com/problems/sleep/

export async function sleep(millis: any): any {
    return new Promise(function(resolve) {
        setTimeout(resolve, millis);
    });
}
