function hasAllCodes(s: any, k: any): any { const seen=new Set(); for(let i=0;i+k<=s.length;i++)seen.add(s.slice(i,i+k)); return seen.size===(1<<k); }
