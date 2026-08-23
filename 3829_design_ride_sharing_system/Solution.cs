// LeetCode 3829 - Design Ride Sharing System
// https://leetcode.com/problems/design-ride-sharing-system/

using System.Collections.Generic;

public class RideSharingSystem {
    int t = 0;
    SortedDictionary<int, int> riders = new SortedDictionary<int, int>();
    SortedDictionary<int, int> drivers = new SortedDictionary<int, int>();
    Dictionary<int, int> d = new Dictionary<int, int>();

    public RideSharingSystem() {}

    public void AddRider(int riderId) {
        d[riderId] = t;
        riders[t] = riderId;
        t++;
    }

    public void AddDriver(int driverId) {
        drivers[t] = driverId;
        t++;
    }

    public int[] MatchDriverWithRider() {
        if (riders.Count == 0 || drivers.Count == 0) return new int[] { -1, -1 };
        int dKey = 0, rKey = 0;
        foreach (var kv in drivers) { dKey = kv.Key; break; }
        foreach (var kv in riders) { rKey = kv.Key; break; }
        int driverId = drivers[dKey], riderId = riders[rKey];
        drivers.Remove(dKey);
        riders.Remove(rKey);
        return new int[] { driverId, riderId };
    }

    public void CancelRider(int riderId) {
        if (!d.ContainsKey(riderId)) return;
        riders.Remove(d[riderId]);
    }
}
