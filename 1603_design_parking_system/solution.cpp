// LeetCode 1603 - Design Parking System
// https://leetcode.com/problems/design-parking-system/

#include <vector>

class ParkingSystem {
    std::vector<int> spaces_;

public:
    ParkingSystem(int big, int medium, int small) : spaces_{0, big, medium, small} {}

    bool addCar(int carType) {
        if (spaces_[carType] == 0) {
            return false;
        }
        --spaces_[carType];
        return true;
    }
};
