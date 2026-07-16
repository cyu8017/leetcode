impl Solution { pub fn num_distinct(s:String, t:String)->i32 {
    let t=t.as_bytes(); let mut dp=vec![0u64;t.len()+1]; dp[0]=1;
    for a in s.bytes() { for j in (1..=t.len()).rev() { if a==t[j-1] { dp[j]+=dp[j-1]; } } }
    dp[t.len()] as i32
} }