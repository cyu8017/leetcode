// LeetCode 1603 - Design Parking System
// https://leetcode.com/problems/design-parking-system/

export class ParkingSystem {
    private readonly spaces: number[];

    constructor(big: number, medium: number, small: number) {
        this.spaces = [0, big, medium, small];
    }

    addCar(carType: number): boolean {
        if (this.spaces[carType] === 0) return false;
        this.spaces[carType]--;
        return true;
    }
}
