// LeetCode 2753 - Count Houses in a Circular Street II
// https://leetcode.com/problems/count-houses-in-a-circular-street-ii/

export function houseCount(street: Street, k: number): number {
    while (!street.isDoorOpen()) street.moveRight();
    street.closeDoor();
    street.moveRight();
    let ans = 1;
    for (let i = 1; i < k; i++) {
        if (street.isDoorOpen()) {
            street.closeDoor();
            ans = 0;
        }
        ans++;
        street.moveRight();
    }
    return ans;
}
