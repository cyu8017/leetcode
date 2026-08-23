// LeetCode 2728 - Count Houses in a Circular Street
// https://leetcode.com/problems/count-houses-in-a-circular-street/

class Street {
public:
    virtual void openDoor() = 0;
    virtual void closeDoor() = 0;
    virtual bool isDoorOpen() = 0;
    virtual void moveRight() = 0;
    virtual void moveLeft() = 0;
    virtual ~Street() = default;
};

class Solution {
public:
    int countHouses(Street* street, int k) {
        for (int i = 0; i < k; i++) {
            street->closeDoor();
            street->moveRight();
        }
        int ans = 0;
        for (;;) {
            ans++;
            street->openDoor();
            street->moveRight();
            if (street->isDoorOpen()) break;
        }
        return ans;
    }
};
