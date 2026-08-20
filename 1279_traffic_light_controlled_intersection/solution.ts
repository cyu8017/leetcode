// LeetCode 1279 - Traffic Light Controlled Intersection
// https://leetcode.com/problems/traffic-light-controlled-intersection/

class TrafficLight {
    greenRoad: any;

    constructor() {
        this.greenRoad = 1;
    }

    carArrived(carId: number, roadId: number, direction: number, turnGreen: Function, crossCar: Function): void {
        if (roadId !== this.greenRoad) {
            turnGreen();
            this.greenRoad = roadId;
        }
        crossCar();
    }
}
