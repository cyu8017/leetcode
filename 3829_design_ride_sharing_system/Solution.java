// LeetCode 3829 - Design Ride Sharing System
// https://leetcode.com/problems/design_ride_sharing_system/

import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

class RideSharingSystem {
    int t = 0;
    TreeMap<Integer, Integer> riders = new TreeMap<>();
    TreeMap<Integer, Integer> drivers = new TreeMap<>();
    Map<Integer, Integer> d = new HashMap<>();

    public RideSharingSystem() {}

    public void addRider(int riderId) {
        d.put(riderId, t);
        riders.put(t, riderId);
        t++;
    }

    public void addDriver(int driverId) {
        drivers.put(t, driverId);
        t++;
    }

    public int[] matchDriverWithRider() {
        if (riders.isEmpty() || drivers.isEmpty()) return new int[] { -1, -1 };
        int dKey = drivers.firstKey();
        int rKey = riders.firstKey();
        int driverId = drivers.get(dKey), riderId = riders.get(rKey);
        drivers.remove(dKey);
        riders.remove(rKey);
        return new int[] { driverId, riderId };
    }

    public void cancelRider(int riderId) {
        if (!d.containsKey(riderId)) return;
        riders.remove(d.get(riderId));
    }
}
