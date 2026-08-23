// LeetCode 1116 - Print Zero Even Odd
// https://leetcode.com/problems/print-zero-even-odd/

import java.util.concurrent.Semaphore;
import java.util.function.IntConsumer;

class ZeroEvenOdd {
    private final int n;
    private final Semaphore zeroSem = new Semaphore(1);
    private final Semaphore evenSem = new Semaphore(0);
    private final Semaphore oddSem = new Semaphore(0);

    public ZeroEvenOdd(int n) {
        this.n = n;
    }

    public void zero(IntConsumer printNumber) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            zeroSem.acquire();
            printNumber.accept(0);
            if (i % 2 == 0) oddSem.release();
            else evenSem.release();
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int num = 2; num <= n; num += 2) {
            evenSem.acquire();
            printNumber.accept(num);
            zeroSem.release();
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int num = 1; num <= n; num += 2) {
            oddSem.acquire();
            printNumber.accept(num);
            zeroSem.release();
        }
    }
}
