// LeetCode 2469 - Convert the Temperature
// https://leetcode.com/problems/convert-the-temperature/

export function convertTemperature(celsius: number): number[] {
    return [celsius + 273.15, celsius * 1.80 + 32.00];
}
