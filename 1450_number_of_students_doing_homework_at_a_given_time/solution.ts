function busyStudent(startTime: any, endTime: any, queryTime: any): any { return startTime.reduce((answer,start,i: any): any =>answer+(start<=queryTime&&queryTime<=endTime[i]),0); }
