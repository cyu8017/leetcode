"use strict";
// LeetCode 1603 - Design Parking System
// https://leetcode.com/problems/design-parking-system/
Object.defineProperty(exports, "__esModule", { value: true });
exports.ParkingSystem = void 0;
class ParkingSystem {
    constructor(big, medium, small) {
        this.spaces = [0, big, medium, small];
    }
    addCar(carType) {
        if (this.spaces[carType] === 0)
            return false;
        this.spaces[carType]--;
        return true;
    }
}
exports.ParkingSystem = ParkingSystem;
