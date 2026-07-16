impl Solution { pub fn generate(num_rows:i32)->Vec<Vec<i32>> {
    let mut out=Vec::new();
    for i in 0..num_rows as usize { let mut row=vec![1;i+1]; for j in 1..i { row[j]=out[i-1][j-1]+out[i-1][j]; } out.push(row); }
    out
} }