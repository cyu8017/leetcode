// LeetCode 1414: Find The Minimum Number Of Fibonacci Numbers Whose Sum Is K

var findMinFibonacciNumbers = function(k) {
    const fib = [1, 1];
    while (fib.at(-1) < k) fib.push(fib.at(-1) + fib.at(-2));
    let count = 0;
    for (let i = fib.length - 1; i >= 0 && k; i--) if (fib[i] <= k) { k -= fib[i]; count++; }
    return count;
};
