// LeetCode 0412 - Fizz Buzz
export function fizzBuzz(n: number): string[] {
    const result: string[] = [];
    for (let value = 1; value <= n; value += 1) {
        if (value % 15 === 0) result.push("FizzBuzz");
        else if (value % 3 === 0) result.push("Fizz");
        else if (value % 5 === 0) result.push("Buzz");
        else result.push(String(value));
    }
    return result;
}
