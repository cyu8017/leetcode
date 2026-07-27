// LeetCode 1603 - Design Parking System
// https://leetcode.com/problems/design-parking-system/

class ParkingSystem {
    /**
     * @param {number} big
     * @param {number} medium
     * @param {number} small
     */
    constructor(big, medium, small) {
        this.spaces = [0, big, medium, small];
    }

    /**
     * @param {number} carType
     * @return {boolean}
     */
    addCar(carType) {
        if (this.spaces[carType] === 0) return false;
        this.spaces[carType]--;
        return true;
    }
}

module.exports = { ParkingSystem };
