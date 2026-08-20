"use strict";
function busyStudent(startTime, endTime, queryTime) { return startTime.reduce((answer, start, i) => answer + (start <= queryTime && queryTime <= endTime[i]), 0); }
