// LeetCode 1279 - Traffic Light Controlled Intersection
// https://leetcode.com/problems/traffic-light-controlled-intersection/

#include <functional>
#include <mutex>

class TrafficLight {
public:
    TrafficLight() : greenRoad(1) {}

    void carArrived(int carId, int roadId, int direction, std::function<void()> turnGreen,
                    std::function<void()> crossCar) {
        std::lock_guard<std::mutex> lock(mu);
        if (roadId != greenRoad) {
            turnGreen();
            greenRoad = roadId;
        }
        crossCar();
    }

private:
    int greenRoad;
    std::mutex mu;
};
