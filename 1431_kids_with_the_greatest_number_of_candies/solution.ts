function kidsWithCandies(candies: any, extraCandies: any): any {
    const maximum = Math.max(...candies); return candies.map((x: any): any => x + extraCandies >= maximum);
}
