// LeetCode 1117 - Building H2O
// https://leetcode.com/problems/building-h2o/

import java.util.concurrent.Semaphore;

class H2O {
    private final Semaphore hydrogen = new Semaphore(2);
    private final Semaphore oxygen = new Semaphore(0);
    private final Object lock = new Object();
    private int count = 0;

    public H2O() {}

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
        hydrogen.acquire();
        synchronized (lock) {
            count++;
            if (count == 2) oxygen.release();
        }
        releaseHydrogen.run();
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        oxygen.acquire();
        releaseOxygen.run();
        synchronized (lock) {
            count = 0;
            hydrogen.release();
            hydrogen.release();
        }
    }
}
