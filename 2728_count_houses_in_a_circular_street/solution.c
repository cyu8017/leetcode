// LeetCode 2728 - Count Houses in a Circular Street
// https://leetcode.com/problems/count-houses-in-a-circular-street/

#include <stdbool.h>

typedef struct Street Street;
struct Street {
    void (*openDoor)(Street*);
    void (*closeDoor)(Street*);
    bool (*isDoorOpen)(Street*);
    void (*moveRight)(Street*);
    void (*moveLeft)(Street*);
};

int countHouses(Street* street, int k) {
    for (int i = 0; i < k; i++) {
        street->closeDoor(street);
        street->moveRight(street);
    }
    int ans = 0;
    for (;;) {
        ans++;
        street->openDoor(street);
        street->moveRight(street);
        if (street->isDoorOpen(street)) break;
    }
    return ans;
}
