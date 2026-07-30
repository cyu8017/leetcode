// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

using System;
using System.Threading;

public class FizzBuzz {
    private readonly int n;
    private int current = 1;
    private readonly object sync = new object();

    public FizzBuzz(int n) {
        this.n = n;
    }

    public void Fizz(Action printFizz) {
        Run(x => x % 3 == 0 && x % 5 != 0, printFizz);
    }

    public void Buzz(Action printBuzz) {
        Run(x => x % 5 == 0 && x % 3 != 0, printBuzz);
    }

    public void Fizzbuzz(Action printFizzBuzz) {
        Run(x => x % 15 == 0, printFizzBuzz);
    }

    public void Number(Action<int> printNumber) {
        Run(x => x % 3 != 0 && x % 5 != 0, () => printNumber(current));
    }

    private void Run(Func<int, bool> predicate, Action action) {
        while (true) {
            lock (sync) {
                while (current <= n && !predicate(current)) {
                    Monitor.Wait(sync);
                }
                if (current > n) return;
                action();
                current++;
                Monitor.PulseAll(sync);
            }
        }
    }
}
