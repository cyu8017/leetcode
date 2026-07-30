// LeetCode 1279 - Traffic Light Controlled Intersection
// https://leetcode.com/problems/traffic-light-controlled-intersection/

using System;

public class TrafficLight {
    private int greenRoad = 1;
    private readonly object gate = new object();

    public void CarArrived(
        int carId,
        int roadId,
        int direction,
        Action turnGreen,
        Action crossCar) {
        lock (gate) {
            if (roadId != greenRoad) {
                turnGreen();
                greenRoad = roadId;
            }
            crossCar();
        }
    }
}
