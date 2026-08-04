// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

import java.util.function.IntConsumer;

class FizzBuzz {
    private final int n;
    private int current = 1;
    private final Object lock = new Object();

    public FizzBuzz(int n) { this.n = n; }

    public void fizz(Runnable printFizz) throws InterruptedException {
        run(x -> x % 3 == 0 && x % 5 != 0, printFizz);
    }
    public void buzz(Runnable printBuzz) throws InterruptedException {
        run(x -> x % 5 == 0 && x % 3 != 0, printBuzz);
    }
    public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        run(x -> x % 15 == 0, printFizzBuzz);
    }
    public void number(IntConsumer printNumber) throws InterruptedException {
        synchronized (lock) {
            while (current <= n) {
                if (current % 3 != 0 && current % 5 != 0) {
                    printNumber.accept(current);
                    current++;
                    lock.notifyAll();
                } else lock.wait();
            }
        }
    }
    private void run(java.util.function.IntPredicate pred, Runnable action) throws InterruptedException {
        synchronized (lock) {
            while (current <= n) {
                if (pred.test(current)) {
                    action.run();
                    current++;
                    lock.notifyAll();
                } else lock.wait();
            }
        }
    }
}
