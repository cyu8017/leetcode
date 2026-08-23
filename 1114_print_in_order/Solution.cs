// LeetCode 1114 - Print in Order
// https://leetcode.com/problems/print-in-order/

using System;
using System.Threading;

public class Foo {
    private readonly SemaphoreSlim _second = new SemaphoreSlim(0, 1);
    private readonly SemaphoreSlim _third = new SemaphoreSlim(0, 1);

    public void First(Action printFirst) {
        printFirst();
        _second.Release();
    }

    public void Second(Action printSecond) {
        _second.Wait();
        printSecond();
        _third.Release();
    }

    public void Third(Action printThird) {
        _third.Wait();
        printThird();
    }
}
