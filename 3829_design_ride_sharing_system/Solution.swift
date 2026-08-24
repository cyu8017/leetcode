// LeetCode 3829 - Design Ride Sharing System
// https://leetcode.com/problems/design-ride-sharing-system/

class RideSharingSystem {
    private var t = 0
    private var riders = [(Int, Int)]()
    private var drivers = [(Int, Int)]()
    private var d = [Int: Int]()

    init() {}

    func addRider(_ riderId: Int) {
        d[riderId] = t
        riders.append((t, riderId))
        t += 1
    }

    func addDriver(_ driverId: Int) {
        drivers.append((t, driverId))
        t += 1
    }

    func matchDriverWithRider() -> [Int] {
        riders = riders.filter { d[$0.1] == $0.0 }
        if riders.isEmpty || drivers.isEmpty { return [-1, -1] }
        riders.sort { $0.0 < $1.0 }
        drivers.sort { $0.0 < $1.0 }
        let driver = drivers.removeFirst()
        let rider = riders.removeFirst()
        d.removeValue(forKey: rider.1)
        return [driver.1, rider.1]
    }

    func cancelRider(_ riderId: Int) {
        d.removeValue(forKey: riderId)
    }
}
