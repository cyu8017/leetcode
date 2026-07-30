// LeetCode 1117 - Building H2O
// https://leetcode.com/problems/building-h2o/

using System;
using System.Threading;

public class H2O {
    private int h;
    private int o;
    private readonly object lockObj = new object();

    public void Hydrogen(Action releaseHydrogen) {
        lock (lockObj) {
            while (h >= 2) Monitor.Wait(lockObj);
            h++;
            releaseHydrogen();
            if (h == 2 && o == 1) {
                h = 0;
                o = 0;
            }
            Monitor.PulseAll(lockObj);
        }
    }

    public void Oxygen(Action releaseOxygen) {
        lock (lockObj) {
            while (o >= 1) Monitor.Wait(lockObj);
            o++;
            releaseOxygen();
            if (h == 2 && o == 1) {
                h = 0;
                o = 0;
            }
            Monitor.PulseAll(lockObj);
        }
    }
}
