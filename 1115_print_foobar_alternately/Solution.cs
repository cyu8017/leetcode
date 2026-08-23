// LeetCode 1115 - Print FooBar Alternately
// https://leetcode.com/problems/print-foobar-alternately/

using System;
using System.Threading;

public class FooBar {
    private readonly int n;
    private readonly SemaphoreSlim fooSem = new SemaphoreSlim(1, 1);
    private readonly SemaphoreSlim barSem = new SemaphoreSlim(0, 1);

    public FooBar(int n) {
        this.n = n;
    }

    public void Foo(Action printFoo) {
        for (int i = 0; i < n; i++) {
            fooSem.Wait();
            printFoo();
            barSem.Release();
        }
    }

    public void Bar(Action printBar) {
        for (int i = 0; i < n; i++) {
            barSem.Wait();
            printBar();
            fooSem.Release();
        }
    }
}
