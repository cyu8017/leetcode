// LeetCode 2728 - Count Houses in a Circular Street
// https://leetcode.com/problems/count-houses-in-a-circular-street/

interface Street {
    void openDoor();
    void closeDoor();
    boolean isDoorOpen();
    void moveRight();
    void moveLeft();
}

class Solution {
    public int countHouses(Street street, int k) {
        for (int i = 0; i < k; i++) {
            street.closeDoor();
            street.moveRight();
        }
        int ans = 0;
        for (;;) {
            ans++;
            street.openDoor();
            street.moveRight();
            if (street.isDoorOpen()) break;
        }
        return ans;
    }
}
