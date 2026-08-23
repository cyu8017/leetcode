// LeetCode 2739 - Total Distance Traveled
// https://leetcode.com/problems/total-distance-traveled/

/**
 * @param {number} mainTank
 * @param {number} additionalTank
 * @return {number}
 */
var distanceTraveled = function(mainTank, additionalTank) {
    let ans = 0;
    while (mainTank > 0) {
        if (mainTank >= 5) {
            ans += 50;
            mainTank -= 5;
            if (additionalTank > 0) {
                additionalTank--;
                mainTank++;
            }
        } else {
            ans += mainTank * 10;
            mainTank = 0;
        }
    }
    return ans;
};
