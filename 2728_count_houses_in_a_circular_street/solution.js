// LeetCode 2728 - Count Houses in a Circular Street
// https://leetcode.com/problems/count-houses-in-a-circular-street/

/**
 * @param {Street} street
 * @param {number} k
 * @return {number}
 */
var houseCount = function(street, k) {
    for (let i = 0; i < k; i++) {
        street.closeDoor();
        street.moveRight();
    }
    let ans = 0;
    for (;;) {
        ans++;
        street.openDoor();
        street.moveRight();
        if (street.isDoorOpen()) break;
    }
    return ans;
};
