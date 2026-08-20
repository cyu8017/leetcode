// LeetCode 1279 - Traffic Light Controlled Intersection
// https://leetcode.com/problems/traffic-light-controlled-intersection/

import Foundation

class TrafficLight {
    private let lock = NSLock()
    private var road = 1

    func carArrived(
        _ carId: Int,
        _ roadId: Int,
        _ direction: Int,
        _ turnGreen: () -> Void,
        _ crossCar: () -> Void
    ) {
        lock.lock()
        if road != roadId {
            turnGreen()
            road = roadId
        }
        crossCar()
        lock.unlock()
    }
}
