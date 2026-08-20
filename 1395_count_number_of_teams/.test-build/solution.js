"use strict";
// LeetCode 1395: Count Number Of Teams
function numTeams(rating) {
    let teams = 0;
    for (let j = 0; j < rating.length; j++) {
        let lowerLeft = 0, higherLeft = 0, lowerRight = 0, higherRight = 0;
        for (let i = 0; i < j; i++)
            rating[i] < rating[j] ? lowerLeft++ : higherLeft++;
        for (let k = j + 1; k < rating.length; k++)
            rating[k] < rating[j] ? lowerRight++ : higherRight++;
        teams += lowerLeft * higherRight + higherLeft * lowerRight;
    }
    return teams;
}
