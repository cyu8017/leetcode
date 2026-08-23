// LeetCode 1116 - Print Zero Even Odd
// https://leetcode.com/problems/print-zero-even-odd/

using System;
using System.Threading;

public class ZeroEvenOdd {
    private readonly int n;
    private int state; // 0 = zero, 1 = odd, 2 = even
    private readonly object lockObj = new object();

    public ZeroEvenOdd(int n) {
        this.n = n;
    }

    public void Zero(Action<int> printNumber) {
        for (int i = 1; i <= n; i++) {
            lock (lockObj) {
                while (state != 0) Monitor.Wait(lockObj);
                printNumber(0);
                state = (i % 2 == 1) ? 1 : 2;
                Monitor.PulseAll(lockObj);
            }
        }
    }

    public void Even(Action<int> printNumber) {
        for (int num = 2; num <= n; num += 2) {
            lock (lockObj) {
                while (state != 2) Monitor.Wait(lockObj);
                printNumber(num);
                state = 0;
                Monitor.PulseAll(lockObj);
            }
        }
    }

    public void Odd(Action<int> printNumber) {
        for (int num = 1; num <= n; num += 2) {
            lock (lockObj) {
                while (state != 1) Monitor.Wait(lockObj);
                printNumber(num);
                state = 0;
                Monitor.PulseAll(lockObj);
            }
        }
    }
}
