// LeetCode 1279 - Traffic Light Controlled Intersection
// https://leetcode.com/problems/traffic-light-controlled-intersection/

class TrafficLight {
    private int greenRoad = 1;
    private final Object lock = new Object();

    public TrafficLight() {}

    public void carArrived(
            int carId,
            int roadId,
            int direction,
            Runnable turnGreen,
            Runnable crossCar) {
        synchronized (lock) {
            if (roadId != greenRoad) {
                turnGreen.run();
                greenRoad = roadId;
            }
            crossCar.run();
        }
    }
}
